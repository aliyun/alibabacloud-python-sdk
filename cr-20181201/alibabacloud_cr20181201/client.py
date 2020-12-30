# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cr20181201 import models as cr_20181201_models
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

    def cancel_repo_build_record_with_options(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CancelRepoBuildRecordResponse().from_map(
            self.do_rpcrequest('CancelRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.CancelRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CancelRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CancelRepoBuildRecordResponse().from_map(
            await self.do_rpcrequest_async('CancelRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_build_record_by_rule_with_options(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateBuildRecordByRuleResponse().from_map(
            self.do_rpcrequest('CreateBuildRecordByRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_build_record_by_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateBuildRecordByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateBuildRecordByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateBuildRecordByRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateBuildRecordByRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_chart_namespace_with_options(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateChartNamespaceResponse().from_map(
            self.do_rpcrequest('CreateChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.CreateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateChartNamespaceResponse().from_map(
            await self.do_rpcrequest_async('CreateChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateChartRepositoryResponse().from_map(
            self.do_rpcrequest('CreateChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.CreateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateChartRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateChartRepositoryResponse().from_map(
            await self.do_rpcrequest_async('CreateChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateInstanceEndpointAclPolicyResponse().from_map(
            self.do_rpcrequest('CreateInstanceEndpointAclPolicy', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_endpoint_acl_policy_with_options_async(
        self,
        request: cr_20181201_models.CreateInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateInstanceEndpointAclPolicyResponse().from_map(
            await self.do_rpcrequest_async('CreateInstanceEndpointAclPolicy', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse().from_map(
            self.do_rpcrequest('CreateInstanceVpcEndpointLinkedVpc', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse().from_map(
            await self.do_rpcrequest_async('CreateInstanceVpcEndpointLinkedVpc', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_vpc_endpoint_linked_vpc(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    async def create_instance_vpc_endpoint_linked_vpc_async(
        self,
        request: cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_vpc_endpoint_linked_vpc_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateNamespaceResponse().from_map(
            self.do_rpcrequest('CreateNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: cr_20181201_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateNamespaceResponse().from_map(
            await self.do_rpcrequest_async('CreateNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoBuildRuleResponse().from_map(
            self.do_rpcrequest('CreateRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoBuildRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_repository_with_options(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepositoryResponse().from_map(
            self.do_rpcrequest('CreateRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: cr_20181201_models.CreateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepositoryResponse().from_map(
            await self.do_rpcrequest_async('CreateRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoSyncRuleResponse().from_map(
            self.do_rpcrequest('CreateRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoSyncRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_repo_sync_task_by_rule_with_options(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoSyncTaskByRuleResponse().from_map(
            self.do_rpcrequest('CreateRepoSyncTaskByRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repo_sync_task_by_rule_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoSyncTaskByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoSyncTaskByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoSyncTaskByRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateRepoSyncTaskByRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_repo_tag_scan_task_with_options(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoTagScanTaskResponse().from_map(
            self.do_rpcrequest('CreateRepoTagScanTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repo_tag_scan_task_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoTagScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTagScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoTagScanTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateRepoTagScanTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoTriggerResponse().from_map(
            self.do_rpcrequest('CreateRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.CreateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.CreateRepoTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.CreateRepoTriggerResponse().from_map(
            await self.do_rpcrequest_async('CreateRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_chart_namespace_with_options(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartNamespaceResponse().from_map(
            self.do_rpcrequest('DeleteChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartNamespaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_chart_namespace(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_namespace_with_options(request, runtime)

    async def delete_chart_namespace_async(
        self,
        request: cr_20181201_models.DeleteChartNamespaceRequest,
    ) -> cr_20181201_models.DeleteChartNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_chart_namespace_with_options_async(request, runtime)

    def delete_chart_release_with_options(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartReleaseResponse().from_map(
            self.do_rpcrequest('DeleteChartRelease', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_chart_release_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartReleaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartReleaseResponse().from_map(
            await self.do_rpcrequest_async('DeleteChartRelease', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartRepositoryResponse().from_map(
            self.do_rpcrequest('DeleteChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.DeleteChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteChartRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteChartRepositoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_instance_endpoint_acl_policy_with_options(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse().from_map(
            self.do_rpcrequest('DeleteInstanceEndpointAclPolicy', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_endpoint_acl_policy_with_options_async(
        self,
        request: cr_20181201_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstanceEndpointAclPolicy', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse().from_map(
            self.do_rpcrequest('DeleteInstanceVpcEndpointLinkedVpc', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstanceVpcEndpointLinkedVpc', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteNamespaceResponse().from_map(
            self.do_rpcrequest('DeleteNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteNamespaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_namespace(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: cr_20181201_models.DeleteNamespaceRequest,
    ) -> cr_20181201_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_repo_build_rule_with_options(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoBuildRuleResponse().from_map(
            self.do_rpcrequest('DeleteRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoBuildRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_repository_with_options(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepositoryResponse().from_map(
            self.do_rpcrequest('DeleteRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepositoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_repository(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_repository_with_options(request, runtime)

    async def delete_repository_async(
        self,
        request: cr_20181201_models.DeleteRepositoryRequest,
    ) -> cr_20181201_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_repository_with_options_async(request, runtime)

    def delete_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoSyncRuleResponse().from_map(
            self.do_rpcrequest('DeleteRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoSyncRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoTagResponse().from_map(
            self.do_rpcrequest('DeleteRepoTag', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoTagResponse().from_map(
            await self.do_rpcrequest_async('DeleteRepoTag', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoTriggerResponse().from_map(
            self.do_rpcrequest('DeleteRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.DeleteRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.DeleteRepoTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.DeleteRepoTriggerResponse().from_map(
            await self.do_rpcrequest_async('DeleteRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_authorization_token_with_options(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetAuthorizationTokenResponse().from_map(
            self.do_rpcrequest('GetAuthorizationToken', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_authorization_token_with_options_async(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetAuthorizationTokenResponse().from_map(
            await self.do_rpcrequest_async('GetAuthorizationToken', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authorization_token(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_token_with_options(request, runtime)

    async def get_authorization_token_async(
        self,
        request: cr_20181201_models.GetAuthorizationTokenRequest,
    ) -> cr_20181201_models.GetAuthorizationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_authorization_token_with_options_async(request, runtime)

    def get_chart_namespace_with_options(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetChartNamespaceResponse().from_map(
            self.do_rpcrequest('GetChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.GetChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetChartNamespaceResponse().from_map(
            await self.do_rpcrequest_async('GetChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetChartRepositoryResponse().from_map(
            self.do_rpcrequest('GetChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.GetChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetChartRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetChartRepositoryResponse().from_map(
            await self.do_rpcrequest_async('GetChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceResponse().from_map(
            self.do_rpcrequest('GetInstance', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceResponse().from_map(
            await self.do_rpcrequest_async('GetInstance', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return cr_20181201_models.GetInstanceCountResponse().from_map(
            self.do_rpcrequest('GetInstanceCount', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceCountResponse:
        req = open_api_models.OpenApiRequest()
        return cr_20181201_models.GetInstanceCountResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceCount', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceEndpointResponse().from_map(
            self.do_rpcrequest('GetInstanceEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_endpoint_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceEndpointResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceUsageResponse().from_map(
            self.do_rpcrequest('GetInstanceUsage', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_usage_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceUsageResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceUsage', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceVpcEndpointResponse().from_map(
            self.do_rpcrequest('GetInstanceVpcEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_vpc_endpoint_with_options_async(
        self,
        request: cr_20181201_models.GetInstanceVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetInstanceVpcEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetInstanceVpcEndpointResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceVpcEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetNamespaceResponse().from_map(
            self.do_rpcrequest('GetNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        request: cr_20181201_models.GetNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetNamespaceResponse().from_map(
            await self.do_rpcrequest_async('GetNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoBuildRecordResponse().from_map(
            self.do_rpcrequest('GetRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoBuildRecordResponse().from_map(
            await self.do_rpcrequest_async('GetRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_repo_build_record(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repo_build_record_with_options(request, runtime)

    async def get_repo_build_record_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordRequest,
    ) -> cr_20181201_models.GetRepoBuildRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repo_build_record_with_options_async(request, runtime)

    def get_repo_build_record_status_with_options(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoBuildRecordStatusResponse().from_map(
            self.do_rpcrequest('GetRepoBuildRecordStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_build_record_status_with_options_async(
        self,
        request: cr_20181201_models.GetRepoBuildRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoBuildRecordStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoBuildRecordStatusResponse().from_map(
            await self.do_rpcrequest_async('GetRepoBuildRecordStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_repository_with_options(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepositoryResponse().from_map(
            self.do_rpcrequest('GetRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        request: cr_20181201_models.GetRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepositoryResponse().from_map(
            await self.do_rpcrequest_async('GetRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_repo_sync_task_with_options(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoSyncTaskResponse().from_map(
            self.do_rpcrequest('GetRepoSyncTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_sync_task_with_options_async(
        self,
        request: cr_20181201_models.GetRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoSyncTaskResponse().from_map(
            await self.do_rpcrequest_async('GetRepoSyncTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_repo_tag_layers_with_options(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagLayersResponse().from_map(
            self.do_rpcrequest('GetRepoTagLayers', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_tag_layers_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagLayersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagLayersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagLayersResponse().from_map(
            await self.do_rpcrequest_async('GetRepoTagLayers', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagManifestResponse().from_map(
            self.do_rpcrequest('GetRepoTagManifest', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_tag_manifest_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagManifestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagManifestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagManifestResponse().from_map(
            await self.do_rpcrequest_async('GetRepoTagManifest', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagScanStatusResponse().from_map(
            self.do_rpcrequest('GetRepoTagScanStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_tag_scan_status_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagScanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagScanStatusResponse().from_map(
            await self.do_rpcrequest_async('GetRepoTagScanStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagScanSummaryResponse().from_map(
            self.do_rpcrequest('GetRepoTagScanSummary', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_repo_tag_scan_summary_with_options_async(
        self,
        request: cr_20181201_models.GetRepoTagScanSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.GetRepoTagScanSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.GetRepoTagScanSummaryResponse().from_map(
            await self.do_rpcrequest_async('GetRepoTagScanSummary', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_chart_namespace_with_options(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartNamespaceResponse().from_map(
            self.do_rpcrequest('ListChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.ListChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartNamespaceResponse().from_map(
            await self.do_rpcrequest_async('ListChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartReleaseResponse().from_map(
            self.do_rpcrequest('ListChartRelease', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_chart_release_with_options_async(
        self,
        request: cr_20181201_models.ListChartReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartReleaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartReleaseResponse().from_map(
            await self.do_rpcrequest_async('ListChartRelease', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartRepositoryResponse().from_map(
            self.do_rpcrequest('ListChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.ListChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListChartRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListChartRepositoryResponse().from_map(
            await self.do_rpcrequest_async('ListChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_instance_with_options(
        self,
        request: cr_20181201_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceResponse().from_map(
            self.do_rpcrequest('ListInstance', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceResponse().from_map(
            await self.do_rpcrequest_async('ListInstance', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceEndpointResponse().from_map(
            self.do_rpcrequest('ListInstanceEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_endpoint_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceEndpointResponse().from_map(
            await self.do_rpcrequest_async('ListInstanceEndpoint', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceRegionResponse().from_map(
            self.do_rpcrequest('ListInstanceRegion', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_region_with_options_async(
        self,
        request: cr_20181201_models.ListInstanceRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListInstanceRegionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListInstanceRegionResponse().from_map(
            await self.do_rpcrequest_async('ListInstanceRegion', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListNamespaceResponse().from_map(
            self.do_rpcrequest('ListNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_namespace_with_options_async(
        self,
        request: cr_20181201_models.ListNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListNamespaceResponse().from_map(
            await self.do_rpcrequest_async('ListNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRecordResponse().from_map(
            self.do_rpcrequest('ListRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_build_record_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRecordResponse().from_map(
            await self.do_rpcrequest_async('ListRepoBuildRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRecordLogResponse().from_map(
            self.do_rpcrequest('ListRepoBuildRecordLog', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_build_record_log_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRecordLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRecordLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRecordLogResponse().from_map(
            await self.do_rpcrequest_async('ListRepoBuildRecordLog', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRuleResponse().from_map(
            self.do_rpcrequest('ListRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.ListRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoBuildRuleResponse().from_map(
            await self.do_rpcrequest_async('ListRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_repository_with_options(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepositoryResponse().from_map(
            self.do_rpcrequest('ListRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repository_with_options_async(
        self,
        request: cr_20181201_models.ListRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepositoryResponse().from_map(
            await self.do_rpcrequest_async('ListRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_repo_sync_rule_with_options(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoSyncRuleResponse().from_map(
            self.do_rpcrequest('ListRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_sync_rule_with_options_async(
        self,
        request: cr_20181201_models.ListRepoSyncRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoSyncRuleResponse().from_map(
            await self.do_rpcrequest_async('ListRepoSyncRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoSyncTaskResponse().from_map(
            self.do_rpcrequest('ListRepoSyncTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_sync_task_with_options_async(
        self,
        request: cr_20181201_models.ListRepoSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoSyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoSyncTaskResponse().from_map(
            await self.do_rpcrequest_async('ListRepoSyncTask', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTagResponse().from_map(
            self.do_rpcrequest('ListRepoTag', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_tag_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTagResponse().from_map(
            await self.do_rpcrequest_async('ListRepoTag', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTagScanResultResponse().from_map(
            self.do_rpcrequest('ListRepoTagScanResult', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_tag_scan_result_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTagScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTagScanResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTagScanResultResponse().from_map(
            await self.do_rpcrequest_async('ListRepoTagScanResult', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTriggerResponse().from_map(
            self.do_rpcrequest('ListRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTriggerResponse().from_map(
            await self.do_rpcrequest_async('ListRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_repo_trigger_record_with_options(
        self,
        request: cr_20181201_models.ListRepoTriggerRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTriggerRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTriggerRecordResponse().from_map(
            self.do_rpcrequest('ListRepoTriggerRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_repo_trigger_record_with_options_async(
        self,
        request: cr_20181201_models.ListRepoTriggerRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ListRepoTriggerRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ListRepoTriggerRecordResponse().from_map(
            await self.do_rpcrequest_async('ListRepoTriggerRecord', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_repo_trigger_record(
        self,
        request: cr_20181201_models.ListRepoTriggerRecordRequest,
    ) -> cr_20181201_models.ListRepoTriggerRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_repo_trigger_record_with_options(request, runtime)

    async def list_repo_trigger_record_async(
        self,
        request: cr_20181201_models.ListRepoTriggerRecordRequest,
    ) -> cr_20181201_models.ListRepoTriggerRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_repo_trigger_record_with_options_async(request, runtime)

    def reset_login_password_with_options(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ResetLoginPasswordResponse().from_map(
            self.do_rpcrequest('ResetLoginPassword', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_login_password_with_options_async(
        self,
        request: cr_20181201_models.ResetLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.ResetLoginPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.ResetLoginPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetLoginPassword', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_chart_namespace_with_options(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateChartNamespaceResponse().from_map(
            self.do_rpcrequest('UpdateChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_chart_namespace_with_options_async(
        self,
        request: cr_20181201_models.UpdateChartNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateChartNamespaceResponse().from_map(
            await self.do_rpcrequest_async('UpdateChartNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateChartRepositoryResponse().from_map(
            self.do_rpcrequest('UpdateChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_chart_repository_with_options_async(
        self,
        request: cr_20181201_models.UpdateChartRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateChartRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateChartRepositoryResponse().from_map(
            await self.do_rpcrequest_async('UpdateChartRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_instance_endpoint_status_with_options(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateInstanceEndpointStatusResponse().from_map(
            self.do_rpcrequest('UpdateInstanceEndpointStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_endpoint_status_with_options_async(
        self,
        request: cr_20181201_models.UpdateInstanceEndpointStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateInstanceEndpointStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateInstanceEndpointStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateInstanceEndpointStatus', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateNamespaceResponse().from_map(
            self.do_rpcrequest('UpdateNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: cr_20181201_models.UpdateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateNamespaceResponse().from_map(
            await self.do_rpcrequest_async('UpdateNamespace', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepoBuildRuleResponse().from_map(
            self.do_rpcrequest('UpdateRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_repo_build_rule_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepoBuildRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoBuildRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepoBuildRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateRepoBuildRule', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_repository_with_options(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepositoryResponse().from_map(
            self.do_rpcrequest('UpdateRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepositoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepositoryResponse().from_map(
            await self.do_rpcrequest_async('UpdateRepository', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_repo_trigger_with_options(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepoTriggerResponse().from_map(
            self.do_rpcrequest('UpdateRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_repo_trigger_with_options_async(
        self,
        request: cr_20181201_models.UpdateRepoTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cr_20181201_models.UpdateRepoTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cr_20181201_models.UpdateRepoTriggerResponse().from_map(
            await self.do_rpcrequest_async('UpdateRepoTrigger', '2018-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
