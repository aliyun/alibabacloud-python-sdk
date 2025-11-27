# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms20240330 import models as cms_20240330_models
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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_addon_release_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.CreateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateAddonReleaseResponse:
        """
        @summary Install the access component, representing a single access attempt
        
        @description Used to create a site monitoring task
        
        @param request: CreateAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addon_name):
            body['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not UtilClient.is_unset(request.env_type):
            body['envType'] = request.env_type
        if not UtilClient.is_unset(request.parent_addon_release_id):
            body['parentAddonReleaseId'] = request.parent_addon_release_id
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_addon_release_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.CreateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateAddonReleaseResponse:
        """
        @summary Install the access component, representing a single access attempt
        
        @description Used to create a site monitoring task
        
        @param request: CreateAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addon_name):
            body['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not UtilClient.is_unset(request.env_type):
            body['envType'] = request.env_type
        if not UtilClient.is_unset(request.parent_addon_release_id):
            body['parentAddonReleaseId'] = request.parent_addon_release_id
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_addon_release(
        self,
        policy_id: str,
        request: cms_20240330_models.CreateAddonReleaseRequest,
    ) -> cms_20240330_models.CreateAddonReleaseResponse:
        """
        @summary Install the access component, representing a single access attempt
        
        @description Used to create a site monitoring task
        
        @param request: CreateAddonReleaseRequest
        @return: CreateAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_addon_release_with_options(policy_id, request, headers, runtime)

    async def create_addon_release_async(
        self,
        policy_id: str,
        request: cms_20240330_models.CreateAddonReleaseRequest,
    ) -> cms_20240330_models.CreateAddonReleaseResponse:
        """
        @summary Install the access component, representing a single access attempt
        
        @description Used to create a site monitoring task
        
        @param request: CreateAddonReleaseRequest
        @return: CreateAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_addon_release_with_options_async(policy_id, request, headers, runtime)

    def create_agg_task_group_with_options(
        self,
        instance_id: str,
        request: cms_20240330_models.CreateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateAggTaskGroupResponse:
        """
        @summary Create Aggregation Task Group
        
        @param request: CreateAggTaskGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.override_if_exists):
            query['overrideIfExists'] = request.override_if_exists
        body = {}
        if not UtilClient.is_unset(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not UtilClient.is_unset(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not UtilClient.is_unset(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not UtilClient.is_unset(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.delay):
            body['delay'] = request.delay
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.from_time):
            body['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not UtilClient.is_unset(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not UtilClient.is_unset(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not UtilClient.is_unset(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not UtilClient.is_unset(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not UtilClient.is_unset(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agg_task_group_with_options_async(
        self,
        instance_id: str,
        request: cms_20240330_models.CreateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateAggTaskGroupResponse:
        """
        @summary Create Aggregation Task Group
        
        @param request: CreateAggTaskGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAggTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.override_if_exists):
            query['overrideIfExists'] = request.override_if_exists
        body = {}
        if not UtilClient.is_unset(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not UtilClient.is_unset(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not UtilClient.is_unset(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not UtilClient.is_unset(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.delay):
            body['delay'] = request.delay
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.from_time):
            body['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not UtilClient.is_unset(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not UtilClient.is_unset(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not UtilClient.is_unset(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not UtilClient.is_unset(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not UtilClient.is_unset(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agg_task_group(
        self,
        instance_id: str,
        request: cms_20240330_models.CreateAggTaskGroupRequest,
    ) -> cms_20240330_models.CreateAggTaskGroupResponse:
        """
        @summary Create Aggregation Task Group
        
        @param request: CreateAggTaskGroupRequest
        @return: CreateAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_agg_task_group_with_options(instance_id, request, headers, runtime)

    async def create_agg_task_group_async(
        self,
        instance_id: str,
        request: cms_20240330_models.CreateAggTaskGroupRequest,
    ) -> cms_20240330_models.CreateAggTaskGroupResponse:
        """
        @summary Create Aggregation Task Group
        
        @param request: CreateAggTaskGroupRequest
        @return: CreateAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_agg_task_group_with_options_async(instance_id, request, headers, runtime)

    def create_biz_trace_with_options(
        self,
        request: cms_20240330_models.CreateBizTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateBizTraceResponse:
        """
        @summary 创建业务链路
        
        @param request: CreateBizTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not UtilClient.is_unset(request.biz_trace_code):
            body['bizTraceCode'] = request.biz_trace_code
        if not UtilClient.is_unset(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not UtilClient.is_unset(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_trace_with_options_async(
        self,
        request: cms_20240330_models.CreateBizTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateBizTraceResponse:
        """
        @summary 创建业务链路
        
        @param request: CreateBizTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not UtilClient.is_unset(request.biz_trace_code):
            body['bizTraceCode'] = request.biz_trace_code
        if not UtilClient.is_unset(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not UtilClient.is_unset(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_trace(
        self,
        request: cms_20240330_models.CreateBizTraceRequest,
    ) -> cms_20240330_models.CreateBizTraceResponse:
        """
        @summary 创建业务链路
        
        @param request: CreateBizTraceRequest
        @return: CreateBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_biz_trace_with_options(request, headers, runtime)

    async def create_biz_trace_async(
        self,
        request: cms_20240330_models.CreateBizTraceRequest,
    ) -> cms_20240330_models.CreateBizTraceResponse:
        """
        @summary 创建业务链路
        
        @param request: CreateBizTraceRequest
        @return: CreateBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_biz_trace_with_options_async(request, headers, runtime)

    def create_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateCloudResourceResponse:
        """
        @summary 创建云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateCloudResourceResponse:
        """
        @summary 创建云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_resource(self) -> cms_20240330_models.CreateCloudResourceResponse:
        """
        @summary 创建云资源中心
        
        @return: CreateCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cloud_resource_with_options(headers, runtime)

    async def create_cloud_resource_async(self) -> cms_20240330_models.CreateCloudResourceResponse:
        """
        @summary 创建云资源中心
        
        @return: CreateCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cloud_resource_with_options_async(headers, runtime)

    def create_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary Create storage related to EntityStore
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary Create storage related to EntityStore
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary Create storage related to EntityStore
        
        @return: CreateEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_entity_store_with_options(workspace_name, headers, runtime)

    async def create_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary Create storage related to EntityStore
        
        @return: CreateEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_entity_store_with_options_async(workspace_name, headers, runtime)

    def create_integration_policy_with_options(
        self,
        request: cms_20240330_models.CreateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateIntegrationPolicyResponse:
        """
        @summary Create Access Center Policy
        
        @description This interface is used to support users in creating event integration.
        
        @param request: CreateIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_group):
            body['entityGroup'] = request.entity_group
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            body['policyType'] = request.policy_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_integration_policy_with_options_async(
        self,
        request: cms_20240330_models.CreateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateIntegrationPolicyResponse:
        """
        @summary Create Access Center Policy
        
        @description This interface is used to support users in creating event integration.
        
        @param request: CreateIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_group):
            body['entityGroup'] = request.entity_group
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            body['policyType'] = request.policy_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_integration_policy(
        self,
        request: cms_20240330_models.CreateIntegrationPolicyRequest,
    ) -> cms_20240330_models.CreateIntegrationPolicyResponse:
        """
        @summary Create Access Center Policy
        
        @description This interface is used to support users in creating event integration.
        
        @param request: CreateIntegrationPolicyRequest
        @return: CreateIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_integration_policy_with_options(request, headers, runtime)

    async def create_integration_policy_async(
        self,
        request: cms_20240330_models.CreateIntegrationPolicyRequest,
    ) -> cms_20240330_models.CreateIntegrationPolicyResponse:
        """
        @summary Create Access Center Policy
        
        @description This interface is used to support users in creating event integration.
        
        @param request: CreateIntegrationPolicyRequest
        @return: CreateIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_integration_policy_with_options_async(request, headers, runtime)

    def create_prometheus_instance_with_options(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary Create a Prometheus monitoring instance
        
        @param request: CreatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_instance_with_options_async(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary Create a Prometheus monitoring instance
        
        @param request: CreatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_instance(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary Create a Prometheus monitoring instance
        
        @param request: CreatePrometheusInstanceRequest
        @return: CreatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_prometheus_instance_with_options(request, headers, runtime)

    async def create_prometheus_instance_async(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary Create a Prometheus monitoring instance
        
        @param request: CreatePrometheusInstanceRequest
        @return: CreatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_prometheus_instance_with_options_async(request, headers, runtime)

    def create_prometheus_view_with_options(
        self,
        request: cms_20240330_models.CreatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusViewResponse:
        """
        @summary Create Prometheus View
        
        @description Used to create a site monitoring task
        
        @param request: CreatePrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not UtilClient.is_unset(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_view_with_options_async(
        self,
        request: cms_20240330_models.CreatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusViewResponse:
        """
        @summary Create Prometheus View
        
        @description Used to create a site monitoring task
        
        @param request: CreatePrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not UtilClient.is_unset(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_view(
        self,
        request: cms_20240330_models.CreatePrometheusViewRequest,
    ) -> cms_20240330_models.CreatePrometheusViewResponse:
        """
        @summary Create Prometheus View
        
        @description Used to create a site monitoring task
        
        @param request: CreatePrometheusViewRequest
        @return: CreatePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_prometheus_view_with_options(request, headers, runtime)

    async def create_prometheus_view_async(
        self,
        request: cms_20240330_models.CreatePrometheusViewRequest,
    ) -> cms_20240330_models.CreatePrometheusViewResponse:
        """
        @summary Create Prometheus View
        
        @description Used to create a site monitoring task
        
        @param request: CreatePrometheusViewRequest
        @return: CreatePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_prometheus_view_with_options_async(request, headers, runtime)

    def create_prometheus_virtual_instance_with_options(
        self,
        request: cms_20240330_models.CreatePrometheusVirtualInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusVirtualInstanceResponse:
        """
        @summary Create Prometheus Monitoring Instance
        
        @description Create a Prometheus monitoring virtual instance.
        
        @param request: CreatePrometheusVirtualInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusVirtualInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusVirtualInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/virtual-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusVirtualInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_virtual_instance_with_options_async(
        self,
        request: cms_20240330_models.CreatePrometheusVirtualInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusVirtualInstanceResponse:
        """
        @summary Create Prometheus Monitoring Instance
        
        @description Create a Prometheus monitoring virtual instance.
        
        @param request: CreatePrometheusVirtualInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusVirtualInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusVirtualInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/virtual-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusVirtualInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_virtual_instance(
        self,
        request: cms_20240330_models.CreatePrometheusVirtualInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusVirtualInstanceResponse:
        """
        @summary Create Prometheus Monitoring Instance
        
        @description Create a Prometheus monitoring virtual instance.
        
        @param request: CreatePrometheusVirtualInstanceRequest
        @return: CreatePrometheusVirtualInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_prometheus_virtual_instance_with_options(request, headers, runtime)

    async def create_prometheus_virtual_instance_async(
        self,
        request: cms_20240330_models.CreatePrometheusVirtualInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusVirtualInstanceResponse:
        """
        @summary Create Prometheus Monitoring Instance
        
        @description Create a Prometheus monitoring virtual instance.
        
        @param request: CreatePrometheusVirtualInstanceRequest
        @return: CreatePrometheusVirtualInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_prometheus_virtual_instance_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateServiceResponse:
        """
        @summary Create Service
        
        @param request: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.pid):
            body['pid'] = request.pid
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_status):
            body['serviceStatus'] = request.service_status
        if not UtilClient.is_unset(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateServiceResponse:
        """
        @summary Create Service
        
        @param request: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.pid):
            body['pid'] = request.pid
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_status):
            body['serviceStatus'] = request.service_status
        if not UtilClient.is_unset(request.service_type):
            body['serviceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        workspace: str,
        request: cms_20240330_models.CreateServiceRequest,
    ) -> cms_20240330_models.CreateServiceResponse:
        """
        @summary Create Service
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(workspace, request, headers, runtime)

    async def create_service_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateServiceRequest,
    ) -> cms_20240330_models.CreateServiceResponse:
        """
        @summary Create Service
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(workspace, request, headers, runtime)

    def create_ticket_with_options(
        self,
        request: cms_20240330_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateTicketResponse:
        """
        @summary Create Ticket
        
        @param request: CreateTicketRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not UtilClient.is_unset(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/tickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: cms_20240330_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateTicketResponse:
        """
        @summary Create Ticket
        
        @param request: CreateTicketRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not UtilClient.is_unset(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/tickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: cms_20240330_models.CreateTicketRequest,
    ) -> cms_20240330_models.CreateTicketResponse:
        """
        @summary Create Ticket
        
        @param request: CreateTicketRequest
        @return: CreateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(request, headers, runtime)

    async def create_ticket_async(
        self,
        request: cms_20240330_models.CreateTicketRequest,
    ) -> cms_20240330_models.CreateTicketResponse:
        """
        @summary Create Ticket
        
        @param request: CreateTicketRequest
        @return: CreateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ticket_with_options_async(request, headers, runtime)

    def create_umodel_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary Create Umodel configuration
        
        @description Create Umodel configuration in the specified workspace
        
        @param request: CreateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_umodel_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary Create Umodel configuration
        
        @description Create Umodel configuration in the specified workspace
        
        @param request: CreateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_umodel(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary Create Umodel configuration
        
        @description Create Umodel configuration in the specified workspace
        
        @param request: CreateUmodelRequest
        @return: CreateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_umodel_with_options(workspace, request, headers, runtime)

    async def create_umodel_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary Create Umodel configuration
        
        @description Create Umodel configuration in the specified workspace
        
        @param request: CreateUmodelRequest
        @return: CreateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_umodel_with_options_async(workspace, request, headers, runtime)

    def delete_addon_release_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteAddonReleaseResponse:
        """
        @summary Delete addon release information
        
        @param request: DeleteAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.release_name):
            query['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_addon_release_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteAddonReleaseResponse:
        """
        @summary Delete addon release information
        
        @param request: DeleteAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.release_name):
            query['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_addon_release(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteAddonReleaseRequest,
    ) -> cms_20240330_models.DeleteAddonReleaseResponse:
        """
        @summary Delete addon release information
        
        @param request: DeleteAddonReleaseRequest
        @return: DeleteAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_addon_release_with_options(policy_id, request, headers, runtime)

    async def delete_addon_release_async(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteAddonReleaseRequest,
    ) -> cms_20240330_models.DeleteAddonReleaseResponse:
        """
        @summary Delete addon release information
        
        @param request: DeleteAddonReleaseRequest
        @return: DeleteAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_addon_release_with_options_async(policy_id, request, headers, runtime)

    def delete_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteAggTaskGroupResponse:
        """
        @summary Delete Aggregation Task Group
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggTaskGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteAggTaskGroupResponse:
        """
        @summary Delete Aggregation Task Group
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAggTaskGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
    ) -> cms_20240330_models.DeleteAggTaskGroupResponse:
        """
        @summary Delete Aggregation Task Group
        
        @return: DeleteAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_agg_task_group_with_options(instance_id, group_id, headers, runtime)

    async def delete_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
    ) -> cms_20240330_models.DeleteAggTaskGroupResponse:
        """
        @summary Delete Aggregation Task Group
        
        @return: DeleteAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def delete_biz_trace_with_options(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteBizTraceResponse:
        """
        @summary 删除业务链路
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteBizTraceResponse:
        """
        @summary 删除业务链路
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_trace(
        self,
        biz_trace_id: str,
    ) -> cms_20240330_models.DeleteBizTraceResponse:
        """
        @summary 删除业务链路
        
        @return: DeleteBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_biz_trace_with_options(biz_trace_id, headers, runtime)

    async def delete_biz_trace_async(
        self,
        biz_trace_id: str,
    ) -> cms_20240330_models.DeleteBizTraceResponse:
        """
        @summary 删除业务链路
        
        @return: DeleteBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_biz_trace_with_options_async(biz_trace_id, headers, runtime)

    def delete_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteCloudResourceResponse:
        """
        @summary 删除云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteCloudResourceResponse:
        """
        @summary 删除云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_resource(self) -> cms_20240330_models.DeleteCloudResourceResponse:
        """
        @summary 删除云资源中心
        
        @return: DeleteCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cloud_resource_with_options(headers, runtime)

    async def delete_cloud_resource_async(self) -> cms_20240330_models.DeleteCloudResourceResponse:
        """
        @summary 删除云资源中心
        
        @return: DeleteCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cloud_resource_with_options_async(headers, runtime)

    def delete_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary Delete EntityStore related storage
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary Delete EntityStore related storage
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary Delete EntityStore related storage
        
        @return: DeleteEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_entity_store_with_options(workspace_name, headers, runtime)

    async def delete_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary Delete EntityStore related storage
        
        @return: DeleteEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_entity_store_with_options_async(workspace_name, headers, runtime)

    def delete_integration_policy_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteIntegrationPolicyResponse:
        """
        @summary Delete Access Center Policy
        
        @param request: DeleteIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integration_policy_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteIntegrationPolicyResponse:
        """
        @summary Delete Access Center Policy
        
        @param request: DeleteIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integration_policy(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteIntegrationPolicyRequest,
    ) -> cms_20240330_models.DeleteIntegrationPolicyResponse:
        """
        @summary Delete Access Center Policy
        
        @param request: DeleteIntegrationPolicyRequest
        @return: DeleteIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_integration_policy_with_options(policy_id, request, headers, runtime)

    async def delete_integration_policy_async(
        self,
        policy_id: str,
        request: cms_20240330_models.DeleteIntegrationPolicyRequest,
    ) -> cms_20240330_models.DeleteIntegrationPolicyResponse:
        """
        @summary Delete Access Center Policy
        
        @param request: DeleteIntegrationPolicyRequest
        @return: DeleteIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_integration_policy_with_options_async(policy_id, request, headers, runtime)

    def delete_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeletePrometheusInstanceResponse:
        """
        @summary Delete prom instance
        
        @description Delete a Prometheus instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrometheusInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeletePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeletePrometheusInstanceResponse:
        """
        @summary Delete prom instance
        
        @description Delete a Prometheus instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrometheusInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeletePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_instance(
        self,
        prometheus_instance_id: str,
    ) -> cms_20240330_models.DeletePrometheusInstanceResponse:
        """
        @summary Delete prom instance
        
        @description Delete a Prometheus instance.
        
        @return: DeletePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_prometheus_instance_with_options(prometheus_instance_id, headers, runtime)

    async def delete_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
    ) -> cms_20240330_models.DeletePrometheusInstanceResponse:
        """
        @summary Delete prom instance
        
        @description Delete a Prometheus instance.
        
        @return: DeletePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_prometheus_instance_with_options_async(prometheus_instance_id, headers, runtime)

    def delete_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeletePrometheusViewResponse:
        """
        @summary Delete prometheus view instance
        
        @description Delete prometheus view instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrometheusViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeletePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeletePrometheusViewResponse:
        """
        @summary Delete prometheus view instance
        
        @description Delete prometheus view instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrometheusViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeletePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_view(
        self,
        prometheus_view_id: str,
    ) -> cms_20240330_models.DeletePrometheusViewResponse:
        """
        @summary Delete prometheus view instance
        
        @description Delete prometheus view instance.
        
        @return: DeletePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_prometheus_view_with_options(prometheus_view_id, headers, runtime)

    async def delete_prometheus_view_async(
        self,
        prometheus_view_id: str,
    ) -> cms_20240330_models.DeletePrometheusViewResponse:
        """
        @summary Delete prometheus view instance
        
        @description Delete prometheus view instance.
        
        @return: DeletePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_prometheus_view_with_options_async(prometheus_view_id, headers, runtime)

    def delete_service_with_options(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteServiceResponse:
        """
        @summary Delete Service
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteServiceResponse:
        """
        @summary Delete Service
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        workspace: str,
        service_id: str,
    ) -> cms_20240330_models.DeleteServiceResponse:
        """
        @summary Delete Service
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(workspace, service_id, headers, runtime)

    async def delete_service_async(
        self,
        workspace: str,
        service_id: str,
    ) -> cms_20240330_models.DeleteServiceResponse:
        """
        @summary Delete Service
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(workspace, service_id, headers, runtime)

    def delete_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary Delete Umodel configuration information
        
        @description Delete the Umodel under the specified workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary Delete Umodel configuration information
        
        @description Delete the Umodel under the specified workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel(
        self,
        workspace: str,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary Delete Umodel configuration information
        
        @description Delete the Umodel under the specified workspace
        
        @return: DeleteUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_umodel_with_options(workspace, headers, runtime)

    async def delete_umodel_async(
        self,
        workspace: str,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary Delete Umodel configuration information
        
        @description Delete the Umodel under the specified workspace
        
        @return: DeleteUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_with_options_async(workspace, headers, runtime)

    def delete_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelCommonSchemaRefResponse:
        """
        @summary 删除Umodel配置信息
        
        @param request: DeleteUmodelCommonSchemaRefRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelCommonSchemaRefResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelCommonSchemaRefResponse:
        """
        @summary 删除Umodel配置信息
        
        @param request: DeleteUmodelCommonSchemaRefRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelCommonSchemaRefResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel_common_schema_ref(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelCommonSchemaRefRequest,
    ) -> cms_20240330_models.DeleteUmodelCommonSchemaRefResponse:
        """
        @summary 删除Umodel配置信息
        
        @param request: DeleteUmodelCommonSchemaRefRequest
        @return: DeleteUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_umodel_common_schema_ref_with_options(workspace, request, headers, runtime)

    async def delete_umodel_common_schema_ref_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelCommonSchemaRefRequest,
    ) -> cms_20240330_models.DeleteUmodelCommonSchemaRefResponse:
        """
        @summary 删除Umodel配置信息
        
        @param request: DeleteUmodelCommonSchemaRefRequest
        @return: DeleteUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_common_schema_ref_with_options_async(workspace, request, headers, runtime)

    def delete_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary Delete Umodel Elements
        
        @description Delete the Umodel Data under a specified workspace
        
        @param request: DeleteUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary Delete Umodel Elements
        
        @description Delete the Umodel Data under a specified workspace
        
        @param request: DeleteUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary Delete Umodel Elements
        
        @description Delete the Umodel Data under a specified workspace
        
        @param request: DeleteUmodelDataRequest
        @return: DeleteUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_umodel_data_with_options(workspace, request, headers, runtime)

    async def delete_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary Delete Umodel Elements
        
        @description Delete the Umodel Data under a specified workspace
        
        @param request: DeleteUmodelDataRequest
        @return: DeleteUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_data_with_options_async(workspace, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary Delete Workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary Delete Workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary Delete Workspace
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_name, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary Delete Workspace
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_name, headers, runtime)

    def describe_regions_with_options(
        self,
        request: cms_20240330_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cms_20240330_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cms_20240330_models.DescribeRegionsRequest,
    ) -> cms_20240330_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: cms_20240330_models.DescribeRegionsRequest,
    ) -> cms_20240330_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def get_addon_with_options(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonResponse:
        """
        @summary 插件详情(Addon)
        
        @param request: GetAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddon',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_with_options_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonResponse:
        """
        @summary 插件详情(Addon)
        
        @param request: GetAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddon',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonRequest,
    ) -> cms_20240330_models.GetAddonResponse:
        """
        @summary 插件详情(Addon)
        
        @param request: GetAddonRequest
        @return: GetAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_addon_with_options(addon_name, request, headers, runtime)

    async def get_addon_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonRequest,
    ) -> cms_20240330_models.GetAddonResponse:
        """
        @summary 插件详情(Addon)
        
        @param request: GetAddonRequest
        @return: GetAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_addon_with_options_async(addon_name, request, headers, runtime)

    def get_addon_code_template_with_options(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonCodeTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonCodeTemplateResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonCodeTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonCodeTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_type):
            query['environmentType'] = request.environment_type
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddonCodeTemplate',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}/alert-code-template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonCodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_code_template_with_options_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonCodeTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonCodeTemplateResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonCodeTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonCodeTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_type):
            query['environmentType'] = request.environment_type
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddonCodeTemplate',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}/alert-code-template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonCodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_code_template(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonCodeTemplateRequest,
    ) -> cms_20240330_models.GetAddonCodeTemplateResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonCodeTemplateRequest
        @return: GetAddonCodeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_addon_code_template_with_options(addon_name, request, headers, runtime)

    async def get_addon_code_template_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonCodeTemplateRequest,
    ) -> cms_20240330_models.GetAddonCodeTemplateResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonCodeTemplateRequest
        @return: GetAddonCodeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_addon_code_template_with_options_async(addon_name, request, headers, runtime)

    def get_addon_release_with_options(
        self,
        release_name: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonReleaseResponse:
        """
        @summary Check addon release (view connection status)
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonReleaseResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases/{OpenApiUtilClient.get_encode_param(release_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_release_with_options_async(
        self,
        release_name: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonReleaseResponse:
        """
        @summary Check addon release (view connection status)
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonReleaseResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases/{OpenApiUtilClient.get_encode_param(release_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_release(
        self,
        release_name: str,
        policy_id: str,
    ) -> cms_20240330_models.GetAddonReleaseResponse:
        """
        @summary Check addon release (view connection status)
        
        @return: GetAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_addon_release_with_options(release_name, policy_id, headers, runtime)

    async def get_addon_release_async(
        self,
        release_name: str,
        policy_id: str,
    ) -> cms_20240330_models.GetAddonReleaseResponse:
        """
        @summary Check addon release (view connection status)
        
        @return: GetAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_addon_release_with_options_async(release_name, policy_id, headers, runtime)

    def get_addon_schema_with_options(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonSchemaResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonSchemaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonSchemaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_type):
            query['environmentType'] = request.environment_type
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddonSchema',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_schema_with_options_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonSchemaResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonSchemaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonSchemaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_type):
            query['environmentType'] = request.environment_type
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddonSchema',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAddonSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon_schema(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonSchemaRequest,
    ) -> cms_20240330_models.GetAddonSchemaResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonSchemaRequest
        @return: GetAddonSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_addon_schema_with_options(addon_name, request, headers, runtime)

    async def get_addon_schema_async(
        self,
        addon_name: str,
        request: cms_20240330_models.GetAddonSchemaRequest,
    ) -> cms_20240330_models.GetAddonSchemaResponse:
        """
        @summary 插件schema详情(Addon)
        
        @param request: GetAddonSchemaRequest
        @return: GetAddonSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_addon_schema_with_options_async(addon_name, request, headers, runtime)

    def get_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAggTaskGroupResponse:
        """
        @summary Describes the aggregation task group
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggTaskGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAggTaskGroupResponse:
        """
        @summary Describes the aggregation task group
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAggTaskGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
    ) -> cms_20240330_models.GetAggTaskGroupResponse:
        """
        @summary Describes the aggregation task group
        
        @return: GetAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agg_task_group_with_options(instance_id, group_id, headers, runtime)

    async def get_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
    ) -> cms_20240330_models.GetAggTaskGroupResponse:
        """
        @summary Describes the aggregation task group
        
        @return: GetAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def get_biz_trace_with_options(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetBizTraceResponse:
        """
        @summary 查询业务链路
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetBizTraceResponse:
        """
        @summary 查询业务链路
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_trace(
        self,
        biz_trace_id: str,
    ) -> cms_20240330_models.GetBizTraceResponse:
        """
        @summary 查询业务链路
        
        @return: GetBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_biz_trace_with_options(biz_trace_id, headers, runtime)

    async def get_biz_trace_async(
        self,
        biz_trace_id: str,
    ) -> cms_20240330_models.GetBizTraceResponse:
        """
        @summary 查询业务链路
        
        @return: GetBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_biz_trace_with_options_async(biz_trace_id, headers, runtime)

    def get_cloud_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCloudResourceResponse:
        """
        @summary 查询云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCloudResourceResponse:
        """
        @summary 查询云资源中心
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCloudResource',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource(self) -> cms_20240330_models.GetCloudResourceResponse:
        """
        @summary 查询云资源中心
        
        @return: GetCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cloud_resource_with_options(headers, runtime)

    async def get_cloud_resource_async(self) -> cms_20240330_models.GetCloudResourceResponse:
        """
        @summary 查询云资源中心
        
        @return: GetCloudResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cloud_resource_with_options_async(headers, runtime)

    def get_cloud_resource_data_with_options(
        self,
        request: cms_20240330_models.GetCloudResourceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCloudResourceDataResponse:
        """
        @summary 查询云资源中心数据
        
        @param request: GetCloudResourceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudResourceDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResourceData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource/data',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCloudResourceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_data_with_options_async(
        self,
        request: cms_20240330_models.GetCloudResourceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCloudResourceDataResponse:
        """
        @summary 查询云资源中心数据
        
        @param request: GetCloudResourceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudResourceDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResourceData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cloudresource/data',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCloudResourceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource_data(
        self,
        request: cms_20240330_models.GetCloudResourceDataRequest,
    ) -> cms_20240330_models.GetCloudResourceDataResponse:
        """
        @summary 查询云资源中心数据
        
        @param request: GetCloudResourceDataRequest
        @return: GetCloudResourceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cloud_resource_data_with_options(request, headers, runtime)

    async def get_cloud_resource_data_async(
        self,
        request: cms_20240330_models.GetCloudResourceDataRequest,
    ) -> cms_20240330_models.GetCloudResourceDataResponse:
        """
        @summary 查询云资源中心数据
        
        @param request: GetCloudResourceDataRequest
        @return: GetCloudResourceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cloud_resource_data_with_options_async(request, headers, runtime)

    def get_cms_service_with_options(
        self,
        request: cms_20240330_models.GetCmsServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCmsServiceResponse:
        """
        @summary 获取云监控开通状态
        
        @param request: GetCmsServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCmsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.service):
            query['service'] = request.service
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCmsService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cmsservice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cms_service_with_options_async(
        self,
        request: cms_20240330_models.GetCmsServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetCmsServiceResponse:
        """
        @summary 获取云监控开通状态
        
        @param request: GetCmsServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCmsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.service):
            query['service'] = request.service
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCmsService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/cmsservice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetCmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cms_service(
        self,
        request: cms_20240330_models.GetCmsServiceRequest,
    ) -> cms_20240330_models.GetCmsServiceResponse:
        """
        @summary 获取云监控开通状态
        
        @param request: GetCmsServiceRequest
        @return: GetCmsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cms_service_with_options(request, headers, runtime)

    async def get_cms_service_async(
        self,
        request: cms_20240330_models.GetCmsServiceRequest,
    ) -> cms_20240330_models.GetCmsServiceResponse:
        """
        @summary 获取云监控开通状态
        
        @param request: GetCmsServiceRequest
        @return: GetCmsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cms_service_with_options_async(request, headers, runtime)

    def get_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary Get EntityStore related storage information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary Get EntityStore related storage information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary Get EntityStore related storage information
        
        @return: GetEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_entity_store_with_options(workspace_name, headers, runtime)

    async def get_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary Get EntityStore related storage information
        
        @return: GetEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_entity_store_with_options_async(workspace_name, headers, runtime)

    def get_entity_store_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
        headers: cms_20240330_models.GetEntityStoreDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary Query the entity and relationship data under a specified Workspace, returning the entity data within a certain time range (the returned result is transmitted after compression).
        
        @param request: GetEntityStoreDataRequest
        @param headers: GetEntityStoreDataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['acceptEncoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEntityStoreData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/entitiesAndRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
        headers: cms_20240330_models.GetEntityStoreDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary Query the entity and relationship data under a specified Workspace, returning the entity data within a certain time range (the returned result is transmitted after compression).
        
        @param request: GetEntityStoreDataRequest
        @param headers: GetEntityStoreDataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['acceptEncoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEntityStoreData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/entitiesAndRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store_data(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary Query the entity and relationship data under a specified Workspace, returning the entity data within a certain time range (the returned result is transmitted after compression).
        
        @param request: GetEntityStoreDataRequest
        @return: GetEntityStoreDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cms_20240330_models.GetEntityStoreDataHeaders()
        return self.get_entity_store_data_with_options(workspace, request, headers, runtime)

    async def get_entity_store_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary Query the entity and relationship data under a specified Workspace, returning the entity data within a certain time range (the returned result is transmitted after compression).
        
        @param request: GetEntityStoreDataRequest
        @return: GetEntityStoreDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cms_20240330_models.GetEntityStoreDataHeaders()
        return await self.get_entity_store_data_with_options_async(workspace, request, headers, runtime)

    def get_integration_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetIntegrationPolicyResponse:
        """
        @summary Query the list of access center policies
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetIntegrationPolicyResponse:
        """
        @summary Query the list of access center policies
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_policy(
        self,
        policy_id: str,
    ) -> cms_20240330_models.GetIntegrationPolicyResponse:
        """
        @summary Query the list of access center policies
        
        @return: GetIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_integration_policy_with_options(policy_id, headers, runtime)

    async def get_integration_policy_async(
        self,
        policy_id: str,
    ) -> cms_20240330_models.GetIntegrationPolicyResponse:
        """
        @summary Query the list of access center policies
        
        @return: GetIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_integration_policy_with_options_async(policy_id, headers, runtime)

    def get_integration_version_for_cswith_options(
        self,
        request: cms_20240330_models.GetIntegrationVersionForCSRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetIntegrationVersionForCSResponse:
        """
        @summary 查询接入中心在CS的版本
        
        @param request: GetIntegrationVersionForCSRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationVersionForCSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationVersionForCS',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-version/cs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetIntegrationVersionForCSResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_version_for_cswith_options_async(
        self,
        request: cms_20240330_models.GetIntegrationVersionForCSRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetIntegrationVersionForCSResponse:
        """
        @summary 查询接入中心在CS的版本
        
        @param request: GetIntegrationVersionForCSRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationVersionForCSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationVersionForCS',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-version/cs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetIntegrationVersionForCSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_version_for_cs(
        self,
        request: cms_20240330_models.GetIntegrationVersionForCSRequest,
    ) -> cms_20240330_models.GetIntegrationVersionForCSResponse:
        """
        @summary 查询接入中心在CS的版本
        
        @param request: GetIntegrationVersionForCSRequest
        @return: GetIntegrationVersionForCSResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_integration_version_for_cswith_options(request, headers, runtime)

    async def get_integration_version_for_cs_async(
        self,
        request: cms_20240330_models.GetIntegrationVersionForCSRequest,
    ) -> cms_20240330_models.GetIntegrationVersionForCSResponse:
        """
        @summary 查询接入中心在CS的版本
        
        @param request: GetIntegrationVersionForCSRequest
        @return: GetIntegrationVersionForCSResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_integration_version_for_cswith_options_async(request, headers, runtime)

    def get_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.GetPrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusInstanceResponse:
        """
        @summary Query the instance in a specified environment
        
        @description Retrieve details of a Prometheus instance.
        
        @param request: GetPrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.GetPrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusInstanceResponse:
        """
        @summary Query the instance in a specified environment
        
        @description Retrieve details of a Prometheus instance.
        
        @param request: GetPrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_instance(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.GetPrometheusInstanceRequest,
    ) -> cms_20240330_models.GetPrometheusInstanceResponse:
        """
        @summary Query the instance in a specified environment
        
        @description Retrieve details of a Prometheus instance.
        
        @param request: GetPrometheusInstanceRequest
        @return: GetPrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_prometheus_instance_with_options(prometheus_instance_id, request, headers, runtime)

    async def get_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.GetPrometheusInstanceRequest,
    ) -> cms_20240330_models.GetPrometheusInstanceResponse:
        """
        @summary Query the instance in a specified environment
        
        @description Retrieve details of a Prometheus instance.
        
        @param request: GetPrometheusInstanceRequest
        @return: GetPrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def get_prometheus_user_setting_with_options(
        self,
        request: cms_20240330_models.GetPrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusUserSettingResponse:
        """
        @summary 查询指定环境实例
        
        @param request: GetPrometheusUserSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusUserSetting',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-user-setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_user_setting_with_options_async(
        self,
        request: cms_20240330_models.GetPrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusUserSettingResponse:
        """
        @summary 查询指定环境实例
        
        @param request: GetPrometheusUserSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusUserSetting',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-user-setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_user_setting(
        self,
        request: cms_20240330_models.GetPrometheusUserSettingRequest,
    ) -> cms_20240330_models.GetPrometheusUserSettingResponse:
        """
        @summary 查询指定环境实例
        
        @param request: GetPrometheusUserSettingRequest
        @return: GetPrometheusUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_prometheus_user_setting_with_options(request, headers, runtime)

    async def get_prometheus_user_setting_async(
        self,
        request: cms_20240330_models.GetPrometheusUserSettingRequest,
    ) -> cms_20240330_models.GetPrometheusUserSettingResponse:
        """
        @summary 查询指定环境实例
        
        @param request: GetPrometheusUserSettingRequest
        @return: GetPrometheusUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_prometheus_user_setting_with_options_async(request, headers, runtime)

    def get_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.GetPrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusViewResponse:
        """
        @summary Query a specified Prometheus view instance
        
        @description Query a specified Prometheus view instance.
        
        @param request: GetPrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.GetPrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusViewResponse:
        """
        @summary Query a specified Prometheus view instance
        
        @description Query a specified Prometheus view instance.
        
        @param request: GetPrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetPrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_view(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.GetPrometheusViewRequest,
    ) -> cms_20240330_models.GetPrometheusViewResponse:
        """
        @summary Query a specified Prometheus view instance
        
        @description Query a specified Prometheus view instance.
        
        @param request: GetPrometheusViewRequest
        @return: GetPrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_prometheus_view_with_options(prometheus_view_id, request, headers, runtime)

    async def get_prometheus_view_async(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.GetPrometheusViewRequest,
    ) -> cms_20240330_models.GetPrometheusViewResponse:
        """
        @summary Query a specified Prometheus view instance
        
        @description Query a specified Prometheus view instance.
        
        @param request: GetPrometheusViewRequest
        @return: GetPrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_prometheus_view_with_options_async(prometheus_view_id, request, headers, runtime)

    def get_service_with_options(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceResponse:
        """
        @summary Query Service
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceResponse:
        """
        @summary Query Service
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        workspace: str,
        service_id: str,
    ) -> cms_20240330_models.GetServiceResponse:
        """
        @summary Query Service
        
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(workspace, service_id, headers, runtime)

    async def get_service_async(
        self,
        workspace: str,
        service_id: str,
    ) -> cms_20240330_models.GetServiceResponse:
        """
        @summary Query Service
        
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(workspace, service_id, headers, runtime)

    def get_service_observability_with_options(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary Get Application Observability Instance
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceObservabilityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceObservability',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service-observability/{OpenApiUtilClient.get_encode_param(type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceObservabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_observability_with_options_async(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary Get Application Observability Instance
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceObservabilityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceObservability',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service-observability/{OpenApiUtilClient.get_encode_param(type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceObservabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_observability(
        self,
        workspace: str,
        type: str,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary Get Application Observability Instance
        
        @return: GetServiceObservabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_observability_with_options(workspace, type, headers, runtime)

    async def get_service_observability_async(
        self,
        workspace: str,
        type: str,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary Get Application Observability Instance
        
        @return: GetServiceObservabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_observability_with_options_async(workspace, type, headers, runtime)

    def get_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary Get Umodel configuration information
        
        @description Get Umodel configuration information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary Get Umodel configuration information
        
        @description Get Umodel configuration information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary Get Umodel configuration information
        
        @description Get Umodel configuration information
        
        @return: GetUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_umodel_with_options(workspace, headers, runtime)

    async def get_umodel_async(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary Get Umodel configuration information
        
        @description Get Umodel configuration information
        
        @return: GetUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_with_options_async(workspace, headers, runtime)

    def get_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelCommonSchemaRefResponse:
        """
        @summary 获取Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelCommonSchemaRefResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelCommonSchemaRefResponse:
        """
        @summary 获取Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelCommonSchemaRefResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel_common_schema_ref(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelCommonSchemaRefResponse:
        """
        @summary 获取Umodel配置信息
        
        @return: GetUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_umodel_common_schema_ref_with_options(workspace, headers, runtime)

    async def get_umodel_common_schema_ref_async(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelCommonSchemaRefResponse:
        """
        @summary 获取Umodel配置信息
        
        @return: GetUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_common_schema_ref_with_options_async(workspace, headers, runtime)

    def get_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary Retrieve associated Umodel graph data
        
        @description Find Umodel
        
        @param request: GetUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/graph',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary Retrieve associated Umodel graph data
        
        @description Find Umodel
        
        @param request: GetUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/graph',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary Retrieve associated Umodel graph data
        
        @description Find Umodel
        
        @param request: GetUmodelDataRequest
        @return: GetUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_umodel_data_with_options(workspace, request, headers, runtime)

    async def get_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary Retrieve associated Umodel graph data
        
        @description Find Umodel
        
        @param request: GetUmodelDataRequest
        @return: GetUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_data_with_options_async(workspace, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary Get Workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary Get Workspace
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary Get Workspace
        
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_name, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary Get Workspace
        
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_name, headers, runtime)

    def list_addon_releases_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListAddonReleasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAddonReleasesResponse:
        """
        @summary List of addon releases
        
        @description Query the list of access configurations
        
        @param request: ListAddonReleasesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonReleasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.parent_addon_release_id):
            query['parentAddonReleaseId'] = request.parent_addon_release_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonReleases',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAddonReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_releases_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListAddonReleasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAddonReleasesResponse:
        """
        @summary List of addon releases
        
        @description Query the list of access configurations
        
        @param request: ListAddonReleasesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonReleasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.parent_addon_release_id):
            query['parentAddonReleaseId'] = request.parent_addon_release_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonReleases',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAddonReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_releases(
        self,
        policy_id: str,
        request: cms_20240330_models.ListAddonReleasesRequest,
    ) -> cms_20240330_models.ListAddonReleasesResponse:
        """
        @summary List of addon releases
        
        @description Query the list of access configurations
        
        @param request: ListAddonReleasesRequest
        @return: ListAddonReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_addon_releases_with_options(policy_id, request, headers, runtime)

    async def list_addon_releases_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListAddonReleasesRequest,
    ) -> cms_20240330_models.ListAddonReleasesResponse:
        """
        @summary List of addon releases
        
        @description Query the list of access configurations
        
        @param request: ListAddonReleasesRequest
        @return: ListAddonReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_addon_releases_with_options_async(policy_id, request, headers, runtime)

    def list_addons_with_options(
        self,
        request: cms_20240330_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAddonsResponse:
        """
        @summary 新版接入中心产品列表(分组)
        
        @param request: ListAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.regexp):
            query['regexp'] = request.regexp
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: cms_20240330_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAddonsResponse:
        """
        @summary 新版接入中心产品列表(分组)
        
        @param request: ListAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.regexp):
            query['regexp'] = request.regexp
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: cms_20240330_models.ListAddonsRequest,
    ) -> cms_20240330_models.ListAddonsResponse:
        """
        @summary 新版接入中心产品列表(分组)
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    async def list_addons_async(
        self,
        request: cms_20240330_models.ListAddonsRequest,
    ) -> cms_20240330_models.ListAddonsResponse:
        """
        @summary 新版接入中心产品列表(分组)
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_addons_with_options_async(request, headers, runtime)

    def list_agg_task_groups_with_options(
        self,
        instance_id: str,
        tmp_req: cms_20240330_models.ListAggTaskGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAggTaskGroupsResponse:
        """
        @summary List Aggregation Task Groups
        
        @param tmp_req: ListAggTaskGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggTaskGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAggTaskGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_agg_task_group_ids):
            query['filterAggTaskGroupIds'] = request.filter_agg_task_group_ids
        if not UtilClient.is_unset(request.filter_agg_task_group_names):
            query['filterAggTaskGroupNames'] = request.filter_agg_task_group_names
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_prometheus_id):
            query['targetPrometheusId'] = request.target_prometheus_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggTaskGroups',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAggTaskGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agg_task_groups_with_options_async(
        self,
        instance_id: str,
        tmp_req: cms_20240330_models.ListAggTaskGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAggTaskGroupsResponse:
        """
        @summary List Aggregation Task Groups
        
        @param tmp_req: ListAggTaskGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAggTaskGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAggTaskGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_agg_task_group_ids):
            query['filterAggTaskGroupIds'] = request.filter_agg_task_group_ids
        if not UtilClient.is_unset(request.filter_agg_task_group_names):
            query['filterAggTaskGroupNames'] = request.filter_agg_task_group_names
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_prometheus_id):
            query['targetPrometheusId'] = request.target_prometheus_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggTaskGroups',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAggTaskGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agg_task_groups(
        self,
        instance_id: str,
        request: cms_20240330_models.ListAggTaskGroupsRequest,
    ) -> cms_20240330_models.ListAggTaskGroupsResponse:
        """
        @summary List Aggregation Task Groups
        
        @param request: ListAggTaskGroupsRequest
        @return: ListAggTaskGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agg_task_groups_with_options(instance_id, request, headers, runtime)

    async def list_agg_task_groups_async(
        self,
        instance_id: str,
        request: cms_20240330_models.ListAggTaskGroupsRequest,
    ) -> cms_20240330_models.ListAggTaskGroupsResponse:
        """
        @summary List Aggregation Task Groups
        
        @param request: ListAggTaskGroupsRequest
        @return: ListAggTaskGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agg_task_groups_with_options_async(instance_id, request, headers, runtime)

    def list_alert_actions_with_options(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary Query Alert Actions
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_actions_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary Query Alert Actions
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_actions(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary Query Alert Actions
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alert_actions_with_options(request, headers, runtime)

    async def list_alert_actions_async(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary Query Alert Actions
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alert_actions_with_options_async(request, headers, runtime)

    def list_biz_traces_with_options(
        self,
        request: cms_20240330_models.ListBizTracesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListBizTracesResponse:
        """
        @summary 业务链路列表
        
        @param request: ListBizTracesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizTraces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTraces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListBizTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_traces_with_options_async(
        self,
        request: cms_20240330_models.ListBizTracesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListBizTracesResponse:
        """
        @summary 业务链路列表
        
        @param request: ListBizTracesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizTraces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTraces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListBizTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_traces(
        self,
        request: cms_20240330_models.ListBizTracesRequest,
    ) -> cms_20240330_models.ListBizTracesResponse:
        """
        @summary 业务链路列表
        
        @param request: ListBizTracesRequest
        @return: ListBizTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_biz_traces_with_options(request, headers, runtime)

    async def list_biz_traces_async(
        self,
        request: cms_20240330_models.ListBizTracesRequest,
    ) -> cms_20240330_models.ListBizTracesResponse:
        """
        @summary 业务链路列表
        
        @param request: ListBizTracesRequest
        @return: ListBizTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_biz_traces_with_options_async(request, headers, runtime)

    def list_integration_policies_with_options(
        self,
        tmp_req: cms_20240330_models.ListIntegrationPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPoliciesResponse:
        """
        @summary Query Access Center Policy List Information
        
        @description Query integration list
        
        @param tmp_req: ListIntegrationPoliciesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPoliciesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListIntegrationPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.bind_resource_id):
            query['bindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.entity_group_ids):
            query['entityGroupIds'] = request.entity_group_ids
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            query['policyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['policyType'] = request.policy_type
        if not UtilClient.is_unset(request.prometheus_instance_id):
            query['prometheusInstanceId'] = request.prometheus_instance_id
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicies',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policies_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListIntegrationPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPoliciesResponse:
        """
        @summary Query Access Center Policy List Information
        
        @description Query integration list
        
        @param tmp_req: ListIntegrationPoliciesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPoliciesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListIntegrationPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.bind_resource_id):
            query['bindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.entity_group_ids):
            query['entityGroupIds'] = request.entity_group_ids
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            query['policyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['policyType'] = request.policy_type
        if not UtilClient.is_unset(request.prometheus_instance_id):
            query['prometheusInstanceId'] = request.prometheus_instance_id
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicies',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policies(
        self,
        request: cms_20240330_models.ListIntegrationPoliciesRequest,
    ) -> cms_20240330_models.ListIntegrationPoliciesResponse:
        """
        @summary Query Access Center Policy List Information
        
        @description Query integration list
        
        @param request: ListIntegrationPoliciesRequest
        @return: ListIntegrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policies_with_options(request, headers, runtime)

    async def list_integration_policies_async(
        self,
        request: cms_20240330_models.ListIntegrationPoliciesRequest,
    ) -> cms_20240330_models.ListIntegrationPoliciesResponse:
        """
        @summary Query Access Center Policy List Information
        
        @description Query integration list
        
        @param request: ListIntegrationPoliciesRequest
        @return: ListIntegrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policies_with_options_async(request, headers, runtime)

    def list_integration_policy_addons_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyAddonsResponse:
        """
        @summary 策略addon列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyAddonsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyAddons',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_addons_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyAddonsResponse:
        """
        @summary 策略addon列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyAddonsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyAddons',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_addons(
        self,
        policy_id: str,
    ) -> cms_20240330_models.ListIntegrationPolicyAddonsResponse:
        """
        @summary 策略addon列表
        
        @return: ListIntegrationPolicyAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_addons_with_options(policy_id, headers, runtime)

    async def list_integration_policy_addons_async(
        self,
        policy_id: str,
    ) -> cms_20240330_models.ListIntegrationPolicyAddonsResponse:
        """
        @summary 策略addon列表
        
        @return: ListIntegrationPolicyAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_addons_with_options_async(policy_id, headers, runtime)

    def list_integration_policy_collectors_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCollectorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyCollectorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyCollectorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyCollectorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.collector_type):
            query['collectorType'] = request.collector_type
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyCollectors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/collectors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyCollectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_collectors_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCollectorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyCollectorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyCollectorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyCollectorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.collector_type):
            query['collectorType'] = request.collector_type
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyCollectors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/collectors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyCollectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_collectors(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCollectorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyCollectorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyCollectorsRequest
        @return: ListIntegrationPolicyCollectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_collectors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_collectors_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCollectorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyCollectorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyCollectorsRequest
        @return: ListIntegrationPolicyCollectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_collectors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_custom_scrape_job_rules_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        """
        @summary Get storage requirement information for the access center policy
        
        @param request: ListIntegrationPolicyCustomScrapeJobRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyCustomScrapeJobRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyCustomScrapeJobRules',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/custom-scrape-job-rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_custom_scrape_job_rules_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        """
        @summary Get storage requirement information for the access center policy
        
        @param request: ListIntegrationPolicyCustomScrapeJobRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyCustomScrapeJobRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyCustomScrapeJobRules',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/custom-scrape-job-rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_custom_scrape_job_rules(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        """
        @summary Get storage requirement information for the access center policy
        
        @param request: ListIntegrationPolicyCustomScrapeJobRulesRequest
        @return: ListIntegrationPolicyCustomScrapeJobRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_custom_scrape_job_rules_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_custom_scrape_job_rules_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        """
        @summary Get storage requirement information for the access center policy
        
        @param request: ListIntegrationPolicyCustomScrapeJobRulesRequest
        @return: ListIntegrationPolicyCustomScrapeJobRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_custom_scrape_job_rules_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_dashboards_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyDashboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyDashboardsResponse:
        """
        @summary Policy Dashboard List
        
        @description This article provides an example of querying the alarm template list. The result shows that there are 2 alarm templates in the list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyDashboards',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_dashboards_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyDashboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyDashboardsResponse:
        """
        @summary Policy Dashboard List
        
        @description This article provides an example of querying the alarm template list. The result shows that there are 2 alarm templates in the list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyDashboards',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_dashboards(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyDashboardsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyDashboardsResponse:
        """
        @summary Policy Dashboard List
        
        @description This article provides an example of querying the alarm template list. The result shows that there are 2 alarm templates in the list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @return: ListIntegrationPolicyDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_dashboards_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_dashboards_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyDashboardsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyDashboardsResponse:
        """
        @summary Policy Dashboard List
        
        @description This article provides an example of querying the alarm template list. The result shows that there are 2 alarm templates in the list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @return: ListIntegrationPolicyDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_dashboards_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_pod_monitors_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyPodMonitorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse:
        """
        @summary Get PodMonitor Resources of Access Center Policy
        
        @description This article provides an example to query the alarm template list. The result shows that there are 2 alarm templates in the alarm template list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyPodMonitorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyPodMonitorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyPodMonitors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/pod-monitors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_pod_monitors_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyPodMonitorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse:
        """
        @summary Get PodMonitor Resources of Access Center Policy
        
        @description This article provides an example to query the alarm template list. The result shows that there are 2 alarm templates in the alarm template list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyPodMonitorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyPodMonitorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyPodMonitors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/pod-monitors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_pod_monitors(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyPodMonitorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse:
        """
        @summary Get PodMonitor Resources of Access Center Policy
        
        @description This article provides an example to query the alarm template list. The result shows that there are 2 alarm templates in the alarm template list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyPodMonitorsRequest
        @return: ListIntegrationPolicyPodMonitorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_pod_monitors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_pod_monitors_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyPodMonitorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyPodMonitorsResponse:
        """
        @summary Get PodMonitor Resources of Access Center Policy
        
        @description This article provides an example to query the alarm template list. The result shows that there are 2 alarm templates in the alarm template list, which are `ECS_Template1` and `ECS_Template2`.
        
        @param request: ListIntegrationPolicyPodMonitorsRequest
        @return: ListIntegrationPolicyPodMonitorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_pod_monitors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_service_monitors_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyServiceMonitorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyServiceMonitorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyServiceMonitorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyServiceMonitors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/service-monitors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_service_monitors_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyServiceMonitorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyServiceMonitorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyServiceMonitorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['encryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyServiceMonitors',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/service-monitors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_service_monitors(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyServiceMonitorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyServiceMonitorsRequest
        @return: ListIntegrationPolicyServiceMonitorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_service_monitors_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_service_monitors_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyServiceMonitorsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyServiceMonitorsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
        @param request: ListIntegrationPolicyServiceMonitorsRequest
        @return: ListIntegrationPolicyServiceMonitorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_service_monitors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_storage_requirements_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyStorageRequirementsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse:
        """
        @summary Get Storage Requirements Information for Access Center Policy
        
        @description During the effective period of the policy, all alarms within the application group will no longer send notifications.
        
        This article provides an example of creating a pause alarm notification policy `PauseNotify` for the application group `7301***`. This application group will pause alarms from `1622949300000` to `1623208500000` (Beijing Time `2021-06-06 11:15:00` to `2021-06-09 11:15:00`).
        
        @param request: ListIntegrationPolicyStorageRequirementsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyStorageRequirementsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.storage_type):
            query['storageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyStorageRequirements',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/storage-requirements',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_policy_storage_requirements_with_options_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyStorageRequirementsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse:
        """
        @summary Get Storage Requirements Information for Access Center Policy
        
        @description During the effective period of the policy, all alarms within the application group will no longer send notifications.
        
        This article provides an example of creating a pause alarm notification policy `PauseNotify` for the application group `7301***`. This application group will pause alarms from `1622949300000` to `1623208500000` (Beijing Time `2021-06-06 11:15:00` to `2021-06-09 11:15:00`).
        
        @param request: ListIntegrationPolicyStorageRequirementsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyStorageRequirementsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_release_name):
            query['addonReleaseName'] = request.addon_release_name
        if not UtilClient.is_unset(request.storage_type):
            query['storageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegrationPolicyStorageRequirements',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/storage-requirements',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_policy_storage_requirements(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyStorageRequirementsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse:
        """
        @summary Get Storage Requirements Information for Access Center Policy
        
        @description During the effective period of the policy, all alarms within the application group will no longer send notifications.
        
        This article provides an example of creating a pause alarm notification policy `PauseNotify` for the application group `7301***`. This application group will pause alarms from `1622949300000` to `1623208500000` (Beijing Time `2021-06-06 11:15:00` to `2021-06-09 11:15:00`).
        
        @param request: ListIntegrationPolicyStorageRequirementsRequest
        @return: ListIntegrationPolicyStorageRequirementsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_policy_storage_requirements_with_options(policy_id, request, headers, runtime)

    async def list_integration_policy_storage_requirements_async(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyStorageRequirementsRequest,
    ) -> cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse:
        """
        @summary Get Storage Requirements Information for Access Center Policy
        
        @description During the effective period of the policy, all alarms within the application group will no longer send notifications.
        
        This article provides an example of creating a pause alarm notification policy `PauseNotify` for the application group `7301***`. This application group will pause alarms from `1622949300000` to `1623208500000` (Beijing Time `2021-06-06 11:15:00` to `2021-06-09 11:15:00`).
        
        @param request: ListIntegrationPolicyStorageRequirementsRequest
        @return: ListIntegrationPolicyStorageRequirementsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_storage_requirements_with_options_async(policy_id, request, headers, runtime)

    def list_prometheus_dashboards_with_options(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.ListPrometheusDashboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusDashboardsResponse:
        """
        @summary Get Prometheus Instance Dashboard List
        
        @description Get the list of Prometheus instance dashboards.
        
        @param request: ListPrometheusDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusDashboards',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_dashboards_with_options_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.ListPrometheusDashboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusDashboardsResponse:
        """
        @summary Get Prometheus Instance Dashboard List
        
        @description Get the list of Prometheus instance dashboards.
        
        @param request: ListPrometheusDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['aliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusDashboards',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_dashboards(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.ListPrometheusDashboardsRequest,
    ) -> cms_20240330_models.ListPrometheusDashboardsResponse:
        """
        @summary Get Prometheus Instance Dashboard List
        
        @description Get the list of Prometheus instance dashboards.
        
        @param request: ListPrometheusDashboardsRequest
        @return: ListPrometheusDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_prometheus_dashboards_with_options(prometheus_instance_id, request, headers, runtime)

    async def list_prometheus_dashboards_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.ListPrometheusDashboardsRequest,
    ) -> cms_20240330_models.ListPrometheusDashboardsResponse:
        """
        @summary Get Prometheus Instance Dashboard List
        
        @description Get the list of Prometheus instance dashboards.
        
        @param request: ListPrometheusDashboardsRequest
        @return: ListPrometheusDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_prometheus_dashboards_with_options_async(prometheus_instance_id, request, headers, runtime)

    def list_prometheus_instances_with_options(
        self,
        tmp_req: cms_20240330_models.ListPrometheusInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusInstancesResponse:
        """
        @summary Get the list of Prometheus instance information
        
        @description Get the list of Prometheus instances.
        
        @param tmp_req: ListPrometheusInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListPrometheusInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prometheus_instance_ids):
            query['prometheusInstanceIds'] = request.prometheus_instance_ids
        if not UtilClient.is_unset(request.prometheus_instance_name):
            query['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstances',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instances_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListPrometheusInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusInstancesResponse:
        """
        @summary Get the list of Prometheus instance information
        
        @description Get the list of Prometheus instances.
        
        @param tmp_req: ListPrometheusInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListPrometheusInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prometheus_instance_ids):
            query['prometheusInstanceIds'] = request.prometheus_instance_ids
        if not UtilClient.is_unset(request.prometheus_instance_name):
            query['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstances',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instances(
        self,
        request: cms_20240330_models.ListPrometheusInstancesRequest,
    ) -> cms_20240330_models.ListPrometheusInstancesResponse:
        """
        @summary Get the list of Prometheus instance information
        
        @description Get the list of Prometheus instances.
        
        @param request: ListPrometheusInstancesRequest
        @return: ListPrometheusInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_prometheus_instances_with_options(request, headers, runtime)

    async def list_prometheus_instances_async(
        self,
        request: cms_20240330_models.ListPrometheusInstancesRequest,
    ) -> cms_20240330_models.ListPrometheusInstancesResponse:
        """
        @summary Get the list of Prometheus instance information
        
        @description Get the list of Prometheus instances.
        
        @param request: ListPrometheusInstancesRequest
        @return: ListPrometheusInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_prometheus_instances_with_options_async(request, headers, runtime)

    def list_prometheus_views_with_options(
        self,
        tmp_req: cms_20240330_models.ListPrometheusViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusViewsResponse:
        """
        @summary Retrieve a list of Prometheus view instance information
        
        @description Retrieve a list of Prometheus view instance information.
        
        @param tmp_req: ListPrometheusViewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusViewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListPrometheusViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prometheus_view_ids):
            query['prometheusViewIds'] = request.prometheus_view_ids
        if not UtilClient.is_unset(request.prometheus_view_name):
            query['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusViews',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_views_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListPrometheusViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusViewsResponse:
        """
        @summary Retrieve a list of Prometheus view instance information
        
        @description Retrieve a list of Prometheus view instance information.
        
        @param tmp_req: ListPrometheusViewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusViewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListPrometheusViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_region_ids):
            query['filterRegionIds'] = request.filter_region_ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prometheus_view_ids):
            query['prometheusViewIds'] = request.prometheus_view_ids
        if not UtilClient.is_unset(request.prometheus_view_name):
            query['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusViews',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_views(
        self,
        request: cms_20240330_models.ListPrometheusViewsRequest,
    ) -> cms_20240330_models.ListPrometheusViewsResponse:
        """
        @summary Retrieve a list of Prometheus view instance information
        
        @description Retrieve a list of Prometheus view instance information.
        
        @param request: ListPrometheusViewsRequest
        @return: ListPrometheusViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_prometheus_views_with_options(request, headers, runtime)

    async def list_prometheus_views_async(
        self,
        request: cms_20240330_models.ListPrometheusViewsRequest,
    ) -> cms_20240330_models.ListPrometheusViewsResponse:
        """
        @summary Retrieve a list of Prometheus view instance information
        
        @description Retrieve a list of Prometheus view instance information.
        
        @param request: ListPrometheusViewsRequest
        @return: ListPrometheusViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_prometheus_views_with_options_async(request, headers, runtime)

    def list_prometheus_virtual_instances_with_options(
        self,
        request: cms_20240330_models.ListPrometheusVirtualInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusVirtualInstancesResponse:
        """
        @summary Get Prometheus Virtual Instance
        
        @description Used for creating a site monitoring task
        
        @param request: ListPrometheusVirtualInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusVirtualInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusVirtualInstances',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/virtual-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusVirtualInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_virtual_instances_with_options_async(
        self,
        request: cms_20240330_models.ListPrometheusVirtualInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListPrometheusVirtualInstancesResponse:
        """
        @summary Get Prometheus Virtual Instance
        
        @description Used for creating a site monitoring task
        
        @param request: ListPrometheusVirtualInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrometheusVirtualInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusVirtualInstances',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/virtual-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListPrometheusVirtualInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_virtual_instances(
        self,
        request: cms_20240330_models.ListPrometheusVirtualInstancesRequest,
    ) -> cms_20240330_models.ListPrometheusVirtualInstancesResponse:
        """
        @summary Get Prometheus Virtual Instance
        
        @description Used for creating a site monitoring task
        
        @param request: ListPrometheusVirtualInstancesRequest
        @return: ListPrometheusVirtualInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_prometheus_virtual_instances_with_options(request, headers, runtime)

    async def list_prometheus_virtual_instances_async(
        self,
        request: cms_20240330_models.ListPrometheusVirtualInstancesRequest,
    ) -> cms_20240330_models.ListPrometheusVirtualInstancesResponse:
        """
        @summary Get Prometheus Virtual Instance
        
        @description Used for creating a site monitoring task
        
        @param request: ListPrometheusVirtualInstancesRequest
        @return: ListPrometheusVirtualInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_prometheus_virtual_instances_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListServicesResponse:
        """
        @summary List Resource Services
        
        @param request: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListServicesResponse:
        """
        @summary List Resource Services
        
        @param request: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        workspace: str,
        request: cms_20240330_models.ListServicesRequest,
    ) -> cms_20240330_models.ListServicesResponse:
        """
        @summary List Resource Services
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(workspace, request, headers, runtime)

    async def list_services_async(
        self,
        workspace: str,
        request: cms_20240330_models.ListServicesRequest,
    ) -> cms_20240330_models.ListServicesResponse:
        """
        @summary List Resource Services
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(workspace, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: cms_20240330_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary Get Workspace List
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not UtilClient.is_unset(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary Get Workspace List
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not UtilClient.is_unset(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: cms_20240330_models.ListWorkspacesRequest,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary Get Workspace List
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: cms_20240330_models.ListWorkspacesRequest,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary Get Workspace List
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def put_workspace_with_options(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary Create Workspace
        
        @param request: PutWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.PutWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_workspace_with_options_async(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary Create Workspace
        
        @param request: PutWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.PutWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_workspace(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary Create Workspace
        
        @param request: PutWorkspaceRequest
        @return: PutWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_workspace_with_options(workspace_name, request, headers, runtime)

    async def put_workspace_async(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary Create Workspace
        
        @param request: PutWorkspaceRequest
        @return: PutWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_workspace_with_options_async(workspace_name, request, headers, runtime)

    def update_addon_release_with_options(
        self,
        release_name: str,
        policy_id: str,
        request: cms_20240330_models.UpdateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAddonReleaseResponse:
        """
        @summary Upgrade Access Component
        
        @param request: UpdateAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addon_version):
            body['addonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases/{OpenApiUtilClient.get_encode_param(release_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_addon_release_with_options_async(
        self,
        release_name: str,
        policy_id: str,
        request: cms_20240330_models.UpdateAddonReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAddonReleaseResponse:
        """
        @summary Upgrade Access Component
        
        @param request: UpdateAddonReleaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAddonReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.addon_version):
            body['addonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entity_rules):
            body['entityRules'] = request.entity_rules
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddonRelease',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(policy_id)}/addon-releases/{OpenApiUtilClient.get_encode_param(release_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_addon_release(
        self,
        release_name: str,
        policy_id: str,
        request: cms_20240330_models.UpdateAddonReleaseRequest,
    ) -> cms_20240330_models.UpdateAddonReleaseResponse:
        """
        @summary Upgrade Access Component
        
        @param request: UpdateAddonReleaseRequest
        @return: UpdateAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_addon_release_with_options(release_name, policy_id, request, headers, runtime)

    async def update_addon_release_async(
        self,
        release_name: str,
        policy_id: str,
        request: cms_20240330_models.UpdateAddonReleaseRequest,
    ) -> cms_20240330_models.UpdateAddonReleaseResponse:
        """
        @summary Upgrade Access Component
        
        @param request: UpdateAddonReleaseRequest
        @return: UpdateAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_addon_release_with_options_async(release_name, policy_id, request, headers, runtime)

    def update_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAggTaskGroupResponse:
        """
        @summary Apply Aggregation Task Group
        
        @param request: UpdateAggTaskGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggTaskGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not UtilClient.is_unset(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not UtilClient.is_unset(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not UtilClient.is_unset(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.delay):
            body['delay'] = request.delay
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.from_time):
            body['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not UtilClient.is_unset(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not UtilClient.is_unset(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not UtilClient.is_unset(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not UtilClient.is_unset(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not UtilClient.is_unset(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAggTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agg_task_group_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAggTaskGroupResponse:
        """
        @summary Apply Aggregation Task Group
        
        @param request: UpdateAggTaskGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggTaskGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agg_task_group_config):
            body['aggTaskGroupConfig'] = request.agg_task_group_config
        if not UtilClient.is_unset(request.agg_task_group_config_type):
            body['aggTaskGroupConfigType'] = request.agg_task_group_config_type
        if not UtilClient.is_unset(request.agg_task_group_name):
            body['aggTaskGroupName'] = request.agg_task_group_name
        if not UtilClient.is_unset(request.cron_expr):
            body['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.delay):
            body['delay'] = request.delay
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.from_time):
            body['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.max_retries):
            body['maxRetries'] = request.max_retries
        if not UtilClient.is_unset(request.max_run_time_in_seconds):
            body['maxRunTimeInSeconds'] = request.max_run_time_in_seconds
        if not UtilClient.is_unset(request.precheck_string):
            body['precheckString'] = request.precheck_string
        if not UtilClient.is_unset(request.schedule_mode):
            body['scheduleMode'] = request.schedule_mode
        if not UtilClient.is_unset(request.schedule_time_expr):
            body['scheduleTimeExpr'] = request.schedule_time_expr
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.target_prometheus_id):
            body['targetPrometheusId'] = request.target_prometheus_id
        if not UtilClient.is_unset(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggTaskGroup',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAggTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agg_task_group(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupRequest,
    ) -> cms_20240330_models.UpdateAggTaskGroupResponse:
        """
        @summary Apply Aggregation Task Group
        
        @param request: UpdateAggTaskGroupRequest
        @return: UpdateAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_agg_task_group_with_options(instance_id, group_id, request, headers, runtime)

    async def update_agg_task_group_async(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupRequest,
    ) -> cms_20240330_models.UpdateAggTaskGroupResponse:
        """
        @summary Apply Aggregation Task Group
        
        @param request: UpdateAggTaskGroupRequest
        @return: UpdateAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_agg_task_group_with_options_async(instance_id, group_id, request, headers, runtime)

    def update_agg_task_group_status_with_options(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAggTaskGroupStatusResponse:
        """
        @summary Update Aggregation Task Group Status
        
        @param request: UpdateAggTaskGroupStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggTaskGroupStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggTaskGroupStatus',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAggTaskGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agg_task_group_status_with_options_async(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateAggTaskGroupStatusResponse:
        """
        @summary Update Aggregation Task Group Status
        
        @param request: UpdateAggTaskGroupStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAggTaskGroupStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAggTaskGroupStatus',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(instance_id)}/agg-task-groups/{OpenApiUtilClient.get_encode_param(group_id)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateAggTaskGroupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agg_task_group_status(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupStatusRequest,
    ) -> cms_20240330_models.UpdateAggTaskGroupStatusResponse:
        """
        @summary Update Aggregation Task Group Status
        
        @param request: UpdateAggTaskGroupStatusRequest
        @return: UpdateAggTaskGroupStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_agg_task_group_status_with_options(instance_id, group_id, request, headers, runtime)

    async def update_agg_task_group_status_async(
        self,
        instance_id: str,
        group_id: str,
        request: cms_20240330_models.UpdateAggTaskGroupStatusRequest,
    ) -> cms_20240330_models.UpdateAggTaskGroupStatusResponse:
        """
        @summary Update Aggregation Task Group Status
        
        @param request: UpdateAggTaskGroupStatusRequest
        @return: UpdateAggTaskGroupStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_agg_task_group_status_with_options_async(instance_id, group_id, request, headers, runtime)

    def update_biz_trace_with_options(
        self,
        biz_trace_id: str,
        request: cms_20240330_models.UpdateBizTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateBizTraceResponse:
        """
        @summary 修改业务链路
        
        @param request: UpdateBizTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not UtilClient.is_unset(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not UtilClient.is_unset(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateBizTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_trace_with_options_async(
        self,
        biz_trace_id: str,
        request: cms_20240330_models.UpdateBizTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateBizTraceResponse:
        """
        @summary 修改业务链路
        
        @param request: UpdateBizTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_config):
            body['advancedConfig'] = request.advanced_config
        if not UtilClient.is_unset(request.biz_trace_name):
            body['bizTraceName'] = request.biz_trace_name
        if not UtilClient.is_unset(request.rule_config):
            body['ruleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizTrace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/bizTrace/{OpenApiUtilClient.get_encode_param(biz_trace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateBizTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_trace(
        self,
        biz_trace_id: str,
        request: cms_20240330_models.UpdateBizTraceRequest,
    ) -> cms_20240330_models.UpdateBizTraceResponse:
        """
        @summary 修改业务链路
        
        @param request: UpdateBizTraceRequest
        @return: UpdateBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_biz_trace_with_options(biz_trace_id, request, headers, runtime)

    async def update_biz_trace_async(
        self,
        biz_trace_id: str,
        request: cms_20240330_models.UpdateBizTraceRequest,
    ) -> cms_20240330_models.UpdateBizTraceResponse:
        """
        @summary 修改业务链路
        
        @param request: UpdateBizTraceRequest
        @return: UpdateBizTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_biz_trace_with_options_async(biz_trace_id, request, headers, runtime)

    def update_integration_policy_with_options(
        self,
        integration_policy_id: str,
        request: cms_20240330_models.UpdateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateIntegrationPolicyResponse:
        """
        @summary Update the specified policy
        
        @param request: UpdateIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_package):
            body['feePackage'] = request.fee_package
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(integration_policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateIntegrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integration_policy_with_options_async(
        self,
        integration_policy_id: str,
        request: cms_20240330_models.UpdateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateIntegrationPolicyResponse:
        """
        @summary Update the specified policy
        
        @param request: UpdateIntegrationPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntegrationPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fee_package):
            body['feePackage'] = request.fee_package
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegrationPolicy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/integration-policies/{OpenApiUtilClient.get_encode_param(integration_policy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateIntegrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integration_policy(
        self,
        integration_policy_id: str,
        request: cms_20240330_models.UpdateIntegrationPolicyRequest,
    ) -> cms_20240330_models.UpdateIntegrationPolicyResponse:
        """
        @summary Update the specified policy
        
        @param request: UpdateIntegrationPolicyRequest
        @return: UpdateIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_integration_policy_with_options(integration_policy_id, request, headers, runtime)

    async def update_integration_policy_async(
        self,
        integration_policy_id: str,
        request: cms_20240330_models.UpdateIntegrationPolicyRequest,
    ) -> cms_20240330_models.UpdateIntegrationPolicyResponse:
        """
        @summary Update the specified policy
        
        @param request: UpdateIntegrationPolicyRequest
        @return: UpdateIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_integration_policy_with_options_async(integration_policy_id, request, headers, runtime)

    def update_notify_strategy_with_options(
        self,
        notify_strategy_id: str,
        request: cms_20240330_models.UpdateNotifyStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateNotifyStrategyResponse:
        """
        @summary 更新通知策略
        
        @param request: UpdateNotifyStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNotifyStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateNotifyStrategy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/notifyStrategies/{OpenApiUtilClient.get_encode_param(notify_strategy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateNotifyStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_notify_strategy_with_options_async(
        self,
        notify_strategy_id: str,
        request: cms_20240330_models.UpdateNotifyStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateNotifyStrategyResponse:
        """
        @summary 更新通知策略
        
        @param request: UpdateNotifyStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNotifyStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateNotifyStrategy',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/notifyStrategies/{OpenApiUtilClient.get_encode_param(notify_strategy_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateNotifyStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_notify_strategy(
        self,
        notify_strategy_id: str,
        request: cms_20240330_models.UpdateNotifyStrategyRequest,
    ) -> cms_20240330_models.UpdateNotifyStrategyResponse:
        """
        @summary 更新通知策略
        
        @param request: UpdateNotifyStrategyRequest
        @return: UpdateNotifyStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_notify_strategy_with_options(notify_strategy_id, request, headers, runtime)

    async def update_notify_strategy_async(
        self,
        notify_strategy_id: str,
        request: cms_20240330_models.UpdateNotifyStrategyRequest,
    ) -> cms_20240330_models.UpdateNotifyStrategyResponse:
        """
        @summary 更新通知策略
        
        @param request: UpdateNotifyStrategyRequest
        @return: UpdateNotifyStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_notify_strategy_with_options_async(notify_strategy_id, request, headers, runtime)

    def update_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.UpdatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusInstanceResponse:
        """
        @summary Update Prometheus instance information
        
        @description Update Prometheus instance information.
        
        @param request: UpdatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_instance_with_options_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.UpdatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusInstanceResponse:
        """
        @summary Update Prometheus instance information
        
        @description Update Prometheus instance information.
        
        @param request: UpdatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances/{OpenApiUtilClient.get_encode_param(prometheus_instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_instance(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.UpdatePrometheusInstanceRequest,
    ) -> cms_20240330_models.UpdatePrometheusInstanceResponse:
        """
        @summary Update Prometheus instance information
        
        @description Update Prometheus instance information.
        
        @param request: UpdatePrometheusInstanceRequest
        @return: UpdatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_prometheus_instance_with_options(prometheus_instance_id, request, headers, runtime)

    async def update_prometheus_instance_async(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.UpdatePrometheusInstanceRequest,
    ) -> cms_20240330_models.UpdatePrometheusInstanceResponse:
        """
        @summary Update Prometheus instance information
        
        @description Update Prometheus instance information.
        
        @param request: UpdatePrometheusInstanceRequest
        @return: UpdatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def update_prometheus_user_setting_with_options(
        self,
        setting_key: str,
        request: cms_20240330_models.UpdatePrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusUserSettingResponse:
        """
        @summary 更新Prom实例信息
        
        @param request: UpdatePrometheusUserSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.setting_value):
            query['settingValue'] = request.setting_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusUserSetting',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-user-setting/{OpenApiUtilClient.get_encode_param(setting_key)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_user_setting_with_options_async(
        self,
        setting_key: str,
        request: cms_20240330_models.UpdatePrometheusUserSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusUserSettingResponse:
        """
        @summary 更新Prom实例信息
        
        @param request: UpdatePrometheusUserSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.setting_value):
            query['settingValue'] = request.setting_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusUserSetting',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-user-setting/{OpenApiUtilClient.get_encode_param(setting_key)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_user_setting(
        self,
        setting_key: str,
        request: cms_20240330_models.UpdatePrometheusUserSettingRequest,
    ) -> cms_20240330_models.UpdatePrometheusUserSettingResponse:
        """
        @summary 更新Prom实例信息
        
        @param request: UpdatePrometheusUserSettingRequest
        @return: UpdatePrometheusUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_prometheus_user_setting_with_options(setting_key, request, headers, runtime)

    async def update_prometheus_user_setting_async(
        self,
        setting_key: str,
        request: cms_20240330_models.UpdatePrometheusUserSettingRequest,
    ) -> cms_20240330_models.UpdatePrometheusUserSettingResponse:
        """
        @summary 更新Prom实例信息
        
        @param request: UpdatePrometheusUserSettingRequest
        @return: UpdatePrometheusUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_prometheus_user_setting_with_options_async(setting_key, request, headers, runtime)

    def update_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.UpdatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusViewResponse:
        """
        @summary Update Prometheus view instance information
        
        @description Update Prometheus view instance information.
        
        @param request: UpdatePrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not UtilClient.is_unset(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_view_with_options_async(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.UpdatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusViewResponse:
        """
        @summary Update Prometheus view instance information
        
        @description Update Prometheus view instance information.
        
        @param request: UpdatePrometheusViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrometheusViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.prometheus_instances):
            body['prometheusInstances'] = request.prometheus_instances
        if not UtilClient.is_unset(request.prometheus_view_name):
            body['prometheusViewName'] = request.prometheus_view_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusView',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-views/{OpenApiUtilClient.get_encode_param(prometheus_view_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdatePrometheusViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_view(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.UpdatePrometheusViewRequest,
    ) -> cms_20240330_models.UpdatePrometheusViewResponse:
        """
        @summary Update Prometheus view instance information
        
        @description Update Prometheus view instance information.
        
        @param request: UpdatePrometheusViewRequest
        @return: UpdatePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_prometheus_view_with_options(prometheus_view_id, request, headers, runtime)

    async def update_prometheus_view_async(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.UpdatePrometheusViewRequest,
    ) -> cms_20240330_models.UpdatePrometheusViewResponse:
        """
        @summary Update Prometheus view instance information
        
        @description Update Prometheus view instance information.
        
        @param request: UpdatePrometheusViewRequest
        @return: UpdatePrometheusViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_prometheus_view_with_options_async(prometheus_view_id, request, headers, runtime)

    def update_service_with_options(
        self,
        workspace: str,
        service_id: str,
        request: cms_20240330_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateServiceResponse:
        """
        @summary Update Service
        
        @param request: UpdateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.service_status):
            body['serviceStatus'] = request.service_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        workspace: str,
        service_id: str,
        request: cms_20240330_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateServiceResponse:
        """
        @summary Update Service
        
        @param request: UpdateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.service_status):
            body['serviceStatus'] = request.service_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service/{OpenApiUtilClient.get_encode_param(service_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        workspace: str,
        service_id: str,
        request: cms_20240330_models.UpdateServiceRequest,
    ) -> cms_20240330_models.UpdateServiceResponse:
        """
        @summary Update Service
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(workspace, service_id, request, headers, runtime)

    async def update_service_async(
        self,
        workspace: str,
        service_id: str,
        request: cms_20240330_models.UpdateServiceRequest,
    ) -> cms_20240330_models.UpdateServiceResponse:
        """
        @summary Update Service
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(workspace, service_id, request, headers, runtime)

    def update_subscription_with_options(
        self,
        subscription_id: str,
        request: cms_20240330_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateSubscriptionResponse:
        """
        @summary 更新订阅
        
        @param request: UpdateSubscriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/subscriptions/{OpenApiUtilClient.get_encode_param(subscription_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        subscription_id: str,
        request: cms_20240330_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateSubscriptionResponse:
        """
        @summary 更新订阅
        
        @param request: UpdateSubscriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/subscriptions/{OpenApiUtilClient.get_encode_param(subscription_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        subscription_id: str,
        request: cms_20240330_models.UpdateSubscriptionRequest,
    ) -> cms_20240330_models.UpdateSubscriptionResponse:
        """
        @summary 更新订阅
        
        @param request: UpdateSubscriptionRequest
        @return: UpdateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_subscription_with_options(subscription_id, request, headers, runtime)

    async def update_subscription_async(
        self,
        subscription_id: str,
        request: cms_20240330_models.UpdateSubscriptionRequest,
    ) -> cms_20240330_models.UpdateSubscriptionResponse:
        """
        @summary 更新订阅
        
        @param request: UpdateSubscriptionRequest
        @return: UpdateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_subscription_with_options_async(subscription_id, request, headers, runtime)

    def update_umodel_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary Update Umodel configuration information
        
        @description Update Umodel configuration information
        
        @param request: UpdateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_umodel_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary Update Umodel configuration information
        
        @description Update Umodel configuration information
        
        @param request: UpdateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_umodel(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary Update Umodel configuration information
        
        @description Update Umodel configuration information
        
        @param request: UpdateUmodelRequest
        @return: UpdateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_umodel_with_options(workspace, request, headers, runtime)

    async def update_umodel_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary Update Umodel configuration information
        
        @description Update Umodel configuration information
        
        @param request: UpdateUmodelRequest
        @return: UpdateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_umodel_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_common_schema_ref_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelCommonSchemaRefResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpsertUmodelCommonSchemaRefRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelCommonSchemaRefResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpsertUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelCommonSchemaRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_umodel_common_schema_ref_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelCommonSchemaRefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelCommonSchemaRefResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpsertUmodelCommonSchemaRefRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelCommonSchemaRefResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpsertUmodelCommonSchemaRef',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/common-schema-ref',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelCommonSchemaRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_umodel_common_schema_ref(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelCommonSchemaRefRequest,
    ) -> cms_20240330_models.UpsertUmodelCommonSchemaRefResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpsertUmodelCommonSchemaRefRequest
        @return: UpsertUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upsert_umodel_common_schema_ref_with_options(workspace, request, headers, runtime)

    async def upsert_umodel_common_schema_ref_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelCommonSchemaRefRequest,
    ) -> cms_20240330_models.UpsertUmodelCommonSchemaRefResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpsertUmodelCommonSchemaRefRequest
        @return: UpsertUmodelCommonSchemaRefResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_common_schema_ref_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary Write Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.elements):
            body['elements'] = request.elements
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary Write Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.elements):
            body['elements'] = request.elements
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary Write Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @return: UpsertUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upsert_umodel_data_with_options(workspace, request, headers, runtime)

    async def upsert_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary Write Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @return: UpsertUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_data_with_options_async(workspace, request, headers, runtime)
