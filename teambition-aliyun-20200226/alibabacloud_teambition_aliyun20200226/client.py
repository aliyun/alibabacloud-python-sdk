# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_teambition_aliyun20200226 import models as teambition_aliyun_20200226_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('teambition-aliyun', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_project_members_with_options(
        self,
        request: teambition_aliyun_20200226_models.AddProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.AddProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.AddProjectMembersResponse().from_map(
            self.do_rpcrequest('AddProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_project_members_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.AddProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.AddProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.AddProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('AddProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_project_members(
        self,
        request: teambition_aliyun_20200226_models.AddProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.AddProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_project_members_with_options(request, runtime)

    async def add_project_members_async(
        self,
        request: teambition_aliyun_20200226_models.AddProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.AddProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_project_members_with_options_async(request, runtime)

    def apply_small_micro_with_options(
        self,
        request: teambition_aliyun_20200226_models.ApplySmallMicroRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ApplySmallMicroResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ApplySmallMicroResponse().from_map(
            self.do_rpcrequest('ApplySmallMicro', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_small_micro_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ApplySmallMicroRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ApplySmallMicroResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ApplySmallMicroResponse().from_map(
            await self.do_rpcrequest_async('ApplySmallMicro', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_small_micro(
        self,
        request: teambition_aliyun_20200226_models.ApplySmallMicroRequest,
    ) -> teambition_aliyun_20200226_models.ApplySmallMicroResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_small_micro_with_options(request, runtime)

    async def apply_small_micro_async(
        self,
        request: teambition_aliyun_20200226_models.ApplySmallMicroRequest,
    ) -> teambition_aliyun_20200226_models.ApplySmallMicroResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_small_micro_with_options_async(request, runtime)

    def bactch_insert_members_with_options(
        self,
        request: teambition_aliyun_20200226_models.BactchInsertMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.BactchInsertMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.BactchInsertMembersResponse().from_map(
            self.do_rpcrequest('BactchInsertMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bactch_insert_members_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.BactchInsertMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.BactchInsertMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.BactchInsertMembersResponse().from_map(
            await self.do_rpcrequest_async('BactchInsertMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bactch_insert_members(
        self,
        request: teambition_aliyun_20200226_models.BactchInsertMembersRequest,
    ) -> teambition_aliyun_20200226_models.BactchInsertMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.bactch_insert_members_with_options(request, runtime)

    async def bactch_insert_members_async(
        self,
        request: teambition_aliyun_20200226_models.BactchInsertMembersRequest,
    ) -> teambition_aliyun_20200226_models.BactchInsertMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bactch_insert_members_with_options_async(request, runtime)

    def check_aliyun_user_exists_with_options(
        self,
        request: teambition_aliyun_20200226_models.CheckAliyunUserExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse().from_map(
            self.do_rpcrequest('CheckAliyunUserExists', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_aliyun_user_exists_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.CheckAliyunUserExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse().from_map(
            await self.do_rpcrequest_async('CheckAliyunUserExists', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_aliyun_user_exists(
        self,
        request: teambition_aliyun_20200226_models.CheckAliyunUserExistsRequest,
    ) -> teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_aliyun_user_exists_with_options(request, runtime)

    async def check_aliyun_user_exists_async(
        self,
        request: teambition_aliyun_20200226_models.CheckAliyunUserExistsRequest,
    ) -> teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_aliyun_user_exists_with_options_async(request, runtime)

    def create_devops_org_with_options(
        self,
        request: teambition_aliyun_20200226_models.CreateDevopsOrgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateDevopsOrgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateDevopsOrgResponse().from_map(
            self.do_rpcrequest('CreateDevopsOrg', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_devops_org_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.CreateDevopsOrgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateDevopsOrgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateDevopsOrgResponse().from_map(
            await self.do_rpcrequest_async('CreateDevopsOrg', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_org(
        self,
        request: teambition_aliyun_20200226_models.CreateDevopsOrgRequest,
    ) -> teambition_aliyun_20200226_models.CreateDevopsOrgResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devops_org_with_options(request, runtime)

    async def create_devops_org_async(
        self,
        request: teambition_aliyun_20200226_models.CreateDevopsOrgRequest,
    ) -> teambition_aliyun_20200226_models.CreateDevopsOrgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devops_org_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectResponse().from_map(
            self.do_rpcrequest('CreateProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_sprint_with_options(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectSprintResponse().from_map(
            self.do_rpcrequest('CreateProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_sprint_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('CreateProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_sprint(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_sprint_with_options(request, runtime)

    async def create_project_sprint_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_sprint_with_options_async(request, runtime)

    def create_project_task_with_options(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectTaskResponse().from_map(
            self.do_rpcrequest('CreateProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_task_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.CreateProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.CreateProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_task(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_task_with_options(request, runtime)

    async def create_project_task_async(
        self,
        request: teambition_aliyun_20200226_models.CreateProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.CreateProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_task_with_options_async(request, runtime)

    def delete_members_for_org_with_options(
        self,
        request: teambition_aliyun_20200226_models.DeleteMembersForOrgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteMembersForOrgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteMembersForOrgResponse().from_map(
            self.do_rpcrequest('DeleteMembersForOrg', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_members_for_org_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteMembersForOrgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteMembersForOrgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteMembersForOrgResponse().from_map(
            await self.do_rpcrequest_async('DeleteMembersForOrg', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_members_for_org(
        self,
        request: teambition_aliyun_20200226_models.DeleteMembersForOrgRequest,
    ) -> teambition_aliyun_20200226_models.DeleteMembersForOrgResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_members_for_org_with_options(request, runtime)

    async def delete_members_for_org_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteMembersForOrgRequest,
    ) -> teambition_aliyun_20200226_models.DeleteMembersForOrgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_members_for_org_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectResponse().from_map(
            self.do_rpcrequest('DeleteProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_project_members_with_options(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectMembersResponse().from_map(
            self.do_rpcrequest('DeleteProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_members_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('DeleteProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_members(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_members_with_options(request, runtime)

    async def delete_project_members_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_members_with_options_async(request, runtime)

    def delete_project_sprint_with_options(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectSprintResponse().from_map(
            self.do_rpcrequest('DeleteProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_sprint_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('DeleteProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_sprint(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_sprint_with_options(request, runtime)

    async def delete_project_sprint_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_sprint_with_options_async(request, runtime)

    def delete_project_task_with_options(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectTaskResponse().from_map(
            self.do_rpcrequest('DeleteProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_task_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.DeleteProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.DeleteProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_task(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_task_with_options(request, runtime)

    async def delete_project_task_async(
        self,
        request: teambition_aliyun_20200226_models.DeleteProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.DeleteProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_task_with_options_async(request, runtime)

    def get_organization_members_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetOrganizationMembersResponse().from_map(
            self.do_rpcrequest('GetOrganizationMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_organization_members_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetOrganizationMembersResponse().from_map(
            await self.do_rpcrequest_async('GetOrganizationMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_organization_members(
        self,
        request: teambition_aliyun_20200226_models.GetOrganizationMembersRequest,
    ) -> teambition_aliyun_20200226_models.GetOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_organization_members_with_options(request, runtime)

    async def get_organization_members_async(
        self,
        request: teambition_aliyun_20200226_models.GetOrganizationMembersRequest,
    ) -> teambition_aliyun_20200226_models.GetOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_organization_members_with_options_async(request, runtime)

    def get_project_info_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectInfoResponse().from_map(
            self.do_rpcrequest('GetProjectInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_info_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectInfoResponse().from_map(
            await self.do_rpcrequest_async('GetProjectInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_info(
        self,
        request: teambition_aliyun_20200226_models.GetProjectInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_info_with_options(request, runtime)

    async def get_project_info_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_info_with_options_async(request, runtime)

    def get_project_members_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectMembersResponse().from_map(
            self.do_rpcrequest('GetProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_members_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('GetProjectMembers', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_members(
        self,
        request: teambition_aliyun_20200226_models.GetProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_members_with_options(request, runtime)

    async def get_project_members_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectMembersRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_members_with_options_async(request, runtime)

    def get_project_sprint_info_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetProjectSprintInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectSprintInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectSprintInfoResponse().from_map(
            self.do_rpcrequest('GetProjectSprintInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_sprint_info_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectSprintInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectSprintInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectSprintInfoResponse().from_map(
            await self.do_rpcrequest_async('GetProjectSprintInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_sprint_info(
        self,
        request: teambition_aliyun_20200226_models.GetProjectSprintInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_sprint_info_with_options(request, runtime)

    async def get_project_sprint_info_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectSprintInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_sprint_info_with_options_async(request, runtime)

    def get_project_task_info_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetProjectTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectTaskInfoResponse().from_map(
            self.do_rpcrequest('GetProjectTaskInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_task_info_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetProjectTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetProjectTaskInfoResponse().from_map(
            await self.do_rpcrequest_async('GetProjectTaskInfo', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_task_info(
        self,
        request: teambition_aliyun_20200226_models.GetProjectTaskInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_task_info_with_options(request, runtime)

    async def get_project_task_info_async(
        self,
        request: teambition_aliyun_20200226_models.GetProjectTaskInfoRequest,
    ) -> teambition_aliyun_20200226_models.GetProjectTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_task_info_with_options_async(request, runtime)

    def get_user_by_uid_with_options(
        self,
        request: teambition_aliyun_20200226_models.GetUserByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetUserByUidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetUserByUidResponse().from_map(
            self.do_rpcrequest('GetUserByUid', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_by_uid_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.GetUserByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.GetUserByUidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.GetUserByUidResponse().from_map(
            await self.do_rpcrequest_async('GetUserByUid', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_by_uid(
        self,
        request: teambition_aliyun_20200226_models.GetUserByUidRequest,
    ) -> teambition_aliyun_20200226_models.GetUserByUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_uid_with_options(request, runtime)

    async def get_user_by_uid_async(
        self,
        request: teambition_aliyun_20200226_models.GetUserByUidRequest,
    ) -> teambition_aliyun_20200226_models.GetUserByUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_by_uid_with_options_async(request, runtime)

    def insert_devops_member_with_options(
        self,
        request: teambition_aliyun_20200226_models.InsertDevopsMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.InsertDevopsMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.InsertDevopsMemberResponse().from_map(
            self.do_rpcrequest('InsertDevopsMember', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_devops_member_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.InsertDevopsMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.InsertDevopsMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.InsertDevopsMemberResponse().from_map(
            await self.do_rpcrequest_async('InsertDevopsMember', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_devops_member(
        self,
        request: teambition_aliyun_20200226_models.InsertDevopsMemberRequest,
    ) -> teambition_aliyun_20200226_models.InsertDevopsMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_devops_member_with_options(request, runtime)

    async def insert_devops_member_async(
        self,
        request: teambition_aliyun_20200226_models.InsertDevopsMemberRequest,
    ) -> teambition_aliyun_20200226_models.InsertDevopsMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_devops_member_with_options_async(request, runtime)

    def list_project_sprints_with_options(
        self,
        request: teambition_aliyun_20200226_models.ListProjectSprintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectSprintsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectSprintsResponse().from_map(
            self.do_rpcrequest('ListProjectSprints', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_sprints_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectSprintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectSprintsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectSprintsResponse().from_map(
            await self.do_rpcrequest_async('ListProjectSprints', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_sprints(
        self,
        request: teambition_aliyun_20200226_models.ListProjectSprintsRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectSprintsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_sprints_with_options(request, runtime)

    async def list_project_sprints_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectSprintsRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectSprintsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_sprints_with_options_async(request, runtime)

    def list_project_task_flow_with_options(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTaskFlowResponse().from_map(
            self.do_rpcrequest('ListProjectTaskFlow', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_task_flow_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTaskFlowResponse().from_map(
            await self.do_rpcrequest_async('ListProjectTaskFlow', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_task_flow(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_task_flow_with_options(request, runtime)

    async def list_project_task_flow_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_task_flow_with_options_async(request, runtime)

    def list_project_task_flow_status_with_options(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse().from_map(
            self.do_rpcrequest('ListProjectTaskFlowStatus', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_task_flow_status_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse().from_map(
            await self.do_rpcrequest_async('ListProjectTaskFlowStatus', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_task_flow_status(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowStatusRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_task_flow_status_with_options(request, runtime)

    async def list_project_task_flow_status_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTaskFlowStatusRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_task_flow_status_with_options_async(request, runtime)

    def list_project_tasks_with_options(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTasksResponse().from_map(
            self.do_rpcrequest('ListProjectTasks', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_tasks_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListProjectTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListProjectTasksResponse().from_map(
            await self.do_rpcrequest_async('ListProjectTasks', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_tasks(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTasksRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_tasks_with_options(request, runtime)

    async def list_project_tasks_async(
        self,
        request: teambition_aliyun_20200226_models.ListProjectTasksRequest,
    ) -> teambition_aliyun_20200226_models.ListProjectTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_tasks_with_options_async(request, runtime)

    def list_scenario_field_config_with_options(
        self,
        request: teambition_aliyun_20200226_models.ListScenarioFieldConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse().from_map(
            self.do_rpcrequest('ListScenarioFieldConfig', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenario_field_config_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ListScenarioFieldConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse().from_map(
            await self.do_rpcrequest_async('ListScenarioFieldConfig', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenario_field_config(
        self,
        request: teambition_aliyun_20200226_models.ListScenarioFieldConfigRequest,
    ) -> teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_field_config_with_options(request, runtime)

    async def list_scenario_field_config_async(
        self,
        request: teambition_aliyun_20200226_models.ListScenarioFieldConfigRequest,
    ) -> teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_field_config_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectResponse().from_map(
            self.do_rpcrequest('UpdateProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateProject', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_project_sprint_with_options(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectSprintResponse().from_map(
            self.do_rpcrequest('UpdateProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_sprint_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('UpdateProjectSprint', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project_sprint(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_sprint_with_options(request, runtime)

    async def update_project_sprint_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectSprintRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_sprint_with_options_async(request, runtime)

    def update_project_task_with_options(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectTaskResponse().from_map(
            self.do_rpcrequest('UpdateProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_task_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.UpdateProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return teambition_aliyun_20200226_models.UpdateProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('UpdateProjectTask', '2020-02-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project_task(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_task_with_options(request, runtime)

    async def update_project_task_async(
        self,
        request: teambition_aliyun_20200226_models.UpdateProjectTaskRequest,
    ) -> teambition_aliyun_20200226_models.UpdateProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_task_with_options_async(request, runtime)
