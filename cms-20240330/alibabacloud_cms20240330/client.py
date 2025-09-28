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
        @summary 安装接入组件，代表进行一次接入
        
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
        @summary 安装接入组件，代表进行一次接入
        
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
        @summary 安装接入组件，代表进行一次接入
        
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
        @summary 安装接入组件，代表进行一次接入
        
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
        @summary 创建聚合任务组
        
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
        @summary 创建聚合任务组
        
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
        @summary 创建聚合任务组
        
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
        @summary 创建聚合任务组
        
        @param request: CreateAggTaskGroupRequest
        @return: CreateAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_agg_task_group_with_options_async(instance_id, request, headers, runtime)

    def create_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary 创建EntityStore相关存储
        
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
        @summary 创建EntityStore相关存储
        
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
        @summary 创建EntityStore相关存储
        
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
        @summary 创建EntityStore相关存储
        
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
        @summary 创建接入中心策略
        
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
        @summary 创建接入中心策略
        
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
        @summary 创建接入中心策略
        
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
        @summary 创建接入中心策略
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建prometheus视图
        
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
        @summary 创建prometheus视图
        
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
        @summary 创建prometheus视图
        
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
        @summary 创建prometheus视图
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Prometheus监控实例
        
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
        @summary 创建Service
        
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
        @summary 创建Service
        
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
        @summary 创建Service
        
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
        @summary 创建Service
        
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
        @summary 创建票据
        
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
        @summary 创建票据
        
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
        @summary 创建票据
        
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
        @summary 创建票据
        
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
        @summary 创建Umodel配置
        
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
        @summary 创建Umodel配置
        
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
        @summary 创建Umodel配置
        
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
        @summary 创建Umodel配置
        
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
        @summary 删除addon release信息
        
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
        @summary 删除addon release信息
        
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
        @summary 删除addon release信息
        
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
        @summary 删除addon release信息
        
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
        @summary 删除聚合任务组
        
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
        @summary 删除聚合任务组
        
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
        @summary 删除聚合任务组
        
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
        @summary 删除聚合任务组
        
        @return: DeleteAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def delete_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary 删除EntityStore相关存储
        
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
        @summary 删除EntityStore相关存储
        
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
        @summary 删除EntityStore相关存储
        
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
        @summary 删除EntityStore相关存储
        
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
        @summary 删除接入中心策略
        
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
        @summary 删除接入中心策略
        
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
        @summary 删除接入中心策略
        
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
        @summary 删除接入中心策略
        
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
        @summary 删除prom实例
        
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
        @summary 删除prom实例
        
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
        @summary 删除prom实例
        
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
        @summary 删除prom实例
        
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
        @summary 删除prometheus视图实例
        
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
        @summary 删除prometheus视图实例
        
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
        @summary 删除prometheus视图实例
        
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
        @summary 删除prometheus视图实例
        
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
        @summary 删除Service
        
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
        @summary 删除Service
        
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
        @summary 删除Service
        
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
        @summary 删除Service
        
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
        @summary 删除Umodel配置信息
        
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
        @summary 删除Umodel配置信息
        
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
        @summary 删除Umodel配置信息
        
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
        @summary 删除Umodel配置信息
        
        @return: DeleteUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_with_options_async(workspace, headers, runtime)

    def delete_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary 删除 Umodel Elements
        
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
        @summary 删除 Umodel Elements
        
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
        @summary 删除 Umodel Elements
        
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
        @summary 删除 Umodel Elements
        
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
        @summary 删除工作空间
        
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
        @summary 删除工作空间
        
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
        @summary 删除工作空间
        
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
        @summary 删除工作空间
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_name, headers, runtime)

    def get_addon_release_with_options(
        self,
        release_name: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAddonReleaseResponse:
        """
        @summary 查看addon release(查看接入状态)
        
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
        @summary 查看addon release(查看接入状态)
        
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
        @summary 查看addon release(查看接入状态)
        
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
        @summary 查看addon release(查看接入状态)
        
        @return: GetAddonReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_addon_release_with_options_async(release_name, policy_id, headers, runtime)

    def get_agg_task_group_with_options(
        self,
        instance_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetAggTaskGroupResponse:
        """
        @summary 描述聚合任务组
        
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
        @summary 描述聚合任务组
        
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
        @summary 描述聚合任务组
        
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
        @summary 描述聚合任务组
        
        @return: GetAggTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agg_task_group_with_options_async(instance_id, group_id, headers, runtime)

    def get_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary 获取EntityStore相关存储信息
        
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
        @summary 获取EntityStore相关存储信息
        
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
        @summary 获取EntityStore相关存储信息
        
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
        @summary 获取EntityStore相关存储信息
        
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
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
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
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
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
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
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
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
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
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
        @return: GetIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_integration_policy_with_options_async(policy_id, headers, runtime)

    def get_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.GetPrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusInstanceResponse:
        """
        @summary 查询指定环境实例
        
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
        @summary 查询指定环境实例
        
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
        @summary 查询指定环境实例
        
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
        @summary 查询指定环境实例
        
        @param request: GetPrometheusInstanceRequest
        @return: GetPrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def get_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.GetPrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetPrometheusViewResponse:
        """
        @summary 查询指定Prometheus视图实例
        
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
        @summary 查询指定Prometheus视图实例
        
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
        @summary 查询指定Prometheus视图实例
        
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
        @summary 查询指定Prometheus视图实例
        
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
        @summary 查询 Service
        
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
        @summary 查询 Service
        
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
        @summary 查询 Service
        
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
        @summary 查询 Service
        
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
        @summary 获取应用可观测实例
        
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
        @summary 获取应用可观测实例
        
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
        @summary 获取应用可观测实例
        
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
        @summary 获取应用可观测实例
        
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
        @summary 获取Umodel配置信息
        
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
        @summary 获取Umodel配置信息
        
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
        @summary 获取Umodel配置信息
        
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
        @summary 获取Umodel配置信息
        
        @return: GetUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_with_options_async(workspace, headers, runtime)

    def get_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary 获取相关联的 Umodel 图数据
        
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
        @summary 获取相关联的 Umodel 图数据
        
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
        @summary 获取相关联的 Umodel 图数据
        
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
        @summary 获取相关联的 Umodel 图数据
        
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
        @summary 获取工作空间
        
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
        @summary 获取工作空间
        
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
        @summary 获取工作空间
        
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
        @summary 获取工作空间
        
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
        @summary addon的release列表
        
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
        @summary addon的release列表
        
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
        @summary addon的release列表
        
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
        @summary addon的release列表
        
        @param request: ListAddonReleasesRequest
        @return: ListAddonReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_addon_releases_with_options_async(policy_id, request, headers, runtime)

    def list_agg_task_groups_with_options(
        self,
        instance_id: str,
        tmp_req: cms_20240330_models.ListAggTaskGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAggTaskGroupsResponse:
        """
        @summary 列举聚合任务组
        
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
        @summary 列举聚合任务组
        
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
        @summary 列举聚合任务组
        
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
        @summary 列举聚合任务组
        
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
        @summary 查询告警动作
        
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
        @summary 查询告警动作
        
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
        @summary 查询告警动作
        
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
        @summary 查询告警动作
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alert_actions_with_options_async(request, headers, runtime)

    def list_integration_policies_with_options(
        self,
        tmp_req: cms_20240330_models.ListIntegrationPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPoliciesResponse:
        """
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
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
        @summary 查询接入中心策略列表信息
        
        @param request: ListIntegrationPoliciesRequest
        @return: ListIntegrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policies_with_options_async(request, headers, runtime)

    def list_integration_policy_custom_scrape_job_rules_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyCustomScrapeJobRulesResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 策略大盘列表
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
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
        @summary 策略大盘列表
        
        @param request: ListIntegrationPolicyDashboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntegrationPolicyDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['addonName'] = request.addon_name
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
        @summary 策略大盘列表
        
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
        @summary 策略大盘列表
        
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
        @summary 获取接入中心策略的PodMonitor资源
        
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
        @summary 获取接入中心策略的PodMonitor资源
        
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
        @summary 获取接入中心策略的PodMonitor资源
        
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
        @summary 获取接入中心策略的PodMonitor资源
        
        @param request: ListIntegrationPolicyPodMonitorsRequest
        @return: ListIntegrationPolicyPodMonitorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_policy_pod_monitors_with_options_async(policy_id, request, headers, runtime)

    def list_integration_policy_storage_requirements_with_options(
        self,
        policy_id: str,
        request: cms_20240330_models.ListIntegrationPolicyStorageRequirementsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListIntegrationPolicyStorageRequirementsResponse:
        """
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取接入中心策略的存储要求信息
        
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
        @summary 获取Prometheus实例大盘列表
        
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
        @summary 获取Prometheus实例大盘列表
        
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
        @summary 获取Prometheus实例大盘列表
        
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
        @summary 获取Prometheus实例大盘列表
        
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
        @summary 获取Prometheus实例信息列表
        
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
        @summary 获取Prometheus实例信息列表
        
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
        @summary 获取Prometheus实例信息列表
        
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
        @summary 获取Prometheus实例信息列表
        
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
        @summary 获取Prometheus视图实例信息列表
        
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
        @summary 获取Prometheus视图实例信息列表
        
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
        @summary 获取Prometheus视图实例信息列表
        
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
        @summary 获取Prometheus视图实例信息列表
        
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
        @summary 获取Prometheus虚拟实例
        
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
        @summary 获取Prometheus虚拟实例
        
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
        @summary 获取Prometheus虚拟实例
        
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
        @summary 获取Prometheus虚拟实例
        
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
        @summary 列出资源Service
        
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
        @summary 列出资源Service
        
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
        @summary 列出资源Service
        
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
        @summary 列出资源Service
        
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
        @summary 获取工作空间列表
        
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
        @summary 获取工作空间列表
        
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
        @summary 获取工作空间列表
        
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
        @summary 获取工作空间列表
        
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
        @summary 创建工作空间
        
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
        @summary 创建工作空间
        
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
        @summary 创建工作空间
        
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
        @summary 创建工作空间
        
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
        @summary 升级接入组件
        
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
        @summary 升级接入组件
        
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
        @summary 升级接入组件
        
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
        @summary 升级接入组件
        
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
        @summary 应用聚合任务组
        
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
        @summary 应用聚合任务组
        
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
        @summary 应用聚合任务组
        
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
        @summary 应用聚合任务组
        
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
        @summary 更新聚合任务组状态
        
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
        @summary 更新聚合任务组状态
        
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
        @summary 更新聚合任务组状态
        
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
        @summary 更新聚合任务组状态
        
        @param request: UpdateAggTaskGroupStatusRequest
        @return: UpdateAggTaskGroupStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_agg_task_group_status_with_options_async(instance_id, group_id, request, headers, runtime)

    def update_integration_policy_with_options(
        self,
        integration_policy_id: str,
        request: cms_20240330_models.UpdateIntegrationPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateIntegrationPolicyResponse:
        """
        @summary 更新指定策略
        
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
        @summary 更新指定策略
        
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
        @summary 更新指定策略
        
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
        @summary 更新指定策略
        
        @param request: UpdateIntegrationPolicyRequest
        @return: UpdateIntegrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_integration_policy_with_options_async(integration_policy_id, request, headers, runtime)

    def update_prometheus_instance_with_options(
        self,
        prometheus_instance_id: str,
        request: cms_20240330_models.UpdatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusInstanceResponse:
        """
        @summary 更新Prom实例信息
        
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
        @summary 更新Prom实例信息
        
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
        @summary 更新Prom实例信息
        
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
        @summary 更新Prom实例信息
        
        @param request: UpdatePrometheusInstanceRequest
        @return: UpdatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_prometheus_instance_with_options_async(prometheus_instance_id, request, headers, runtime)

    def update_prometheus_view_with_options(
        self,
        prometheus_view_id: str,
        request: cms_20240330_models.UpdatePrometheusViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdatePrometheusViewResponse:
        """
        @summary 更新Prom视图实例信息
        
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
        @summary 更新Prom视图实例信息
        
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
        @summary 更新Prom视图实例信息
        
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
        @summary 更新Prom视图实例信息
        
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
        @summary 更新UpdateService
        
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
        @summary 更新UpdateService
        
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
        @summary 更新UpdateService
        
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
        @summary 更新UpdateService
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(workspace, service_id, request, headers, runtime)

    def update_umodel_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary 更新Umodel配置信息
        
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
        @summary 更新Umodel配置信息
        
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
        @summary 更新Umodel配置信息
        
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
        @summary 更新Umodel配置信息
        
        @param request: UpdateUmodelRequest
        @return: UpdateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_umodel_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary 写入 Umodel Elements
        
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
        @summary 写入 Umodel Elements
        
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
        @summary 写入 Umodel Elements
        
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
        @summary 写入 Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @return: UpsertUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_data_with_options_async(workspace, request, headers, runtime)
