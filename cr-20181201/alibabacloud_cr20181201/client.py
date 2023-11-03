# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cr20181201 import models as cr_20181201_models
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
        self._endpoint = self.get_endpoint('cr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_artifact_build_task_with_options(
        self,
        request: cr_20181201_models.CancelArtifactBuildTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelArtifactBuildTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_artifact_build_task_with_options_async(
        self,
        request: cr_20181201_models.CancelArtifactBuildTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelArtifactBuildTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelArtifactBuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_artifact_build_task(
        self,
        request: cr_20181201_models.CancelArtifactBuildTaskRequest,
    ) -> cr_20181201_models.CancelArtifactBuildTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_artifact_build_task_with_options(request, runtime)

    async def cancel_artifact_build_task_async(
        self,
        request: cr_20181201_models.CancelArtifactBuildTaskRequest,
    ) -> cr_20181201_models.CancelArtifactBuildTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_artifact_build_task_with_options_async(request, runtime)

    def cancel_repo_build_record_with_options(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_repo_build_record(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_repo_build_record_with_options(request, runtime)

    async def cancel_repo_build_record_async(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_repo_build_record_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: cr_20181201_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: cr_20181201_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: cr_20181201_models.ChangeResourceGroupRequest,
    ) -> cr_20181201_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: cr_20181201_models.ChangeResourceGroupRequest,
    ) -> cr_20181201_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_artifact_build_rule_with_options(
        self,
        tmp_req: cr_20181201_models.CreateArtifactBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateArtifactBuildRuleResponse:
        """
        The ID of the rule.
        
        @param tmp_req: CreateArtifactBuildRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactBuildRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.CreateArtifactBuildRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.scope_id):
            query['ScopeId'] = request.scope_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_build_rule_with_options_async(
        self,
        tmp_req: cr_20181201_models.CreateArtifactBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateArtifactBuildRuleResponse:
        """
        The ID of the rule.
        
        @param tmp_req: CreateArtifactBuildRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactBuildRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.CreateArtifactBuildRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.scope_id):
            query['ScopeId'] = request.scope_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateArtifactBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact_build_rule(
        self,
        request: cr_20181201_models.CreateArtifactBuildRuleRequest,
    ) -> cr_20181201_models.CreateArtifactBuildRuleResponse:
        """
        The ID of the rule.
        
        @param request: CreateArtifactBuildRuleRequest
        @return: CreateArtifactBuildRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_artifact_build_rule_with_options(request, runtime)

    async def create_artifact_build_rule_async(
        self,
        request: cr_20181201_models.CreateArtifactBuildRuleRequest,
    ) -> cr_20181201_models.CreateArtifactBuildRuleResponse:
        """
        The ID of the rule.
        
        @param request: CreateArtifactBuildRuleRequest
        @return: CreateArtifactBuildRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_artifact_build_rule_with_options_async(request, runtime)

    def create_build_record_by_record_with_options(
        self,
        request: cr_20181201_models.CreateBuildRecordByRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_build_record_by_record_with_options_async(
        self,
        request: cr_20181201_models.CreateBuildRecordByRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_build_record_by_record(
        self,
        request: cr_20181201_models.CreateBuildRecordByRecordRequest,
    ) -> cr_20181201_models.CreateBuildRecordByRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_build_record_by_record_with_options(request, runtime)

    async def create_build_record_by_record_async(
        self,
        request: cr_20181201_models.CreateBuildRecordByRecordRequest,
    ) -> cr_20181201_models.CreateBuildRecordByRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_build_record_by_record_with_options_async(request, runtime)

    def create_build_record_by_rule_with_options(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_build_record_by_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_build_record_by_rule(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_build_record_by_rule_with_options(request, runtime)

    async def create_build_record_by_rule_async(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_build_record_by_rule_with_options_async(request, runtime)

    def create_chain_with_options(
        self,
        request: cr_20181201_models.CreateChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chain_with_options_async(
        self,
        request: cr_20181201_models.CreateChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chain(
        self,
        request: cr_20181201_models.CreateChainRequest,
    ) -> cr_20181201_models.CreateChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_chain_with_options(request, runtime)

    async def create_chain_async(
        self,
        request: cr_20181201_models.CreateChainRequest,
    ) -> cr_20181201_models.CreateChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_chain_with_options_async(request, runtime)

    def create_chart_namespace_with_options(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chart_namespace(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_chart_namespace_with_options(request, runtime)

    async def create_chart_namespace_async(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_chart_namespace_with_options_async(request, runtime)

    def create_chart_repository_with_options(
        self,
        request: cr_20181201_models.CreateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.CreateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chart_repository(
        self,
        request: cr_20181201_models.CreateChartRepositoryRequest,
    ) -> cr_20181201_models.CreateChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_chart_repository_with_options(request, runtime)

    async def create_chart_repository_async(
        self,
        request: cr_20181201_models.CreateChartRepositoryRequest,
    ) -> cr_20181201_models.CreateChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_chart_repository_with_options_async(request, runtime)

    def create_instance_endpoint_acl_policy_with_options(
        self,
        request: cr_20181201_models.CreateInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_endpoint_acl_policy_with_options_async(
        self,
        request: cr_20181201_models.CreateInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceEndpointAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_endpoint_acl_policy(
        self,
        request: cr_20181201_models.CreateInstanceEndpointAclPolicyRequest,
    ) -> cr_20181201_models.CreateInstanceEndpointAclPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_endpoint_acl_policy_with_options(request, runtime)

    async def create_instance_endpoint_acl_policy_async(
        self,
        request: cr_20181201_models.CreateInstanceEndpointAclPolicyRequest,
    ) -> cr_20181201_models.CreateInstanceEndpointAclPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_endpoint_acl_policy_with_options_async(request, runtime)

    def create_instance_vpc_endpoint_linked_vpc_with_options(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        """
        The ID of the request.
        
        @param request: CreateInstanceVpcEndpointLinkedVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_create_dnsrecord_in_pvzt):
            query['EnableCreateDNSRecordInPvzt'] = request.enable_create_dnsrecord_in_pvzt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        """
        The ID of the request.
        
        @param request: CreateInstanceVpcEndpointLinkedVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_create_dnsrecord_in_pvzt):
            query['EnableCreateDNSRecordInPvzt'] = request.enable_create_dnsrecord_in_pvzt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_vpc_endpoint_linked_vpc(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        """
        The ID of the request.
        
        @param request: CreateInstanceVpcEndpointLinkedVpcRequest
        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    async def create_instance_vpc_endpoint_linked_vpc_async(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        """
        The ID of the request.
        
        @param request: CreateInstanceVpcEndpointLinkedVpcRequest
        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_vpc_endpoint_linked_vpc_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_repo_build_rule_with_options(
        self,
        request: cr_20181201_models.CreateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_build_rule(
        self,
        request: cr_20181201_models.CreateRepoBuildRuleRequest,
    ) -> cr_20181201_models.CreateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_build_rule_with_options(request, runtime)

    async def create_repo_build_rule_async(
        self,
        request: cr_20181201_models.CreateRepoBuildRuleRequest,
    ) -> cr_20181201_models.CreateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_build_rule_with_options_async(request, runtime)

    def create_repo_source_code_repo_with_options(
        self,
        request: cr_20181201_models.CreateRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_source_code_repo_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_source_code_repo(
        self,
        request: cr_20181201_models.CreateRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.CreateRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_source_code_repo_with_options(request, runtime)

    async def create_repo_source_code_repo_async(
        self,
        request: cr_20181201_models.CreateRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.CreateRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_source_code_repo_with_options_async(request, runtime)

    def create_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.sync_rule_name):
            query['SyncRuleName'] = request.sync_rule_name
        if not UtilClient.is_unset(request.sync_scope):
            query['SyncScope'] = request.sync_scope
        if not UtilClient.is_unset(request.sync_trigger):
            query['SyncTrigger'] = request.sync_trigger
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace_name):
            query['TargetNamespaceName'] = request.target_namespace_name
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.sync_rule_name):
            query['SyncRuleName'] = request.sync_rule_name
        if not UtilClient.is_unset(request.sync_scope):
            query['SyncScope'] = request.sync_scope
        if not UtilClient.is_unset(request.sync_trigger):
            query['SyncTrigger'] = request.sync_trigger
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace_name):
            query['TargetNamespaceName'] = request.target_namespace_name
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_rule(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_rule_with_options(request, runtime)

    async def create_repo_sync_rule_async(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_sync_rule_with_options_async(request, runtime)

    def create_repo_sync_task_with_options(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_tag):
            query['TargetTag'] = request.target_tag
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_task_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_tag):
            query['TargetTag'] = request.target_tag
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_task(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskRequest,
    ) -> cr_20181201_models.CreateRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_task_with_options(request, runtime)

    async def create_repo_sync_task_async(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskRequest,
    ) -> cr_20181201_models.CreateRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_sync_task_with_options_async(request, runtime)

    def create_repo_sync_task_by_rule_with_options(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTaskByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_task_by_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTaskByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_task_by_rule(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_task_by_rule_with_options(request, runtime)

    async def create_repo_sync_task_by_rule_async(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_sync_task_by_rule_with_options_async(request, runtime)

    def create_repo_tag_with_options(
        self,
        request: cr_20181201_models.CreateRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_tag):
            query['FromTag'] = request.from_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.to_tag):
            query['ToTag'] = request.to_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_tag):
            query['FromTag'] = request.from_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.to_tag):
            query['ToTag'] = request.to_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_tag(
        self,
        request: cr_20181201_models.CreateRepoTagRequest,
    ) -> cr_20181201_models.CreateRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_tag_with_options(request, runtime)

    async def create_repo_tag_async(
        self,
        request: cr_20181201_models.CreateRepoTagRequest,
    ) -> cr_20181201_models.CreateRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_tag_with_options_async(request, runtime)

    def create_repo_tag_scan_task_with_options(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_service):
            query['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTagScanTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_tag_scan_task_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_service):
            query['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTagScanTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_tag_scan_task(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_tag_scan_task_with_options(request, runtime)

    async def create_repo_tag_scan_task_async(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_tag_scan_task_with_options_async(request, runtime)

    def create_repo_trigger_with_options(
        self,
        request: cr_20181201_models.CreateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_trigger(
        self,
        request: cr_20181201_models.CreateRepoTriggerRequest,
    ) -> cr_20181201_models.CreateRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repo_trigger_with_options(request, runtime)

    async def create_repo_trigger_async(
        self,
        request: cr_20181201_models.CreateRepoTriggerRequest,
    ) -> cr_20181201_models.CreateRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repo_trigger_with_options_async(request, runtime)

    def create_repository_with_options(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_repository_with_options(request, runtime)

    async def create_repository_async(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_repository_with_options_async(request, runtime)

    def delete_chain_with_options(
        self,
        request: cr_20181201_models.DeleteChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chain_with_options_async(
        self,
        request: cr_20181201_models.DeleteChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chain(
        self,
        request: cr_20181201_models.DeleteChainRequest,
    ) -> cr_20181201_models.DeleteChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_chain_with_options(request, runtime)

    async def delete_chain_async(
        self,
        request: cr_20181201_models.DeleteChainRequest,
    ) -> cr_20181201_models.DeleteChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_chain_with_options_async(request, runtime)

    def delete_chart_namespace_with_options(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        
        @param request: DeleteChartNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChartNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        
        @param request: DeleteChartNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChartNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_namespace(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        
        @param request: DeleteChartNamespaceRequest
        @return: DeleteChartNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_namespace_with_options(request, runtime)

    async def delete_chart_namespace_async(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        
        @param request: DeleteChartNamespaceRequest
        @return: DeleteChartNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chart_namespace_with_options_async(request, runtime)

    def delete_chart_release_with_options(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_release_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_release(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_release_with_options(request, runtime)

    async def delete_chart_release_async(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_chart_release_with_options_async(request, runtime)

    def delete_chart_repository_with_options(
        self,
        request: cr_20181201_models.DeleteChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_repository(
        self,
        request: cr_20181201_models.DeleteChartRepositoryRequest,
    ) -> cr_20181201_models.DeleteChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_repository_with_options(request, runtime)

    async def delete_chart_repository_async(
        self,
        request: cr_20181201_models.DeleteChartRepositoryRequest,
    ) -> cr_20181201_models.DeleteChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_chart_repository_with_options_async(request, runtime)

    def delete_event_center_rule_with_options(
        self,
        request: cr_20181201_models.DeleteEventCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteEventCenterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_center_rule_with_options_async(
        self,
        request: cr_20181201_models.DeleteEventCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteEventCenterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteEventCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_center_rule(
        self,
        request: cr_20181201_models.DeleteEventCenterRuleRequest,
    ) -> cr_20181201_models.DeleteEventCenterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_center_rule_with_options(request, runtime)

    async def delete_event_center_rule_async(
        self,
        request: cr_20181201_models.DeleteEventCenterRuleRequest,
    ) -> cr_20181201_models.DeleteEventCenterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_center_rule_with_options_async(request, runtime)

    def delete_instance_endpoint_acl_policy_with_options(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_endpoint_acl_policy_with_options_async(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_endpoint_acl_policy(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_endpoint_acl_policy_with_options(request, runtime)

    async def delete_instance_endpoint_acl_policy_async(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_endpoint_acl_policy_with_options_async(request, runtime)

    def delete_instance_vpc_endpoint_linked_vpc_with_options(
        self,
        request: cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_vpc_endpoint_linked_vpc(
        self,
        request: cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    async def delete_instance_vpc_endpoint_linked_vpc_async(
        self,
        request: cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_vpc_endpoint_linked_vpc_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        
        @param request: DeleteNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        
        @param request: DeleteNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_repo_build_rule_with_options(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_build_rule(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_build_rule_with_options(request, runtime)

    async def delete_repo_build_rule_async(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_repo_build_rule_with_options_async(request, runtime)

    def delete_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_sync_rule(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_sync_rule_with_options(request, runtime)

    async def delete_repo_sync_rule_async(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_repo_sync_rule_with_options_async(request, runtime)

    def delete_repo_tag_with_options(
        self,
        request: cr_20181201_models.DeleteRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_tag(
        self,
        request: cr_20181201_models.DeleteRepoTagRequest,
    ) -> cr_20181201_models.DeleteRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_tag_with_options(request, runtime)

    async def delete_repo_tag_async(
        self,
        request: cr_20181201_models.DeleteRepoTagRequest,
    ) -> cr_20181201_models.DeleteRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_repo_tag_with_options_async(request, runtime)

    def delete_repo_trigger_with_options(
        self,
        request: cr_20181201_models.DeleteRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_trigger(
        self,
        request: cr_20181201_models.DeleteRepoTriggerRequest,
    ) -> cr_20181201_models.DeleteRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_trigger_with_options(request, runtime)

    async def delete_repo_trigger_async(
        self,
        request: cr_20181201_models.DeleteRepoTriggerRequest,
    ) -> cr_20181201_models.DeleteRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_repo_trigger_with_options_async(request, runtime)

    def delete_repository_with_options(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        """
        If you delete a repository, all images in the repository are also deleted.
        
        @param request: DeleteRepositoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRepositoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        """
        If you delete a repository, all images in the repository are also deleted.
        
        @param request: DeleteRepositoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRepositoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        """
        If you delete a repository, all images in the repository are also deleted.
        
        @param request: DeleteRepositoryRequest
        @return: DeleteRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_repository_with_options(request, runtime)

    async def delete_repository_async(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        """
        If you delete a repository, all images in the repository are also deleted.
        
        @param request: DeleteRepositoryRequest
        @return: DeleteRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_repository_with_options_async(request, runtime)

    def get_artifact_build_rule_with_options(
        self,
        request: cr_20181201_models.GetArtifactBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetArtifactBuildRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_build_rule_with_options_async(
        self,
        request: cr_20181201_models.GetArtifactBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetArtifactBuildRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_build_rule(
        self,
        request: cr_20181201_models.GetArtifactBuildRuleRequest,
    ) -> cr_20181201_models.GetArtifactBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_build_rule_with_options(request, runtime)

    async def get_artifact_build_rule_async(
        self,
        request: cr_20181201_models.GetArtifactBuildRuleRequest,
    ) -> cr_20181201_models.GetArtifactBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_build_rule_with_options_async(request, runtime)

    def get_artifact_build_task_with_options(
        self,
        request: cr_20181201_models.GetArtifactBuildTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetArtifactBuildTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_build_task_with_options_async(
        self,
        request: cr_20181201_models.GetArtifactBuildTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetArtifactBuildTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_build_task(
        self,
        request: cr_20181201_models.GetArtifactBuildTaskRequest,
    ) -> cr_20181201_models.GetArtifactBuildTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_build_task_with_options(request, runtime)

    async def get_artifact_build_task_async(
        self,
        request: cr_20181201_models.GetArtifactBuildTaskRequest,
    ) -> cr_20181201_models.GetArtifactBuildTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_build_task_with_options_async(request, runtime)

    def get_authorization_token_with_options(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        """
        The ID of the Container Registry instance.
        
        @param request: GetAuthorizationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuthorizationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetAuthorizationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_token_with_options_async(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        """
        The ID of the Container Registry instance.
        
        @param request: GetAuthorizationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuthorizationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetAuthorizationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_authorization_token(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        """
        The ID of the Container Registry instance.
        
        @param request: GetAuthorizationTokenRequest
        @return: GetAuthorizationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_token_with_options(request, runtime)

    async def get_authorization_token_async(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        """
        The ID of the Container Registry instance.
        
        @param request: GetAuthorizationTokenRequest
        @return: GetAuthorizationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_authorization_token_with_options_async(request, runtime)

    def get_chain_with_options(
        self,
        request: cr_20181201_models.GetChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chain_with_options_async(
        self,
        request: cr_20181201_models.GetChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chain(
        self,
        request: cr_20181201_models.GetChainRequest,
    ) -> cr_20181201_models.GetChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_chain_with_options(request, runtime)

    async def get_chain_async(
        self,
        request: cr_20181201_models.GetChainRequest,
    ) -> cr_20181201_models.GetChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_chain_with_options_async(request, runtime)

    def get_chart_namespace_with_options(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chart_namespace(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_chart_namespace_with_options(request, runtime)

    async def get_chart_namespace_async(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_chart_namespace_with_options_async(request, runtime)

    def get_chart_repository_with_options(
        self,
        request: cr_20181201_models.GetChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.GetChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chart_repository(
        self,
        request: cr_20181201_models.GetChartRepositoryRequest,
    ) -> cr_20181201_models.GetChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_chart_repository_with_options(request, runtime)

    async def get_chart_repository_async(
        self,
        request: cr_20181201_models.GetChartRepositoryRequest,
    ) -> cr_20181201_models.GetChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_chart_repository_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: cr_20181201_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: cr_20181201_models.GetInstanceRequest,
    ) -> cr_20181201_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: cr_20181201_models.GetInstanceRequest,
    ) -> cr_20181201_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetInstanceCount',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetInstanceCount',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_count(self) -> cr_20181201_models.GetInstanceCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_with_options(runtime)

    async def get_instance_count_async(self) -> cr_20181201_models.GetInstanceCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_count_with_options_async(runtime)

    def get_instance_endpoint_with_options(
        self,
        request: cr_20181201_models.GetInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_endpoint_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_endpoint(
        self,
        request: cr_20181201_models.GetInstanceEndpointRequest,
    ) -> cr_20181201_models.GetInstanceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_endpoint_with_options(request, runtime)

    async def get_instance_endpoint_async(
        self,
        request: cr_20181201_models.GetInstanceEndpointRequest,
    ) -> cr_20181201_models.GetInstanceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_endpoint_with_options_async(request, runtime)

    def get_instance_usage_with_options(
        self,
        request: cr_20181201_models.GetInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceUsage',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_usage_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceUsage',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_usage(
        self,
        request: cr_20181201_models.GetInstanceUsageRequest,
    ) -> cr_20181201_models.GetInstanceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_usage_with_options(request, runtime)

    async def get_instance_usage_async(
        self,
        request: cr_20181201_models.GetInstanceUsageRequest,
    ) -> cr_20181201_models.GetInstanceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_usage_with_options_async(request, runtime)

    def get_instance_vpc_endpoint_with_options(
        self,
        request: cr_20181201_models.GetInstanceVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceVpcEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_vpc_endpoint_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceVpcEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceVpcEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_vpc_endpoint(
        self,
        request: cr_20181201_models.GetInstanceVpcEndpointRequest,
    ) -> cr_20181201_models.GetInstanceVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_vpc_endpoint_with_options(request, runtime)

    async def get_instance_vpc_endpoint_async(
        self,
        request: cr_20181201_models.GetInstanceVpcEndpointRequest,
    ) -> cr_20181201_models.GetInstanceVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_vpc_endpoint_with_options_async(request, runtime)

    def get_namespace_with_options(
        self,
        request: cr_20181201_models.GetNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        request: cr_20181201_models.GetNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_namespace(
        self,
        request: cr_20181201_models.GetNamespaceRequest,
    ) -> cr_20181201_models.GetNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_with_options(request, runtime)

    async def get_namespace_async(
        self,
        request: cr_20181201_models.GetNamespaceRequest,
    ) -> cr_20181201_models.GetNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_namespace_with_options_async(request, runtime)

    def get_repo_build_record_with_options(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        """
        ***\
        
        @param request: GetRepoBuildRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRepoBuildRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        """
        ***\
        
        @param request: GetRepoBuildRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRepoBuildRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_build_record(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        """
        ***\
        
        @param request: GetRepoBuildRecordRequest
        @return: GetRepoBuildRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_repo_build_record_with_options(request, runtime)

    async def get_repo_build_record_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        """
        ***\
        
        @param request: GetRepoBuildRecordRequest
        @return: GetRepoBuildRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_build_record_with_options_async(request, runtime)

    def get_repo_build_record_status_with_options(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecordStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_record_status_with_options_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecordStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_build_record_status(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_build_record_status_with_options(request, runtime)

    async def get_repo_build_record_status_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_build_record_status_with_options_async(request, runtime)

    def get_repo_source_code_repo_with_options(
        self,
        request: cr_20181201_models.GetRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_source_code_repo_with_options_async(
        self,
        request: cr_20181201_models.GetRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_source_code_repo(
        self,
        request: cr_20181201_models.GetRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.GetRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_source_code_repo_with_options(request, runtime)

    async def get_repo_source_code_repo_async(
        self,
        request: cr_20181201_models.GetRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.GetRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_source_code_repo_with_options_async(request, runtime)

    def get_repo_sync_task_with_options(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_sync_task_with_options_async(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_sync_task(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_sync_task_with_options(request, runtime)

    async def get_repo_sync_task_async(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_sync_task_with_options_async(request, runtime)

    def get_repo_tag_with_options(
        self,
        request: cr_20181201_models.GetRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag(
        self,
        request: cr_20181201_models.GetRepoTagRequest,
    ) -> cr_20181201_models.GetRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_with_options(request, runtime)

    async def get_repo_tag_async(
        self,
        request: cr_20181201_models.GetRepoTagRequest,
    ) -> cr_20181201_models.GetRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_tag_with_options_async(request, runtime)

    def get_repo_tag_layers_with_options(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagLayers',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_layers_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagLayers',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_layers(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_layers_with_options(request, runtime)

    async def get_repo_tag_layers_async(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_tag_layers_with_options_async(request, runtime)

    def get_repo_tag_manifest_with_options(
        self,
        request: cr_20181201_models.GetRepoTagManifestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagManifestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagManifest',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagManifestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_manifest_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagManifestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagManifestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagManifest',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagManifestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_manifest(
        self,
        request: cr_20181201_models.GetRepoTagManifestRequest,
    ) -> cr_20181201_models.GetRepoTagManifestResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_manifest_with_options(request, runtime)

    async def get_repo_tag_manifest_async(
        self,
        request: cr_20181201_models.GetRepoTagManifestRequest,
    ) -> cr_20181201_models.GetRepoTagManifestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_tag_manifest_with_options_async(request, runtime)

    def get_repo_tag_scan_status_with_options(
        self,
        request: cr_20181201_models.GetRepoTagScanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_status_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagScanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_scan_status(
        self,
        request: cr_20181201_models.GetRepoTagScanStatusRequest,
    ) -> cr_20181201_models.GetRepoTagScanStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_scan_status_with_options(request, runtime)

    async def get_repo_tag_scan_status_async(
        self,
        request: cr_20181201_models.GetRepoTagScanStatusRequest,
    ) -> cr_20181201_models.GetRepoTagScanStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_tag_scan_status_with_options_async(request, runtime)

    def get_repo_tag_scan_summary_with_options(
        self,
        request: cr_20181201_models.GetRepoTagScanSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_summary_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagScanSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_scan_summary(
        self,
        request: cr_20181201_models.GetRepoTagScanSummaryRequest,
    ) -> cr_20181201_models.GetRepoTagScanSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_scan_summary_with_options(request, runtime)

    async def get_repo_tag_scan_summary_async(
        self,
        request: cr_20181201_models.GetRepoTagScanSummaryRequest,
    ) -> cr_20181201_models.GetRepoTagScanSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_tag_scan_summary_with_options_async(request, runtime)

    def get_repository_with_options(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
    ) -> cr_20181201_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repository_with_options(request, runtime)

    async def get_repository_async(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
    ) -> cr_20181201_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repository_with_options_async(request, runtime)

    def list_artifact_build_task_log_with_options(
        self,
        request: cr_20181201_models.ListArtifactBuildTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListArtifactBuildTaskLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactBuildTaskLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListArtifactBuildTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_build_task_log_with_options_async(
        self,
        request: cr_20181201_models.ListArtifactBuildTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListArtifactBuildTaskLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactBuildTaskLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListArtifactBuildTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_build_task_log(
        self,
        request: cr_20181201_models.ListArtifactBuildTaskLogRequest,
    ) -> cr_20181201_models.ListArtifactBuildTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_build_task_log_with_options(request, runtime)

    async def list_artifact_build_task_log_async(
        self,
        request: cr_20181201_models.ListArtifactBuildTaskLogRequest,
    ) -> cr_20181201_models.ListArtifactBuildTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_artifact_build_task_log_with_options_async(request, runtime)

    def list_chain_with_options(
        self,
        request: cr_20181201_models.ListChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chain_with_options_async(
        self,
        request: cr_20181201_models.ListChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chain(
        self,
        request: cr_20181201_models.ListChainRequest,
    ) -> cr_20181201_models.ListChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chain_with_options(request, runtime)

    async def list_chain_async(
        self,
        request: cr_20181201_models.ListChainRequest,
    ) -> cr_20181201_models.ListChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chain_with_options_async(request, runtime)

    def list_chain_instance_with_options(
        self,
        request: cr_20181201_models.ListChainInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChainInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChainInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chain_instance_with_options_async(
        self,
        request: cr_20181201_models.ListChainInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChainInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChainInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chain_instance(
        self,
        request: cr_20181201_models.ListChainInstanceRequest,
    ) -> cr_20181201_models.ListChainInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chain_instance_with_options(request, runtime)

    async def list_chain_instance_async(
        self,
        request: cr_20181201_models.ListChainInstanceRequest,
    ) -> cr_20181201_models.ListChainInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chain_instance_with_options_async(request, runtime)

    def list_chart_namespace_with_options(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_namespace(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chart_namespace_with_options(request, runtime)

    async def list_chart_namespace_async(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chart_namespace_with_options_async(request, runtime)

    def list_chart_release_with_options(
        self,
        request: cr_20181201_models.ListChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_release_with_options_async(
        self,
        request: cr_20181201_models.ListChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_release(
        self,
        request: cr_20181201_models.ListChartReleaseRequest,
    ) -> cr_20181201_models.ListChartReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chart_release_with_options(request, runtime)

    async def list_chart_release_async(
        self,
        request: cr_20181201_models.ListChartReleaseRequest,
    ) -> cr_20181201_models.ListChartReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chart_release_with_options_async(request, runtime)

    def list_chart_repository_with_options(
        self,
        request: cr_20181201_models.ListChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.ListChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_repository(
        self,
        request: cr_20181201_models.ListChartRepositoryRequest,
    ) -> cr_20181201_models.ListChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chart_repository_with_options(request, runtime)

    async def list_chart_repository_async(
        self,
        request: cr_20181201_models.ListChartRepositoryRequest,
    ) -> cr_20181201_models.ListChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chart_repository_with_options_async(request, runtime)

    def list_event_center_record_with_options(
        self,
        request: cr_20181201_models.ListEventCenterRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListEventCenterRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_center_record_with_options_async(
        self,
        request: cr_20181201_models.ListEventCenterRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListEventCenterRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_center_record(
        self,
        request: cr_20181201_models.ListEventCenterRecordRequest,
    ) -> cr_20181201_models.ListEventCenterRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_center_record_with_options(request, runtime)

    async def list_event_center_record_async(
        self,
        request: cr_20181201_models.ListEventCenterRecordRequest,
    ) -> cr_20181201_models.ListEventCenterRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_center_record_with_options_async(request, runtime)

    def list_event_center_rule_name_with_options(
        self,
        request: cr_20181201_models.ListEventCenterRuleNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListEventCenterRuleNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRuleName',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRuleNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_center_rule_name_with_options_async(
        self,
        request: cr_20181201_models.ListEventCenterRuleNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListEventCenterRuleNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRuleName',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRuleNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_center_rule_name(
        self,
        request: cr_20181201_models.ListEventCenterRuleNameRequest,
    ) -> cr_20181201_models.ListEventCenterRuleNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_center_rule_name_with_options(request, runtime)

    async def list_event_center_rule_name_async(
        self,
        request: cr_20181201_models.ListEventCenterRuleNameRequest,
    ) -> cr_20181201_models.ListEventCenterRuleNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_center_rule_name_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: cr_20181201_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: cr_20181201_models.ListInstanceRequest,
    ) -> cr_20181201_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: cr_20181201_models.ListInstanceRequest,
    ) -> cr_20181201_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_instance_endpoint_with_options(
        self,
        request: cr_20181201_models.ListInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_endpoint_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_endpoint(
        self,
        request: cr_20181201_models.ListInstanceEndpointRequest,
    ) -> cr_20181201_models.ListInstanceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_endpoint_with_options(request, runtime)

    async def list_instance_endpoint_async(
        self,
        request: cr_20181201_models.ListInstanceEndpointRequest,
    ) -> cr_20181201_models.ListInstanceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_endpoint_with_options_async(request, runtime)

    def list_instance_region_with_options(
        self,
        request: cr_20181201_models.ListInstanceRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceRegion',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_region_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceRegion',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_region(
        self,
        request: cr_20181201_models.ListInstanceRegionRequest,
    ) -> cr_20181201_models.ListInstanceRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_region_with_options(request, runtime)

    async def list_instance_region_async(
        self,
        request: cr_20181201_models.ListInstanceRegionRequest,
    ) -> cr_20181201_models.ListInstanceRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_region_with_options_async(request, runtime)

    def list_namespace_with_options(
        self,
        request: cr_20181201_models.ListNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespace_with_options_async(
        self,
        request: cr_20181201_models.ListNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespace(
        self,
        request: cr_20181201_models.ListNamespaceRequest,
    ) -> cr_20181201_models.ListNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_namespace_with_options(request, runtime)

    async def list_namespace_async(
        self,
        request: cr_20181201_models.ListNamespaceRequest,
    ) -> cr_20181201_models.ListNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_namespace_with_options_async(request, runtime)

    def list_repo_build_record_with_options(
        self,
        request: cr_20181201_models.ListRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_record(
        self,
        request: cr_20181201_models.ListRepoBuildRecordRequest,
    ) -> cr_20181201_models.ListRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_record_with_options(request, runtime)

    async def list_repo_build_record_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordRequest,
    ) -> cr_20181201_models.ListRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_build_record_with_options_async(request, runtime)

    def list_repo_build_record_log_with_options(
        self,
        request: cr_20181201_models.ListRepoBuildRecordLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecordLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_record_log_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecordLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_record_log(
        self,
        request: cr_20181201_models.ListRepoBuildRecordLogRequest,
    ) -> cr_20181201_models.ListRepoBuildRecordLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_record_log_with_options(request, runtime)

    async def list_repo_build_record_log_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordLogRequest,
    ) -> cr_20181201_models.ListRepoBuildRecordLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_build_record_log_with_options_async(request, runtime)

    def list_repo_build_rule_with_options(
        self,
        request: cr_20181201_models.ListRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_rule(
        self,
        request: cr_20181201_models.ListRepoBuildRuleRequest,
    ) -> cr_20181201_models.ListRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_rule_with_options(request, runtime)

    async def list_repo_build_rule_async(
        self,
        request: cr_20181201_models.ListRepoBuildRuleRequest,
    ) -> cr_20181201_models.ListRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_build_rule_with_options_async(request, runtime)

    def list_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_sync_rule(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_sync_rule_with_options(request, runtime)

    async def list_repo_sync_rule_async(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_sync_rule_with_options_async(request, runtime)

    def list_repo_sync_task_with_options(
        self,
        request: cr_20181201_models.ListRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.sync_record_id):
            query['SyncRecordId'] = request.sync_record_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_sync_task_with_options_async(
        self,
        request: cr_20181201_models.ListRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.sync_record_id):
            query['SyncRecordId'] = request.sync_record_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_sync_task(
        self,
        request: cr_20181201_models.ListRepoSyncTaskRequest,
    ) -> cr_20181201_models.ListRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_sync_task_with_options(request, runtime)

    async def list_repo_sync_task_async(
        self,
        request: cr_20181201_models.ListRepoSyncTaskRequest,
    ) -> cr_20181201_models.ListRepoSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_sync_task_with_options_async(request, runtime)

    def list_repo_tag_with_options(
        self,
        request: cr_20181201_models.ListRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_tag(
        self,
        request: cr_20181201_models.ListRepoTagRequest,
    ) -> cr_20181201_models.ListRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_tag_with_options(request, runtime)

    async def list_repo_tag_async(
        self,
        request: cr_20181201_models.ListRepoTagRequest,
    ) -> cr_20181201_models.ListRepoTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_tag_with_options_async(request, runtime)

    def list_repo_tag_scan_result_with_options(
        self,
        request: cr_20181201_models.ListRepoTagScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vul_query_key):
            query['VulQueryKey'] = request.vul_query_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTagScanResult',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_tag_scan_result_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTagScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagScanResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vul_query_key):
            query['VulQueryKey'] = request.vul_query_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTagScanResult',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_tag_scan_result(
        self,
        request: cr_20181201_models.ListRepoTagScanResultRequest,
    ) -> cr_20181201_models.ListRepoTagScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_tag_scan_result_with_options(request, runtime)

    async def list_repo_tag_scan_result_async(
        self,
        request: cr_20181201_models.ListRepoTagScanResultRequest,
    ) -> cr_20181201_models.ListRepoTagScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_tag_scan_result_with_options_async(request, runtime)

    def list_repo_trigger_with_options(
        self,
        request: cr_20181201_models.ListRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_trigger(
        self,
        request: cr_20181201_models.ListRepoTriggerRequest,
    ) -> cr_20181201_models.ListRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_trigger_with_options(request, runtime)

    async def list_repo_trigger_async(
        self,
        request: cr_20181201_models.ListRepoTriggerRequest,
    ) -> cr_20181201_models.ListRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_trigger_with_options_async(request, runtime)

    def list_repository_with_options(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_with_options_async(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
    ) -> cr_20181201_models.ListRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repository_with_options(request, runtime)

    async def list_repository_async(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
    ) -> cr_20181201_models.ListRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repository_with_options_async(request, runtime)

    def reset_login_password_with_options(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetLoginPassword',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ResetLoginPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_login_password_with_options_async(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetLoginPassword',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ResetLoginPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_login_password(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_login_password_with_options(request, runtime)

    async def reset_login_password_async(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_login_password_with_options_async(request, runtime)

    def update_chain_with_options(
        self,
        request: cr_20181201_models.UpdateChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chain_with_options_async(
        self,
        request: cr_20181201_models.UpdateChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chain(
        self,
        request: cr_20181201_models.UpdateChainRequest,
    ) -> cr_20181201_models.UpdateChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_chain_with_options(request, runtime)

    async def update_chain_async(
        self,
        request: cr_20181201_models.UpdateChainRequest,
    ) -> cr_20181201_models.UpdateChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_chain_with_options_async(request, runtime)

    def update_chart_namespace_with_options(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chart_namespace(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_chart_namespace_with_options(request, runtime)

    async def update_chart_namespace_async(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_chart_namespace_with_options_async(request, runtime)

    def update_chart_repository_with_options(
        self,
        request: cr_20181201_models.UpdateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.UpdateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chart_repository(
        self,
        request: cr_20181201_models.UpdateChartRepositoryRequest,
    ) -> cr_20181201_models.UpdateChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_chart_repository_with_options(request, runtime)

    async def update_chart_repository_async(
        self,
        request: cr_20181201_models.UpdateChartRepositoryRequest,
    ) -> cr_20181201_models.UpdateChartRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_chart_repository_with_options_async(request, runtime)

    def update_event_center_rule_with_options(
        self,
        tmp_req: cr_20181201_models.UpdateEventCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateEventCenterRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.UpdateEventCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespaces):
            request.namespaces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not UtilClient.is_unset(tmp_req.repo_names):
            request.repo_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_channel):
            query['EventChannel'] = request.event_channel
        if not UtilClient.is_unset(request.event_config):
            query['EventConfig'] = request.event_config
        if not UtilClient.is_unset(request.event_scope):
            query['EventScope'] = request.event_scope
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not UtilClient.is_unset(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not UtilClient.is_unset(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_center_rule_with_options_async(
        self,
        tmp_req: cr_20181201_models.UpdateEventCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateEventCenterRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.UpdateEventCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespaces):
            request.namespaces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not UtilClient.is_unset(tmp_req.repo_names):
            request.repo_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_channel):
            query['EventChannel'] = request.event_channel
        if not UtilClient.is_unset(request.event_config):
            query['EventConfig'] = request.event_config
        if not UtilClient.is_unset(request.event_scope):
            query['EventScope'] = request.event_scope
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not UtilClient.is_unset(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not UtilClient.is_unset(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateEventCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_center_rule(
        self,
        request: cr_20181201_models.UpdateEventCenterRuleRequest,
    ) -> cr_20181201_models.UpdateEventCenterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_center_rule_with_options(request, runtime)

    async def update_event_center_rule_async(
        self,
        request: cr_20181201_models.UpdateEventCenterRuleRequest,
    ) -> cr_20181201_models.UpdateEventCenterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_center_rule_with_options_async(request, runtime)

    def update_instance_endpoint_status_with_options(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceEndpointStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateInstanceEndpointStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_endpoint_status_with_options_async(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceEndpointStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateInstanceEndpointStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_endpoint_status(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_endpoint_status_with_options(request, runtime)

    async def update_instance_endpoint_status_async(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_endpoint_status_with_options_async(request, runtime)

    def update_namespace_with_options(
        self,
        request: cr_20181201_models.UpdateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: cr_20181201_models.UpdateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: cr_20181201_models.UpdateNamespaceRequest,
    ) -> cr_20181201_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_with_options(request, runtime)

    async def update_namespace_async(
        self,
        request: cr_20181201_models.UpdateNamespaceRequest,
    ) -> cr_20181201_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_namespace_with_options_async(request, runtime)

    def update_repo_build_rule_with_options(
        self,
        request: cr_20181201_models.UpdateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_build_rule(
        self,
        request: cr_20181201_models.UpdateRepoBuildRuleRequest,
    ) -> cr_20181201_models.UpdateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_repo_build_rule_with_options(request, runtime)

    async def update_repo_build_rule_async(
        self,
        request: cr_20181201_models.UpdateRepoBuildRuleRequest,
    ) -> cr_20181201_models.UpdateRepoBuildRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_repo_build_rule_with_options_async(request, runtime)

    def update_repo_source_code_repo_with_options(
        self,
        request: cr_20181201_models.UpdateRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_id):
            query['CodeRepoId'] = request.code_repo_id
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_source_code_repo_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepoSourceCodeRepoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoSourceCodeRepoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_id):
            query['CodeRepoId'] = request.code_repo_id
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_source_code_repo(
        self,
        request: cr_20181201_models.UpdateRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.UpdateRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_repo_source_code_repo_with_options(request, runtime)

    async def update_repo_source_code_repo_async(
        self,
        request: cr_20181201_models.UpdateRepoSourceCodeRepoRequest,
    ) -> cr_20181201_models.UpdateRepoSourceCodeRepoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_repo_source_code_repo_with_options_async(request, runtime)

    def update_repo_trigger_with_options(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_trigger(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_repo_trigger_with_options(request, runtime)

    async def update_repo_trigger_async(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_repo_trigger_with_options_async(request, runtime)

    def update_repository_with_options(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_repository_with_options(request, runtime)

    async def update_repository_async(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_repository_with_options_async(request, runtime)
