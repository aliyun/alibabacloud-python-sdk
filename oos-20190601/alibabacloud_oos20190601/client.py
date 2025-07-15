# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oos20190601 import models as oos_20190601_models
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
        self._endpoint = self.get_endpoint('oos', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_git_repository_with_options(
        self,
        request: oos_20190601_models.AnalyzeGitRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.AnalyzeGitRepositoryResponse:
        """
        @summary 分析仓库
        
        @param request: AnalyzeGitRepositoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeGitRepositoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.branch):
            query['Branch'] = request.branch
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeGitRepository',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.AnalyzeGitRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_git_repository_with_options_async(
        self,
        request: oos_20190601_models.AnalyzeGitRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.AnalyzeGitRepositoryResponse:
        """
        @summary 分析仓库
        
        @param request: AnalyzeGitRepositoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeGitRepositoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.branch):
            query['Branch'] = request.branch
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeGitRepository',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.AnalyzeGitRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_git_repository(
        self,
        request: oos_20190601_models.AnalyzeGitRepositoryRequest,
    ) -> oos_20190601_models.AnalyzeGitRepositoryResponse:
        """
        @summary 分析仓库
        
        @param request: AnalyzeGitRepositoryRequest
        @return: AnalyzeGitRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.analyze_git_repository_with_options(request, runtime)

    async def analyze_git_repository_async(
        self,
        request: oos_20190601_models.AnalyzeGitRepositoryRequest,
    ) -> oos_20190601_models.AnalyzeGitRepositoryResponse:
        """
        @summary 分析仓库
        
        @param request: AnalyzeGitRepositoryRequest
        @return: AnalyzeGitRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.analyze_git_repository_with_options_async(request, runtime)

    def cancel_execution_with_options(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CancelExecutionResponse:
        """
        @summary Cancels an execution.
        
        @param request: CancelExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CancelExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_execution_with_options_async(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CancelExecutionResponse:
        """
        @summary Cancels an execution.
        
        @param request: CancelExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CancelExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_execution(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
    ) -> oos_20190601_models.CancelExecutionResponse:
        """
        @summary Cancels an execution.
        
        @param request: CancelExecutionRequest
        @return: CancelExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_execution_with_options(request, runtime)

    async def cancel_execution_async(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
    ) -> oos_20190601_models.CancelExecutionResponse:
        """
        @summary Cancels an execution.
        
        @param request: CancelExecutionRequest
        @return: CancelExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_execution_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: oos_20190601_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ChangeResourceGroupResponse:
        """
        @summary Modifies the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: oos_20190601_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ChangeResourceGroupResponse:
        """
        @summary Modifies the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: oos_20190601_models.ChangeResourceGroupRequest,
    ) -> oos_20190601_models.ChangeResourceGroupResponse:
        """
        @summary Modifies the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: oos_20190601_models.ChangeResourceGroupRequest,
    ) -> oos_20190601_models.ChangeResourceGroupResponse:
        """
        @summary Modifies the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def continue_deploy_application_group_with_options(
        self,
        request: oos_20190601_models.ContinueDeployApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ContinueDeployApplicationGroupResponse:
        """
        @summary Continues deploying an application group when an error occurs for calling the DeployApplicationGroup operation. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ContinueDeployApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueDeployApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueDeployApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ContinueDeployApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deploy_application_group_with_options_async(
        self,
        request: oos_20190601_models.ContinueDeployApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ContinueDeployApplicationGroupResponse:
        """
        @summary Continues deploying an application group when an error occurs for calling the DeployApplicationGroup operation. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ContinueDeployApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueDeployApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueDeployApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ContinueDeployApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deploy_application_group(
        self,
        request: oos_20190601_models.ContinueDeployApplicationGroupRequest,
    ) -> oos_20190601_models.ContinueDeployApplicationGroupResponse:
        """
        @summary Continues deploying an application group when an error occurs for calling the DeployApplicationGroup operation. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ContinueDeployApplicationGroupRequest
        @return: ContinueDeployApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_application_group_with_options(request, runtime)

    async def continue_deploy_application_group_async(
        self,
        request: oos_20190601_models.ContinueDeployApplicationGroupRequest,
    ) -> oos_20190601_models.ContinueDeployApplicationGroupResponse:
        """
        @summary Continues deploying an application group when an error occurs for calling the DeployApplicationGroup operation. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ContinueDeployApplicationGroupRequest
        @return: ContinueDeployApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continue_deploy_application_group_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: oos_20190601_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateApplicationResponse:
        """
        @summary Creates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_config):
            request.alarm_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not UtilClient.is_unset(request.application_source):
            query['ApplicationSource'] = request.application_source
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateApplicationResponse:
        """
        @summary Creates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_config):
            request.alarm_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not UtilClient.is_unset(request.application_source):
            query['ApplicationSource'] = request.application_source
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: oos_20190601_models.CreateApplicationRequest,
    ) -> oos_20190601_models.CreateApplicationResponse:
        """
        @summary Creates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: oos_20190601_models.CreateApplicationRequest,
    ) -> oos_20190601_models.CreateApplicationResponse:
        """
        @summary Creates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_application_group_with_options(
        self,
        request: oos_20190601_models.CreateApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateApplicationGroupResponse:
        """
        @summary Creates an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cms_group_id):
            query['CmsGroupId'] = request.cms_group_id
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.import_tag_key):
            query['ImportTagKey'] = request.import_tag_key
        if not UtilClient.is_unset(request.import_tag_value):
            query['ImportTagValue'] = request.import_tag_value
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_group_with_options_async(
        self,
        request: oos_20190601_models.CreateApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateApplicationGroupResponse:
        """
        @summary Creates an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cms_group_id):
            query['CmsGroupId'] = request.cms_group_id
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.import_tag_key):
            query['ImportTagKey'] = request.import_tag_key
        if not UtilClient.is_unset(request.import_tag_value):
            query['ImportTagValue'] = request.import_tag_value
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_group(
        self,
        request: oos_20190601_models.CreateApplicationGroupRequest,
    ) -> oos_20190601_models.CreateApplicationGroupResponse:
        """
        @summary Creates an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationGroupRequest
        @return: CreateApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_group_with_options(request, runtime)

    async def create_application_group_async(
        self,
        request: oos_20190601_models.CreateApplicationGroupRequest,
    ) -> oos_20190601_models.CreateApplicationGroupResponse:
        """
        @summary Creates an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: CreateApplicationGroupRequest
        @return: CreateApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_group_with_options_async(request, runtime)

    def create_ops_item_with_options(
        self,
        tmp_req: oos_20190601_models.CreateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateOpsItemResponse:
        """
        @summary Creates an O\\\\\\\\\\\\&M Item.
        
        @param tmp_req: CreateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpsItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateOpsItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.solutions):
            query['Solutions'] = request.solutions
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ops_item_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateOpsItemResponse:
        """
        @summary Creates an O\\\\\\\\\\\\&M Item.
        
        @param tmp_req: CreateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpsItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateOpsItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.solutions):
            query['Solutions'] = request.solutions
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ops_item(
        self,
        request: oos_20190601_models.CreateOpsItemRequest,
    ) -> oos_20190601_models.CreateOpsItemResponse:
        """
        @summary Creates an O\\\\\\\\\\\\&M Item.
        
        @param request: CreateOpsItemRequest
        @return: CreateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ops_item_with_options(request, runtime)

    async def create_ops_item_async(
        self,
        request: oos_20190601_models.CreateOpsItemRequest,
    ) -> oos_20190601_models.CreateOpsItemResponse:
        """
        @summary Creates an O\\\\\\\\\\\\&M Item.
        
        @param request: CreateOpsItemRequest
        @return: CreateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ops_item_with_options_async(request, runtime)

    def create_parameter_with_options(
        self,
        tmp_req: oos_20190601_models.CreateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateParameterResponse:
        """
        @summary Creates a common parameter.
        
        @param tmp_req: CreateParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateParameterResponse:
        """
        @summary Creates a common parameter.
        
        @param tmp_req: CreateParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter(
        self,
        request: oos_20190601_models.CreateParameterRequest,
    ) -> oos_20190601_models.CreateParameterResponse:
        """
        @summary Creates a common parameter.
        
        @param request: CreateParameterRequest
        @return: CreateParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_with_options(request, runtime)

    async def create_parameter_async(
        self,
        request: oos_20190601_models.CreateParameterRequest,
    ) -> oos_20190601_models.CreateParameterResponse:
        """
        @summary Creates a common parameter.
        
        @param request: CreateParameterRequest
        @return: CreateParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_with_options_async(request, runtime)

    def create_patch_baseline_with_options(
        self,
        tmp_req: oos_20190601_models.CreatePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreatePatchBaselineResponse:
        """
        @summary Creates a patch baseline.
        
        @param tmp_req: CreatePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePatchBaselineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreatePatchBaselineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.rejected_patches):
            request.rejected_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not UtilClient.is_unset(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreatePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_patch_baseline_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreatePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreatePatchBaselineResponse:
        """
        @summary Creates a patch baseline.
        
        @param tmp_req: CreatePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePatchBaselineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreatePatchBaselineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.rejected_patches):
            request.rejected_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not UtilClient.is_unset(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreatePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_patch_baseline(
        self,
        request: oos_20190601_models.CreatePatchBaselineRequest,
    ) -> oos_20190601_models.CreatePatchBaselineResponse:
        """
        @summary Creates a patch baseline.
        
        @param request: CreatePatchBaselineRequest
        @return: CreatePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_patch_baseline_with_options(request, runtime)

    async def create_patch_baseline_async(
        self,
        request: oos_20190601_models.CreatePatchBaselineRequest,
    ) -> oos_20190601_models.CreatePatchBaselineResponse:
        """
        @summary Creates a patch baseline.
        
        @param request: CreatePatchBaselineRequest
        @return: CreatePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_patch_baseline_with_options_async(request, runtime)

    def create_secret_parameter_with_options(
        self,
        tmp_req: oos_20190601_models.CreateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        """
        @summary Creates an encryption parameter. Make sure that you have the permissions to call this operation.
        
        @param tmp_req: CreateSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateSecretParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_parameter_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        """
        @summary Creates an encryption parameter. Make sure that you have the permissions to call this operation.
        
        @param tmp_req: CreateSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateSecretParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret_parameter(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        """
        @summary Creates an encryption parameter. Make sure that you have the permissions to call this operation.
        
        @param request: CreateSecretParameterRequest
        @return: CreateSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_secret_parameter_with_options(request, runtime)

    async def create_secret_parameter_async(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        """
        @summary Creates an encryption parameter. Make sure that you have the permissions to call this operation.
        
        @param request: CreateSecretParameterRequest
        @return: CreateSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_parameter_with_options_async(request, runtime)

    def create_state_configuration_with_options(
        self,
        tmp_req: oos_20190601_models.CreateStateConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateStateConfigurationResponse:
        """
        @summary Creates a desired-state configuration.
        
        @param tmp_req: CreateStateConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStateConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateStateConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStateConfiguration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateStateConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_state_configuration_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateStateConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateStateConfigurationResponse:
        """
        @summary Creates a desired-state configuration.
        
        @param tmp_req: CreateStateConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStateConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateStateConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStateConfiguration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateStateConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_state_configuration(
        self,
        request: oos_20190601_models.CreateStateConfigurationRequest,
    ) -> oos_20190601_models.CreateStateConfigurationResponse:
        """
        @summary Creates a desired-state configuration.
        
        @param request: CreateStateConfigurationRequest
        @return: CreateStateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_state_configuration_with_options(request, runtime)

    async def create_state_configuration_async(
        self,
        request: oos_20190601_models.CreateStateConfigurationRequest,
    ) -> oos_20190601_models.CreateStateConfigurationResponse:
        """
        @summary Creates a desired-state configuration.
        
        @param request: CreateStateConfigurationRequest
        @return: CreateStateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_state_configuration_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        tmp_req: oos_20190601_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateTemplateResponse:
        """
        @summary Creates a template.
        
        @param tmp_req: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateTemplateResponse:
        """
        @summary Creates a template.
        
        @param tmp_req: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: oos_20190601_models.CreateTemplateRequest,
    ) -> oos_20190601_models.CreateTemplateResponse:
        """
        @summary Creates a template.
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: oos_20190601_models.CreateTemplateRequest,
    ) -> oos_20190601_models.CreateTemplateResponse:
        """
        @summary Creates a template.
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: oos_20190601_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteApplicationResponse:
        """
        @summary Deletes an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: oos_20190601_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteApplicationResponse:
        """
        @summary Deletes an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: oos_20190601_models.DeleteApplicationRequest,
    ) -> oos_20190601_models.DeleteApplicationResponse:
        """
        @summary Deletes an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: oos_20190601_models.DeleteApplicationRequest,
    ) -> oos_20190601_models.DeleteApplicationResponse:
        """
        @summary Deletes an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_application_group_with_options(
        self,
        request: oos_20190601_models.DeleteApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteApplicationGroupResponse:
        """
        @summary Deletes an application group. You can call this operation only for the application groups which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_group_with_options_async(
        self,
        request: oos_20190601_models.DeleteApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteApplicationGroupResponse:
        """
        @summary Deletes an application group. You can call this operation only for the application groups which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_group(
        self,
        request: oos_20190601_models.DeleteApplicationGroupRequest,
    ) -> oos_20190601_models.DeleteApplicationGroupResponse:
        """
        @summary Deletes an application group. You can call this operation only for the application groups which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationGroupRequest
        @return: DeleteApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_group_with_options(request, runtime)

    async def delete_application_group_async(
        self,
        request: oos_20190601_models.DeleteApplicationGroupRequest,
    ) -> oos_20190601_models.DeleteApplicationGroupResponse:
        """
        @summary Deletes an application group. You can call this operation only for the application groups which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeleteApplicationGroupRequest
        @return: DeleteApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_group_with_options_async(request, runtime)

    def delete_executions_with_options(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        """
        @summary Deletes multiple executions.
        
        @param request: DeleteExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_ids):
            query['ExecutionIds'] = request.execution_ids
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_executions_with_options_async(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        """
        @summary Deletes multiple executions.
        
        @param request: DeleteExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_ids):
            query['ExecutionIds'] = request.execution_ids
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_executions(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        """
        @summary Deletes multiple executions.
        
        @param request: DeleteExecutionsRequest
        @return: DeleteExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_executions_with_options(request, runtime)

    async def delete_executions_async(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        """
        @summary Deletes multiple executions.
        
        @param request: DeleteExecutionsRequest
        @return: DeleteExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_executions_with_options_async(request, runtime)

    def delete_ops_items_with_options(
        self,
        request: oos_20190601_models.DeleteOpsItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteOpsItemsResponse:
        """
        @summary Deletes O\\\\\\&M Items.
        
        @param request: DeleteOpsItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOpsItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ops_item_ids):
            query['OpsItemIds'] = request.ops_item_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOpsItems',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteOpsItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ops_items_with_options_async(
        self,
        request: oos_20190601_models.DeleteOpsItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteOpsItemsResponse:
        """
        @summary Deletes O\\\\\\&M Items.
        
        @param request: DeleteOpsItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOpsItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ops_item_ids):
            query['OpsItemIds'] = request.ops_item_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOpsItems',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteOpsItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ops_items(
        self,
        request: oos_20190601_models.DeleteOpsItemsRequest,
    ) -> oos_20190601_models.DeleteOpsItemsResponse:
        """
        @summary Deletes O\\\\\\&M Items.
        
        @param request: DeleteOpsItemsRequest
        @return: DeleteOpsItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ops_items_with_options(request, runtime)

    async def delete_ops_items_async(
        self,
        request: oos_20190601_models.DeleteOpsItemsRequest,
    ) -> oos_20190601_models.DeleteOpsItemsResponse:
        """
        @summary Deletes O\\\\\\&M Items.
        
        @param request: DeleteOpsItemsRequest
        @return: DeleteOpsItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ops_items_with_options_async(request, runtime)

    def delete_parameter_with_options(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteParameterResponse:
        """
        @summary Deletes a common parameter.
        
        @param request: DeleteParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_with_options_async(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteParameterResponse:
        """
        @summary Deletes a common parameter.
        
        @param request: DeleteParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
    ) -> oos_20190601_models.DeleteParameterResponse:
        """
        @summary Deletes a common parameter.
        
        @param request: DeleteParameterRequest
        @return: DeleteParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_with_options(request, runtime)

    async def delete_parameter_async(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
    ) -> oos_20190601_models.DeleteParameterResponse:
        """
        @summary Deletes a common parameter.
        
        @param request: DeleteParameterRequest
        @return: DeleteParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_with_options_async(request, runtime)

    def delete_patch_baseline_with_options(
        self,
        request: oos_20190601_models.DeletePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeletePatchBaselineResponse:
        """
        @summary Deletes a patch baseline.
        
        @param request: DeletePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeletePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_patch_baseline_with_options_async(
        self,
        request: oos_20190601_models.DeletePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeletePatchBaselineResponse:
        """
        @summary Deletes a patch baseline.
        
        @param request: DeletePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeletePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_patch_baseline(
        self,
        request: oos_20190601_models.DeletePatchBaselineRequest,
    ) -> oos_20190601_models.DeletePatchBaselineResponse:
        """
        @summary Deletes a patch baseline.
        
        @param request: DeletePatchBaselineRequest
        @return: DeletePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_patch_baseline_with_options(request, runtime)

    async def delete_patch_baseline_async(
        self,
        request: oos_20190601_models.DeletePatchBaselineRequest,
    ) -> oos_20190601_models.DeletePatchBaselineResponse:
        """
        @summary Deletes a patch baseline.
        
        @param request: DeletePatchBaselineRequest
        @return: DeletePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_patch_baseline_with_options_async(request, runtime)

    def delete_secret_parameter_with_options(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        """
        @summary Deletes an encryption parameter. Make sure that you have the permissions to call the DeleteSecret operation before you call this operation.
        
        @param request: DeleteSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        """
        @summary Deletes an encryption parameter. Make sure that you have the permissions to call the DeleteSecret operation before you call this operation.
        
        @param request: DeleteSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_parameter(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        """
        @summary Deletes an encryption parameter. Make sure that you have the permissions to call the DeleteSecret operation before you call this operation.
        
        @param request: DeleteSecretParameterRequest
        @return: DeleteSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_parameter_with_options(request, runtime)

    async def delete_secret_parameter_async(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        """
        @summary Deletes an encryption parameter. Make sure that you have the permissions to call the DeleteSecret operation before you call this operation.
        
        @param request: DeleteSecretParameterRequest
        @return: DeleteSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_parameter_with_options_async(request, runtime)

    def delete_state_configurations_with_options(
        self,
        request: oos_20190601_models.DeleteStateConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteStateConfigurationsResponse:
        """
        @summary Deletes multiple desired-state configurations at a time.
        
        @param request: DeleteStateConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStateConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStateConfigurations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteStateConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_state_configurations_with_options_async(
        self,
        request: oos_20190601_models.DeleteStateConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteStateConfigurationsResponse:
        """
        @summary Deletes multiple desired-state configurations at a time.
        
        @param request: DeleteStateConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStateConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStateConfigurations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteStateConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_state_configurations(
        self,
        request: oos_20190601_models.DeleteStateConfigurationsRequest,
    ) -> oos_20190601_models.DeleteStateConfigurationsResponse:
        """
        @summary Deletes multiple desired-state configurations at a time.
        
        @param request: DeleteStateConfigurationsRequest
        @return: DeleteStateConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_state_configurations_with_options(request, runtime)

    async def delete_state_configurations_async(
        self,
        request: oos_20190601_models.DeleteStateConfigurationsRequest,
    ) -> oos_20190601_models.DeleteStateConfigurationsResponse:
        """
        @summary Deletes multiple desired-state configurations at a time.
        
        @param request: DeleteStateConfigurationsRequest
        @return: DeleteStateConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_state_configurations_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        """
        @summary Deletes a template.
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        """
        @summary Deletes a template.
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        """
        @summary Deletes a template.
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        """
        @summary Deletes a template.
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_templates_with_options(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        """
        @summary Deletes multiple templates.
        
        @param request: DeleteTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_templates_with_options_async(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        """
        @summary Deletes multiple templates.
        
        @param request: DeleteTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeleteTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_templates(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        """
        @summary Deletes multiple templates.
        
        @param request: DeleteTemplatesRequest
        @return: DeleteTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_templates_with_options(request, runtime)

    async def delete_templates_async(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        """
        @summary Deletes multiple templates.
        
        @param request: DeleteTemplatesRequest
        @return: DeleteTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_templates_with_options_async(request, runtime)

    def deploy_application_group_with_options(
        self,
        request: oos_20190601_models.DeployApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeployApplicationGroupResponse:
        """
        @summary Deploys an application group. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeployApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeployApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_group_with_options_async(
        self,
        request: oos_20190601_models.DeployApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeployApplicationGroupResponse:
        """
        @summary Deploys an application group. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeployApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DeployApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application_group(
        self,
        request: oos_20190601_models.DeployApplicationGroupRequest,
    ) -> oos_20190601_models.DeployApplicationGroupResponse:
        """
        @summary Deploys an application group. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeployApplicationGroupRequest
        @return: DeployApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_application_group_with_options(request, runtime)

    async def deploy_application_group_async(
        self,
        request: oos_20190601_models.DeployApplicationGroupRequest,
    ) -> oos_20190601_models.DeployApplicationGroupResponse:
        """
        @summary Deploys an application group. You can call this operation only for the applications which reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: DeployApplicationGroupRequest
        @return: DeployApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_application_group_with_options_async(request, runtime)

    def describe_application_group_bill_with_options(
        self,
        request: oos_20190601_models.DescribeApplicationGroupBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeApplicationGroupBillResponse:
        """
        @summary 查询应用分组资源成本
        
        @param request: DescribeApplicationGroupBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationGroupBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroupBill',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DescribeApplicationGroupBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_group_bill_with_options_async(
        self,
        request: oos_20190601_models.DescribeApplicationGroupBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeApplicationGroupBillResponse:
        """
        @summary 查询应用分组资源成本
        
        @param request: DescribeApplicationGroupBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationGroupBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroupBill',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DescribeApplicationGroupBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_group_bill(
        self,
        request: oos_20190601_models.DescribeApplicationGroupBillRequest,
    ) -> oos_20190601_models.DescribeApplicationGroupBillResponse:
        """
        @summary 查询应用分组资源成本
        
        @param request: DescribeApplicationGroupBillRequest
        @return: DescribeApplicationGroupBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_application_group_bill_with_options(request, runtime)

    async def describe_application_group_bill_async(
        self,
        request: oos_20190601_models.DescribeApplicationGroupBillRequest,
    ) -> oos_20190601_models.DescribeApplicationGroupBillResponse:
        """
        @summary 查询应用分组资源成本
        
        @param request: DescribeApplicationGroupBillRequest
        @return: DescribeApplicationGroupBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_application_group_bill_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def generate_execution_policy_with_options(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        """
        @summary Queries the Resource Access Management (RAM) policy required for template execution.
        
        @param request: GenerateExecutionPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateExecutionPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateExecutionPolicy',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GenerateExecutionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_execution_policy_with_options_async(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        """
        @summary Queries the Resource Access Management (RAM) policy required for template execution.
        
        @param request: GenerateExecutionPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateExecutionPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateExecutionPolicy',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GenerateExecutionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_execution_policy(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        """
        @summary Queries the Resource Access Management (RAM) policy required for template execution.
        
        @param request: GenerateExecutionPolicyRequest
        @return: GenerateExecutionPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_execution_policy_with_options(request, runtime)

    async def generate_execution_policy_async(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        """
        @summary Queries the Resource Access Management (RAM) policy required for template execution.
        
        @param request: GenerateExecutionPolicyRequest
        @return: GenerateExecutionPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_execution_policy_with_options_async(request, runtime)

    def generate_ops_item_with_options(
        self,
        request: oos_20190601_models.GenerateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateOpsItemResponse:
        """
        @summary Generates an O\\\\\\&M item.
        
        @param request: GenerateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOpsItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_id):
            query['ConfigurationId'] = request.configuration_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GenerateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_ops_item_with_options_async(
        self,
        request: oos_20190601_models.GenerateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateOpsItemResponse:
        """
        @summary Generates an O\\\\\\&M item.
        
        @param request: GenerateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOpsItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_id):
            query['ConfigurationId'] = request.configuration_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GenerateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_ops_item(
        self,
        request: oos_20190601_models.GenerateOpsItemRequest,
    ) -> oos_20190601_models.GenerateOpsItemResponse:
        """
        @summary Generates an O\\\\\\&M item.
        
        @param request: GenerateOpsItemRequest
        @return: GenerateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_ops_item_with_options(request, runtime)

    async def generate_ops_item_async(
        self,
        request: oos_20190601_models.GenerateOpsItemRequest,
    ) -> oos_20190601_models.GenerateOpsItemResponse:
        """
        @summary Generates an O\\\\\\&M item.
        
        @param request: GenerateOpsItemRequest
        @return: GenerateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_ops_item_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: oos_20190601_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetApplicationResponse:
        """
        @summary Queries the information of an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: oos_20190601_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetApplicationResponse:
        """
        @summary Queries the information of an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: oos_20190601_models.GetApplicationRequest,
    ) -> oos_20190601_models.GetApplicationResponse:
        """
        @summary Queries the information of an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: oos_20190601_models.GetApplicationRequest,
    ) -> oos_20190601_models.GetApplicationResponse:
        """
        @summary Queries the information of an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_group_with_options(
        self,
        request: oos_20190601_models.GetApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetApplicationGroupResponse:
        """
        @summary Queries the information about an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_group_with_options_async(
        self,
        request: oos_20190601_models.GetApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetApplicationGroupResponse:
        """
        @summary Queries the information about an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_group(
        self,
        request: oos_20190601_models.GetApplicationGroupRequest,
    ) -> oos_20190601_models.GetApplicationGroupResponse:
        """
        @summary Queries the information about an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationGroupRequest
        @return: GetApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_group_with_options(request, runtime)

    async def get_application_group_async(
        self,
        request: oos_20190601_models.GetApplicationGroupRequest,
    ) -> oos_20190601_models.GetApplicationGroupResponse:
        """
        @summary Queries the information about an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: GetApplicationGroupRequest
        @return: GetApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_group_with_options_async(request, runtime)

    def get_execution_template_with_options(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        """
        @summary Queries the information about the template of an execution, including the content of the template.
        
        @param request: GetExecutionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecutionTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecutionTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetExecutionTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execution_template_with_options_async(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        """
        @summary Queries the information about the template of an execution, including the content of the template.
        
        @param request: GetExecutionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecutionTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecutionTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetExecutionTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execution_template(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        """
        @summary Queries the information about the template of an execution, including the content of the template.
        
        @param request: GetExecutionTemplateRequest
        @return: GetExecutionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_execution_template_with_options(request, runtime)

    async def get_execution_template_async(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        """
        @summary Queries the information about the template of an execution, including the content of the template.
        
        @param request: GetExecutionTemplateRequest
        @return: GetExecutionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_execution_template_with_options_async(request, runtime)

    def get_inventory_schema_with_options(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        """
        @summary Queries the properties of a configuration list.
        
        @param request: GetInventorySchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInventorySchemaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInventorySchema',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetInventorySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inventory_schema_with_options_async(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        """
        @summary Queries the properties of a configuration list.
        
        @param request: GetInventorySchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInventorySchemaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInventorySchema',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetInventorySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inventory_schema(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        """
        @summary Queries the properties of a configuration list.
        
        @param request: GetInventorySchemaRequest
        @return: GetInventorySchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_schema_with_options(request, runtime)

    async def get_inventory_schema_async(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        """
        @summary Queries the properties of a configuration list.
        
        @param request: GetInventorySchemaRequest
        @return: GetInventorySchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_inventory_schema_with_options_async(request, runtime)

    def get_ops_item_with_options(
        self,
        request: oos_20190601_models.GetOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetOpsItemResponse:
        """
        @summary Queries the details of an O\\\\\\\\\\\\&M item.
        
        @param request: GetOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpsItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ops_item_with_options_async(
        self,
        request: oos_20190601_models.GetOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetOpsItemResponse:
        """
        @summary Queries the details of an O\\\\\\\\\\\\&M item.
        
        @param request: GetOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpsItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ops_item(
        self,
        request: oos_20190601_models.GetOpsItemRequest,
    ) -> oos_20190601_models.GetOpsItemResponse:
        """
        @summary Queries the details of an O\\\\\\\\\\\\&M item.
        
        @param request: GetOpsItemRequest
        @return: GetOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ops_item_with_options(request, runtime)

    async def get_ops_item_async(
        self,
        request: oos_20190601_models.GetOpsItemRequest,
    ) -> oos_20190601_models.GetOpsItemResponse:
        """
        @summary Queries the details of an O\\\\\\\\\\\\&M item.
        
        @param request: GetOpsItemRequest
        @return: GetOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ops_item_with_options_async(request, runtime)

    def get_parameter_with_options(
        self,
        request: oos_20190601_models.GetParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParameterResponse:
        """
        @summary Queries a common parameter and its value.
        
        @param request: GetParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameter_with_options_async(
        self,
        request: oos_20190601_models.GetParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParameterResponse:
        """
        @summary Queries a common parameter and its value.
        
        @param request: GetParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameter(
        self,
        request: oos_20190601_models.GetParameterRequest,
    ) -> oos_20190601_models.GetParameterResponse:
        """
        @summary Queries a common parameter and its value.
        
        @param request: GetParameterRequest
        @return: GetParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_parameter_with_options(request, runtime)

    async def get_parameter_async(
        self,
        request: oos_20190601_models.GetParameterRequest,
    ) -> oos_20190601_models.GetParameterResponse:
        """
        @summary Queries a common parameter and its value.
        
        @param request: GetParameterRequest
        @return: GetParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_parameter_with_options_async(request, runtime)

    def get_parameters_with_options(
        self,
        request: oos_20190601_models.GetParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersResponse:
        """
        @summary Queries the information about one or more parameters.
        
        @param request: GetParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_with_options_async(
        self,
        request: oos_20190601_models.GetParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersResponse:
        """
        @summary Queries the information about one or more parameters.
        
        @param request: GetParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters(
        self,
        request: oos_20190601_models.GetParametersRequest,
    ) -> oos_20190601_models.GetParametersResponse:
        """
        @summary Queries the information about one or more parameters.
        
        @param request: GetParametersRequest
        @return: GetParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_with_options(request, runtime)

    async def get_parameters_async(
        self,
        request: oos_20190601_models.GetParametersRequest,
    ) -> oos_20190601_models.GetParametersResponse:
        """
        @summary Queries the information about one or more parameters.
        
        @param request: GetParametersRequest
        @return: GetParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_with_options_async(request, runtime)

    def get_parameters_by_path_with_options(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        """
        @summary Queries one or more parameters by path.
        
        @param request: GetParametersByPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersByPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParametersByPath',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParametersByPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_by_path_with_options_async(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        """
        @summary Queries one or more parameters by path.
        
        @param request: GetParametersByPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersByPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParametersByPath',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetParametersByPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters_by_path(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        """
        @summary Queries one or more parameters by path.
        
        @param request: GetParametersByPathRequest
        @return: GetParametersByPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_by_path_with_options(request, runtime)

    async def get_parameters_by_path_async(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        """
        @summary Queries one or more parameters by path.
        
        @param request: GetParametersByPathRequest
        @return: GetParametersByPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_by_path_with_options_async(request, runtime)

    def get_patch_baseline_with_options(
        self,
        request: oos_20190601_models.GetPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetPatchBaselineResponse:
        """
        @summary Queries the information of a patch baseline.
        
        @param request: GetPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patch_baseline_with_options_async(
        self,
        request: oos_20190601_models.GetPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetPatchBaselineResponse:
        """
        @summary Queries the information of a patch baseline.
        
        @param request: GetPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patch_baseline(
        self,
        request: oos_20190601_models.GetPatchBaselineRequest,
    ) -> oos_20190601_models.GetPatchBaselineResponse:
        """
        @summary Queries the information of a patch baseline.
        
        @param request: GetPatchBaselineRequest
        @return: GetPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_patch_baseline_with_options(request, runtime)

    async def get_patch_baseline_async(
        self,
        request: oos_20190601_models.GetPatchBaselineRequest,
    ) -> oos_20190601_models.GetPatchBaselineResponse:
        """
        @summary Queries the information of a patch baseline.
        
        @param request: GetPatchBaselineRequest
        @return: GetPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_patch_baseline_with_options_async(request, runtime)

    def get_secret_parameter_with_options(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        """
        @summary Queries the information about an encryption parameter, including the parameter value. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        """
        @summary Queries the information about an encryption parameter, including the parameter value. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameter(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        """
        @summary Queries the information about an encryption parameter, including the parameter value. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParameterRequest
        @return: GetSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameter_with_options(request, runtime)

    async def get_secret_parameter_async(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        """
        @summary Queries the information about an encryption parameter, including the parameter value. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParameterRequest
        @return: GetSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameter_with_options_async(request, runtime)

    def get_secret_parameters_with_options(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        """
        @summary Queries the information about one or more encryption parameters. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameters_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        """
        @summary Queries the information about one or more encryption parameters. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameters(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        """
        @summary Queries the information about one or more encryption parameters. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersRequest
        @return: GetSecretParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameters_with_options(request, runtime)

    async def get_secret_parameters_async(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        """
        @summary Queries the information about one or more encryption parameters. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersRequest
        @return: GetSecretParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameters_with_options_async(request, runtime)

    def get_secret_parameters_by_path_with_options(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        """
        @summary Queries encryption parameters by path. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersByPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParametersByPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParametersByPath',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParametersByPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameters_by_path_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        """
        @summary Queries encryption parameters by path. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersByPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretParametersByPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretParametersByPath',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetSecretParametersByPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameters_by_path(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        """
        @summary Queries encryption parameters by path. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersByPathRequest
        @return: GetSecretParametersByPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameters_by_path_with_options(request, runtime)

    async def get_secret_parameters_by_path_async(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        """
        @summary Queries encryption parameters by path. Make sure that you have the permissions to call the GetSecretValue operation before you call this operation.
        
        @param request: GetSecretParametersByPathRequest
        @return: GetSecretParametersByPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameters_by_path_with_options_async(request, runtime)

    def get_service_settings_with_options(
        self,
        request: oos_20190601_models.GetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        """
        @summary Queries the settings of the delivery feature.
        
        @param request: GetServiceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceSettingsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceSettings',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_settings_with_options_async(
        self,
        request: oos_20190601_models.GetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        """
        @summary Queries the settings of the delivery feature.
        
        @param request: GetServiceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceSettingsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceSettings',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_settings(
        self,
        request: oos_20190601_models.GetServiceSettingsRequest,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        """
        @summary Queries the settings of the delivery feature.
        
        @param request: GetServiceSettingsRequest
        @return: GetServiceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_settings_with_options(request, runtime)

    async def get_service_settings_async(
        self,
        request: oos_20190601_models.GetServiceSettingsRequest,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        """
        @summary Queries the settings of the delivery feature.
        
        @param request: GetServiceSettingsRequest
        @return: GetServiceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_settings_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: oos_20190601_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateResponse:
        """
        @summary Queries the information about a template, including the content of the template.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: oos_20190601_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateResponse:
        """
        @summary Queries the information about a template, including the content of the template.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: oos_20190601_models.GetTemplateRequest,
    ) -> oos_20190601_models.GetTemplateResponse:
        """
        @summary Queries the information about a template, including the content of the template.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: oos_20190601_models.GetTemplateRequest,
    ) -> oos_20190601_models.GetTemplateResponse:
        """
        @summary Queries the information about a template, including the content of the template.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_parameter_constraints_with_options(
        self,
        request: oos_20190601_models.GetTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateParameterConstraintsResponse:
        """
        @summary 获取参数可用值
        
        @param request: GetTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateParameterConstraints',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_parameter_constraints_with_options_async(
        self,
        request: oos_20190601_models.GetTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateParameterConstraintsResponse:
        """
        @summary 获取参数可用值
        
        @param request: GetTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateParameterConstraints',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.GetTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_parameter_constraints(
        self,
        request: oos_20190601_models.GetTemplateParameterConstraintsRequest,
    ) -> oos_20190601_models.GetTemplateParameterConstraintsResponse:
        """
        @summary 获取参数可用值
        
        @param request: GetTemplateParameterConstraintsRequest
        @return: GetTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_parameter_constraints_with_options(request, runtime)

    async def get_template_parameter_constraints_async(
        self,
        request: oos_20190601_models.GetTemplateParameterConstraintsRequest,
    ) -> oos_20190601_models.GetTemplateParameterConstraintsResponse:
        """
        @summary 获取参数可用值
        
        @param request: GetTemplateParameterConstraintsRequest
        @return: GetTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_parameter_constraints_with_options_async(request, runtime)

    def list_actions_with_options(
        self,
        request: oos_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListActionsResponse:
        """
        @summary Queries the available actions, including atomic actions and cloud product actions.
        
        @param request: ListActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_actions_with_options_async(
        self,
        request: oos_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListActionsResponse:
        """
        @summary Queries the available actions, including atomic actions and cloud product actions.
        
        @param request: ListActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_actions(
        self,
        request: oos_20190601_models.ListActionsRequest,
    ) -> oos_20190601_models.ListActionsResponse:
        """
        @summary Queries the available actions, including atomic actions and cloud product actions.
        
        @param request: ListActionsRequest
        @return: ListActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_actions_with_options(request, runtime)

    async def list_actions_async(
        self,
        request: oos_20190601_models.ListActionsRequest,
    ) -> oos_20190601_models.ListActionsResponse:
        """
        @summary Queries the available actions, including atomic actions and cloud product actions.
        
        @param request: ListActionsRequest
        @return: ListActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_actions_with_options_async(request, runtime)

    def list_application_groups_with_options(
        self,
        request: oos_20190601_models.ListApplicationGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListApplicationGroupsResponse:
        """
        @summary Queries a list of application groups. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationGroups',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_groups_with_options_async(
        self,
        request: oos_20190601_models.ListApplicationGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListApplicationGroupsResponse:
        """
        @summary Queries a list of application groups. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationGroups',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListApplicationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_groups(
        self,
        request: oos_20190601_models.ListApplicationGroupsRequest,
    ) -> oos_20190601_models.ListApplicationGroupsResponse:
        """
        @summary Queries a list of application groups. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationGroupsRequest
        @return: ListApplicationGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_groups_with_options(request, runtime)

    async def list_application_groups_async(
        self,
        request: oos_20190601_models.ListApplicationGroupsRequest,
    ) -> oos_20190601_models.ListApplicationGroupsResponse:
        """
        @summary Queries a list of application groups. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationGroupsRequest
        @return: ListApplicationGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_groups_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        tmp_req: oos_20190601_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: oos_20190601_models.ListApplicationsRequest,
    ) -> oos_20190601_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: oos_20190601_models.ListApplicationsRequest,
    ) -> oos_20190601_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_execution_logs_with_options(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        """
        @summary Queries the logs of an execution.
        
        @description ***\
        
        @param request: ListExecutionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutionLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_execution_logs_with_options_async(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        """
        @summary Queries the logs of an execution.
        
        @description ***\
        
        @param request: ListExecutionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutionLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_execution_logs(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        """
        @summary Queries the logs of an execution.
        
        @description ***\
        
        @param request: ListExecutionLogsRequest
        @return: ListExecutionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_execution_logs_with_options(request, runtime)

    async def list_execution_logs_async(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        """
        @summary Queries the logs of an execution.
        
        @description ***\
        
        @param request: ListExecutionLogsRequest
        @return: ListExecutionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_logs_with_options_async(request, runtime)

    def list_execution_risky_tasks_with_options(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        """
        @summary Queries high-risk tasks in the execution of a template.
        
        @param request: ListExecutionRiskyTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionRiskyTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutionRiskyTasks',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionRiskyTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_execution_risky_tasks_with_options_async(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        """
        @summary Queries high-risk tasks in the execution of a template.
        
        @param request: ListExecutionRiskyTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionRiskyTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutionRiskyTasks',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionRiskyTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_execution_risky_tasks(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        """
        @summary Queries high-risk tasks in the execution of a template.
        
        @param request: ListExecutionRiskyTasksRequest
        @return: ListExecutionRiskyTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_execution_risky_tasks_with_options(request, runtime)

    async def list_execution_risky_tasks_async(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        """
        @summary Queries high-risk tasks in the execution of a template.
        
        @param request: ListExecutionRiskyTasksRequest
        @return: ListExecutionRiskyTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_risky_tasks_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        tmp_req: oos_20190601_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionsResponse:
        """
        @summary Queries executions. Multiple methods are supported to filter executions.
        
        @param tmp_req: ListExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.categories):
            query['Categories'] = request.categories
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_template_name):
            query['ResourceTemplateName'] = request.resource_template_name
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionsResponse:
        """
        @summary Queries executions. Multiple methods are supported to filter executions.
        
        @param tmp_req: ListExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.categories):
            query['Categories'] = request.categories
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_template_name):
            query['ResourceTemplateName'] = request.resource_template_name
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executions(
        self,
        request: oos_20190601_models.ListExecutionsRequest,
    ) -> oos_20190601_models.ListExecutionsResponse:
        """
        @summary Queries executions. Multiple methods are supported to filter executions.
        
        @param request: ListExecutionsRequest
        @return: ListExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: oos_20190601_models.ListExecutionsRequest,
    ) -> oos_20190601_models.ListExecutionsResponse:
        """
        @summary Queries executions. Multiple methods are supported to filter executions.
        
        @param request: ListExecutionsRequest
        @return: ListExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_instance_package_states_with_options(
        self,
        request: oos_20190601_models.ListInstancePackageStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePackageStatesResponse:
        """
        @summary List Instance Package States
        
        @param request: ListInstancePackageStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePackageStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePackageStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePackageStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_package_states_with_options_async(
        self,
        request: oos_20190601_models.ListInstancePackageStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePackageStatesResponse:
        """
        @summary List Instance Package States
        
        @param request: ListInstancePackageStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePackageStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePackageStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePackageStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_package_states(
        self,
        request: oos_20190601_models.ListInstancePackageStatesRequest,
    ) -> oos_20190601_models.ListInstancePackageStatesResponse:
        """
        @summary List Instance Package States
        
        @param request: ListInstancePackageStatesRequest
        @return: ListInstancePackageStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_package_states_with_options(request, runtime)

    async def list_instance_package_states_async(
        self,
        request: oos_20190601_models.ListInstancePackageStatesRequest,
    ) -> oos_20190601_models.ListInstancePackageStatesResponse:
        """
        @summary List Instance Package States
        
        @param request: ListInstancePackageStatesRequest
        @return: ListInstancePackageStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_package_states_with_options_async(request, runtime)

    def list_instance_patch_states_with_options(
        self,
        request: oos_20190601_models.ListInstancePatchStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePatchStatesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePatchStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePatchStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePatchStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_patch_states_with_options_async(
        self,
        request: oos_20190601_models.ListInstancePatchStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePatchStatesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePatchStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePatchStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePatchStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_patch_states(
        self,
        request: oos_20190601_models.ListInstancePatchStatesRequest,
    ) -> oos_20190601_models.ListInstancePatchStatesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchStatesRequest
        @return: ListInstancePatchStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_patch_states_with_options(request, runtime)

    async def list_instance_patch_states_async(
        self,
        request: oos_20190601_models.ListInstancePatchStatesRequest,
    ) -> oos_20190601_models.ListInstancePatchStatesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchStatesRequest
        @return: ListInstancePatchStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_patch_states_with_options_async(request, runtime)

    def list_instance_patches_with_options(
        self,
        request: oos_20190601_models.ListInstancePatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePatchesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.patch_statuses):
            query['PatchStatuses'] = request.patch_statuses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePatches',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_patches_with_options_async(
        self,
        request: oos_20190601_models.ListInstancePatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInstancePatchesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.patch_statuses):
            query['PatchStatuses'] = request.patch_statuses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePatches',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInstancePatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_patches(
        self,
        request: oos_20190601_models.ListInstancePatchesRequest,
    ) -> oos_20190601_models.ListInstancePatchesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchesRequest
        @return: ListInstancePatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_patches_with_options(request, runtime)

    async def list_instance_patches_async(
        self,
        request: oos_20190601_models.ListInstancePatchesRequest,
    ) -> oos_20190601_models.ListInstancePatchesResponse:
        """
        @summary Queries the information about the patches of an instance.
        
        @param request: ListInstancePatchesRequest
        @return: ListInstancePatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_patches_with_options_async(request, runtime)

    def list_inventory_entries_with_options(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        """
        @summary Queries the configurations of an Elastic Compute Service (ECS) instance.
        
        @param request: ListInventoryEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInventoryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInventoryEntries',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInventoryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inventory_entries_with_options_async(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        """
        @summary Queries the configurations of an Elastic Compute Service (ECS) instance.
        
        @param request: ListInventoryEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInventoryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInventoryEntries',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListInventoryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inventory_entries(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        """
        @summary Queries the configurations of an Elastic Compute Service (ECS) instance.
        
        @param request: ListInventoryEntriesRequest
        @return: ListInventoryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_inventory_entries_with_options(request, runtime)

    async def list_inventory_entries_async(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        """
        @summary Queries the configurations of an Elastic Compute Service (ECS) instance.
        
        @param request: ListInventoryEntriesRequest
        @return: ListInventoryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_inventory_entries_with_options_async(request, runtime)

    def list_ops_items_with_options(
        self,
        tmp_req: oos_20190601_models.ListOpsItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListOpsItemsResponse:
        """
        @summary Queries O\\&M items.
        
        @param tmp_req: ListOpsItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOpsItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListOpsItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_tags):
            request.resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_tags, 'ResourceTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tags_shrink):
            query['ResourceTags'] = request.resource_tags_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpsItems',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListOpsItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ops_items_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListOpsItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListOpsItemsResponse:
        """
        @summary Queries O\\&M items.
        
        @param tmp_req: ListOpsItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOpsItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListOpsItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_tags):
            request.resource_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_tags, 'ResourceTags', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tags_shrink):
            query['ResourceTags'] = request.resource_tags_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpsItems',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListOpsItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ops_items(
        self,
        request: oos_20190601_models.ListOpsItemsRequest,
    ) -> oos_20190601_models.ListOpsItemsResponse:
        """
        @summary Queries O\\&M items.
        
        @param request: ListOpsItemsRequest
        @return: ListOpsItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ops_items_with_options(request, runtime)

    async def list_ops_items_async(
        self,
        request: oos_20190601_models.ListOpsItemsRequest,
    ) -> oos_20190601_models.ListOpsItemsResponse:
        """
        @summary Queries O\\&M items.
        
        @param request: ListOpsItemsRequest
        @return: ListOpsItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ops_items_with_options_async(request, runtime)

    def list_parameter_versions_with_options(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        """
        @summary Queries the versions of a common parameter.
        
        @param request: ListParameterVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListParameterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameter_versions_with_options_async(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        """
        @summary Queries the versions of a common parameter.
        
        @param request: ListParameterVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListParameterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameter_versions(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        """
        @summary Queries the versions of a common parameter.
        
        @param request: ListParameterVersionsRequest
        @return: ListParameterVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_parameter_versions_with_options(request, runtime)

    async def list_parameter_versions_async(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        """
        @summary Queries the versions of a common parameter.
        
        @param request: ListParameterVersionsRequest
        @return: ListParameterVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_parameter_versions_with_options_async(request, runtime)

    def list_parameters_with_options(
        self,
        tmp_req: oos_20190601_models.ListParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParametersResponse:
        """
        @summary Queries common parameters. Multiple methods are supported to filter common parameters.
        
        @param tmp_req: ListParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParametersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListParametersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameters_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParametersResponse:
        """
        @summary Queries common parameters. Multiple methods are supported to filter common parameters.
        
        @param tmp_req: ListParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParametersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListParametersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameters(
        self,
        request: oos_20190601_models.ListParametersRequest,
    ) -> oos_20190601_models.ListParametersResponse:
        """
        @summary Queries common parameters. Multiple methods are supported to filter common parameters.
        
        @param request: ListParametersRequest
        @return: ListParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_parameters_with_options(request, runtime)

    async def list_parameters_async(
        self,
        request: oos_20190601_models.ListParametersRequest,
    ) -> oos_20190601_models.ListParametersResponse:
        """
        @summary Queries common parameters. Multiple methods are supported to filter common parameters.
        
        @param request: ListParametersRequest
        @return: ListParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_parameters_with_options_async(request, runtime)

    def list_patch_baselines_with_options(
        self,
        tmp_req: oos_20190601_models.ListPatchBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListPatchBaselinesResponse:
        """
        @summary Queries a list of patch baselines.
        
        @param tmp_req: ListPatchBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPatchBaselinesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListPatchBaselinesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPatchBaselines',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListPatchBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_patch_baselines_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListPatchBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListPatchBaselinesResponse:
        """
        @summary Queries a list of patch baselines.
        
        @param tmp_req: ListPatchBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPatchBaselinesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListPatchBaselinesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPatchBaselines',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListPatchBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_patch_baselines(
        self,
        request: oos_20190601_models.ListPatchBaselinesRequest,
    ) -> oos_20190601_models.ListPatchBaselinesResponse:
        """
        @summary Queries a list of patch baselines.
        
        @param request: ListPatchBaselinesRequest
        @return: ListPatchBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_patch_baselines_with_options(request, runtime)

    async def list_patch_baselines_async(
        self,
        request: oos_20190601_models.ListPatchBaselinesRequest,
    ) -> oos_20190601_models.ListPatchBaselinesResponse:
        """
        @summary Queries a list of patch baselines.
        
        @param request: ListPatchBaselinesRequest
        @return: ListPatchBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_patch_baselines_with_options_async(request, runtime)

    def list_resource_execution_status_with_options(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        """
        @summary Queries the information about a scheduled execution that involves O&M operations on Elastic Compute Service (ECS) instances.
        
        @param request: ListResourceExecutionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExecutionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExecutionStatus',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListResourceExecutionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_execution_status_with_options_async(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        """
        @summary Queries the information about a scheduled execution that involves O&M operations on Elastic Compute Service (ECS) instances.
        
        @param request: ListResourceExecutionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExecutionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExecutionStatus',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListResourceExecutionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_execution_status(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        """
        @summary Queries the information about a scheduled execution that involves O&M operations on Elastic Compute Service (ECS) instances.
        
        @param request: ListResourceExecutionStatusRequest
        @return: ListResourceExecutionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_execution_status_with_options(request, runtime)

    async def list_resource_execution_status_async(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        """
        @summary Queries the information about a scheduled execution that involves O&M operations on Elastic Compute Service (ECS) instances.
        
        @param request: ListResourceExecutionStatusRequest
        @return: ListResourceExecutionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_execution_status_with_options_async(request, runtime)

    def list_secret_parameter_versions_with_options(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        """
        @summary Queries versions of an encryption parameter.
        
        @param request: ListSecretParameterVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretParameterVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretParameterVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListSecretParameterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_parameter_versions_with_options_async(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        """
        @summary Queries versions of an encryption parameter.
        
        @param request: ListSecretParameterVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretParameterVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretParameterVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListSecretParameterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_parameter_versions(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        """
        @summary Queries versions of an encryption parameter.
        
        @param request: ListSecretParameterVersionsRequest
        @return: ListSecretParameterVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secret_parameter_versions_with_options(request, runtime)

    async def list_secret_parameter_versions_async(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        """
        @summary Queries versions of an encryption parameter.
        
        @param request: ListSecretParameterVersionsRequest
        @return: ListSecretParameterVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_parameter_versions_with_options_async(request, runtime)

    def list_secret_parameters_with_options(
        self,
        tmp_req: oos_20190601_models.ListSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        """
        @summary Queries common parameters. Multiple types of queries are supported.
        
        @description Before you call this operation, make sure that you have the permission to manage Key Management Service (KMS) secrets.
        
        @param tmp_req: ListSecretParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretParametersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListSecretParametersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListSecretParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_parameters_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        """
        @summary Queries common parameters. Multiple types of queries are supported.
        
        @description Before you call this operation, make sure that you have the permission to manage Key Management Service (KMS) secrets.
        
        @param tmp_req: ListSecretParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretParametersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListSecretParametersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListSecretParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_parameters(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        """
        @summary Queries common parameters. Multiple types of queries are supported.
        
        @description Before you call this operation, make sure that you have the permission to manage Key Management Service (KMS) secrets.
        
        @param request: ListSecretParametersRequest
        @return: ListSecretParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secret_parameters_with_options(request, runtime)

    async def list_secret_parameters_async(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        """
        @summary Queries common parameters. Multiple types of queries are supported.
        
        @description Before you call this operation, make sure that you have the permission to manage Key Management Service (KMS) secrets.
        
        @param request: ListSecretParametersRequest
        @return: ListSecretParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_parameters_with_options_async(request, runtime)

    def list_state_configurations_with_options(
        self,
        tmp_req: oos_20190601_models.ListStateConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListStateConfigurationsResponse:
        """
        @summary Queries desired-state configurations.
        
        @param tmp_req: ListStateConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStateConfigurationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListStateConfigurationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStateConfigurations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListStateConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_state_configurations_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListStateConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListStateConfigurationsResponse:
        """
        @summary Queries desired-state configurations.
        
        @param tmp_req: ListStateConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStateConfigurationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListStateConfigurationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStateConfigurations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListStateConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_state_configurations(
        self,
        request: oos_20190601_models.ListStateConfigurationsRequest,
    ) -> oos_20190601_models.ListStateConfigurationsResponse:
        """
        @summary Queries desired-state configurations.
        
        @param request: ListStateConfigurationsRequest
        @return: ListStateConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_state_configurations_with_options(request, runtime)

    async def list_state_configurations_async(
        self,
        request: oos_20190601_models.ListStateConfigurationsRequest,
    ) -> oos_20190601_models.ListStateConfigurationsResponse:
        """
        @summary Queries desired-state configurations.
        
        @param request: ListStateConfigurationsRequest
        @return: ListStateConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_state_configurations_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagKeysResponse:
        """
        @summary Queries the tags.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagKeysResponse:
        """
        @summary Queries the tags.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
    ) -> oos_20190601_models.ListTagKeysResponse:
        """
        @summary Queries the tags.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
    ) -> oos_20190601_models.ListTagKeysResponse:
        """
        @summary Queries the tags.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to one or more resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to one or more resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: oos_20190601_models.ListTagResourcesRequest,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: oos_20190601_models.ListTagResourcesRequest,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to one or more resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagValuesResponse:
        """
        @summary Queries the values of created tags.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagValuesResponse:
        """
        @summary Queries the values of created tags.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
    ) -> oos_20190601_models.ListTagValuesResponse:
        """
        @summary Queries the values of created tags.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
    ) -> oos_20190601_models.ListTagValuesResponse:
        """
        @summary Queries the values of created tags.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_task_executions_with_options(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        """
        @summary Queries task executions. Multiple methods are supported to filter task executions.
        
        @param request: ListTaskExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTaskExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_executions_with_options_async(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        """
        @summary Queries task executions. Multiple methods are supported to filter task executions.
        
        @param request: ListTaskExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTaskExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_executions(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        """
        @summary Queries task executions. Multiple methods are supported to filter task executions.
        
        @param request: ListTaskExecutionsRequest
        @return: ListTaskExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_executions_with_options(request, runtime)

    async def list_task_executions_async(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        """
        @summary Queries task executions. Multiple methods are supported to filter task executions.
        
        @param request: ListTaskExecutionsRequest
        @return: ListTaskExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_executions_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        """
        @summary Queries a list of versions of a template.
        
        @param request: ListTemplateVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        """
        @summary Queries a list of versions of a template.
        
        @param request: ListTemplateVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateVersions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTemplateVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_versions(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        """
        @summary Queries a list of versions of a template.
        
        @param request: ListTemplateVersionsRequest
        @return: ListTemplateVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        """
        @summary Queries a list of versions of a template.
        
        @param request: ListTemplateVersionsRequest
        @return: ListTemplateVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        tmp_req: oos_20190601_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplatesResponse:
        """
        @summary Queries templates. Multiple methods are supported to filter templates.
        
        @param tmp_req: ListTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.has_trigger):
            query['HasTrigger'] = request.has_trigger
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.is_favorite):
            query['IsFavorite'] = request.is_favorite
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplatesResponse:
        """
        @summary Queries templates. Multiple methods are supported to filter templates.
        
        @param tmp_req: ListTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.has_trigger):
            query['HasTrigger'] = request.has_trigger
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.is_favorite):
            query['IsFavorite'] = request.is_favorite
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: oos_20190601_models.ListTemplatesRequest,
    ) -> oos_20190601_models.ListTemplatesResponse:
        """
        @summary Queries templates. Multiple methods are supported to filter templates.
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: oos_20190601_models.ListTemplatesRequest,
    ) -> oos_20190601_models.ListTemplatesResponse:
        """
        @summary Queries templates. Multiple methods are supported to filter templates.
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def notify_execution_with_options(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        """
        @summary Notifies an execution in the Waiting state of the subsequent operations.
        
        @description You can call this operation to notify an execution in the following scenarios:
        If a template contains a special task, such as an approval task, the Operation Orchestration Service (OOS) execution engine sets the execution state to Waiting when the approval task is being run. You can call this operation to specify whether to continue the execution.
        If you perform debugging in the debug mode, you can call this operation to notify the execution of the subsequent operations after the execution is created or a task is complete.
        If a high-risk operation task waits for approval, you can call this operation to specify whether to continue the execution.
        
        @param request: NotifyExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NotifyExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.loop_item):
            query['LoopItem'] = request.loop_item
        if not UtilClient.is_unset(request.notify_note):
            query['NotifyNote'] = request.notify_note
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_execution_ids):
            query['TaskExecutionIds'] = request.task_execution_ids
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.NotifyExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_execution_with_options_async(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        """
        @summary Notifies an execution in the Waiting state of the subsequent operations.
        
        @description You can call this operation to notify an execution in the following scenarios:
        If a template contains a special task, such as an approval task, the Operation Orchestration Service (OOS) execution engine sets the execution state to Waiting when the approval task is being run. You can call this operation to specify whether to continue the execution.
        If you perform debugging in the debug mode, you can call this operation to notify the execution of the subsequent operations after the execution is created or a task is complete.
        If a high-risk operation task waits for approval, you can call this operation to specify whether to continue the execution.
        
        @param request: NotifyExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NotifyExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.loop_item):
            query['LoopItem'] = request.loop_item
        if not UtilClient.is_unset(request.notify_note):
            query['NotifyNote'] = request.notify_note
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_execution_ids):
            query['TaskExecutionIds'] = request.task_execution_ids
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.NotifyExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_execution(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        """
        @summary Notifies an execution in the Waiting state of the subsequent operations.
        
        @description You can call this operation to notify an execution in the following scenarios:
        If a template contains a special task, such as an approval task, the Operation Orchestration Service (OOS) execution engine sets the execution state to Waiting when the approval task is being run. You can call this operation to specify whether to continue the execution.
        If you perform debugging in the debug mode, you can call this operation to notify the execution of the subsequent operations after the execution is created or a task is complete.
        If a high-risk operation task waits for approval, you can call this operation to specify whether to continue the execution.
        
        @param request: NotifyExecutionRequest
        @return: NotifyExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.notify_execution_with_options(request, runtime)

    async def notify_execution_async(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        """
        @summary Notifies an execution in the Waiting state of the subsequent operations.
        
        @description You can call this operation to notify an execution in the following scenarios:
        If a template contains a special task, such as an approval task, the Operation Orchestration Service (OOS) execution engine sets the execution state to Waiting when the approval task is being run. You can call this operation to specify whether to continue the execution.
        If you perform debugging in the debug mode, you can call this operation to notify the execution of the subsequent operations after the execution is created or a task is complete.
        If a high-risk operation task waits for approval, you can call this operation to specify whether to continue the execution.
        
        @param request: NotifyExecutionRequest
        @return: NotifyExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.notify_execution_with_options_async(request, runtime)

    def register_default_patch_baseline_with_options(
        self,
        request: oos_20190601_models.RegisterDefaultPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.RegisterDefaultPatchBaselineResponse:
        """
        @summary Registers the default patch baseline.
        
        @param request: RegisterDefaultPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDefaultPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDefaultPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.RegisterDefaultPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_default_patch_baseline_with_options_async(
        self,
        request: oos_20190601_models.RegisterDefaultPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.RegisterDefaultPatchBaselineResponse:
        """
        @summary Registers the default patch baseline.
        
        @param request: RegisterDefaultPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDefaultPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDefaultPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.RegisterDefaultPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_default_patch_baseline(
        self,
        request: oos_20190601_models.RegisterDefaultPatchBaselineRequest,
    ) -> oos_20190601_models.RegisterDefaultPatchBaselineResponse:
        """
        @summary Registers the default patch baseline.
        
        @param request: RegisterDefaultPatchBaselineRequest
        @return: RegisterDefaultPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_default_patch_baseline_with_options(request, runtime)

    async def register_default_patch_baseline_async(
        self,
        request: oos_20190601_models.RegisterDefaultPatchBaselineRequest,
    ) -> oos_20190601_models.RegisterDefaultPatchBaselineResponse:
        """
        @summary Registers the default patch baseline.
        
        @param request: RegisterDefaultPatchBaselineRequest
        @return: RegisterDefaultPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_default_patch_baseline_with_options_async(request, runtime)

    def search_inventory_with_options(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SearchInventoryResponse:
        """
        @summary Queries the details or aggregate information of a configuration inventory.
        
        @param request: SearchInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchInventory',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.SearchInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_inventory_with_options_async(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SearchInventoryResponse:
        """
        @summary Queries the details or aggregate information of a configuration inventory.
        
        @param request: SearchInventoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchInventoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchInventory',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.SearchInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_inventory(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
    ) -> oos_20190601_models.SearchInventoryResponse:
        """
        @summary Queries the details or aggregate information of a configuration inventory.
        
        @param request: SearchInventoryRequest
        @return: SearchInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_inventory_with_options(request, runtime)

    async def search_inventory_async(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
    ) -> oos_20190601_models.SearchInventoryResponse:
        """
        @summary Queries the details or aggregate information of a configuration inventory.
        
        @param request: SearchInventoryRequest
        @return: SearchInventoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_inventory_with_options_async(request, runtime)

    def set_service_settings_with_options(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        """
        @summary Enables or disables the feature of delivering template execution records and sets the storage location.
        
        @param request: SetServiceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetServiceSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_oss_bucket_name):
            query['DeliveryOssBucketName'] = request.delivery_oss_bucket_name
        if not UtilClient.is_unset(request.delivery_oss_enabled):
            query['DeliveryOssEnabled'] = request.delivery_oss_enabled
        if not UtilClient.is_unset(request.delivery_oss_key_prefix):
            query['DeliveryOssKeyPrefix'] = request.delivery_oss_key_prefix
        if not UtilClient.is_unset(request.delivery_sls_enabled):
            query['DeliverySlsEnabled'] = request.delivery_sls_enabled
        if not UtilClient.is_unset(request.delivery_sls_project_name):
            query['DeliverySlsProjectName'] = request.delivery_sls_project_name
        if not UtilClient.is_unset(request.rdc_enterprise_id):
            query['RdcEnterpriseId'] = request.rdc_enterprise_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetServiceSettings',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.SetServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_service_settings_with_options_async(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        """
        @summary Enables or disables the feature of delivering template execution records and sets the storage location.
        
        @param request: SetServiceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetServiceSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_oss_bucket_name):
            query['DeliveryOssBucketName'] = request.delivery_oss_bucket_name
        if not UtilClient.is_unset(request.delivery_oss_enabled):
            query['DeliveryOssEnabled'] = request.delivery_oss_enabled
        if not UtilClient.is_unset(request.delivery_oss_key_prefix):
            query['DeliveryOssKeyPrefix'] = request.delivery_oss_key_prefix
        if not UtilClient.is_unset(request.delivery_sls_enabled):
            query['DeliverySlsEnabled'] = request.delivery_sls_enabled
        if not UtilClient.is_unset(request.delivery_sls_project_name):
            query['DeliverySlsProjectName'] = request.delivery_sls_project_name
        if not UtilClient.is_unset(request.rdc_enterprise_id):
            query['RdcEnterpriseId'] = request.rdc_enterprise_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetServiceSettings',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.SetServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_service_settings(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        """
        @summary Enables or disables the feature of delivering template execution records and sets the storage location.
        
        @param request: SetServiceSettingsRequest
        @return: SetServiceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_service_settings_with_options(request, runtime)

    async def set_service_settings_async(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        """
        @summary Enables or disables the feature of delivering template execution records and sets the storage location.
        
        @param request: SetServiceSettingsRequest
        @return: SetServiceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_service_settings_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        tmp_req: oos_20190601_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.StartExecutionResponse:
        """
        @summary Starts an execution.
        
        @param tmp_req: StartExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.StartExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.loop_mode):
            query['LoopMode'] = request.loop_mode
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.safety_check):
            query['SafetyCheck'] = request.safety_check
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.StartExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        tmp_req: oos_20190601_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.StartExecutionResponse:
        """
        @summary Starts an execution.
        
        @param tmp_req: StartExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.StartExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.loop_mode):
            query['LoopMode'] = request.loop_mode
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.safety_check):
            query['SafetyCheck'] = request.safety_check
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.StartExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_execution(
        self,
        request: oos_20190601_models.StartExecutionRequest,
    ) -> oos_20190601_models.StartExecutionResponse:
        """
        @summary Starts an execution.
        
        @param request: StartExecutionRequest
        @return: StartExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: oos_20190601_models.StartExecutionRequest,
    ) -> oos_20190601_models.StartExecutionResponse:
        """
        @summary Starts an execution.
        
        @param request: StartExecutionRequest
        @return: StartExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TagResourcesResponse:
        """
        @summary Adds tags to one or more resources.
        
        @param tmp_req: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TagResourcesResponse:
        """
        @summary Adds tags to one or more resources.
        
        @param tmp_req: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: oos_20190601_models.TagResourcesRequest,
    ) -> oos_20190601_models.TagResourcesResponse:
        """
        @summary Adds tags to one or more resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: oos_20190601_models.TagResourcesRequest,
    ) -> oos_20190601_models.TagResourcesResponse:
        """
        @summary Adds tags to one or more resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def trigger_execution_with_options(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        """
        @summary Debugs a started execution that contains an event trigger task or alert trigger task. If the operation is called, a message body is sent to the event trigger task or alert trigger task. After the trigger task receives the message body, the trigger task generates a new child execution.
        
        @param request: TriggerExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.TriggerExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_execution_with_options_async(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        """
        @summary Debugs a started execution that contains an event trigger task or alert trigger task. If the operation is called, a message body is sent to the event trigger task or alert trigger task. After the trigger task receives the message body, the trigger task generates a new child execution.
        
        @param request: TriggerExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.TriggerExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_execution(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        """
        @summary Debugs a started execution that contains an event trigger task or alert trigger task. If the operation is called, a message body is sent to the event trigger task or alert trigger task. After the trigger task receives the message body, the trigger task generates a new child execution.
        
        @param request: TriggerExecutionRequest
        @return: TriggerExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_execution_with_options(request, runtime)

    async def trigger_execution_async(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        """
        @summary Debugs a started execution that contains an event trigger task or alert trigger task. If the operation is called, a message body is sent to the event trigger task or alert trigger task. After the trigger task receives the message body, the trigger task generates a new child execution.
        
        @param request: TriggerExecutionRequest
        @return: TriggerExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_execution_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more resources.
        
        @param tmp_req: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more resources.
        
        @param tmp_req: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: oos_20190601_models.UntagResourcesRequest,
    ) -> oos_20190601_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: oos_20190601_models.UntagResourcesRequest,
    ) -> oos_20190601_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_application_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateApplicationResponse:
        """
        @summary Updates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: UpdateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_config):
            request.alarm_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not UtilClient.is_unset(request.delete_alarm_rules_before_update):
            query['DeleteAlarmRulesBeforeUpdate'] = request.delete_alarm_rules_before_update
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateApplicationResponse:
        """
        @summary Updates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: UpdateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_config):
            request.alarm_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not UtilClient.is_unset(request.delete_alarm_rules_before_update):
            query['DeleteAlarmRulesBeforeUpdate'] = request.delete_alarm_rules_before_update
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        request: oos_20190601_models.UpdateApplicationRequest,
    ) -> oos_20190601_models.UpdateApplicationResponse:
        """
        @summary Updates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: UpdateApplicationRequest
        @return: UpdateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: oos_20190601_models.UpdateApplicationRequest,
    ) -> oos_20190601_models.UpdateApplicationResponse:
        """
        @summary Updates an application. You can call this operation only for the applications that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: UpdateApplicationRequest
        @return: UpdateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def update_application_group_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateApplicationGroupResponse:
        """
        @summary Updates the information of an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: UpdateApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateApplicationGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deployed_revision_id):
            query['DeployedRevisionId'] = request.deployed_revision_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_name):
            query['NewName'] = request.new_name
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_group_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateApplicationGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateApplicationGroupResponse:
        """
        @summary Updates the information of an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param tmp_req: UpdateApplicationGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateApplicationGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.deployed_revision_id):
            query['DeployedRevisionId'] = request.deployed_revision_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_name):
            query['NewName'] = request.new_name
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationGroup',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_group(
        self,
        request: oos_20190601_models.UpdateApplicationGroupRequest,
    ) -> oos_20190601_models.UpdateApplicationGroupResponse:
        """
        @summary Updates the information of an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: UpdateApplicationGroupRequest
        @return: UpdateApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_group_with_options(request, runtime)

    async def update_application_group_async(
        self,
        request: oos_20190601_models.UpdateApplicationGroupRequest,
    ) -> oos_20190601_models.UpdateApplicationGroupResponse:
        """
        @summary Updates the information of an application group. You can call this operation only for the application groups that reside in the China (Hangzhou) region. Use an endpoint of the China (Hangzhou) region.
        
        @param request: UpdateApplicationGroupRequest
        @return: UpdateApplicationGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_group_with_options_async(request, runtime)

    def update_execution_with_options(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        """
        @summary Update executions that are in Running or Waiting status.
        
        @param request: UpdateExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_execution_with_options_async(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        """
        @summary Update executions that are in Running or Waiting status.
        
        @param request: UpdateExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_execution(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        """
        @summary Update executions that are in Running or Waiting status.
        
        @param request: UpdateExecutionRequest
        @return: UpdateExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_execution_with_options(request, runtime)

    async def update_execution_async(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        """
        @summary Update executions that are in Running or Waiting status.
        
        @param request: UpdateExecutionRequest
        @return: UpdateExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_execution_with_options_async(request, runtime)

    def update_instance_package_state_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateInstancePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateInstancePackageStateResponse:
        """
        @summary Updates the installed extensions of an instance.
        
        @param tmp_req: UpdateInstancePackageStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstancePackageStateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateInstancePackageStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.configure_action):
            query['ConfigureAction'] = request.configure_action
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstancePackageState',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateInstancePackageStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_package_state_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateInstancePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateInstancePackageStateResponse:
        """
        @summary Updates the installed extensions of an instance.
        
        @param tmp_req: UpdateInstancePackageStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstancePackageStateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateInstancePackageStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.configure_action):
            query['ConfigureAction'] = request.configure_action
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstancePackageState',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateInstancePackageStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_package_state(
        self,
        request: oos_20190601_models.UpdateInstancePackageStateRequest,
    ) -> oos_20190601_models.UpdateInstancePackageStateResponse:
        """
        @summary Updates the installed extensions of an instance.
        
        @param request: UpdateInstancePackageStateRequest
        @return: UpdateInstancePackageStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_package_state_with_options(request, runtime)

    async def update_instance_package_state_async(
        self,
        request: oos_20190601_models.UpdateInstancePackageStateRequest,
    ) -> oos_20190601_models.UpdateInstancePackageStateResponse:
        """
        @summary Updates the installed extensions of an instance.
        
        @param request: UpdateInstancePackageStateRequest
        @return: UpdateInstancePackageStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_package_state_with_options_async(request, runtime)

    def update_ops_item_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateOpsItemResponse:
        """
        @summary Modifies an O\\\\\\\\\\\\&M item.
        
        @param tmp_req: UpdateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOpsItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateOpsItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.solutions):
            query['Solutions'] = request.solutions
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ops_item_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateOpsItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateOpsItemResponse:
        """
        @summary Modifies an O\\\\\\\\\\\\&M item.
        
        @param tmp_req: UpdateOpsItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOpsItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateOpsItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.solutions):
            query['Solutions'] = request.solutions
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOpsItem',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ops_item(
        self,
        request: oos_20190601_models.UpdateOpsItemRequest,
    ) -> oos_20190601_models.UpdateOpsItemResponse:
        """
        @summary Modifies an O\\\\\\\\\\\\&M item.
        
        @param request: UpdateOpsItemRequest
        @return: UpdateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ops_item_with_options(request, runtime)

    async def update_ops_item_async(
        self,
        request: oos_20190601_models.UpdateOpsItemRequest,
    ) -> oos_20190601_models.UpdateOpsItemResponse:
        """
        @summary Modifies an O\\\\\\\\\\\\&M item.
        
        @param request: UpdateOpsItemRequest
        @return: UpdateOpsItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ops_item_with_options_async(request, runtime)

    def update_parameter_with_options(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateParameterResponse:
        """
        @summary Updates a common parameter.
        
        @param request: UpdateParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_parameter_with_options_async(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateParameterResponse:
        """
        @summary Updates a common parameter.
        
        @param request: UpdateParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_parameter(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
    ) -> oos_20190601_models.UpdateParameterResponse:
        """
        @summary Updates a common parameter.
        
        @param request: UpdateParameterRequest
        @return: UpdateParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_parameter_with_options(request, runtime)

    async def update_parameter_async(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
    ) -> oos_20190601_models.UpdateParameterResponse:
        """
        @summary Updates a common parameter.
        
        @param request: UpdateParameterRequest
        @return: UpdateParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_parameter_with_options_async(request, runtime)

    def update_patch_baseline_with_options(
        self,
        tmp_req: oos_20190601_models.UpdatePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdatePatchBaselineResponse:
        """
        @summary Updates a patch baseline.
        
        @param tmp_req: UpdatePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePatchBaselineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdatePatchBaselineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.rejected_patches):
            request.rejected_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not UtilClient.is_unset(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdatePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_patch_baseline_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdatePatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdatePatchBaselineResponse:
        """
        @summary Updates a patch baseline.
        
        @param tmp_req: UpdatePatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePatchBaselineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdatePatchBaselineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approved_patches):
            request.approved_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.rejected_patches):
            request.rejected_patches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not UtilClient.is_unset(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not UtilClient.is_unset(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdatePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_patch_baseline(
        self,
        request: oos_20190601_models.UpdatePatchBaselineRequest,
    ) -> oos_20190601_models.UpdatePatchBaselineResponse:
        """
        @summary Updates a patch baseline.
        
        @param request: UpdatePatchBaselineRequest
        @return: UpdatePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_patch_baseline_with_options(request, runtime)

    async def update_patch_baseline_async(
        self,
        request: oos_20190601_models.UpdatePatchBaselineRequest,
    ) -> oos_20190601_models.UpdatePatchBaselineResponse:
        """
        @summary Updates a patch baseline.
        
        @param request: UpdatePatchBaselineRequest
        @return: UpdatePatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_patch_baseline_with_options_async(request, runtime)

    def update_secret_parameter_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        """
        @summary Updates an encryption parameter.
        
        @param tmp_req: UpdateSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateSecretParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_parameter_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        """
        @summary Updates an encryption parameter.
        
        @param tmp_req: UpdateSecretParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretParameterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateSecretParameterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_parameter(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        """
        @summary Updates an encryption parameter.
        
        @param request: UpdateSecretParameterRequest
        @return: UpdateSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_parameter_with_options(request, runtime)

    async def update_secret_parameter_async(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        """
        @summary Updates an encryption parameter.
        
        @param request: UpdateSecretParameterRequest
        @return: UpdateSecretParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_parameter_with_options_async(request, runtime)

    def update_state_configuration_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateStateConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateStateConfigurationResponse:
        """
        @summary Updates a desired-state configuration.
        
        @param tmp_req: UpdateStateConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStateConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateStateConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.state_configuration_id):
            query['StateConfigurationId'] = request.state_configuration_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStateConfiguration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateStateConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_state_configuration_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateStateConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateStateConfigurationResponse:
        """
        @summary Updates a desired-state configuration.
        
        @param tmp_req: UpdateStateConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStateConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateStateConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.state_configuration_id):
            query['StateConfigurationId'] = request.state_configuration_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStateConfiguration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateStateConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_state_configuration(
        self,
        request: oos_20190601_models.UpdateStateConfigurationRequest,
    ) -> oos_20190601_models.UpdateStateConfigurationResponse:
        """
        @summary Updates a desired-state configuration.
        
        @param request: UpdateStateConfigurationRequest
        @return: UpdateStateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_state_configuration_with_options(request, runtime)

    async def update_state_configuration_async(
        self,
        request: oos_20190601_models.UpdateStateConfigurationRequest,
    ) -> oos_20190601_models.UpdateStateConfigurationResponse:
        """
        @summary Updates a desired-state configuration.
        
        @param request: UpdateStateConfigurationRequest
        @return: UpdateStateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_state_configuration_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        """
        @summary Updates the information about an existing template.
        
        @param tmp_req: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        """
        @summary Updates the information about an existing template.
        
        @param tmp_req: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: oos_20190601_models.UpdateTemplateRequest,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        """
        @summary Updates the information about an existing template.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: oos_20190601_models.UpdateTemplateRequest,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        """
        @summary Updates the information about an existing template.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def validate_template_content_with_options(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        """
        @summary Check whether a template is valid.
        
        @param request: ValidateTemplateContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateTemplateContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateTemplateContent',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ValidateTemplateContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_template_content_with_options_async(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        """
        @summary Check whether a template is valid.
        
        @param request: ValidateTemplateContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateTemplateContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateTemplateContent',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oos_20190601_models.ValidateTemplateContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_template_content(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        """
        @summary Check whether a template is valid.
        
        @param request: ValidateTemplateContentRequest
        @return: ValidateTemplateContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_template_content_with_options(request, runtime)

    async def validate_template_content_async(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        """
        @summary Check whether a template is valid.
        
        @param request: ValidateTemplateContentRequest
        @return: ValidateTemplateContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_template_content_with_options_async(request, runtime)
