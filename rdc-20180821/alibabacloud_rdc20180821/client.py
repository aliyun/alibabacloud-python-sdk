# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rdc20180821 import models as rdc_20180821_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('rdc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_enterprise_member_with_options(
        self,
        request: rdc_20180821_models.AddEnterpriseMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.AddEnterpriseMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.AddEnterpriseMemberResponse().from_map(
            self.do_rpcrequest('AddEnterpriseMember', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_enterprise_member_with_options_async(
        self,
        request: rdc_20180821_models.AddEnterpriseMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.AddEnterpriseMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.AddEnterpriseMemberResponse().from_map(
            await self.do_rpcrequest_async('AddEnterpriseMember', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_enterprise_member(
        self,
        request: rdc_20180821_models.AddEnterpriseMemberRequest,
    ) -> rdc_20180821_models.AddEnterpriseMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_enterprise_member_with_options(request, runtime)

    async def add_enterprise_member_async(
        self,
        request: rdc_20180821_models.AddEnterpriseMemberRequest,
    ) -> rdc_20180821_models.AddEnterpriseMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_enterprise_member_with_options_async(request, runtime)

    def add_ram_member_with_options(
        self,
        request: rdc_20180821_models.AddRamMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.AddRamMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.AddRamMemberResponse().from_map(
            self.do_rpcrequest('AddRamMember', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_ram_member_with_options_async(
        self,
        request: rdc_20180821_models.AddRamMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.AddRamMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.AddRamMemberResponse().from_map(
            await self.do_rpcrequest_async('AddRamMember', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_ram_member(
        self,
        request: rdc_20180821_models.AddRamMemberRequest,
    ) -> rdc_20180821_models.AddRamMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ram_member_with_options(request, runtime)

    async def add_ram_member_async(
        self,
        request: rdc_20180821_models.AddRamMemberRequest,
    ) -> rdc_20180821_models.AddRamMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ram_member_with_options_async(request, runtime)

    def approve_join_company_with_options(
        self,
        request: rdc_20180821_models.ApproveJoinCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.ApproveJoinCompanyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.ApproveJoinCompanyResponse().from_map(
            self.do_rpcrequest('ApproveJoinCompany', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_join_company_with_options_async(
        self,
        request: rdc_20180821_models.ApproveJoinCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.ApproveJoinCompanyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.ApproveJoinCompanyResponse().from_map(
            await self.do_rpcrequest_async('ApproveJoinCompany', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_join_company(
        self,
        request: rdc_20180821_models.ApproveJoinCompanyRequest,
    ) -> rdc_20180821_models.ApproveJoinCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_join_company_with_options(request, runtime)

    async def approve_join_company_async(
        self,
        request: rdc_20180821_models.ApproveJoinCompanyRequest,
    ) -> rdc_20180821_models.ApproveJoinCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_join_company_with_options_async(request, runtime)

    def create_enterprise_with_options(
        self,
        tmp_req: rdc_20180821_models.CreateEnterpriseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.CreateEnterpriseResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.CreateEnterpriseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.emails):
            request.emails_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.emails, 'Emails', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.CreateEnterpriseResponse().from_map(
            self.do_rpcrequest('CreateEnterprise', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_enterprise_with_options_async(
        self,
        tmp_req: rdc_20180821_models.CreateEnterpriseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.CreateEnterpriseResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.CreateEnterpriseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.emails):
            request.emails_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.emails, 'Emails', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.CreateEnterpriseResponse().from_map(
            await self.do_rpcrequest_async('CreateEnterprise', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_enterprise(
        self,
        request: rdc_20180821_models.CreateEnterpriseRequest,
    ) -> rdc_20180821_models.CreateEnterpriseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_enterprise_with_options(request, runtime)

    async def create_enterprise_async(
        self,
        request: rdc_20180821_models.CreateEnterpriseRequest,
    ) -> rdc_20180821_models.CreateEnterpriseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_enterprise_with_options_async(request, runtime)

    def create_workitem_with_options(
        self,
        request: rdc_20180821_models.CreateWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.CreateWorkitemResponse().from_map(
            self.do_rpcrequest('CreateWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_workitem_with_options_async(
        self,
        request: rdc_20180821_models.CreateWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.CreateWorkitemResponse().from_map(
            await self.do_rpcrequest_async('CreateWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_workitem(
        self,
        request: rdc_20180821_models.CreateWorkitemRequest,
    ) -> rdc_20180821_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_workitem_with_options(request, runtime)

    async def create_workitem_async(
        self,
        request: rdc_20180821_models.CreateWorkitemRequest,
    ) -> rdc_20180821_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_workitem_with_options_async(request, runtime)

    def get_binded_user_by_ding_id_with_options(
        self,
        request: rdc_20180821_models.GetBindedUserByDingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetBindedUserByDingIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetBindedUserByDingIdResponse().from_map(
            self.do_rpcrequest('GetBindedUserByDingId', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_binded_user_by_ding_id_with_options_async(
        self,
        request: rdc_20180821_models.GetBindedUserByDingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetBindedUserByDingIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetBindedUserByDingIdResponse().from_map(
            await self.do_rpcrequest_async('GetBindedUserByDingId', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_binded_user_by_ding_id(
        self,
        request: rdc_20180821_models.GetBindedUserByDingIdRequest,
    ) -> rdc_20180821_models.GetBindedUserByDingIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_binded_user_by_ding_id_with_options(request, runtime)

    async def get_binded_user_by_ding_id_async(
        self,
        request: rdc_20180821_models.GetBindedUserByDingIdRequest,
    ) -> rdc_20180821_models.GetBindedUserByDingIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_binded_user_by_ding_id_with_options_async(request, runtime)

    def get_change_log_with_options(
        self,
        tmp_req: rdc_20180821_models.GetChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetChangeLogResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.GetChangeLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_ids):
            request.target_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetChangeLogResponse().from_map(
            self.do_rpcrequest('GetChangeLog', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_change_log_with_options_async(
        self,
        tmp_req: rdc_20180821_models.GetChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetChangeLogResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.GetChangeLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_ids):
            request.target_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetChangeLogResponse().from_map(
            await self.do_rpcrequest_async('GetChangeLog', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_change_log(
        self,
        request: rdc_20180821_models.GetChangeLogRequest,
    ) -> rdc_20180821_models.GetChangeLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_change_log_with_options(request, runtime)

    async def get_change_log_async(
        self,
        request: rdc_20180821_models.GetChangeLogRequest,
    ) -> rdc_20180821_models.GetChangeLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_change_log_with_options_async(request, runtime)

    def get_custom_fields_by_template_id_with_options(
        self,
        request: rdc_20180821_models.GetCustomFieldsByTemplateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetCustomFieldsByTemplateIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetCustomFieldsByTemplateIdResponse().from_map(
            self.do_rpcrequest('GetCustomFieldsByTemplateId', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_custom_fields_by_template_id_with_options_async(
        self,
        request: rdc_20180821_models.GetCustomFieldsByTemplateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetCustomFieldsByTemplateIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetCustomFieldsByTemplateIdResponse().from_map(
            await self.do_rpcrequest_async('GetCustomFieldsByTemplateId', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_custom_fields_by_template_id(
        self,
        request: rdc_20180821_models.GetCustomFieldsByTemplateIdRequest,
    ) -> rdc_20180821_models.GetCustomFieldsByTemplateIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_custom_fields_by_template_id_with_options(request, runtime)

    async def get_custom_fields_by_template_id_async(
        self,
        request: rdc_20180821_models.GetCustomFieldsByTemplateIdRequest,
    ) -> rdc_20180821_models.GetCustomFieldsByTemplateIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_fields_by_template_id_with_options_async(request, runtime)

    def get_issue_by_id_with_options(
        self,
        request: rdc_20180821_models.GetIssueByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetIssueByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetIssueByIdResponse().from_map(
            self.do_rpcrequest('GetIssueById', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_issue_by_id_with_options_async(
        self,
        request: rdc_20180821_models.GetIssueByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetIssueByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetIssueByIdResponse().from_map(
            await self.do_rpcrequest_async('GetIssueById', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_issue_by_id(
        self,
        request: rdc_20180821_models.GetIssueByIdRequest,
    ) -> rdc_20180821_models.GetIssueByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_issue_by_id_with_options(request, runtime)

    async def get_issue_by_id_async(
        self,
        request: rdc_20180821_models.GetIssueByIdRequest,
    ) -> rdc_20180821_models.GetIssueByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_issue_by_id_with_options_async(request, runtime)

    def get_join_code_with_options(
        self,
        request: rdc_20180821_models.GetJoinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetJoinCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetJoinCodeResponse().from_map(
            self.do_rpcrequest('GetJoinCode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_join_code_with_options_async(
        self,
        request: rdc_20180821_models.GetJoinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetJoinCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetJoinCodeResponse().from_map(
            await self.do_rpcrequest_async('GetJoinCode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_join_code(
        self,
        request: rdc_20180821_models.GetJoinCodeRequest,
    ) -> rdc_20180821_models.GetJoinCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_join_code_with_options(request, runtime)

    async def get_join_code_async(
        self,
        request: rdc_20180821_models.GetJoinCodeRequest,
    ) -> rdc_20180821_models.GetJoinCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_join_code_with_options_async(request, runtime)

    def get_project_members_with_options(
        self,
        request: rdc_20180821_models.GetProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetProjectMembersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetProjectMembersResponse().from_map(
            self.do_rpcrequest('GetProjectMembers', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_project_members_with_options_async(
        self,
        request: rdc_20180821_models.GetProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetProjectMembersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('GetProjectMembers', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_project_members(
        self,
        request: rdc_20180821_models.GetProjectMembersRequest,
    ) -> rdc_20180821_models.GetProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_members_with_options(request, runtime)

    async def get_project_members_async(
        self,
        request: rdc_20180821_models.GetProjectMembersRequest,
    ) -> rdc_20180821_models.GetProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_members_with_options_async(request, runtime)

    def get_user_by_aliyun_pk_with_options(
        self,
        request: rdc_20180821_models.GetUserByAliyunPkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetUserByAliyunPkResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetUserByAliyunPkResponse().from_map(
            self.do_rpcrequest('GetUserByAliyunPk', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_user_by_aliyun_pk_with_options_async(
        self,
        request: rdc_20180821_models.GetUserByAliyunPkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetUserByAliyunPkResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.GetUserByAliyunPkResponse().from_map(
            await self.do_rpcrequest_async('GetUserByAliyunPk', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_user_by_aliyun_pk(
        self,
        request: rdc_20180821_models.GetUserByAliyunPkRequest,
    ) -> rdc_20180821_models.GetUserByAliyunPkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_aliyun_pk_with_options(request, runtime)

    async def get_user_by_aliyun_pk_async(
        self,
        request: rdc_20180821_models.GetUserByAliyunPkRequest,
    ) -> rdc_20180821_models.GetUserByAliyunPkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_by_aliyun_pk_with_options_async(request, runtime)

    def get_workitem_by_id_with_options(
        self,
        request: rdc_20180821_models.GetWorkitemByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetWorkitemByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetWorkitemByIdResponse().from_map(
            self.do_rpcrequest('GetWorkitemById', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_workitem_by_id_with_options_async(
        self,
        request: rdc_20180821_models.GetWorkitemByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.GetWorkitemByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.GetWorkitemByIdResponse().from_map(
            await self.do_rpcrequest_async('GetWorkitemById', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_workitem_by_id(
        self,
        request: rdc_20180821_models.GetWorkitemByIdRequest,
    ) -> rdc_20180821_models.GetWorkitemByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workitem_by_id_with_options(request, runtime)

    async def get_workitem_by_id_async(
        self,
        request: rdc_20180821_models.GetWorkitemByIdRequest,
    ) -> rdc_20180821_models.GetWorkitemByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workitem_by_id_with_options_async(request, runtime)

    def join_company_with_options(
        self,
        request: rdc_20180821_models.JoinCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.JoinCompanyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.JoinCompanyResponse().from_map(
            self.do_rpcrequest('JoinCompany', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_company_with_options_async(
        self,
        request: rdc_20180821_models.JoinCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.JoinCompanyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.JoinCompanyResponse().from_map(
            await self.do_rpcrequest_async('JoinCompany', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_company(
        self,
        request: rdc_20180821_models.JoinCompanyRequest,
    ) -> rdc_20180821_models.JoinCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_company_with_options(request, runtime)

    async def join_company_async(
        self,
        request: rdc_20180821_models.JoinCompanyRequest,
    ) -> rdc_20180821_models.JoinCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_company_with_options_async(request, runtime)

    def search_projects_by_region_with_options(
        self,
        request: rdc_20180821_models.SearchProjectsByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchProjectsByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.SearchProjectsByRegionResponse().from_map(
            self.do_rpcrequest('SearchProjectsByRegion', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def search_projects_by_region_with_options_async(
        self,
        request: rdc_20180821_models.SearchProjectsByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchProjectsByRegionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return rdc_20180821_models.SearchProjectsByRegionResponse().from_map(
            await self.do_rpcrequest_async('SearchProjectsByRegion', '2018-08-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def search_projects_by_region(
        self,
        request: rdc_20180821_models.SearchProjectsByRegionRequest,
    ) -> rdc_20180821_models.SearchProjectsByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_projects_by_region_with_options(request, runtime)

    async def search_projects_by_region_async(
        self,
        request: rdc_20180821_models.SearchProjectsByRegionRequest,
    ) -> rdc_20180821_models.SearchProjectsByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_projects_by_region_with_options_async(request, runtime)

    def search_test_case_with_options(
        self,
        request: rdc_20180821_models.SearchTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchTestCaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchTestCaseResponse().from_map(
            self.do_rpcrequest('SearchTestCase', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_test_case_with_options_async(
        self,
        request: rdc_20180821_models.SearchTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchTestCaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchTestCaseResponse().from_map(
            await self.do_rpcrequest_async('SearchTestCase', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_test_case(
        self,
        request: rdc_20180821_models.SearchTestCaseRequest,
    ) -> rdc_20180821_models.SearchTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_test_case_with_options(request, runtime)

    async def search_test_case_async(
        self,
        request: rdc_20180821_models.SearchTestCaseRequest,
    ) -> rdc_20180821_models.SearchTestCaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_test_case_with_options_async(request, runtime)

    def search_workitem_with_options(
        self,
        request: rdc_20180821_models.SearchWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchWorkitemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchWorkitemResponse().from_map(
            self.do_rpcrequest('SearchWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_workitem_with_options_async(
        self,
        request: rdc_20180821_models.SearchWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchWorkitemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchWorkitemResponse().from_map(
            await self.do_rpcrequest_async('SearchWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_workitem(
        self,
        request: rdc_20180821_models.SearchWorkitemRequest,
    ) -> rdc_20180821_models.SearchWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_workitem_with_options(request, runtime)

    async def search_workitem_async(
        self,
        request: rdc_20180821_models.SearchWorkitemRequest,
    ) -> rdc_20180821_models.SearchWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_workitem_with_options_async(request, runtime)

    def search_workitem_with_total_count_with_options(
        self,
        request: rdc_20180821_models.SearchWorkitemWithTotalCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchWorkitemWithTotalCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchWorkitemWithTotalCountResponse().from_map(
            self.do_rpcrequest('SearchWorkitemWithTotalCount', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_workitem_with_total_count_with_options_async(
        self,
        request: rdc_20180821_models.SearchWorkitemWithTotalCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SearchWorkitemWithTotalCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SearchWorkitemWithTotalCountResponse().from_map(
            await self.do_rpcrequest_async('SearchWorkitemWithTotalCount', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_workitem_with_total_count(
        self,
        request: rdc_20180821_models.SearchWorkitemWithTotalCountRequest,
    ) -> rdc_20180821_models.SearchWorkitemWithTotalCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_workitem_with_total_count_with_options(request, runtime)

    async def search_workitem_with_total_count_async(
        self,
        request: rdc_20180821_models.SearchWorkitemWithTotalCountRequest,
    ) -> rdc_20180821_models.SearchWorkitemWithTotalCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_workitem_with_total_count_with_options_async(request, runtime)

    def sync_user_to_rdc_with_options(
        self,
        request: rdc_20180821_models.SyncUserToRdcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SyncUserToRdcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SyncUserToRdcResponse().from_map(
            self.do_rpcrequest('SyncUserToRdc', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_user_to_rdc_with_options_async(
        self,
        request: rdc_20180821_models.SyncUserToRdcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.SyncUserToRdcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.SyncUserToRdcResponse().from_map(
            await self.do_rpcrequest_async('SyncUserToRdc', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_user_to_rdc(
        self,
        request: rdc_20180821_models.SyncUserToRdcRequest,
    ) -> rdc_20180821_models.SyncUserToRdcResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_user_to_rdc_with_options(request, runtime)

    async def sync_user_to_rdc_async(
        self,
        request: rdc_20180821_models.SyncUserToRdcRequest,
    ) -> rdc_20180821_models.SyncUserToRdcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_user_to_rdc_with_options_async(request, runtime)

    def update_workitem_with_options(
        self,
        tmp_req: rdc_20180821_models.UpdateWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.UpdateWorkitemResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.UpdateWorkitemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cf_list):
            request.cf_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cf_list, 'CfList', 'json')
        if not UtilClient.is_unset(tmp_req.cfs):
            request.cfs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cfs, 'Cfs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.UpdateWorkitemResponse().from_map(
            self.do_rpcrequest('UpdateWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_workitem_with_options_async(
        self,
        tmp_req: rdc_20180821_models.UpdateWorkitemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rdc_20180821_models.UpdateWorkitemResponse:
        UtilClient.validate_model(tmp_req)
        request = rdc_20180821_models.UpdateWorkitemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cf_list):
            request.cf_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cf_list, 'CfList', 'json')
        if not UtilClient.is_unset(tmp_req.cfs):
            request.cfs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cfs, 'Cfs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rdc_20180821_models.UpdateWorkitemResponse().from_map(
            await self.do_rpcrequest_async('UpdateWorkitem', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_workitem(
        self,
        request: rdc_20180821_models.UpdateWorkitemRequest,
    ) -> rdc_20180821_models.UpdateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_workitem_with_options(request, runtime)

    async def update_workitem_async(
        self,
        request: rdc_20180821_models.UpdateWorkitemRequest,
    ) -> rdc_20180821_models.UpdateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_workitem_with_options_async(request, runtime)
