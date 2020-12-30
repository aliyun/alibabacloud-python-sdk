# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops_rdc20200303 import models as devops_rdc_20200303_models
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
        self._endpoint = self.get_endpoint('devops-rdc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_insert_members_with_options(
        self,
        request: devops_rdc_20200303_models.BatchInsertMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.BatchInsertMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.BatchInsertMembersResponse().from_map(
            self.do_rpcrequest('BatchInsertMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_insert_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.BatchInsertMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.BatchInsertMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.BatchInsertMembersResponse().from_map(
            await self.do_rpcrequest_async('BatchInsertMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_insert_members(
        self,
        request: devops_rdc_20200303_models.BatchInsertMembersRequest,
    ) -> devops_rdc_20200303_models.BatchInsertMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_insert_members_with_options(request, runtime)

    async def batch_insert_members_async(
        self,
        request: devops_rdc_20200303_models.BatchInsertMembersRequest,
    ) -> devops_rdc_20200303_models.BatchInsertMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_insert_members_with_options_async(request, runtime)

    def cancel_pipeline_with_options(
        self,
        request: devops_rdc_20200303_models.CancelPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CancelPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CancelPipelineResponse().from_map(
            self.do_rpcrequest('CancelPipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_pipeline_with_options_async(
        self,
        request: devops_rdc_20200303_models.CancelPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CancelPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CancelPipelineResponse().from_map(
            await self.do_rpcrequest_async('CancelPipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_pipeline(
        self,
        request: devops_rdc_20200303_models.CancelPipelineRequest,
    ) -> devops_rdc_20200303_models.CancelPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_pipeline_with_options(request, runtime)

    async def cancel_pipeline_async(
        self,
        request: devops_rdc_20200303_models.CancelPipelineRequest,
    ) -> devops_rdc_20200303_models.CancelPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_pipeline_with_options_async(request, runtime)

    def check_aliyun_account_exists_with_options(
        self,
        request: devops_rdc_20200303_models.CheckAliyunAccountExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CheckAliyunAccountExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CheckAliyunAccountExistsResponse().from_map(
            self.do_rpcrequest('CheckAliyunAccountExists', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_aliyun_account_exists_with_options_async(
        self,
        request: devops_rdc_20200303_models.CheckAliyunAccountExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CheckAliyunAccountExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CheckAliyunAccountExistsResponse().from_map(
            await self.do_rpcrequest_async('CheckAliyunAccountExists', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_aliyun_account_exists(
        self,
        request: devops_rdc_20200303_models.CheckAliyunAccountExistsRequest,
    ) -> devops_rdc_20200303_models.CheckAliyunAccountExistsResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_aliyun_account_exists_with_options(request, runtime)

    async def check_aliyun_account_exists_async(
        self,
        request: devops_rdc_20200303_models.CheckAliyunAccountExistsRequest,
    ) -> devops_rdc_20200303_models.CheckAliyunAccountExistsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_aliyun_account_exists_with_options_async(request, runtime)

    def create_common_group_with_options(
        self,
        request: devops_rdc_20200303_models.CreateCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateCommonGroupResponse().from_map(
            self.do_rpcrequest('CreateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_common_group_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateCommonGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_common_group(
        self,
        request: devops_rdc_20200303_models.CreateCommonGroupRequest,
    ) -> devops_rdc_20200303_models.CreateCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_common_group_with_options(request, runtime)

    async def create_common_group_async(
        self,
        request: devops_rdc_20200303_models.CreateCommonGroupRequest,
    ) -> devops_rdc_20200303_models.CreateCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_common_group_with_options_async(request, runtime)

    def create_credential_with_options(
        self,
        request: devops_rdc_20200303_models.CreateCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateCredentialResponse().from_map(
            self.do_rpcrequest('CreateCredential', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateCredentialResponse().from_map(
            await self.do_rpcrequest_async('CreateCredential', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_credential(
        self,
        request: devops_rdc_20200303_models.CreateCredentialRequest,
    ) -> devops_rdc_20200303_models.CreateCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_credential_with_options(request, runtime)

    async def create_credential_async(
        self,
        request: devops_rdc_20200303_models.CreateCredentialRequest,
    ) -> devops_rdc_20200303_models.CreateCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_credential_with_options_async(request, runtime)

    def create_devops_organization_with_options(
        self,
        request: devops_rdc_20200303_models.CreateDevopsOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsOrganizationResponse().from_map(
            self.do_rpcrequest('CreateDevopsOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_devops_organization_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsOrganizationResponse().from_map(
            await self.do_rpcrequest_async('CreateDevopsOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_organization(
        self,
        request: devops_rdc_20200303_models.CreateDevopsOrganizationRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devops_organization_with_options(request, runtime)

    async def create_devops_organization_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsOrganizationRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devops_organization_with_options_async(request, runtime)

    def create_devops_project_with_options(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectResponse().from_map(
            self.do_rpcrequest('CreateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_devops_project_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_with_options(request, runtime)

    async def create_devops_project_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devops_project_with_options_async(request, runtime)

    def create_devops_project_sprint_with_options(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectSprintResponse().from_map(
            self.do_rpcrequest('CreateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_devops_project_sprint_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('CreateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project_sprint(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_sprint_with_options(request, runtime)

    async def create_devops_project_sprint_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devops_project_sprint_with_options_async(request, runtime)

    def create_devops_project_task_with_options(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectTaskResponse().from_map(
            self.do_rpcrequest('CreateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_devops_project_task_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateDevopsProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project_task(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_task_with_options(request, runtime)

    async def create_devops_project_task_async(
        self,
        request: devops_rdc_20200303_models.CreateDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.CreateDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devops_project_task_with_options_async(request, runtime)

    def create_pipeline_with_options(
        self,
        request: devops_rdc_20200303_models.CreatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreatePipelineResponse().from_map(
            self.do_rpcrequest('CreatePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreatePipelineResponse().from_map(
            await self.do_rpcrequest_async('CreatePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pipeline(
        self,
        request: devops_rdc_20200303_models.CreatePipelineRequest,
    ) -> devops_rdc_20200303_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_with_options(request, runtime)

    async def create_pipeline_async(
        self,
        request: devops_rdc_20200303_models.CreatePipelineRequest,
    ) -> devops_rdc_20200303_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pipeline_with_options_async(request, runtime)

    def create_service_connection_with_options(
        self,
        request: devops_rdc_20200303_models.CreateServiceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateServiceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateServiceConnectionResponse().from_map(
            self.do_rpcrequest('CreateServiceConnection', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_connection_with_options_async(
        self,
        request: devops_rdc_20200303_models.CreateServiceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.CreateServiceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.CreateServiceConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreateServiceConnection', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_connection(
        self,
        request: devops_rdc_20200303_models.CreateServiceConnectionRequest,
    ) -> devops_rdc_20200303_models.CreateServiceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_connection_with_options(request, runtime)

    async def create_service_connection_async(
        self,
        request: devops_rdc_20200303_models.CreateServiceConnectionRequest,
    ) -> devops_rdc_20200303_models.CreateServiceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_connection_with_options_async(request, runtime)

    def delete_common_group_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteCommonGroupResponse().from_map(
            self.do_rpcrequest('DeleteCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_common_group_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteCommonGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_common_group(
        self,
        request: devops_rdc_20200303_models.DeleteCommonGroupRequest,
    ) -> devops_rdc_20200303_models.DeleteCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_common_group_with_options(request, runtime)

    async def delete_common_group_async(
        self,
        request: devops_rdc_20200303_models.DeleteCommonGroupRequest,
    ) -> devops_rdc_20200303_models.DeleteCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_common_group_with_options_async(request, runtime)

    def delete_devops_organization_members_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse().from_map(
            self.do_rpcrequest('DeleteDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_devops_organization_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_organization_members(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsOrganizationMembersRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_organization_members_with_options(request, runtime)

    async def delete_devops_organization_members_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsOrganizationMembersRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devops_organization_members_with_options_async(request, runtime)

    def delete_devops_project_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectResponse().from_map(
            self.do_rpcrequest('DeleteDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_devops_project_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_with_options(request, runtime)

    async def delete_devops_project_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devops_project_with_options_async(request, runtime)

    def delete_devops_project_members_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse().from_map(
            self.do_rpcrequest('DeleteDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_devops_project_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_members(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectMembersRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_members_with_options(request, runtime)

    async def delete_devops_project_members_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectMembersRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devops_project_members_with_options_async(request, runtime)

    def delete_devops_project_sprint_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse().from_map(
            self.do_rpcrequest('DeleteDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_devops_project_sprint_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_sprint(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_sprint_with_options(request, runtime)

    async def delete_devops_project_sprint_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devops_project_sprint_with_options_async(request, runtime)

    def delete_devops_project_task_with_options(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse().from_map(
            self.do_rpcrequest('DeleteDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_devops_project_task_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_task(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_task_with_options(request, runtime)

    async def delete_devops_project_task_async(
        self,
        request: devops_rdc_20200303_models.DeleteDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devops_project_task_with_options_async(request, runtime)

    def delete_pipeline_member_with_options(
        self,
        request: devops_rdc_20200303_models.DeletePipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeletePipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeletePipelineMemberResponse().from_map(
            self.do_rpcrequest('DeletePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_pipeline_member_with_options_async(
        self,
        request: devops_rdc_20200303_models.DeletePipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.DeletePipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.DeletePipelineMemberResponse().from_map(
            await self.do_rpcrequest_async('DeletePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pipeline_member(
        self,
        request: devops_rdc_20200303_models.DeletePipelineMemberRequest,
    ) -> devops_rdc_20200303_models.DeletePipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_member_with_options(request, runtime)

    async def delete_pipeline_member_async(
        self,
        request: devops_rdc_20200303_models.DeletePipelineMemberRequest,
    ) -> devops_rdc_20200303_models.DeletePipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pipeline_member_with_options_async(request, runtime)

    def execute_pipeline_with_options(
        self,
        request: devops_rdc_20200303_models.ExecutePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ExecutePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ExecutePipelineResponse().from_map(
            self.do_rpcrequest('ExecutePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_pipeline_with_options_async(
        self,
        request: devops_rdc_20200303_models.ExecutePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ExecutePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ExecutePipelineResponse().from_map(
            await self.do_rpcrequest_async('ExecutePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_pipeline(
        self,
        request: devops_rdc_20200303_models.ExecutePipelineRequest,
    ) -> devops_rdc_20200303_models.ExecutePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_pipeline_with_options(request, runtime)

    async def execute_pipeline_async(
        self,
        request: devops_rdc_20200303_models.ExecutePipelineRequest,
    ) -> devops_rdc_20200303_models.ExecutePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_pipeline_with_options_async(request, runtime)

    def get_devops_organization_members_with_options(
        self,
        request: devops_rdc_20200303_models.GetDevopsOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse().from_map(
            self.do_rpcrequest('GetDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_devops_organization_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse().from_map(
            await self.do_rpcrequest_async('GetDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_organization_members(
        self,
        request: devops_rdc_20200303_models.GetDevopsOrganizationMembersRequest,
    ) -> devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_devops_organization_members_with_options(request, runtime)

    async def get_devops_organization_members_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsOrganizationMembersRequest,
    ) -> devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_devops_organization_members_with_options_async(request, runtime)

    def get_devops_project_info_with_options(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectInfoResponse().from_map(
            self.do_rpcrequest('GetDevopsProjectInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_devops_project_info_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectInfoResponse().from_map(
            await self.do_rpcrequest_async('GetDevopsProjectInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_info(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_info_with_options(request, runtime)

    async def get_devops_project_info_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_devops_project_info_with_options_async(request, runtime)

    def get_devops_project_members_with_options(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectMembersResponse().from_map(
            self.do_rpcrequest('GetDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_devops_project_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('GetDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_members(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectMembersRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_members_with_options(request, runtime)

    async def get_devops_project_members_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectMembersRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_devops_project_members_with_options_async(request, runtime)

    def get_devops_project_sprint_info_with_options(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectSprintInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse().from_map(
            self.do_rpcrequest('GetDevopsProjectSprintInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_devops_project_sprint_info_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectSprintInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse().from_map(
            await self.do_rpcrequest_async('GetDevopsProjectSprintInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_sprint_info(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectSprintInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_sprint_info_with_options(request, runtime)

    async def get_devops_project_sprint_info_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectSprintInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_devops_project_sprint_info_with_options_async(request, runtime)

    def get_devops_project_task_info_with_options(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse().from_map(
            self.do_rpcrequest('GetDevopsProjectTaskInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_devops_project_task_info_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse().from_map(
            await self.do_rpcrequest_async('GetDevopsProjectTaskInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_task_info(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectTaskInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_task_info_with_options(request, runtime)

    async def get_devops_project_task_info_async(
        self,
        request: devops_rdc_20200303_models.GetDevopsProjectTaskInfoRequest,
    ) -> devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_devops_project_task_info_with_options_async(request, runtime)

    def get_pipeline_instance_build_number_status_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse().from_map(
            self.do_rpcrequest('GetPipelineInstanceBuildNumberStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_instance_build_number_status_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineInstanceBuildNumberStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_build_number_status(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_build_number_status_with_options(request, runtime)

    async def get_pipeline_instance_build_number_status_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_instance_build_number_status_with_options_async(request, runtime)

    def get_pipeline_instance_group_status_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse().from_map(
            self.do_rpcrequest('GetPipelineInstanceGroupStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_instance_group_status_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineInstanceGroupStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_group_status(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceGroupStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_group_status_with_options(request, runtime)

    async def get_pipeline_instance_group_status_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceGroupStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_instance_group_status_with_options_async(request, runtime)

    def get_pipeline_instance_info_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceInfoResponse().from_map(
            self.do_rpcrequest('GetPipelineInstanceInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_instance_info_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceInfoResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineInstanceInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_info(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceInfoRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_info_with_options(request, runtime)

    async def get_pipeline_instance_info_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceInfoRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_instance_info_with_options_async(request, runtime)

    def get_pipeline_instance_status_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceStatusResponse().from_map(
            self.do_rpcrequest('GetPipelineInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_instance_status_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_status(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_status_with_options(request, runtime)

    async def get_pipeline_instance_status_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstanceStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_instance_status_with_options_async(request, runtime)

    def get_pipeline_inst_history_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstHistoryResponse().from_map(
            self.do_rpcrequest('GetPipelineInstHistory', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_inst_history_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineInstHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineInstHistoryResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineInstHistory', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_inst_history(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstHistoryRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_inst_history_with_options(request, runtime)

    async def get_pipeline_inst_history_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineInstHistoryRequest,
    ) -> devops_rdc_20200303_models.GetPipelineInstHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_inst_history_with_options_async(request, runtime)

    def get_pipeline_log_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineLogResponse().from_map(
            self.do_rpcrequest('GetPipelineLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_log_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineLogResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_log(
        self,
        request: devops_rdc_20200303_models.GetPipelineLogRequest,
    ) -> devops_rdc_20200303_models.GetPipelineLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_log_with_options(request, runtime)

    async def get_pipeline_log_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineLogRequest,
    ) -> devops_rdc_20200303_models.GetPipelineLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_log_with_options_async(request, runtime)

    def get_pipeline_step_log_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipelineStepLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineStepLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineStepLogResponse().from_map(
            self.do_rpcrequest('GetPipelineStepLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipeline_step_log_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineStepLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipelineStepLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipelineStepLogResponse().from_map(
            await self.do_rpcrequest_async('GetPipelineStepLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_step_log(
        self,
        request: devops_rdc_20200303_models.GetPipelineStepLogRequest,
    ) -> devops_rdc_20200303_models.GetPipelineStepLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_step_log_with_options(request, runtime)

    async def get_pipeline_step_log_async(
        self,
        request: devops_rdc_20200303_models.GetPipelineStepLogRequest,
    ) -> devops_rdc_20200303_models.GetPipelineStepLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_step_log_with_options_async(request, runtime)

    def get_pipleine_latest_instance_status_with_options(
        self,
        request: devops_rdc_20200303_models.GetPipleineLatestInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse().from_map(
            self.do_rpcrequest('GetPipleineLatestInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pipleine_latest_instance_status_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetPipleineLatestInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('GetPipleineLatestInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipleine_latest_instance_status(
        self,
        request: devops_rdc_20200303_models.GetPipleineLatestInstanceStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipleine_latest_instance_status_with_options(request, runtime)

    async def get_pipleine_latest_instance_status_async(
        self,
        request: devops_rdc_20200303_models.GetPipleineLatestInstanceStatusRequest,
    ) -> devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipleine_latest_instance_status_with_options_async(request, runtime)

    def get_project_option_with_options(
        self,
        request: devops_rdc_20200303_models.GetProjectOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetProjectOptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetProjectOptionResponse().from_map(
            self.do_rpcrequest('GetProjectOption', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_option_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetProjectOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetProjectOptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetProjectOptionResponse().from_map(
            await self.do_rpcrequest_async('GetProjectOption', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_option(
        self,
        request: devops_rdc_20200303_models.GetProjectOptionRequest,
    ) -> devops_rdc_20200303_models.GetProjectOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_option_with_options(request, runtime)

    async def get_project_option_async(
        self,
        request: devops_rdc_20200303_models.GetProjectOptionRequest,
    ) -> devops_rdc_20200303_models.GetProjectOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_option_with_options_async(request, runtime)

    def get_task_detail_activity_with_options(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskDetailActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskDetailActivityResponse().from_map(
            self.do_rpcrequest('GetTaskDetailActivity', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_detail_activity_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskDetailActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskDetailActivityResponse().from_map(
            await self.do_rpcrequest_async('GetTaskDetailActivity', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_detail_activity(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailActivityRequest,
    ) -> devops_rdc_20200303_models.GetTaskDetailActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_detail_activity_with_options(request, runtime)

    async def get_task_detail_activity_async(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailActivityRequest,
    ) -> devops_rdc_20200303_models.GetTaskDetailActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_detail_activity_with_options_async(request, runtime)

    def get_task_detail_base_with_options(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskDetailBaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskDetailBaseResponse().from_map(
            self.do_rpcrequest('GetTaskDetailBase', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_detail_base_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskDetailBaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskDetailBaseResponse().from_map(
            await self.do_rpcrequest_async('GetTaskDetailBase', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_detail_base(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailBaseRequest,
    ) -> devops_rdc_20200303_models.GetTaskDetailBaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_detail_base_with_options(request, runtime)

    async def get_task_detail_base_async(
        self,
        request: devops_rdc_20200303_models.GetTaskDetailBaseRequest,
    ) -> devops_rdc_20200303_models.GetTaskDetailBaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_detail_base_with_options_async(request, runtime)

    def get_task_list_filter_with_options(
        self,
        request: devops_rdc_20200303_models.GetTaskListFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskListFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskListFilterResponse().from_map(
            self.do_rpcrequest('GetTaskListFilter', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_list_filter_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetTaskListFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetTaskListFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetTaskListFilterResponse().from_map(
            await self.do_rpcrequest_async('GetTaskListFilter', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_list_filter(
        self,
        request: devops_rdc_20200303_models.GetTaskListFilterRequest,
    ) -> devops_rdc_20200303_models.GetTaskListFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_list_filter_with_options(request, runtime)

    async def get_task_list_filter_async(
        self,
        request: devops_rdc_20200303_models.GetTaskListFilterRequest,
    ) -> devops_rdc_20200303_models.GetTaskListFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_list_filter_with_options_async(request, runtime)

    def get_user_by_aliyun_uid_with_options(
        self,
        request: devops_rdc_20200303_models.GetUserByAliyunUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetUserByAliyunUidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetUserByAliyunUidResponse().from_map(
            self.do_rpcrequest('GetUserByAliyunUid', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_by_aliyun_uid_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetUserByAliyunUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetUserByAliyunUidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetUserByAliyunUidResponse().from_map(
            await self.do_rpcrequest_async('GetUserByAliyunUid', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_by_aliyun_uid(
        self,
        request: devops_rdc_20200303_models.GetUserByAliyunUidRequest,
    ) -> devops_rdc_20200303_models.GetUserByAliyunUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_aliyun_uid_with_options(request, runtime)

    async def get_user_by_aliyun_uid_async(
        self,
        request: devops_rdc_20200303_models.GetUserByAliyunUidRequest,
    ) -> devops_rdc_20200303_models.GetUserByAliyunUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_by_aliyun_uid_with_options_async(request, runtime)

    def get_user_name_with_options(
        self,
        request: devops_rdc_20200303_models.GetUserNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetUserNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetUserNameResponse().from_map(
            self.do_rpcrequest('GetUserName', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_name_with_options_async(
        self,
        request: devops_rdc_20200303_models.GetUserNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.GetUserNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.GetUserNameResponse().from_map(
            await self.do_rpcrequest_async('GetUserName', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_name(
        self,
        request: devops_rdc_20200303_models.GetUserNameRequest,
    ) -> devops_rdc_20200303_models.GetUserNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_name_with_options(request, runtime)

    async def get_user_name_async(
        self,
        request: devops_rdc_20200303_models.GetUserNameRequest,
    ) -> devops_rdc_20200303_models.GetUserNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_name_with_options_async(request, runtime)

    def insert_devops_user_with_options(
        self,
        request: devops_rdc_20200303_models.InsertDevopsUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertDevopsUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertDevopsUserResponse().from_map(
            self.do_rpcrequest('InsertDevopsUser', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_devops_user_with_options_async(
        self,
        request: devops_rdc_20200303_models.InsertDevopsUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertDevopsUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertDevopsUserResponse().from_map(
            await self.do_rpcrequest_async('InsertDevopsUser', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_devops_user(
        self,
        request: devops_rdc_20200303_models.InsertDevopsUserRequest,
    ) -> devops_rdc_20200303_models.InsertDevopsUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_devops_user_with_options(request, runtime)

    async def insert_devops_user_async(
        self,
        request: devops_rdc_20200303_models.InsertDevopsUserRequest,
    ) -> devops_rdc_20200303_models.InsertDevopsUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_devops_user_with_options_async(request, runtime)

    def insert_pipeline_member_with_options(
        self,
        request: devops_rdc_20200303_models.InsertPipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertPipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertPipelineMemberResponse().from_map(
            self.do_rpcrequest('InsertPipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_pipeline_member_with_options_async(
        self,
        request: devops_rdc_20200303_models.InsertPipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertPipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertPipelineMemberResponse().from_map(
            await self.do_rpcrequest_async('InsertPipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_pipeline_member(
        self,
        request: devops_rdc_20200303_models.InsertPipelineMemberRequest,
    ) -> devops_rdc_20200303_models.InsertPipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_pipeline_member_with_options(request, runtime)

    async def insert_pipeline_member_async(
        self,
        request: devops_rdc_20200303_models.InsertPipelineMemberRequest,
    ) -> devops_rdc_20200303_models.InsertPipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_pipeline_member_with_options_async(request, runtime)

    def insert_project_members_with_options(
        self,
        request: devops_rdc_20200303_models.InsertProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertProjectMembersResponse().from_map(
            self.do_rpcrequest('InsertProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_project_members_with_options_async(
        self,
        request: devops_rdc_20200303_models.InsertProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.InsertProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.InsertProjectMembersResponse().from_map(
            await self.do_rpcrequest_async('InsertProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_project_members(
        self,
        request: devops_rdc_20200303_models.InsertProjectMembersRequest,
    ) -> devops_rdc_20200303_models.InsertProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_project_members_with_options(request, runtime)

    async def insert_project_members_async(
        self,
        request: devops_rdc_20200303_models.InsertProjectMembersRequest,
    ) -> devops_rdc_20200303_models.InsertProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_project_members_with_options_async(request, runtime)

    def list_common_group_with_options(
        self,
        request: devops_rdc_20200303_models.ListCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListCommonGroupResponse().from_map(
            self.do_rpcrequest('ListCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_common_group_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListCommonGroupResponse().from_map(
            await self.do_rpcrequest_async('ListCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_common_group(
        self,
        request: devops_rdc_20200303_models.ListCommonGroupRequest,
    ) -> devops_rdc_20200303_models.ListCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_common_group_with_options(request, runtime)

    async def list_common_group_async(
        self,
        request: devops_rdc_20200303_models.ListCommonGroupRequest,
    ) -> devops_rdc_20200303_models.ListCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_common_group_with_options_async(request, runtime)

    def list_credentials_with_options(
        self,
        request: devops_rdc_20200303_models.ListCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListCredentialsResponse().from_map(
            self.do_rpcrequest('ListCredentials', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListCredentialsResponse().from_map(
            await self.do_rpcrequest_async('ListCredentials', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_credentials(
        self,
        request: devops_rdc_20200303_models.ListCredentialsRequest,
    ) -> devops_rdc_20200303_models.ListCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_credentials_with_options(request, runtime)

    async def list_credentials_async(
        self,
        request: devops_rdc_20200303_models.ListCredentialsRequest,
    ) -> devops_rdc_20200303_models.ListCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_credentials_with_options_async(request, runtime)

    def list_devops_project_sprints_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectSprintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectSprintsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectSprintsResponse().from_map(
            self.do_rpcrequest('ListDevopsProjectSprints', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_project_sprints_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectSprintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectSprintsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectSprintsResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsProjectSprints', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_sprints(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectSprintsRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectSprintsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_sprints_with_options(request, runtime)

    async def list_devops_project_sprints_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectSprintsRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectSprintsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_project_sprints_with_options_async(request, runtime)

    def list_devops_project_task_flow_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse().from_map(
            self.do_rpcrequest('ListDevopsProjectTaskFlow', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_project_task_flow_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsProjectTaskFlow', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_flow(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_flow_with_options(request, runtime)

    async def list_devops_project_task_flow_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_project_task_flow_with_options_async(request, runtime)

    def list_devops_project_task_flow_status_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse().from_map(
            self.do_rpcrequest('ListDevopsProjectTaskFlowStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_project_task_flow_status_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsProjectTaskFlowStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_flow_status(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_flow_status_with_options(request, runtime)

    async def list_devops_project_task_flow_status_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_project_task_flow_status_with_options_async(request, runtime)

    def list_devops_project_task_list_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskListResponse().from_map(
            self.do_rpcrequest('ListDevopsProjectTaskList', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_project_task_list_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTaskListResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsProjectTaskList', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_list(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskListRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_list_with_options(request, runtime)

    async def list_devops_project_task_list_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTaskListRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_project_task_list_with_options_async(request, runtime)

    def list_devops_project_tasks_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTasksResponse().from_map(
            self.do_rpcrequest('ListDevopsProjectTasks', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_project_tasks_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsProjectTasksResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsProjectTasks', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_tasks(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTasksRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_tasks_with_options(request, runtime)

    async def list_devops_project_tasks_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsProjectTasksRequest,
    ) -> devops_rdc_20200303_models.ListDevopsProjectTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_project_tasks_with_options_async(request, runtime)

    def list_devops_scenario_field_config_with_options(
        self,
        request: devops_rdc_20200303_models.ListDevopsScenarioFieldConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse().from_map(
            self.do_rpcrequest('ListDevopsScenarioFieldConfig', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devops_scenario_field_config_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsScenarioFieldConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse().from_map(
            await self.do_rpcrequest_async('ListDevopsScenarioFieldConfig', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_scenario_field_config(
        self,
        request: devops_rdc_20200303_models.ListDevopsScenarioFieldConfigRequest,
    ) -> devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devops_scenario_field_config_with_options(request, runtime)

    async def list_devops_scenario_field_config_async(
        self,
        request: devops_rdc_20200303_models.ListDevopsScenarioFieldConfigRequest,
    ) -> devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devops_scenario_field_config_with_options_async(request, runtime)

    def list_pipelines_with_options(
        self,
        request: devops_rdc_20200303_models.ListPipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListPipelinesResponse().from_map(
            self.do_rpcrequest('ListPipelines', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListPipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListPipelinesResponse().from_map(
            await self.do_rpcrequest_async('ListPipelines', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pipelines(
        self,
        request: devops_rdc_20200303_models.ListPipelinesRequest,
    ) -> devops_rdc_20200303_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pipelines_with_options(request, runtime)

    async def list_pipelines_async(
        self,
        request: devops_rdc_20200303_models.ListPipelinesRequest,
    ) -> devops_rdc_20200303_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pipelines_with_options_async(request, runtime)

    def list_project_custom_fields_with_options(
        self,
        request: devops_rdc_20200303_models.ListProjectCustomFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListProjectCustomFieldsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListProjectCustomFieldsResponse().from_map(
            self.do_rpcrequest('ListProjectCustomFields', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_custom_fields_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListProjectCustomFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListProjectCustomFieldsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListProjectCustomFieldsResponse().from_map(
            await self.do_rpcrequest_async('ListProjectCustomFields', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_custom_fields(
        self,
        request: devops_rdc_20200303_models.ListProjectCustomFieldsRequest,
    ) -> devops_rdc_20200303_models.ListProjectCustomFieldsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_custom_fields_with_options(request, runtime)

    async def list_project_custom_fields_async(
        self,
        request: devops_rdc_20200303_models.ListProjectCustomFieldsRequest,
    ) -> devops_rdc_20200303_models.ListProjectCustomFieldsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_custom_fields_with_options_async(request, runtime)

    def list_service_connections_with_options(
        self,
        request: devops_rdc_20200303_models.ListServiceConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListServiceConnectionsResponse().from_map(
            self.do_rpcrequest('ListServiceConnections', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_connections_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListServiceConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListServiceConnectionsResponse().from_map(
            await self.do_rpcrequest_async('ListServiceConnections', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_connections(
        self,
        request: devops_rdc_20200303_models.ListServiceConnectionsRequest,
    ) -> devops_rdc_20200303_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_connections_with_options(request, runtime)

    async def list_service_connections_async(
        self,
        request: devops_rdc_20200303_models.ListServiceConnectionsRequest,
    ) -> devops_rdc_20200303_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_connections_with_options_async(request, runtime)

    def list_smart_group_with_options(
        self,
        request: devops_rdc_20200303_models.ListSmartGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListSmartGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListSmartGroupResponse().from_map(
            self.do_rpcrequest('ListSmartGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_smart_group_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListSmartGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListSmartGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListSmartGroupResponse().from_map(
            await self.do_rpcrequest_async('ListSmartGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_smart_group(
        self,
        request: devops_rdc_20200303_models.ListSmartGroupRequest,
    ) -> devops_rdc_20200303_models.ListSmartGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_smart_group_with_options(request, runtime)

    async def list_smart_group_async(
        self,
        request: devops_rdc_20200303_models.ListSmartGroupRequest,
    ) -> devops_rdc_20200303_models.ListSmartGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_smart_group_with_options_async(request, runtime)

    def list_user_organization_with_options(
        self,
        request: devops_rdc_20200303_models.ListUserOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListUserOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListUserOrganizationResponse().from_map(
            self.do_rpcrequest('ListUserOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_organization_with_options_async(
        self,
        request: devops_rdc_20200303_models.ListUserOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.ListUserOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.ListUserOrganizationResponse().from_map(
            await self.do_rpcrequest_async('ListUserOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_organization(
        self,
        request: devops_rdc_20200303_models.ListUserOrganizationRequest,
    ) -> devops_rdc_20200303_models.ListUserOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_organization_with_options(request, runtime)

    async def list_user_organization_async(
        self,
        request: devops_rdc_20200303_models.ListUserOrganizationRequest,
    ) -> devops_rdc_20200303_models.ListUserOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_organization_with_options_async(request, runtime)

    def transfer_pipeline_owner_with_options(
        self,
        request: devops_rdc_20200303_models.TransferPipelineOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.TransferPipelineOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.TransferPipelineOwnerResponse().from_map(
            self.do_rpcrequest('TransferPipelineOwner', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_pipeline_owner_with_options_async(
        self,
        request: devops_rdc_20200303_models.TransferPipelineOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.TransferPipelineOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.TransferPipelineOwnerResponse().from_map(
            await self.do_rpcrequest_async('TransferPipelineOwner', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_pipeline_owner(
        self,
        request: devops_rdc_20200303_models.TransferPipelineOwnerRequest,
    ) -> devops_rdc_20200303_models.TransferPipelineOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_pipeline_owner_with_options(request, runtime)

    async def transfer_pipeline_owner_async(
        self,
        request: devops_rdc_20200303_models.TransferPipelineOwnerRequest,
    ) -> devops_rdc_20200303_models.TransferPipelineOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_pipeline_owner_with_options_async(request, runtime)

    def update_common_group_with_options(
        self,
        request: devops_rdc_20200303_models.UpdateCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateCommonGroupResponse().from_map(
            self.do_rpcrequest('UpdateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_common_group_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdateCommonGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateCommonGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateCommonGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_common_group(
        self,
        request: devops_rdc_20200303_models.UpdateCommonGroupRequest,
    ) -> devops_rdc_20200303_models.UpdateCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_common_group_with_options(request, runtime)

    async def update_common_group_async(
        self,
        request: devops_rdc_20200303_models.UpdateCommonGroupRequest,
    ) -> devops_rdc_20200303_models.UpdateCommonGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_common_group_with_options_async(request, runtime)

    def update_devops_project_with_options(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectResponse().from_map(
            self.do_rpcrequest('UpdateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_devops_project_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_with_options(request, runtime)

    async def update_devops_project_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_devops_project_with_options_async(request, runtime)

    def update_devops_project_sprint_with_options(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse().from_map(
            self.do_rpcrequest('UpdateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_devops_project_sprint_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectSprintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse().from_map(
            await self.do_rpcrequest_async('UpdateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project_sprint(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_sprint_with_options(request, runtime)

    async def update_devops_project_sprint_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectSprintRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_devops_project_sprint_with_options_async(request, runtime)

    def update_devops_project_task_with_options(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse().from_map(
            self.do_rpcrequest('UpdateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_devops_project_task_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse().from_map(
            await self.do_rpcrequest_async('UpdateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project_task(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_task_with_options(request, runtime)

    async def update_devops_project_task_async(
        self,
        request: devops_rdc_20200303_models.UpdateDevopsProjectTaskRequest,
    ) -> devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_devops_project_task_with_options_async(request, runtime)

    def update_pipeline_member_with_options(
        self,
        request: devops_rdc_20200303_models.UpdatePipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdatePipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdatePipelineMemberResponse().from_map(
            self.do_rpcrequest('UpdatePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_pipeline_member_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdatePipelineMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdatePipelineMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdatePipelineMemberResponse().from_map(
            await self.do_rpcrequest_async('UpdatePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pipeline_member(
        self,
        request: devops_rdc_20200303_models.UpdatePipelineMemberRequest,
    ) -> devops_rdc_20200303_models.UpdatePipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_member_with_options(request, runtime)

    async def update_pipeline_member_async(
        self,
        request: devops_rdc_20200303_models.UpdatePipelineMemberRequest,
    ) -> devops_rdc_20200303_models.UpdatePipelineMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_pipeline_member_with_options_async(request, runtime)

    def update_task_detail_with_options(
        self,
        request: devops_rdc_20200303_models.UpdateTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateTaskDetailResponse().from_map(
            self.do_rpcrequest('UpdateTaskDetail', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_task_detail_with_options_async(
        self,
        request: devops_rdc_20200303_models.UpdateTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> devops_rdc_20200303_models.UpdateTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return devops_rdc_20200303_models.UpdateTaskDetailResponse().from_map(
            await self.do_rpcrequest_async('UpdateTaskDetail', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_task_detail(
        self,
        request: devops_rdc_20200303_models.UpdateTaskDetailRequest,
    ) -> devops_rdc_20200303_models.UpdateTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_task_detail_with_options(request, runtime)

    async def update_task_detail_async(
        self,
        request: devops_rdc_20200303_models.UpdateTaskDetailRequest,
    ) -> devops_rdc_20200303_models.UpdateTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_task_detail_with_options_async(request, runtime)
