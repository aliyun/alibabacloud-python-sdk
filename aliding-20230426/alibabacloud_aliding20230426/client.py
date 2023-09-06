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

    def add_attendee_with_options(
        self,
        tmp_req: aliding_20230426_models.AddAttendeeRequest,
        tmp_header: aliding_20230426_models.AddAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddAttendeeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_add):
            request.attendees_to_add_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_add, 'AttendeesToAdd', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_add_shrink):
            body['AttendeesToAdd'] = request.attendees_to_add_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='AddAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/addAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_attendee_with_options_async(
        self,
        tmp_req: aliding_20230426_models.AddAttendeeRequest,
        tmp_header: aliding_20230426_models.AddAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddAttendeeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_add):
            request.attendees_to_add_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_add, 'AttendeesToAdd', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_add_shrink):
            body['AttendeesToAdd'] = request.attendees_to_add_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='AddAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/addAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddAttendeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_attendee(
        self,
        request: aliding_20230426_models.AddAttendeeRequest,
    ) -> aliding_20230426_models.AddAttendeeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddAttendeeHeaders()
        return self.add_attendee_with_options(request, headers, runtime)

    async def add_attendee_async(
        self,
        request: aliding_20230426_models.AddAttendeeRequest,
    ) -> aliding_20230426_models.AddAttendeeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddAttendeeHeaders()
        return await self.add_attendee_with_options_async(request, headers, runtime)

    def add_workspace_with_options(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
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
            action='AddWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/addWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_workspace_with_options_async(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
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
            action='AddWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/addWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_workspace(
        self,
        request: aliding_20230426_models.AddWorkspaceRequest,
    ) -> aliding_20230426_models.AddWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceHeaders()
        return self.add_workspace_with_options(request, headers, runtime)

    async def add_workspace_async(
        self,
        request: aliding_20230426_models.AddWorkspaceRequest,
    ) -> aliding_20230426_models.AddWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceHeaders()
        return await self.add_workspace_with_options_async(request, headers, runtime)

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

    def cancel_schedule_conference_with_options(
        self,
        tmp_req: aliding_20230426_models.CancelScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.CancelScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CancelScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CancelScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CancelScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
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
            action='CancelScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/cancelScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CancelScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_schedule_conference_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CancelScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.CancelScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CancelScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CancelScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CancelScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
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
            action='CancelScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/cancelScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CancelScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_schedule_conference(
        self,
        request: aliding_20230426_models.CancelScheduleConferenceRequest,
    ) -> aliding_20230426_models.CancelScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CancelScheduleConferenceHeaders()
        return self.cancel_schedule_conference_with_options(request, headers, runtime)

    async def cancel_schedule_conference_async(
        self,
        request: aliding_20230426_models.CancelScheduleConferenceRequest,
    ) -> aliding_20230426_models.CancelScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CancelScheduleConferenceHeaders()
        return await self.cancel_schedule_conference_with_options_async(request, headers, runtime)

    def clear_with_options(
        self,
        tmp_req: aliding_20230426_models.ClearRequest,
        tmp_header: aliding_20230426_models.ClearHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ClearResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
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
            action='Clear',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ClearRequest,
        tmp_header: aliding_20230426_models.ClearHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ClearResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
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
            action='Clear',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear(
        self,
        request: aliding_20230426_models.ClearRequest,
    ) -> aliding_20230426_models.ClearResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearHeaders()
        return self.clear_with_options(request, headers, runtime)

    async def clear_async(
        self,
        request: aliding_20230426_models.ClearRequest,
    ) -> aliding_20230426_models.ClearResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearHeaders()
        return await self.clear_with_options_async(request, headers, runtime)

    def clear_data_with_options(
        self,
        tmp_req: aliding_20230426_models.ClearDataRequest,
        tmp_header: aliding_20230426_models.ClearDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ClearDataResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
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
            action='ClearData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/clearData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_data_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ClearDataRequest,
        tmp_header: aliding_20230426_models.ClearDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ClearDataResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
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
            action='ClearData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/clearData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_data(
        self,
        request: aliding_20230426_models.ClearDataRequest,
    ) -> aliding_20230426_models.ClearDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearDataHeaders()
        return self.clear_data_with_options(request, headers, runtime)

    async def clear_data_async(
        self,
        request: aliding_20230426_models.ClearDataRequest,
    ) -> aliding_20230426_models.ClearDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearDataHeaders()
        return await self.clear_data_with_options_async(request, headers, runtime)

    def comment_list_report_with_options(
        self,
        tmp_req: aliding_20230426_models.CommentListReportRequest,
        tmp_header: aliding_20230426_models.CommentListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CommentListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CommentListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CommentListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='CommentListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/commentListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CommentListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def comment_list_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CommentListReportRequest,
        tmp_header: aliding_20230426_models.CommentListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CommentListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CommentListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CommentListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='CommentListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/commentListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CommentListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def comment_list_report(
        self,
        request: aliding_20230426_models.CommentListReportRequest,
    ) -> aliding_20230426_models.CommentListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CommentListReportHeaders()
        return self.comment_list_report_with_options(request, headers, runtime)

    async def comment_list_report_async(
        self,
        request: aliding_20230426_models.CommentListReportRequest,
    ) -> aliding_20230426_models.CommentListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CommentListReportHeaders()
        return await self.comment_list_report_with_options_async(request, headers, runtime)

    def create_event_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateEventRequest,
        tmp_header: aliding_20230426_models.CreateEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateEventResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.online_meeting_info):
            request.online_meeting_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.online_meeting_info, 'OnlineMeetingInfo', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.ui_configs):
            request.ui_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ui_configs, 'UiConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.online_meeting_info_shrink):
            body['OnlineMeetingInfo'] = request.online_meeting_info_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs_shrink):
            body['UiConfigs'] = request.ui_configs_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['calendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.start_shrink):
            body['start'] = request.start_shrink
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
            action='CreateEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/createEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateEventRequest,
        tmp_header: aliding_20230426_models.CreateEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateEventResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.online_meeting_info):
            request.online_meeting_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.online_meeting_info, 'OnlineMeetingInfo', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.ui_configs):
            request.ui_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ui_configs, 'UiConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.online_meeting_info_shrink):
            body['OnlineMeetingInfo'] = request.online_meeting_info_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs_shrink):
            body['UiConfigs'] = request.ui_configs_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['calendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.start_shrink):
            body['start'] = request.start_shrink
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
            action='CreateEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/createEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event(
        self,
        request: aliding_20230426_models.CreateEventRequest,
    ) -> aliding_20230426_models.CreateEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateEventHeaders()
        return self.create_event_with_options(request, headers, runtime)

    async def create_event_async(
        self,
        request: aliding_20230426_models.CreateEventRequest,
    ) -> aliding_20230426_models.CreateEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateEventHeaders()
        return await self.create_event_with_options_async(request, headers, runtime)

    def create_live_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateLiveRequest,
        tmp_header: aliding_20230426_models.CreateLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.public_type):
            body['PublicType'] = request.public_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='CreateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateLiveRequest,
        tmp_header: aliding_20230426_models.CreateLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.public_type):
            body['PublicType'] = request.public_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='CreateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live(
        self,
        request: aliding_20230426_models.CreateLiveRequest,
    ) -> aliding_20230426_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateLiveHeaders()
        return self.create_live_with_options(request, headers, runtime)

    async def create_live_async(
        self,
        request: aliding_20230426_models.CreateLiveRequest,
    ) -> aliding_20230426_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateLiveHeaders()
        return await self.create_live_with_options_async(request, headers, runtime)

    def create_meeting_room_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateMeetingRoomRequest,
        tmp_header: aliding_20230426_models.CreateMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
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
            action='CreateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meeting_room_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateMeetingRoomRequest,
        tmp_header: aliding_20230426_models.CreateMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
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
            action='CreateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_meeting_room(
        self,
        request: aliding_20230426_models.CreateMeetingRoomRequest,
    ) -> aliding_20230426_models.CreateMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomHeaders()
        return self.create_meeting_room_with_options(request, headers, runtime)

    async def create_meeting_room_async(
        self,
        request: aliding_20230426_models.CreateMeetingRoomRequest,
    ) -> aliding_20230426_models.CreateMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomHeaders()
        return await self.create_meeting_room_with_options_async(request, headers, runtime)

    def create_meeting_room_group_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.CreateMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['ParentGroupId'] = request.parent_group_id
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
            action='CreateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meeting_room_group_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.CreateMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['ParentGroupId'] = request.parent_group_id
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
            action='CreateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_meeting_room_group(
        self,
        request: aliding_20230426_models.CreateMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.CreateMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomGroupHeaders()
        return self.create_meeting_room_group_with_options(request, headers, runtime)

    async def create_meeting_room_group_async(
        self,
        request: aliding_20230426_models.CreateMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.CreateMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomGroupHeaders()
        return await self.create_meeting_room_group_with_options_async(request, headers, runtime)

    def create_report_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateReportRequest,
        tmp_header: aliding_20230426_models.CreateReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.to_cids):
            request.to_cids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_cids, 'ToCids', 'json')
        if not UtilClient.is_unset(tmp_req.to_userids):
            request.to_userids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_userids, 'ToUserids', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.to_chat):
            body['ToChat'] = request.to_chat
        if not UtilClient.is_unset(request.to_cids_shrink):
            body['ToCids'] = request.to_cids_shrink
        if not UtilClient.is_unset(request.to_userids_shrink):
            body['ToUserids'] = request.to_userids_shrink
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
            action='CreateReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/createReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateReportRequest,
        tmp_header: aliding_20230426_models.CreateReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.to_cids):
            request.to_cids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_cids, 'ToCids', 'json')
        if not UtilClient.is_unset(tmp_req.to_userids):
            request.to_userids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_userids, 'ToUserids', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.to_chat):
            body['ToChat'] = request.to_chat
        if not UtilClient.is_unset(request.to_cids_shrink):
            body['ToCids'] = request.to_cids_shrink
        if not UtilClient.is_unset(request.to_userids_shrink):
            body['ToUserids'] = request.to_userids_shrink
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
            action='CreateReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/createReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_report(
        self,
        request: aliding_20230426_models.CreateReportRequest,
    ) -> aliding_20230426_models.CreateReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateReportHeaders()
        return self.create_report_with_options(request, headers, runtime)

    async def create_report_async(
        self,
        request: aliding_20230426_models.CreateReportRequest,
    ) -> aliding_20230426_models.CreateReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateReportHeaders()
        return await self.create_report_with_options_async(request, headers, runtime)

    def create_schedule_conference_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.CreateScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='CreateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_conference_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.CreateScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='CreateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule_conference(
        self,
        request: aliding_20230426_models.CreateScheduleConferenceRequest,
    ) -> aliding_20230426_models.CreateScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateScheduleConferenceHeaders()
        return self.create_schedule_conference_with_options(request, headers, runtime)

    async def create_schedule_conference_async(
        self,
        request: aliding_20230426_models.CreateScheduleConferenceRequest,
    ) -> aliding_20230426_models.CreateScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateScheduleConferenceHeaders()
        return await self.create_schedule_conference_with_options_async(request, headers, runtime)

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

    def create_video_conference_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateVideoConferenceRequest,
        tmp_header: aliding_20230426_models.CreateVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateVideoConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateVideoConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateVideoConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invite_user_ids):
            request.invite_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invite_user_ids, 'InviteUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['ConfTitle'] = request.conf_title
        if not UtilClient.is_unset(request.invite_caller):
            body['InviteCaller'] = request.invite_caller
        if not UtilClient.is_unset(request.invite_user_ids_shrink):
            body['InviteUserIds'] = request.invite_user_ids_shrink
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
            action='CreateVideoConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createVideoConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateVideoConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_conference_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateVideoConferenceRequest,
        tmp_header: aliding_20230426_models.CreateVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateVideoConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateVideoConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateVideoConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invite_user_ids):
            request.invite_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invite_user_ids, 'InviteUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['ConfTitle'] = request.conf_title
        if not UtilClient.is_unset(request.invite_caller):
            body['InviteCaller'] = request.invite_caller
        if not UtilClient.is_unset(request.invite_user_ids_shrink):
            body['InviteUserIds'] = request.invite_user_ids_shrink
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
            action='CreateVideoConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/createVideoConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateVideoConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_conference(
        self,
        request: aliding_20230426_models.CreateVideoConferenceRequest,
    ) -> aliding_20230426_models.CreateVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateVideoConferenceHeaders()
        return self.create_video_conference_with_options(request, headers, runtime)

    async def create_video_conference_async(
        self,
        request: aliding_20230426_models.CreateVideoConferenceRequest,
    ) -> aliding_20230426_models.CreateVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateVideoConferenceHeaders()
        return await self.create_video_conference_with_options_async(request, headers, runtime)

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

    def delete_columns_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteColumnsRequest,
        tmp_header: aliding_20230426_models.DeleteColumnsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteColumnsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteColumnsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteColumnsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
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
            action='DeleteColumns',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteColumns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_columns_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteColumnsRequest,
        tmp_header: aliding_20230426_models.DeleteColumnsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteColumnsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteColumnsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteColumnsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
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
            action='DeleteColumns',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteColumns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_columns(
        self,
        request: aliding_20230426_models.DeleteColumnsRequest,
    ) -> aliding_20230426_models.DeleteColumnsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteColumnsHeaders()
        return self.delete_columns_with_options(request, headers, runtime)

    async def delete_columns_async(
        self,
        request: aliding_20230426_models.DeleteColumnsRequest,
    ) -> aliding_20230426_models.DeleteColumnsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteColumnsHeaders()
        return await self.delete_columns_with_options_async(request, headers, runtime)

    def delete_event_with_options(
        self,
        request: aliding_20230426_models.DeleteEventRequest,
        tmp_header: aliding_20230426_models.DeleteEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteEventResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='DeleteEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/deleteEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_with_options_async(
        self,
        request: aliding_20230426_models.DeleteEventRequest,
        tmp_header: aliding_20230426_models.DeleteEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteEventResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='DeleteEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/deleteEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event(
        self,
        request: aliding_20230426_models.DeleteEventRequest,
    ) -> aliding_20230426_models.DeleteEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteEventHeaders()
        return self.delete_event_with_options(request, headers, runtime)

    async def delete_event_async(
        self,
        request: aliding_20230426_models.DeleteEventRequest,
    ) -> aliding_20230426_models.DeleteEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteEventHeaders()
        return await self.delete_event_with_options_async(request, headers, runtime)

    def delete_live_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteLiveRequest,
        tmp_header: aliding_20230426_models.DeleteLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='DeleteLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteLiveRequest,
        tmp_header: aliding_20230426_models.DeleteLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='DeleteLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live(
        self,
        request: aliding_20230426_models.DeleteLiveRequest,
    ) -> aliding_20230426_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteLiveHeaders()
        return self.delete_live_with_options(request, headers, runtime)

    async def delete_live_async(
        self,
        request: aliding_20230426_models.DeleteLiveRequest,
    ) -> aliding_20230426_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteLiveHeaders()
        return await self.delete_live_with_options_async(request, headers, runtime)

    def delete_meeting_room_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteMeetingRoomRequest,
        tmp_header: aliding_20230426_models.DeleteMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
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
            action='DeleteMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_meeting_room_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteMeetingRoomRequest,
        tmp_header: aliding_20230426_models.DeleteMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
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
            action='DeleteMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_meeting_room(
        self,
        request: aliding_20230426_models.DeleteMeetingRoomRequest,
    ) -> aliding_20230426_models.DeleteMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomHeaders()
        return self.delete_meeting_room_with_options(request, headers, runtime)

    async def delete_meeting_room_async(
        self,
        request: aliding_20230426_models.DeleteMeetingRoomRequest,
    ) -> aliding_20230426_models.DeleteMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomHeaders()
        return await self.delete_meeting_room_with_options_async(request, headers, runtime)

    def delete_meeting_room_group_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.DeleteMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
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
            action='DeleteMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_meeting_room_group_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.DeleteMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
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
            action='DeleteMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/deleteMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_meeting_room_group(
        self,
        request: aliding_20230426_models.DeleteMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.DeleteMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomGroupHeaders()
        return self.delete_meeting_room_group_with_options(request, headers, runtime)

    async def delete_meeting_room_group_async(
        self,
        request: aliding_20230426_models.DeleteMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.DeleteMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomGroupHeaders()
        return await self.delete_meeting_room_group_with_options_async(request, headers, runtime)

    def delete_rows_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteRowsRequest,
        tmp_header: aliding_20230426_models.DeleteRowsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteRowsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteRowsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteRowsShrinkHeaders()
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
            action='DeleteRows',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteRows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteRowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rows_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteRowsRequest,
        tmp_header: aliding_20230426_models.DeleteRowsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteRowsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteRowsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteRowsShrinkHeaders()
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
            action='DeleteRows',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteRows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteRowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rows(
        self,
        request: aliding_20230426_models.DeleteRowsRequest,
    ) -> aliding_20230426_models.DeleteRowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteRowsHeaders()
        return self.delete_rows_with_options(request, headers, runtime)

    async def delete_rows_async(
        self,
        request: aliding_20230426_models.DeleteRowsRequest,
    ) -> aliding_20230426_models.DeleteRowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteRowsHeaders()
        return await self.delete_rows_with_options_async(request, headers, runtime)

    def delete_sheet_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteSheetRequest,
        tmp_header: aliding_20230426_models.DeleteSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='DeleteSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sheet_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteSheetRequest,
        tmp_header: aliding_20230426_models.DeleteSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='DeleteSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sheet(
        self,
        request: aliding_20230426_models.DeleteSheetRequest,
    ) -> aliding_20230426_models.DeleteSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteSheetHeaders()
        return self.delete_sheet_with_options(request, headers, runtime)

    async def delete_sheet_async(
        self,
        request: aliding_20230426_models.DeleteSheetRequest,
    ) -> aliding_20230426_models.DeleteSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteSheetHeaders()
        return await self.delete_sheet_with_options_async(request, headers, runtime)

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

    def get_all_sheets_with_options(
        self,
        tmp_req: aliding_20230426_models.GetAllSheetsRequest,
        tmp_header: aliding_20230426_models.GetAllSheetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetAllSheetsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetAllSheetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetAllSheetsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='GetAllSheets',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getAllSheets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetAllSheetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_sheets_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetAllSheetsRequest,
        tmp_header: aliding_20230426_models.GetAllSheetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetAllSheetsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetAllSheetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetAllSheetsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='GetAllSheets',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getAllSheets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetAllSheetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_sheets(
        self,
        request: aliding_20230426_models.GetAllSheetsRequest,
    ) -> aliding_20230426_models.GetAllSheetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetAllSheetsHeaders()
        return self.get_all_sheets_with_options(request, headers, runtime)

    async def get_all_sheets_async(
        self,
        request: aliding_20230426_models.GetAllSheetsRequest,
    ) -> aliding_20230426_models.GetAllSheetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetAllSheetsHeaders()
        return await self.get_all_sheets_with_options_async(request, headers, runtime)

    def get_event_with_options(
        self,
        request: aliding_20230426_models.GetEventRequest,
        tmp_header: aliding_20230426_models.GetEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetEventResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['MaxAttendees'] = request.max_attendees
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='GetEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/getEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_with_options_async(
        self,
        request: aliding_20230426_models.GetEventRequest,
        tmp_header: aliding_20230426_models.GetEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetEventResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['MaxAttendees'] = request.max_attendees
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='GetEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/getEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event(
        self,
        request: aliding_20230426_models.GetEventRequest,
    ) -> aliding_20230426_models.GetEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetEventHeaders()
        return self.get_event_with_options(request, headers, runtime)

    async def get_event_async(
        self,
        request: aliding_20230426_models.GetEventRequest,
    ) -> aliding_20230426_models.GetEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetEventHeaders()
        return await self.get_event_with_options_async(request, headers, runtime)

    def get_mine_workspace_with_options(
        self,
        tmp_req: aliding_20230426_models.GetMineWorkspaceRequest,
        tmp_header: aliding_20230426_models.GetMineWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetMineWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetMineWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetMineWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='GetMineWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getMineWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetMineWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mine_workspace_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetMineWorkspaceRequest,
        tmp_header: aliding_20230426_models.GetMineWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetMineWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetMineWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetMineWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='GetMineWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getMineWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetMineWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mine_workspace(
        self,
        request: aliding_20230426_models.GetMineWorkspaceRequest,
    ) -> aliding_20230426_models.GetMineWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetMineWorkspaceHeaders()
        return self.get_mine_workspace_with_options(request, headers, runtime)

    async def get_mine_workspace_async(
        self,
        request: aliding_20230426_models.GetMineWorkspaceRequest,
    ) -> aliding_20230426_models.GetMineWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetMineWorkspaceHeaders()
        return await self.get_mine_workspace_with_options_async(request, headers, runtime)

    def get_node_with_options(
        self,
        tmp_req: aliding_20230426_models.GetNodeRequest,
        tmp_header: aliding_20230426_models.GetNodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        if not UtilClient.is_unset(request.with_statistical_info):
            body['WithStatisticalInfo'] = request.with_statistical_info
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
            action='GetNode',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetNodeRequest,
        tmp_header: aliding_20230426_models.GetNodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        if not UtilClient.is_unset(request.with_statistical_info):
            body['WithStatisticalInfo'] = request.with_statistical_info
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
            action='GetNode',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node(
        self,
        request: aliding_20230426_models.GetNodeRequest,
    ) -> aliding_20230426_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeHeaders()
        return self.get_node_with_options(request, headers, runtime)

    async def get_node_async(
        self,
        request: aliding_20230426_models.GetNodeRequest,
    ) -> aliding_20230426_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeHeaders()
        return await self.get_node_with_options_async(request, headers, runtime)

    def get_node_by_url_with_options(
        self,
        tmp_req: aliding_20230426_models.GetNodeByUrlRequest,
        tmp_header: aliding_20230426_models.GetNodeByUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodeByUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeByUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeByUrlShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
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
            action='GetNodeByUrl',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNodeByUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeByUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_by_url_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetNodeByUrlRequest,
        tmp_header: aliding_20230426_models.GetNodeByUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodeByUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeByUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeByUrlShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
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
            action='GetNodeByUrl',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNodeByUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeByUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_by_url(
        self,
        request: aliding_20230426_models.GetNodeByUrlRequest,
    ) -> aliding_20230426_models.GetNodeByUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeByUrlHeaders()
        return self.get_node_by_url_with_options(request, headers, runtime)

    async def get_node_by_url_async(
        self,
        request: aliding_20230426_models.GetNodeByUrlRequest,
    ) -> aliding_20230426_models.GetNodeByUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeByUrlHeaders()
        return await self.get_node_by_url_with_options_async(request, headers, runtime)

    def get_nodes_with_options(
        self,
        tmp_req: aliding_20230426_models.GetNodesRequest,
        tmp_header: aliding_20230426_models.GetNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
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
            action='GetNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nodes_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetNodesRequest,
        tmp_header: aliding_20230426_models.GetNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
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
            action='GetNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nodes(
        self,
        request: aliding_20230426_models.GetNodesRequest,
    ) -> aliding_20230426_models.GetNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodesHeaders()
        return self.get_nodes_with_options(request, headers, runtime)

    async def get_nodes_async(
        self,
        request: aliding_20230426_models.GetNodesRequest,
    ) -> aliding_20230426_models.GetNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodesHeaders()
        return await self.get_nodes_with_options_async(request, headers, runtime)

    def get_range_with_options(
        self,
        tmp_req: aliding_20230426_models.GetRangeRequest,
        tmp_header: aliding_20230426_models.GetRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetRangeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.select):
            body['Select'] = request.select
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
            action='GetRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_range_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetRangeRequest,
        tmp_header: aliding_20230426_models.GetRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetRangeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.select):
            body['Select'] = request.select
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
            action='GetRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_range(
        self,
        request: aliding_20230426_models.GetRangeRequest,
    ) -> aliding_20230426_models.GetRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetRangeHeaders()
        return self.get_range_with_options(request, headers, runtime)

    async def get_range_async(
        self,
        request: aliding_20230426_models.GetRangeRequest,
    ) -> aliding_20230426_models.GetRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetRangeHeaders()
        return await self.get_range_with_options_async(request, headers, runtime)

    def get_report_template_by_name_with_options(
        self,
        tmp_req: aliding_20230426_models.GetReportTemplateByNameRequest,
        tmp_header: aliding_20230426_models.GetReportTemplateByNameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetReportTemplateByNameResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportTemplateByNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportTemplateByNameShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='GetReportTemplateByName',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getReportTemplateByName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportTemplateByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_template_by_name_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetReportTemplateByNameRequest,
        tmp_header: aliding_20230426_models.GetReportTemplateByNameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetReportTemplateByNameResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportTemplateByNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportTemplateByNameShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='GetReportTemplateByName',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getReportTemplateByName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportTemplateByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_template_by_name(
        self,
        request: aliding_20230426_models.GetReportTemplateByNameRequest,
    ) -> aliding_20230426_models.GetReportTemplateByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportTemplateByNameHeaders()
        return self.get_report_template_by_name_with_options(request, headers, runtime)

    async def get_report_template_by_name_async(
        self,
        request: aliding_20230426_models.GetReportTemplateByNameRequest,
    ) -> aliding_20230426_models.GetReportTemplateByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportTemplateByNameHeaders()
        return await self.get_report_template_by_name_with_options_async(request, headers, runtime)

    def get_report_un_read_count_with_options(
        self,
        tmp_req: aliding_20230426_models.GetReportUnReadCountRequest,
        tmp_header: aliding_20230426_models.GetReportUnReadCountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetReportUnReadCountResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportUnReadCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportUnReadCountShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='GetReportUnReadCount',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getReportUnReadCount',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportUnReadCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_un_read_count_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetReportUnReadCountRequest,
        tmp_header: aliding_20230426_models.GetReportUnReadCountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetReportUnReadCountResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportUnReadCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportUnReadCountShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='GetReportUnReadCount',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getReportUnReadCount',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportUnReadCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_un_read_count(
        self,
        request: aliding_20230426_models.GetReportUnReadCountRequest,
    ) -> aliding_20230426_models.GetReportUnReadCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportUnReadCountHeaders()
        return self.get_report_un_read_count_with_options(request, headers, runtime)

    async def get_report_un_read_count_async(
        self,
        request: aliding_20230426_models.GetReportUnReadCountRequest,
    ) -> aliding_20230426_models.GetReportUnReadCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportUnReadCountHeaders()
        return await self.get_report_un_read_count_with_options_async(request, headers, runtime)

    def get_sheet_with_options(
        self,
        tmp_req: aliding_20230426_models.GetSheetRequest,
        tmp_header: aliding_20230426_models.GetSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='GetSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sheet_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetSheetRequest,
        tmp_header: aliding_20230426_models.GetSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
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
            action='GetSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/getSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sheet(
        self,
        request: aliding_20230426_models.GetSheetRequest,
    ) -> aliding_20230426_models.GetSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSheetHeaders()
        return self.get_sheet_with_options(request, headers, runtime)

    async def get_sheet_async(
        self,
        request: aliding_20230426_models.GetSheetRequest,
    ) -> aliding_20230426_models.GetSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSheetHeaders()
        return await self.get_sheet_with_options_async(request, headers, runtime)

    def get_space_directories_with_options(
        self,
        tmp_req: aliding_20230426_models.GetSpaceDirectoriesRequest,
        tmp_header: aliding_20230426_models.GetSpaceDirectoriesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetSpaceDirectoriesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSpaceDirectoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSpaceDirectoriesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
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
            action='GetSpaceDirectories',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getSpaceDirectories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSpaceDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_space_directories_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetSpaceDirectoriesRequest,
        tmp_header: aliding_20230426_models.GetSpaceDirectoriesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetSpaceDirectoriesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSpaceDirectoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSpaceDirectoriesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
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
            action='GetSpaceDirectories',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getSpaceDirectories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSpaceDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_space_directories(
        self,
        request: aliding_20230426_models.GetSpaceDirectoriesRequest,
    ) -> aliding_20230426_models.GetSpaceDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSpaceDirectoriesHeaders()
        return self.get_space_directories_with_options(request, headers, runtime)

    async def get_space_directories_async(
        self,
        request: aliding_20230426_models.GetSpaceDirectoriesRequest,
    ) -> aliding_20230426_models.GetSpaceDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSpaceDirectoriesHeaders()
        return await self.get_space_directories_with_options_async(request, headers, runtime)

    def get_template_list_by_user_id_with_options(
        self,
        tmp_req: aliding_20230426_models.GetTemplateListByUserIdRequest,
        tmp_header: aliding_20230426_models.GetTemplateListByUserIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetTemplateListByUserIdResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetTemplateListByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetTemplateListByUserIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='GetTemplateListByUserId',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getTemplateListByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetTemplateListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_list_by_user_id_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetTemplateListByUserIdRequest,
        tmp_header: aliding_20230426_models.GetTemplateListByUserIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetTemplateListByUserIdResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetTemplateListByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetTemplateListByUserIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='GetTemplateListByUserId',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/getTemplateListByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetTemplateListByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_list_by_user_id(
        self,
        request: aliding_20230426_models.GetTemplateListByUserIdRequest,
    ) -> aliding_20230426_models.GetTemplateListByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetTemplateListByUserIdHeaders()
        return self.get_template_list_by_user_id_with_options(request, headers, runtime)

    async def get_template_list_by_user_id_async(
        self,
        request: aliding_20230426_models.GetTemplateListByUserIdRequest,
    ) -> aliding_20230426_models.GetTemplateListByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetTemplateListByUserIdHeaders()
        return await self.get_template_list_by_user_id_with_options_async(request, headers, runtime)

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

    def get_workspace_with_options(
        self,
        tmp_req: aliding_20230426_models.GetWorkspaceRequest,
        tmp_header: aliding_20230426_models.GetWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='GetWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetWorkspaceRequest,
        tmp_header: aliding_20230426_models.GetWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='GetWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        request: aliding_20230426_models.GetWorkspaceRequest,
    ) -> aliding_20230426_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspaceHeaders()
        return self.get_workspace_with_options(request, headers, runtime)

    async def get_workspace_async(
        self,
        request: aliding_20230426_models.GetWorkspaceRequest,
    ) -> aliding_20230426_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspaceHeaders()
        return await self.get_workspace_with_options_async(request, headers, runtime)

    def get_workspaces_with_options(
        self,
        tmp_req: aliding_20230426_models.GetWorkspacesRequest,
        tmp_header: aliding_20230426_models.GetWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.workspace_ids):
            request.workspace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_ids, 'WorkspaceIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_ids_shrink):
            body['WorkspaceIds'] = request.workspace_ids_shrink
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
            action='GetWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspaces_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetWorkspacesRequest,
        tmp_header: aliding_20230426_models.GetWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.workspace_ids):
            request.workspace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_ids, 'WorkspaceIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_ids_shrink):
            body['WorkspaceIds'] = request.workspace_ids_shrink
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
            action='GetWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/getWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspaces(
        self,
        request: aliding_20230426_models.GetWorkspacesRequest,
    ) -> aliding_20230426_models.GetWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspacesHeaders()
        return self.get_workspaces_with_options(request, headers, runtime)

    async def get_workspaces_async(
        self,
        request: aliding_20230426_models.GetWorkspacesRequest,
    ) -> aliding_20230426_models.GetWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspacesHeaders()
        return await self.get_workspaces_with_options_async(request, headers, runtime)

    def insert_columns_before_with_options(
        self,
        tmp_req: aliding_20230426_models.InsertColumnsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertColumnsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertColumnsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertColumnsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertColumnsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
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
            action='InsertColumnsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertColumnsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertColumnsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_columns_before_with_options_async(
        self,
        tmp_req: aliding_20230426_models.InsertColumnsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertColumnsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertColumnsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertColumnsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertColumnsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
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
            action='InsertColumnsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertColumnsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertColumnsBeforeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_columns_before(
        self,
        request: aliding_20230426_models.InsertColumnsBeforeRequest,
    ) -> aliding_20230426_models.InsertColumnsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertColumnsBeforeHeaders()
        return self.insert_columns_before_with_options(request, headers, runtime)

    async def insert_columns_before_async(
        self,
        request: aliding_20230426_models.InsertColumnsBeforeRequest,
    ) -> aliding_20230426_models.InsertColumnsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertColumnsBeforeHeaders()
        return await self.insert_columns_before_with_options_async(request, headers, runtime)

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

    def invite_users_with_options(
        self,
        tmp_req: aliding_20230426_models.InviteUsersRequest,
        tmp_header: aliding_20230426_models.InviteUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InviteUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InviteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InviteUsersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invitee_list):
            request.invitee_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invitee_list, 'InviteeList', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.invitee_list_shrink):
            body['InviteeList'] = request.invitee_list_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='InviteUsers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/inviteUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InviteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_users_with_options_async(
        self,
        tmp_req: aliding_20230426_models.InviteUsersRequest,
        tmp_header: aliding_20230426_models.InviteUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InviteUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InviteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InviteUsersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invitee_list):
            request.invitee_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invitee_list, 'InviteeList', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.invitee_list_shrink):
            body['InviteeList'] = request.invitee_list_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='InviteUsers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/inviteUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InviteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_users(
        self,
        request: aliding_20230426_models.InviteUsersRequest,
    ) -> aliding_20230426_models.InviteUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InviteUsersHeaders()
        return self.invite_users_with_options(request, headers, runtime)

    async def invite_users_async(
        self,
        request: aliding_20230426_models.InviteUsersRequest,
    ) -> aliding_20230426_models.InviteUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InviteUsersHeaders()
        return await self.invite_users_with_options_async(request, headers, runtime)

    def list_calendars_with_options(
        self,
        tmp_req: aliding_20230426_models.ListCalendarsRequest,
        tmp_header: aliding_20230426_models.ListCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListCalendarsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListCalendarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListCalendarsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='ListCalendars',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/listCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calendars_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ListCalendarsRequest,
        tmp_header: aliding_20230426_models.ListCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListCalendarsResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListCalendarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListCalendarsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='ListCalendars',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/listCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListCalendarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calendars(
        self,
        request: aliding_20230426_models.ListCalendarsRequest,
    ) -> aliding_20230426_models.ListCalendarsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListCalendarsHeaders()
        return self.list_calendars_with_options(request, headers, runtime)

    async def list_calendars_async(
        self,
        request: aliding_20230426_models.ListCalendarsRequest,
    ) -> aliding_20230426_models.ListCalendarsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListCalendarsHeaders()
        return await self.list_calendars_with_options_async(request, headers, runtime)

    def list_events_with_options(
        self,
        request: aliding_20230426_models.ListEventsRequest,
        tmp_header: aliding_20230426_models.ListEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListEventsResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListEventsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.max_attendees):
            body['MaxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.series_master_id):
            body['SeriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.show_deleted):
            body['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.sync_token):
            body['SyncToken'] = request.sync_token
        if not UtilClient.is_unset(request.time_max):
            body['TimeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            body['TimeMin'] = request.time_min
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
            action='ListEvents',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/listEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_events_with_options_async(
        self,
        request: aliding_20230426_models.ListEventsRequest,
        tmp_header: aliding_20230426_models.ListEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListEventsResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListEventsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.max_attendees):
            body['MaxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.series_master_id):
            body['SeriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.show_deleted):
            body['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.sync_token):
            body['SyncToken'] = request.sync_token
        if not UtilClient.is_unset(request.time_max):
            body['TimeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            body['TimeMin'] = request.time_min
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
            action='ListEvents',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/listEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_events(
        self,
        request: aliding_20230426_models.ListEventsRequest,
    ) -> aliding_20230426_models.ListEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListEventsHeaders()
        return self.list_events_with_options(request, headers, runtime)

    async def list_events_async(
        self,
        request: aliding_20230426_models.ListEventsRequest,
    ) -> aliding_20230426_models.ListEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListEventsHeaders()
        return await self.list_events_with_options_async(request, headers, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: aliding_20230426_models.ListNodesRequest,
        tmp_header: aliding_20230426_models.ListNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='ListNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/listNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ListNodesRequest,
        tmp_header: aliding_20230426_models.ListNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='ListNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/listNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: aliding_20230426_models.ListNodesRequest,
    ) -> aliding_20230426_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListNodesHeaders()
        return self.list_nodes_with_options(request, headers, runtime)

    async def list_nodes_async(
        self,
        request: aliding_20230426_models.ListNodesRequest,
    ) -> aliding_20230426_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListNodesHeaders()
        return await self.list_nodes_with_options_async(request, headers, runtime)

    def list_report_with_options(
        self,
        tmp_req: aliding_20230426_models.ListReportRequest,
        tmp_header: aliding_20230426_models.ListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.modified_end_time):
            body['ModifiedEndTime'] = request.modified_end_time
        if not UtilClient.is_unset(request.modified_start_time):
            body['ModifiedStartTime'] = request.modified_start_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='ListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/listReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ListReportRequest,
        tmp_header: aliding_20230426_models.ListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.modified_end_time):
            body['ModifiedEndTime'] = request.modified_end_time
        if not UtilClient.is_unset(request.modified_start_time):
            body['ModifiedStartTime'] = request.modified_start_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='ListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/listReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_report(
        self,
        request: aliding_20230426_models.ListReportRequest,
    ) -> aliding_20230426_models.ListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListReportHeaders()
        return self.list_report_with_options(request, headers, runtime)

    async def list_report_async(
        self,
        request: aliding_20230426_models.ListReportRequest,
    ) -> aliding_20230426_models.ListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListReportHeaders()
        return await self.list_report_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: aliding_20230426_models.ListWorkspacesRequest,
        tmp_header: aliding_20230426_models.ListWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.team_id):
            body['TeamId'] = request.team_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='ListWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/listWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ListWorkspacesRequest,
        tmp_header: aliding_20230426_models.ListWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.team_id):
            body['TeamId'] = request.team_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
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
            action='ListWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/listWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: aliding_20230426_models.ListWorkspacesRequest,
    ) -> aliding_20230426_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListWorkspacesHeaders()
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: aliding_20230426_models.ListWorkspacesRequest,
    ) -> aliding_20230426_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListWorkspacesHeaders()
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def patch_event_with_options(
        self,
        tmp_req: aliding_20230426_models.PatchEventRequest,
        tmp_header: aliding_20230426_models.PatchEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.PatchEventResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.PatchEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.PatchEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'Start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.start_shrink):
            body['Start'] = request.start_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
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
            action='PatchEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/patchEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.PatchEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def patch_event_with_options_async(
        self,
        tmp_req: aliding_20230426_models.PatchEventRequest,
        tmp_header: aliding_20230426_models.PatchEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.PatchEventResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.PatchEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.PatchEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'Start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.start_shrink):
            body['Start'] = request.start_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
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
            action='PatchEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/patchEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.PatchEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def patch_event(
        self,
        request: aliding_20230426_models.PatchEventRequest,
    ) -> aliding_20230426_models.PatchEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.PatchEventHeaders()
        return self.patch_event_with_options(request, headers, runtime)

    async def patch_event_async(
        self,
        request: aliding_20230426_models.PatchEventRequest,
    ) -> aliding_20230426_models.PatchEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.PatchEventHeaders()
        return await self.patch_event_with_options_async(request, headers, runtime)

    def query_cloud_record_text_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordTextRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordTextResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordTextShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.direction):
            body['Direction'] = request.direction
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryCloudRecordText',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_text_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordTextRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordTextResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordTextShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.direction):
            body['Direction'] = request.direction
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryCloudRecordText',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_text(
        self,
        request: aliding_20230426_models.QueryCloudRecordTextRequest,
    ) -> aliding_20230426_models.QueryCloudRecordTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordTextHeaders()
        return self.query_cloud_record_text_with_options(request, headers, runtime)

    async def query_cloud_record_text_async(
        self,
        request: aliding_20230426_models.QueryCloudRecordTextRequest,
    ) -> aliding_20230426_models.QueryCloudRecordTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordTextHeaders()
        return await self.query_cloud_record_text_with_options_async(request, headers, runtime)

    def query_cloud_record_video_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordVideoRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordVideoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordVideoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryCloudRecordVideo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordVideo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_video_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordVideoRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordVideoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordVideoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryCloudRecordVideo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordVideo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_video(
        self,
        request: aliding_20230426_models.QueryCloudRecordVideoRequest,
    ) -> aliding_20230426_models.QueryCloudRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoHeaders()
        return self.query_cloud_record_video_with_options(request, headers, runtime)

    async def query_cloud_record_video_async(
        self,
        request: aliding_20230426_models.QueryCloudRecordVideoRequest,
    ) -> aliding_20230426_models.QueryCloudRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoHeaders()
        return await self.query_cloud_record_video_with_options_async(request, headers, runtime)

    def query_cloud_record_video_play_info_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordVideoPlayInfoRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordVideoPlayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
            action='QueryCloudRecordVideoPlayInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordVideoPlayInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_video_play_info_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryCloudRecordVideoPlayInfoRequest,
        tmp_header: aliding_20230426_models.QueryCloudRecordVideoPlayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
            action='QueryCloudRecordVideoPlayInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryCloudRecordVideoPlayInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_video_play_info(
        self,
        request: aliding_20230426_models.QueryCloudRecordVideoPlayInfoRequest,
    ) -> aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoHeaders()
        return self.query_cloud_record_video_play_info_with_options(request, headers, runtime)

    async def query_cloud_record_video_play_info_async(
        self,
        request: aliding_20230426_models.QueryCloudRecordVideoPlayInfoRequest,
    ) -> aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoHeaders()
        return await self.query_cloud_record_video_play_info_with_options_async(request, headers, runtime)

    def query_conference_info_with_options(
        self,
        request: aliding_20230426_models.QueryConferenceInfoRequest,
        tmp_header: aliding_20230426_models.QueryConferenceInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryConferenceInfoResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.QueryConferenceInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryConferenceInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryConferenceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conference_info_with_options_async(
        self,
        request: aliding_20230426_models.QueryConferenceInfoRequest,
        tmp_header: aliding_20230426_models.QueryConferenceInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryConferenceInfoResponse:
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.QueryConferenceInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryConferenceInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryConferenceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conference_info(
        self,
        request: aliding_20230426_models.QueryConferenceInfoRequest,
    ) -> aliding_20230426_models.QueryConferenceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceInfoHeaders()
        return self.query_conference_info_with_options(request, headers, runtime)

    async def query_conference_info_async(
        self,
        request: aliding_20230426_models.QueryConferenceInfoRequest,
    ) -> aliding_20230426_models.QueryConferenceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceInfoHeaders()
        return await self.query_conference_info_with_options_async(request, headers, runtime)

    def query_conference_members_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryConferenceMembersRequest,
        tmp_header: aliding_20230426_models.QueryConferenceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryConferenceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryConferenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryConferenceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryConferenceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryConferenceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conference_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryConferenceMembersRequest,
        tmp_header: aliding_20230426_models.QueryConferenceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryConferenceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryConferenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryConferenceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='QueryConferenceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryConferenceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conference_members(
        self,
        request: aliding_20230426_models.QueryConferenceMembersRequest,
    ) -> aliding_20230426_models.QueryConferenceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceMembersHeaders()
        return self.query_conference_members_with_options(request, headers, runtime)

    async def query_conference_members_async(
        self,
        request: aliding_20230426_models.QueryConferenceMembersRequest,
    ) -> aliding_20230426_models.QueryConferenceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceMembersHeaders()
        return await self.query_conference_members_with_options_async(request, headers, runtime)

    def query_dentry_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryDentryRequest,
        tmp_header: aliding_20230426_models.QueryDentryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryDentryResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryDentryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryDentryShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.include_space):
            body['IncludeSpace'] = request.include_space
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
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
            action='QueryDentry',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/queryDentry',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryDentryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dentry_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryDentryRequest,
        tmp_header: aliding_20230426_models.QueryDentryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryDentryResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryDentryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryDentryShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.include_space):
            body['IncludeSpace'] = request.include_space
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
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
            action='QueryDentry',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v2/documents/queryDentry',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryDentryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dentry(
        self,
        request: aliding_20230426_models.QueryDentryRequest,
    ) -> aliding_20230426_models.QueryDentryResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryDentryHeaders()
        return self.query_dentry_with_options(request, headers, runtime)

    async def query_dentry_async(
        self,
        request: aliding_20230426_models.QueryDentryRequest,
    ) -> aliding_20230426_models.QueryDentryResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryDentryHeaders()
        return await self.query_dentry_with_options_async(request, headers, runtime)

    def query_live_info_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryLiveInfoRequest,
        tmp_header: aliding_20230426_models.QueryLiveInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='QueryLiveInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_info_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryLiveInfoRequest,
        tmp_header: aliding_20230426_models.QueryLiveInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='QueryLiveInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_info(
        self,
        request: aliding_20230426_models.QueryLiveInfoRequest,
    ) -> aliding_20230426_models.QueryLiveInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveInfoHeaders()
        return self.query_live_info_with_options(request, headers, runtime)

    async def query_live_info_async(
        self,
        request: aliding_20230426_models.QueryLiveInfoRequest,
    ) -> aliding_20230426_models.QueryLiveInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveInfoHeaders()
        return await self.query_live_info_with_options_async(request, headers, runtime)

    def query_live_watch_detail_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryLiveWatchDetailRequest,
        tmp_header: aliding_20230426_models.QueryLiveWatchDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveWatchDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchDetailShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='QueryLiveWatchDetail',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveWatchDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_watch_detail_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryLiveWatchDetailRequest,
        tmp_header: aliding_20230426_models.QueryLiveWatchDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveWatchDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchDetailShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
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
            action='QueryLiveWatchDetail',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveWatchDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_watch_detail(
        self,
        request: aliding_20230426_models.QueryLiveWatchDetailRequest,
    ) -> aliding_20230426_models.QueryLiveWatchDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchDetailHeaders()
        return self.query_live_watch_detail_with_options(request, headers, runtime)

    async def query_live_watch_detail_async(
        self,
        request: aliding_20230426_models.QueryLiveWatchDetailRequest,
    ) -> aliding_20230426_models.QueryLiveWatchDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchDetailHeaders()
        return await self.query_live_watch_detail_with_options_async(request, headers, runtime)

    def query_live_watch_user_list_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryLiveWatchUserListRequest,
        tmp_header: aliding_20230426_models.QueryLiveWatchUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveWatchUserListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchUserListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchUserListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
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
            action='QueryLiveWatchUserList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveWatchUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_watch_user_list_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryLiveWatchUserListRequest,
        tmp_header: aliding_20230426_models.QueryLiveWatchUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryLiveWatchUserListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchUserListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchUserListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
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
            action='QueryLiveWatchUserList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryLiveWatchUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_watch_user_list(
        self,
        request: aliding_20230426_models.QueryLiveWatchUserListRequest,
    ) -> aliding_20230426_models.QueryLiveWatchUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchUserListHeaders()
        return self.query_live_watch_user_list_with_options(request, headers, runtime)

    async def query_live_watch_user_list_async(
        self,
        request: aliding_20230426_models.QueryLiveWatchUserListRequest,
    ) -> aliding_20230426_models.QueryLiveWatchUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchUserListHeaders()
        return await self.query_live_watch_user_list_with_options_async(request, headers, runtime)

    def query_meeting_room_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
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
            action='QueryMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
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
            action='QueryMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room(
        self,
        request: aliding_20230426_models.QueryMeetingRoomRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomHeaders()
        return self.query_meeting_room_with_options(request, headers, runtime)

    async def query_meeting_room_async(
        self,
        request: aliding_20230426_models.QueryMeetingRoomRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomHeaders()
        return await self.query_meeting_room_with_options_async(request, headers, runtime)

    def query_meeting_room_group_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
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
            action='QueryMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_group_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
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
            action='QueryMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_group(
        self,
        request: aliding_20230426_models.QueryMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupHeaders()
        return self.query_meeting_room_group_with_options(request, headers, runtime)

    async def query_meeting_room_group_async(
        self,
        request: aliding_20230426_models.QueryMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupHeaders()
        return await self.query_meeting_room_group_with_options_async(request, headers, runtime)

    def query_meeting_room_group_list_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomGroupListRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomGroupListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='QueryMeetingRoomGroupList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomGroupList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_group_list_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomGroupListRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomGroupListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
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
            action='QueryMeetingRoomGroupList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomGroupList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_group_list(
        self,
        request: aliding_20230426_models.QueryMeetingRoomGroupListRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupListHeaders()
        return self.query_meeting_room_group_list_with_options(request, headers, runtime)

    async def query_meeting_room_group_list_async(
        self,
        request: aliding_20230426_models.QueryMeetingRoomGroupListRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomGroupListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupListHeaders()
        return await self.query_meeting_room_group_list_with_options_async(request, headers, runtime)

    def query_meeting_room_list_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomListRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
            action='QueryMeetingRoomList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_list_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryMeetingRoomListRequest,
        tmp_header: aliding_20230426_models.QueryMeetingRoomListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryMeetingRoomListResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
            action='QueryMeetingRoomList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryMeetingRoomList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_list(
        self,
        request: aliding_20230426_models.QueryMeetingRoomListRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomListHeaders()
        return self.query_meeting_room_list_with_options(request, headers, runtime)

    async def query_meeting_room_list_async(
        self,
        request: aliding_20230426_models.QueryMeetingRoomListRequest,
    ) -> aliding_20230426_models.QueryMeetingRoomListResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomListHeaders()
        return await self.query_meeting_room_list_with_options_async(request, headers, runtime)

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

    def query_schedule_conference_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.QueryScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_union_id):
            body['RequestUnionId'] = request.request_union_id
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
            action='QueryScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_schedule_conference_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.QueryScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_union_id):
            body['RequestUnionId'] = request.request_union_id
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
            action='QueryScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/queryScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_schedule_conference(
        self,
        request: aliding_20230426_models.QueryScheduleConferenceRequest,
    ) -> aliding_20230426_models.QueryScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryScheduleConferenceHeaders()
        return self.query_schedule_conference_with_options(request, headers, runtime)

    async def query_schedule_conference_async(
        self,
        request: aliding_20230426_models.QueryScheduleConferenceRequest,
    ) -> aliding_20230426_models.QueryScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryScheduleConferenceHeaders()
        return await self.query_schedule_conference_with_options_async(request, headers, runtime)

    def receiver_list_report_with_options(
        self,
        tmp_req: aliding_20230426_models.ReceiverListReportRequest,
        tmp_header: aliding_20230426_models.ReceiverListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ReceiverListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ReceiverListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ReceiverListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='ReceiverListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/receiverListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ReceiverListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def receiver_list_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.ReceiverListReportRequest,
        tmp_header: aliding_20230426_models.ReceiverListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.ReceiverListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ReceiverListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ReceiverListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
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
            action='ReceiverListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/receiverListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ReceiverListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def receiver_list_report(
        self,
        request: aliding_20230426_models.ReceiverListReportRequest,
    ) -> aliding_20230426_models.ReceiverListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ReceiverListReportHeaders()
        return self.receiver_list_report_with_options(request, headers, runtime)

    async def receiver_list_report_async(
        self,
        request: aliding_20230426_models.ReceiverListReportRequest,
    ) -> aliding_20230426_models.ReceiverListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ReceiverListReportHeaders()
        return await self.receiver_list_report_with_options_async(request, headers, runtime)

    def remove_attendee_with_options(
        self,
        tmp_req: aliding_20230426_models.RemoveAttendeeRequest,
        tmp_header: aliding_20230426_models.RemoveAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.RemoveAttendeeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.RemoveAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.RemoveAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_remove):
            request.attendees_to_remove_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_remove, 'AttendeesToRemove', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_remove_shrink):
            body['AttendeesToRemove'] = request.attendees_to_remove_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='RemoveAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/removeAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.RemoveAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_attendee_with_options_async(
        self,
        tmp_req: aliding_20230426_models.RemoveAttendeeRequest,
        tmp_header: aliding_20230426_models.RemoveAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.RemoveAttendeeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.RemoveAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.RemoveAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_remove):
            request.attendees_to_remove_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_remove, 'AttendeesToRemove', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_remove_shrink):
            body['AttendeesToRemove'] = request.attendees_to_remove_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
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
            action='RemoveAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/calendar/removeAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.RemoveAttendeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_attendee(
        self,
        request: aliding_20230426_models.RemoveAttendeeRequest,
    ) -> aliding_20230426_models.RemoveAttendeeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.RemoveAttendeeHeaders()
        return self.remove_attendee_with_options(request, headers, runtime)

    async def remove_attendee_async(
        self,
        request: aliding_20230426_models.RemoveAttendeeRequest,
    ) -> aliding_20230426_models.RemoveAttendeeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.RemoveAttendeeHeaders()
        return await self.remove_attendee_with_options_async(request, headers, runtime)

    def save_content_with_options(
        self,
        tmp_req: aliding_20230426_models.SaveContentRequest,
        tmp_header: aliding_20230426_models.SaveContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SaveContentResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SaveContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SaveContentShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
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
            action='SaveContent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/saveContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SaveContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_content_with_options_async(
        self,
        tmp_req: aliding_20230426_models.SaveContentRequest,
        tmp_header: aliding_20230426_models.SaveContentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SaveContentResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SaveContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SaveContentShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
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
            action='SaveContent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/saveContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SaveContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_content(
        self,
        request: aliding_20230426_models.SaveContentRequest,
    ) -> aliding_20230426_models.SaveContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SaveContentHeaders()
        return self.save_content_with_options(request, headers, runtime)

    async def save_content_async(
        self,
        request: aliding_20230426_models.SaveContentRequest,
    ) -> aliding_20230426_models.SaveContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SaveContentHeaders()
        return await self.save_content_with_options_async(request, headers, runtime)

    def set_columns_visibility_with_options(
        self,
        tmp_req: aliding_20230426_models.SetColumnsVisibilityRequest,
        tmp_header: aliding_20230426_models.SetColumnsVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SetColumnsVisibilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetColumnsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetColumnsVisibilityShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
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
            action='SetColumnsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/setColumnsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetColumnsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_columns_visibility_with_options_async(
        self,
        tmp_req: aliding_20230426_models.SetColumnsVisibilityRequest,
        tmp_header: aliding_20230426_models.SetColumnsVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SetColumnsVisibilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetColumnsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetColumnsVisibilityShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
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
            action='SetColumnsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/setColumnsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetColumnsVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_columns_visibility(
        self,
        request: aliding_20230426_models.SetColumnsVisibilityRequest,
    ) -> aliding_20230426_models.SetColumnsVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetColumnsVisibilityHeaders()
        return self.set_columns_visibility_with_options(request, headers, runtime)

    async def set_columns_visibility_async(
        self,
        request: aliding_20230426_models.SetColumnsVisibilityRequest,
    ) -> aliding_20230426_models.SetColumnsVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetColumnsVisibilityHeaders()
        return await self.set_columns_visibility_with_options_async(request, headers, runtime)

    def set_rows_visibility_with_options(
        self,
        tmp_req: aliding_20230426_models.SetRowsVisibilityRequest,
        tmp_header: aliding_20230426_models.SetRowsVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SetRowsVisibilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetRowsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetRowsVisibilityShrinkHeaders()
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
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
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
            action='SetRowsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/setRowsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetRowsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_rows_visibility_with_options_async(
        self,
        tmp_req: aliding_20230426_models.SetRowsVisibilityRequest,
        tmp_header: aliding_20230426_models.SetRowsVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SetRowsVisibilityResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetRowsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetRowsVisibilityShrinkHeaders()
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
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
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
            action='SetRowsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/setRowsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetRowsVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_rows_visibility(
        self,
        request: aliding_20230426_models.SetRowsVisibilityRequest,
    ) -> aliding_20230426_models.SetRowsVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetRowsVisibilityHeaders()
        return self.set_rows_visibility_with_options(request, headers, runtime)

    async def set_rows_visibility_async(
        self,
        request: aliding_20230426_models.SetRowsVisibilityRequest,
    ) -> aliding_20230426_models.SetRowsVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetRowsVisibilityHeaders()
        return await self.set_rows_visibility_with_options_async(request, headers, runtime)

    def simple_list_report_with_options(
        self,
        tmp_req: aliding_20230426_models.SimpleListReportRequest,
        tmp_header: aliding_20230426_models.SimpleListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SimpleListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SimpleListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SimpleListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='SimpleListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/simpleListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SimpleListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_list_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.SimpleListReportRequest,
        tmp_header: aliding_20230426_models.SimpleListReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.SimpleListReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SimpleListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SimpleListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
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
            action='SimpleListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/simpleListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SimpleListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_list_report(
        self,
        request: aliding_20230426_models.SimpleListReportRequest,
    ) -> aliding_20230426_models.SimpleListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SimpleListReportHeaders()
        return self.simple_list_report_with_options(request, headers, runtime)

    async def simple_list_report_async(
        self,
        request: aliding_20230426_models.SimpleListReportRequest,
    ) -> aliding_20230426_models.SimpleListReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SimpleListReportHeaders()
        return await self.simple_list_report_with_options_async(request, headers, runtime)

    def start_cloud_record_with_options(
        self,
        tmp_req: aliding_20230426_models.StartCloudRecordRequest,
        tmp_header: aliding_20230426_models.StartCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StartCloudRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StartCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StartCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.small_window_position):
            body['SmallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='StartCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/startCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_record_with_options_async(
        self,
        tmp_req: aliding_20230426_models.StartCloudRecordRequest,
        tmp_header: aliding_20230426_models.StartCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StartCloudRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StartCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StartCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.small_window_position):
            body['SmallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='StartCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/startCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StartCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_record(
        self,
        request: aliding_20230426_models.StartCloudRecordRequest,
    ) -> aliding_20230426_models.StartCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StartCloudRecordHeaders()
        return self.start_cloud_record_with_options(request, headers, runtime)

    async def start_cloud_record_async(
        self,
        request: aliding_20230426_models.StartCloudRecordRequest,
    ) -> aliding_20230426_models.StartCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StartCloudRecordHeaders()
        return await self.start_cloud_record_with_options_async(request, headers, runtime)

    def statistics_list_by_type_report_with_options(
        self,
        tmp_req: aliding_20230426_models.StatisticsListByTypeReportRequest,
        tmp_header: aliding_20230426_models.StatisticsListByTypeReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StatisticsListByTypeReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsListByTypeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsListByTypeReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
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
            action='StatisticsListByTypeReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/statisticsListByTypeReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsListByTypeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def statistics_list_by_type_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.StatisticsListByTypeReportRequest,
        tmp_header: aliding_20230426_models.StatisticsListByTypeReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StatisticsListByTypeReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsListByTypeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsListByTypeReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
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
            action='StatisticsListByTypeReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/statisticsListByTypeReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsListByTypeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def statistics_list_by_type_report(
        self,
        request: aliding_20230426_models.StatisticsListByTypeReportRequest,
    ) -> aliding_20230426_models.StatisticsListByTypeReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsListByTypeReportHeaders()
        return self.statistics_list_by_type_report_with_options(request, headers, runtime)

    async def statistics_list_by_type_report_async(
        self,
        request: aliding_20230426_models.StatisticsListByTypeReportRequest,
    ) -> aliding_20230426_models.StatisticsListByTypeReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsListByTypeReportHeaders()
        return await self.statistics_list_by_type_report_with_options_async(request, headers, runtime)

    def statistics_report_with_options(
        self,
        tmp_req: aliding_20230426_models.StatisticsReportRequest,
        tmp_header: aliding_20230426_models.StatisticsReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StatisticsReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
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
            action='StatisticsReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/statisticsReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def statistics_report_with_options_async(
        self,
        tmp_req: aliding_20230426_models.StatisticsReportRequest,
        tmp_header: aliding_20230426_models.StatisticsReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StatisticsReportResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
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
            action='StatisticsReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/log/statisticsReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def statistics_report(
        self,
        request: aliding_20230426_models.StatisticsReportRequest,
    ) -> aliding_20230426_models.StatisticsReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsReportHeaders()
        return self.statistics_report_with_options(request, headers, runtime)

    async def statistics_report_async(
        self,
        request: aliding_20230426_models.StatisticsReportRequest,
    ) -> aliding_20230426_models.StatisticsReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsReportHeaders()
        return await self.statistics_report_with_options_async(request, headers, runtime)

    def stop_cloud_record_with_options(
        self,
        tmp_req: aliding_20230426_models.StopCloudRecordRequest,
        tmp_header: aliding_20230426_models.StopCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StopCloudRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StopCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StopCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='StopCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/stopCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_record_with_options_async(
        self,
        tmp_req: aliding_20230426_models.StopCloudRecordRequest,
        tmp_header: aliding_20230426_models.StopCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.StopCloudRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StopCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StopCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
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
            action='StopCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/stopCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StopCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_record(
        self,
        request: aliding_20230426_models.StopCloudRecordRequest,
    ) -> aliding_20230426_models.StopCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StopCloudRecordHeaders()
        return self.stop_cloud_record_with_options(request, headers, runtime)

    async def stop_cloud_record_async(
        self,
        request: aliding_20230426_models.StopCloudRecordRequest,
    ) -> aliding_20230426_models.StopCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StopCloudRecordHeaders()
        return await self.stop_cloud_record_with_options_async(request, headers, runtime)

    def update_live_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateLiveRequest,
        tmp_header: aliding_20230426_models.UpdateLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='UpdateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateLiveRequest,
        tmp_header: aliding_20230426_models.UpdateLiveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateLiveResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='UpdateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live(
        self,
        request: aliding_20230426_models.UpdateLiveRequest,
    ) -> aliding_20230426_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateLiveHeaders()
        return self.update_live_with_options(request, headers, runtime)

    async def update_live_async(
        self,
        request: aliding_20230426_models.UpdateLiveRequest,
    ) -> aliding_20230426_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateLiveHeaders()
        return await self.update_live_with_options_async(request, headers, runtime)

    def update_meeting_room_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateMeetingRoomRequest,
        tmp_header: aliding_20230426_models.UpdateMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
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
            action='UpdateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_meeting_room_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateMeetingRoomRequest,
        tmp_header: aliding_20230426_models.UpdateMeetingRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateMeetingRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
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
            action='UpdateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_meeting_room(
        self,
        request: aliding_20230426_models.UpdateMeetingRoomRequest,
    ) -> aliding_20230426_models.UpdateMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomHeaders()
        return self.update_meeting_room_with_options(request, headers, runtime)

    async def update_meeting_room_async(
        self,
        request: aliding_20230426_models.UpdateMeetingRoomRequest,
    ) -> aliding_20230426_models.UpdateMeetingRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomHeaders()
        return await self.update_meeting_room_with_options_async(request, headers, runtime)

    def update_meeting_room_group_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.UpdateMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
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
            action='UpdateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_meeting_room_group_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateMeetingRoomGroupRequest,
        tmp_header: aliding_20230426_models.UpdateMeetingRoomGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateMeetingRoomGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
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
            action='UpdateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_meeting_room_group(
        self,
        request: aliding_20230426_models.UpdateMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.UpdateMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomGroupHeaders()
        return self.update_meeting_room_group_with_options(request, headers, runtime)

    async def update_meeting_room_group_async(
        self,
        request: aliding_20230426_models.UpdateMeetingRoomGroupRequest,
    ) -> aliding_20230426_models.UpdateMeetingRoomGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomGroupHeaders()
        return await self.update_meeting_room_group_with_options_async(request, headers, runtime)

    def update_range_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateRangeRequest,
        tmp_header: aliding_20230426_models.UpdateRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateRangeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.background_colors):
            request.background_colors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.background_colors, 'BackgroundColors', 'json')
        if not UtilClient.is_unset(tmp_req.hyperlinks):
            request.hyperlinks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyperlinks, 'Hyperlinks', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        body = {}
        if not UtilClient.is_unset(request.background_colors_shrink):
            body['BackgroundColors'] = request.background_colors_shrink
        if not UtilClient.is_unset(request.hyperlinks_shrink):
            body['Hyperlinks'] = request.hyperlinks_shrink
        if not UtilClient.is_unset(request.number_format):
            body['NumberFormat'] = request.number_format
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.values_shrink):
            body['Values'] = request.values_shrink
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
            action='UpdateRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_range_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateRangeRequest,
        tmp_header: aliding_20230426_models.UpdateRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateRangeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.background_colors):
            request.background_colors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.background_colors, 'BackgroundColors', 'json')
        if not UtilClient.is_unset(tmp_req.hyperlinks):
            request.hyperlinks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyperlinks, 'Hyperlinks', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        body = {}
        if not UtilClient.is_unset(request.background_colors_shrink):
            body['BackgroundColors'] = request.background_colors_shrink
        if not UtilClient.is_unset(request.hyperlinks_shrink):
            body['Hyperlinks'] = request.hyperlinks_shrink
        if not UtilClient.is_unset(request.number_format):
            body['NumberFormat'] = request.number_format
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.values_shrink):
            body['Values'] = request.values_shrink
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
            action='UpdateRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_range(
        self,
        request: aliding_20230426_models.UpdateRangeRequest,
    ) -> aliding_20230426_models.UpdateRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateRangeHeaders()
        return self.update_range_with_options(request, headers, runtime)

    async def update_range_async(
        self,
        request: aliding_20230426_models.UpdateRangeRequest,
    ) -> aliding_20230426_models.UpdateRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateRangeHeaders()
        return await self.update_range_with_options_async(request, headers, runtime)

    def update_schedule_conference_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.UpdateScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='UpdateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schedule_conference_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateScheduleConferenceRequest,
        tmp_header: aliding_20230426_models.UpdateScheduleConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateScheduleConferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
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
            action='UpdateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/ysp/updateScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schedule_conference(
        self,
        request: aliding_20230426_models.UpdateScheduleConferenceRequest,
    ) -> aliding_20230426_models.UpdateScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateScheduleConferenceHeaders()
        return self.update_schedule_conference_with_options(request, headers, runtime)

    async def update_schedule_conference_async(
        self,
        request: aliding_20230426_models.UpdateScheduleConferenceRequest,
    ) -> aliding_20230426_models.UpdateScheduleConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateScheduleConferenceHeaders()
        return await self.update_schedule_conference_with_options_async(request, headers, runtime)

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
