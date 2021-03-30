# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_teambition_aliyun20200226 import models as teambition_aliyun_20200226_models
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
        params = open_api_models.Params(
            action='AddProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.AddProjectMembersResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.AddProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DevelopScale'] = request.develop_scale
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ApplySmallMicro',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ApplySmallMicroResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_small_micro_with_options_async(
        self,
        request: teambition_aliyun_20200226_models.ApplySmallMicroRequest,
        runtime: util_models.RuntimeOptions,
    ) -> teambition_aliyun_20200226_models.ApplySmallMicroResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DevelopScale'] = request.develop_scale
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ApplySmallMicro',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ApplySmallMicroResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='BactchInsertMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.BactchInsertMembersResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='BactchInsertMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.BactchInsertMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CheckAliyunUserExists',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CheckAliyunUserExists',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CheckAliyunUserExistsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateDevopsOrg',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateDevopsOrgResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateDevopsOrg',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateDevopsOrgResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectSprintResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectSprintResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectTaskResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.CreateProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteMembersForOrg',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteMembersForOrgResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteMembersForOrg',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteMembersForOrgResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectMembersResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectSprintResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectSprintResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectTaskResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.DeleteProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetOrganizationMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetOrganizationMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectMembersResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectMembers',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectSprintInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectSprintInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectSprintInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectSprintInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectTaskInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectTaskInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectTaskInfo',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetProjectTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetUserByUid',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetUserByUidResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetUserByUid',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.GetUserByUidResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='InsertDevopsMember',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.InsertDevopsMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='InsertDevopsMember',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.InsertDevopsMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectSprints',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectSprintsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectSprints',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectSprintsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTaskFlow',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTaskFlowResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTaskFlow',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTaskFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTaskFlowStatus',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTaskFlowStatus',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTaskFlowStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTasks',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTasksResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProjectTasks',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListProjectTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListScenarioFieldConfig',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListScenarioFieldConfig',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.ListScenarioFieldConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectSprintResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProjectSprint',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectSprintResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectTaskResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateProjectTask',
            version='2020-02-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            teambition_aliyun_20200226_models.UpdateProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
