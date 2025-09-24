# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_schedulerx320240624 import models as scheduler_x320240624_models
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
        self._endpoint = self.get_endpoint('schedulerx3', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_app_with_options(
        self,
        request: scheduler_x320240624_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token):
            body['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not UtilClient.is_unset(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: scheduler_x320240624_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token):
            body['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not UtilClient.is_unset(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: scheduler_x320240624_models.CreateAppRequest,
    ) -> scheduler_x320240624_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: scheduler_x320240624_models.CreateAppRequest,
    ) -> scheduler_x320240624_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: scheduler_x320240624_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateClusterResponse:
        """
        @summary 创建集群
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switches):
            request.v_switches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.engine_type):
            body['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.v_switches_shrink):
            body['VSwitches'] = request.v_switches_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateClusterResponse:
        """
        @summary 创建集群
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switches):
            request.v_switches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.engine_type):
            body['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.v_switches_shrink):
            body['VSwitches'] = request.v_switches_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: scheduler_x320240624_models.CreateClusterRequest,
    ) -> scheduler_x320240624_models.CreateClusterResponse:
        """
        @summary 创建集群
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: scheduler_x320240624_models.CreateClusterRequest,
    ) -> scheduler_x320240624_models.CreateClusterResponse:
        """
        @summary 创建集群
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: scheduler_x320240624_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateJobResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notice_config):
            request.notice_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notice_contacts):
            request.notice_contacts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not UtilClient.is_unset(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not UtilClient.is_unset(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.CreateJobResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notice_config):
            request.notice_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notice_contacts):
            request.notice_contacts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not UtilClient.is_unset(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not UtilClient.is_unset(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: scheduler_x320240624_models.CreateJobRequest,
    ) -> scheduler_x320240624_models.CreateJobResponse:
        """
        @summary 创建任务
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: scheduler_x320240624_models.CreateJobRequest,
    ) -> scheduler_x320240624_models.CreateJobResponse:
        """
        @summary 创建任务
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: scheduler_x320240624_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteAppResponse:
        """
        @summary 删除应用分组
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: scheduler_x320240624_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteAppResponse:
        """
        @summary 删除应用分组
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: scheduler_x320240624_models.DeleteAppRequest,
    ) -> scheduler_x320240624_models.DeleteAppResponse:
        """
        @summary 删除应用分组
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: scheduler_x320240624_models.DeleteAppRequest,
    ) -> scheduler_x320240624_models.DeleteAppResponse:
        """
        @summary 删除应用分组
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: scheduler_x320240624_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteClusterResponse:
        """
        @summary 释放删除集群
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: scheduler_x320240624_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteClusterResponse:
        """
        @summary 释放删除集群
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: scheduler_x320240624_models.DeleteClusterRequest,
    ) -> scheduler_x320240624_models.DeleteClusterResponse:
        """
        @summary 释放删除集群
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: scheduler_x320240624_models.DeleteClusterRequest,
    ) -> scheduler_x320240624_models.DeleteClusterResponse:
        """
        @summary 释放删除集群
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        tmp_req: scheduler_x320240624_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteJobsResponse:
        """
        @summary 批量删除任务
        
        @param tmp_req: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.DeleteJobsResponse:
        """
        @summary 批量删除任务
        
        @param tmp_req: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: scheduler_x320240624_models.DeleteJobsRequest,
    ) -> scheduler_x320240624_models.DeleteJobsResponse:
        """
        @summary 批量删除任务
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: scheduler_x320240624_models.DeleteJobsRequest,
    ) -> scheduler_x320240624_models.DeleteJobsResponse:
        """
        @summary 批量删除任务
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def export_jobs_with_options(
        self,
        tmp_req: scheduler_x320240624_models.ExportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ExportJobsResponse:
        """
        @summary 批量导出任务信息
        
        @param tmp_req: ExportJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.ExportJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.export_job_type):
            body['ExportJobType'] = request.export_job_type
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='byte'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ExportJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_jobs_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.ExportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ExportJobsResponse:
        """
        @summary 批量导出任务信息
        
        @param tmp_req: ExportJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.ExportJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.export_job_type):
            body['ExportJobType'] = request.export_job_type
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='byte'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ExportJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_jobs(
        self,
        request: scheduler_x320240624_models.ExportJobsRequest,
    ) -> scheduler_x320240624_models.ExportJobsResponse:
        """
        @summary 批量导出任务信息
        
        @param request: ExportJobsRequest
        @return: ExportJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_jobs_with_options(request, runtime)

    async def export_jobs_async(
        self,
        request: scheduler_x320240624_models.ExportJobsRequest,
    ) -> scheduler_x320240624_models.ExportJobsResponse:
        """
        @summary 批量导出任务信息
        
        @param request: ExportJobsRequest
        @return: ExportJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_jobs_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: scheduler_x320240624_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetAppResponse:
        """
        @summary 获取指定应用
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: scheduler_x320240624_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetAppResponse:
        """
        @summary 获取指定应用
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: scheduler_x320240624_models.GetAppRequest,
    ) -> scheduler_x320240624_models.GetAppResponse:
        """
        @summary 获取指定应用
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: scheduler_x320240624_models.GetAppRequest,
    ) -> scheduler_x320240624_models.GetAppResponse:
        """
        @summary 获取指定应用
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: scheduler_x320240624_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetClusterResponse:
        """
        @summary 获取集群详细信息
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: scheduler_x320240624_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetClusterResponse:
        """
        @summary 获取集群详细信息
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: scheduler_x320240624_models.GetClusterRequest,
    ) -> scheduler_x320240624_models.GetClusterResponse:
        """
        @summary 获取集群详细信息
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: scheduler_x320240624_models.GetClusterRequest,
    ) -> scheduler_x320240624_models.GetClusterResponse:
        """
        @summary 获取集群详细信息
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_desigate_info_with_options(
        self,
        request: scheduler_x320240624_models.GetDesigateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetDesigateInfoResponse:
        """
        @summary 获取指定机器信息
        
        @param request: GetDesigateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDesigateInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDesigateInfo',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetDesigateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_desigate_info_with_options_async(
        self,
        request: scheduler_x320240624_models.GetDesigateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetDesigateInfoResponse:
        """
        @summary 获取指定机器信息
        
        @param request: GetDesigateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDesigateInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDesigateInfo',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetDesigateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_desigate_info(
        self,
        request: scheduler_x320240624_models.GetDesigateInfoRequest,
    ) -> scheduler_x320240624_models.GetDesigateInfoResponse:
        """
        @summary 获取指定机器信息
        
        @param request: GetDesigateInfoRequest
        @return: GetDesigateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_desigate_info_with_options(request, runtime)

    async def get_desigate_info_async(
        self,
        request: scheduler_x320240624_models.GetDesigateInfoRequest,
    ) -> scheduler_x320240624_models.GetDesigateInfoResponse:
        """
        @summary 获取指定机器信息
        
        @param request: GetDesigateInfoRequest
        @return: GetDesigateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_desigate_info_with_options_async(request, runtime)

    def get_job_execution_with_options(
        self,
        request: scheduler_x320240624_models.GetJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionResponse:
        """
        @summary 获取任务执行的详细信息
        
        @param request: GetJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.mse_session_id):
            query['MseSessionId'] = request.mse_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_with_options_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionResponse:
        """
        @summary 获取任务执行的详细信息
        
        @param request: GetJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.mse_session_id):
            query['MseSessionId'] = request.mse_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution(
        self,
        request: scheduler_x320240624_models.GetJobExecutionRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionResponse:
        """
        @summary 获取任务执行的详细信息
        
        @param request: GetJobExecutionRequest
        @return: GetJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_execution_with_options(request, runtime)

    async def get_job_execution_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionResponse:
        """
        @summary 获取任务执行的详细信息
        
        @param request: GetJobExecutionRequest
        @return: GetJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_execution_with_options_async(request, runtime)

    def get_job_execution_progress_with_options(
        self,
        request: scheduler_x320240624_models.GetJobExecutionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionProgressResponse:
        """
        @summary 获取任务执行的详情
        
        @param request: GetJobExecutionProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionProgressResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecutionProgress',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_progress_with_options_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionProgressResponse:
        """
        @summary 获取任务执行的详情
        
        @param request: GetJobExecutionProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionProgressResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecutionProgress',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution_progress(
        self,
        request: scheduler_x320240624_models.GetJobExecutionProgressRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionProgressResponse:
        """
        @summary 获取任务执行的详情
        
        @param request: GetJobExecutionProgressRequest
        @return: GetJobExecutionProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_execution_progress_with_options(request, runtime)

    async def get_job_execution_progress_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionProgressRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionProgressResponse:
        """
        @summary 获取任务执行的详情
        
        @param request: GetJobExecutionProgressRequest
        @return: GetJobExecutionProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_execution_progress_with_options_async(request, runtime)

    def get_job_execution_thread_dump_with_options(
        self,
        request: scheduler_x320240624_models.GetJobExecutionThreadDumpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionThreadDumpResponse:
        """
        @summary 查询任务的线程堆栈
        
        @param request: GetJobExecutionThreadDumpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionThreadDumpResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecutionThreadDump',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionThreadDumpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_thread_dump_with_options_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionThreadDumpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetJobExecutionThreadDumpResponse:
        """
        @summary 查询任务的线程堆栈
        
        @param request: GetJobExecutionThreadDumpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobExecutionThreadDumpResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobExecutionThreadDump',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetJobExecutionThreadDumpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution_thread_dump(
        self,
        request: scheduler_x320240624_models.GetJobExecutionThreadDumpRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionThreadDumpResponse:
        """
        @summary 查询任务的线程堆栈
        
        @param request: GetJobExecutionThreadDumpRequest
        @return: GetJobExecutionThreadDumpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_execution_thread_dump_with_options(request, runtime)

    async def get_job_execution_thread_dump_async(
        self,
        request: scheduler_x320240624_models.GetJobExecutionThreadDumpRequest,
    ) -> scheduler_x320240624_models.GetJobExecutionThreadDumpResponse:
        """
        @summary 查询任务的线程堆栈
        
        @param request: GetJobExecutionThreadDumpRequest
        @return: GetJobExecutionThreadDumpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_execution_thread_dump_with_options_async(request, runtime)

    def get_log_with_options(
        self,
        request: scheduler_x320240624_models.GetLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetLogResponse:
        """
        @summary 查询日志
        
        @param request: GetLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLog',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_with_options_async(
        self,
        request: scheduler_x320240624_models.GetLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetLogResponse:
        """
        @summary 查询日志
        
        @param request: GetLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLog',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log(
        self,
        request: scheduler_x320240624_models.GetLogRequest,
    ) -> scheduler_x320240624_models.GetLogResponse:
        """
        @summary 查询日志
        
        @param request: GetLogRequest
        @return: GetLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_with_options(request, runtime)

    async def get_log_async(
        self,
        request: scheduler_x320240624_models.GetLogRequest,
    ) -> scheduler_x320240624_models.GetLogResponse:
        """
        @summary 查询日志
        
        @param request: GetLogRequest
        @return: GetLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_with_options_async(request, runtime)

    def get_log_event_with_options(
        self,
        request: scheduler_x320240624_models.GetLogEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetLogEventResponse:
        """
        @summary 查询事件
        
        @param request: GetLogEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetLogEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_event_with_options_async(
        self,
        request: scheduler_x320240624_models.GetLogEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.GetLogEventResponse:
        """
        @summary 查询事件
        
        @param request: GetLogEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.GetLogEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_event(
        self,
        request: scheduler_x320240624_models.GetLogEventRequest,
    ) -> scheduler_x320240624_models.GetLogEventResponse:
        """
        @summary 查询事件
        
        @param request: GetLogEventRequest
        @return: GetLogEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_event_with_options(request, runtime)

    async def get_log_event_async(
        self,
        request: scheduler_x320240624_models.GetLogEventRequest,
    ) -> scheduler_x320240624_models.GetLogEventResponse:
        """
        @summary 查询事件
        
        @param request: GetLogEventRequest
        @return: GetLogEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_event_with_options_async(request, runtime)

    def import_calendar_with_options(
        self,
        request: scheduler_x320240624_models.ImportCalendarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ImportCalendarResponse:
        """
        @summary 导入日历
        
        @param request: ImportCalendarRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCalendarResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.months):
            body['Months'] = request.months
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.year):
            body['Year'] = request.year
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportCalendar',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ImportCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_calendar_with_options_async(
        self,
        request: scheduler_x320240624_models.ImportCalendarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ImportCalendarResponse:
        """
        @summary 导入日历
        
        @param request: ImportCalendarRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportCalendarResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.months):
            body['Months'] = request.months
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.year):
            body['Year'] = request.year
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportCalendar',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ImportCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_calendar(
        self,
        request: scheduler_x320240624_models.ImportCalendarRequest,
    ) -> scheduler_x320240624_models.ImportCalendarResponse:
        """
        @summary 导入日历
        
        @param request: ImportCalendarRequest
        @return: ImportCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_calendar_with_options(request, runtime)

    async def import_calendar_async(
        self,
        request: scheduler_x320240624_models.ImportCalendarRequest,
    ) -> scheduler_x320240624_models.ImportCalendarResponse:
        """
        @summary 导入日历
        
        @param request: ImportCalendarRequest
        @return: ImportCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_calendar_with_options_async(request, runtime)

    def import_jobs_with_options(
        self,
        request: scheduler_x320240624_models.ImportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ImportJobsResponse:
        """
        @summary 批量导入任务
        
        @param request: ImportJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportJobsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ImportJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_jobs_with_options_async(
        self,
        request: scheduler_x320240624_models.ImportJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ImportJobsResponse:
        """
        @summary 批量导入任务
        
        @param request: ImportJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportJobsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ImportJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_jobs(
        self,
        request: scheduler_x320240624_models.ImportJobsRequest,
    ) -> scheduler_x320240624_models.ImportJobsResponse:
        """
        @summary 批量导入任务
        
        @param request: ImportJobsRequest
        @return: ImportJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_jobs_with_options(request, runtime)

    async def import_jobs_async(
        self,
        request: scheduler_x320240624_models.ImportJobsRequest,
    ) -> scheduler_x320240624_models.ImportJobsResponse:
        """
        @summary 批量导入任务
        
        @param request: ImportJobsRequest
        @return: ImportJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_jobs_with_options_async(request, runtime)

    def list_alarm_event_with_options(
        self,
        request: scheduler_x320240624_models.ListAlarmEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAlarmEventResponse:
        """
        @summary 获取报警事件
        
        @param request: ListAlarmEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAlarmEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_event_with_options_async(
        self,
        request: scheduler_x320240624_models.ListAlarmEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAlarmEventResponse:
        """
        @summary 获取报警事件
        
        @param request: ListAlarmEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAlarmEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_event(
        self,
        request: scheduler_x320240624_models.ListAlarmEventRequest,
    ) -> scheduler_x320240624_models.ListAlarmEventResponse:
        """
        @summary 获取报警事件
        
        @param request: ListAlarmEventRequest
        @return: ListAlarmEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_event_with_options(request, runtime)

    async def list_alarm_event_async(
        self,
        request: scheduler_x320240624_models.ListAlarmEventRequest,
    ) -> scheduler_x320240624_models.ListAlarmEventResponse:
        """
        @summary 获取报警事件
        
        @param request: ListAlarmEventRequest
        @return: ListAlarmEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_event_with_options_async(request, runtime)

    def list_app_names_with_options(
        self,
        request: scheduler_x320240624_models.ListAppNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAppNamesResponse:
        """
        @summary 获取应用名字列表
        
        @param request: ListAppNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppNamesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppNames',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAppNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_names_with_options_async(
        self,
        request: scheduler_x320240624_models.ListAppNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAppNamesResponse:
        """
        @summary 获取应用名字列表
        
        @param request: ListAppNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppNamesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppNames',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAppNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_names(
        self,
        request: scheduler_x320240624_models.ListAppNamesRequest,
    ) -> scheduler_x320240624_models.ListAppNamesResponse:
        """
        @summary 获取应用名字列表
        
        @param request: ListAppNamesRequest
        @return: ListAppNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_names_with_options(request, runtime)

    async def list_app_names_async(
        self,
        request: scheduler_x320240624_models.ListAppNamesRequest,
    ) -> scheduler_x320240624_models.ListAppNamesResponse:
        """
        @summary 获取应用名字列表
        
        @param request: ListAppNamesRequest
        @return: ListAppNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_names_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: scheduler_x320240624_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAppsResponse:
        """
        @summary 获取应用列表
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: scheduler_x320240624_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListAppsResponse:
        """
        @summary 获取应用列表
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: scheduler_x320240624_models.ListAppsRequest,
    ) -> scheduler_x320240624_models.ListAppsResponse:
        """
        @summary 获取应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: scheduler_x320240624_models.ListAppsRequest,
    ) -> scheduler_x320240624_models.ListAppsResponse:
        """
        @summary 获取应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_calendar_names_with_options(
        self,
        request: scheduler_x320240624_models.ListCalendarNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListCalendarNamesResponse:
        """
        @summary 获取日历名字列表
        
        @param request: ListCalendarNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalendarNamesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCalendarNames',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListCalendarNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calendar_names_with_options_async(
        self,
        request: scheduler_x320240624_models.ListCalendarNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListCalendarNamesResponse:
        """
        @summary 获取日历名字列表
        
        @param request: ListCalendarNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalendarNamesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCalendarNames',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListCalendarNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calendar_names(
        self,
        request: scheduler_x320240624_models.ListCalendarNamesRequest,
    ) -> scheduler_x320240624_models.ListCalendarNamesResponse:
        """
        @summary 获取日历名字列表
        
        @param request: ListCalendarNamesRequest
        @return: ListCalendarNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_calendar_names_with_options(request, runtime)

    async def list_calendar_names_async(
        self,
        request: scheduler_x320240624_models.ListCalendarNamesRequest,
    ) -> scheduler_x320240624_models.ListCalendarNamesResponse:
        """
        @summary 获取日历名字列表
        
        @param request: ListCalendarNamesRequest
        @return: ListCalendarNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_calendar_names_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: scheduler_x320240624_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListClustersResponse:
        """
        @summary 查询实例列表
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: scheduler_x320240624_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListClustersResponse:
        """
        @summary 查询实例列表
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: scheduler_x320240624_models.ListClustersRequest,
    ) -> scheduler_x320240624_models.ListClustersResponse:
        """
        @summary 查询实例列表
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: scheduler_x320240624_models.ListClustersRequest,
    ) -> scheduler_x320240624_models.ListClustersResponse:
        """
        @summary 查询实例列表
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_executors_with_options(
        self,
        request: scheduler_x320240624_models.ListExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListExecutorsResponse:
        """
        @summary 查询Executor列表
        
        @param request: ListExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutors',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executors_with_options_async(
        self,
        request: scheduler_x320240624_models.ListExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListExecutorsResponse:
        """
        @summary 查询Executor列表
        
        @param request: ListExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutors',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executors(
        self,
        request: scheduler_x320240624_models.ListExecutorsRequest,
    ) -> scheduler_x320240624_models.ListExecutorsResponse:
        """
        @summary 查询Executor列表
        
        @param request: ListExecutorsRequest
        @return: ListExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_executors_with_options(request, runtime)

    async def list_executors_async(
        self,
        request: scheduler_x320240624_models.ListExecutorsRequest,
    ) -> scheduler_x320240624_models.ListExecutorsResponse:
        """
        @summary 查询Executor列表
        
        @param request: ListExecutorsRequest
        @return: ListExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_executors_with_options_async(request, runtime)

    def list_job_executions_with_options(
        self,
        request: scheduler_x320240624_models.ListJobExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobExecutionsResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListJobExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobExecutions',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_executions_with_options_async(
        self,
        request: scheduler_x320240624_models.ListJobExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobExecutionsResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListJobExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobExecutions',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_executions(
        self,
        request: scheduler_x320240624_models.ListJobExecutionsRequest,
    ) -> scheduler_x320240624_models.ListJobExecutionsResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListJobExecutionsRequest
        @return: ListJobExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_executions_with_options(request, runtime)

    async def list_job_executions_async(
        self,
        request: scheduler_x320240624_models.ListJobExecutionsRequest,
    ) -> scheduler_x320240624_models.ListJobExecutionsResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListJobExecutionsRequest
        @return: ListJobExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_executions_with_options_async(request, runtime)

    def list_job_script_history_with_options(
        self,
        request: scheduler_x320240624_models.ListJobScriptHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobScriptHistoryResponse:
        """
        @summary 获取任务脚本历史列表
        
        @param request: ListJobScriptHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobScriptHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobScriptHistory',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobScriptHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_script_history_with_options_async(
        self,
        request: scheduler_x320240624_models.ListJobScriptHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobScriptHistoryResponse:
        """
        @summary 获取任务脚本历史列表
        
        @param request: ListJobScriptHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobScriptHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobScriptHistory',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobScriptHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_script_history(
        self,
        request: scheduler_x320240624_models.ListJobScriptHistoryRequest,
    ) -> scheduler_x320240624_models.ListJobScriptHistoryResponse:
        """
        @summary 获取任务脚本历史列表
        
        @param request: ListJobScriptHistoryRequest
        @return: ListJobScriptHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_script_history_with_options(request, runtime)

    async def list_job_script_history_async(
        self,
        request: scheduler_x320240624_models.ListJobScriptHistoryRequest,
    ) -> scheduler_x320240624_models.ListJobScriptHistoryResponse:
        """
        @summary 获取任务脚本历史列表
        
        @param request: ListJobScriptHistoryRequest
        @return: ListJobScriptHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_script_history_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: scheduler_x320240624_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobsResponse:
        """
        @summary 获取任务列表
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: scheduler_x320240624_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListJobsResponse:
        """
        @summary 获取任务列表
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: scheduler_x320240624_models.ListJobsRequest,
    ) -> scheduler_x320240624_models.ListJobsResponse:
        """
        @summary 获取任务列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: scheduler_x320240624_models.ListJobsRequest,
    ) -> scheduler_x320240624_models.ListJobsResponse:
        """
        @summary 获取任务列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_lables_with_options(
        self,
        request: scheduler_x320240624_models.ListLablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListLablesResponse:
        """
        @summary 获取executor的label列表
        
        @param request: ListLablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLablesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLables',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListLablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lables_with_options_async(
        self,
        request: scheduler_x320240624_models.ListLablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListLablesResponse:
        """
        @summary 获取executor的label列表
        
        @param request: ListLablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLablesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLables',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListLablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lables(
        self,
        request: scheduler_x320240624_models.ListLablesRequest,
    ) -> scheduler_x320240624_models.ListLablesResponse:
        """
        @summary 获取executor的label列表
        
        @param request: ListLablesRequest
        @return: ListLablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lables_with_options(request, runtime)

    async def list_lables_async(
        self,
        request: scheduler_x320240624_models.ListLablesRequest,
    ) -> scheduler_x320240624_models.ListLablesResponse:
        """
        @summary 获取executor的label列表
        
        @param request: ListLablesRequest
        @return: ListLablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_lables_with_options_async(request, runtime)

    def list_region_zone_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListRegionZoneResponse:
        """
        @summary 获取可用区列表
        
        @param request: ListRegionZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionZoneResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegionZone',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListRegionZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_region_zone_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListRegionZoneResponse:
        """
        @summary 获取可用区列表
        
        @param request: ListRegionZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionZoneResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegionZone',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListRegionZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_region_zone(self) -> scheduler_x320240624_models.ListRegionZoneResponse:
        """
        @summary 获取可用区列表
        
        @return: ListRegionZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_region_zone_with_options(runtime)

    async def list_region_zone_async(self) -> scheduler_x320240624_models.ListRegionZoneResponse:
        """
        @summary 获取可用区列表
        
        @return: ListRegionZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_region_zone_with_options_async(runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListRegionsResponse:
        """
        @summary 获取所有region列表
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListRegionsResponse:
        """
        @summary 获取所有region列表
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> scheduler_x320240624_models.ListRegionsResponse:
        """
        @summary 获取所有region列表
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> scheduler_x320240624_models.ListRegionsResponse:
        """
        @summary 获取所有region列表
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_schedule_event_with_options(
        self,
        request: scheduler_x320240624_models.ListScheduleEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListScheduleEventResponse:
        """
        @summary 查询调度事件
        
        @param request: ListScheduleEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduleEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduleEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListScheduleEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedule_event_with_options_async(
        self,
        request: scheduler_x320240624_models.ListScheduleEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListScheduleEventResponse:
        """
        @summary 查询调度事件
        
        @param request: ListScheduleEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduleEventResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduleEvent',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListScheduleEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedule_event(
        self,
        request: scheduler_x320240624_models.ListScheduleEventRequest,
    ) -> scheduler_x320240624_models.ListScheduleEventResponse:
        """
        @summary 查询调度事件
        
        @param request: ListScheduleEventRequest
        @return: ListScheduleEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_schedule_event_with_options(request, runtime)

    async def list_schedule_event_async(
        self,
        request: scheduler_x320240624_models.ListScheduleEventRequest,
    ) -> scheduler_x320240624_models.ListScheduleEventResponse:
        """
        @summary 查询调度事件
        
        @param request: ListScheduleEventRequest
        @return: ListScheduleEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_schedule_event_with_options_async(request, runtime)

    def list_schedule_times_with_options(
        self,
        request: scheduler_x320240624_models.ListScheduleTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListScheduleTimesResponse:
        """
        @summary 获取指定时间类型和表达式未来5次调度时间
        
        @param request: ListScheduleTimesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduleTimesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduleTimes',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListScheduleTimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedule_times_with_options_async(
        self,
        request: scheduler_x320240624_models.ListScheduleTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.ListScheduleTimesResponse:
        """
        @summary 获取指定时间类型和表达式未来5次调度时间
        
        @param request: ListScheduleTimesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduleTimesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduleTimes',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.ListScheduleTimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedule_times(
        self,
        request: scheduler_x320240624_models.ListScheduleTimesRequest,
    ) -> scheduler_x320240624_models.ListScheduleTimesResponse:
        """
        @summary 获取指定时间类型和表达式未来5次调度时间
        
        @param request: ListScheduleTimesRequest
        @return: ListScheduleTimesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_schedule_times_with_options(request, runtime)

    async def list_schedule_times_async(
        self,
        request: scheduler_x320240624_models.ListScheduleTimesRequest,
    ) -> scheduler_x320240624_models.ListScheduleTimesResponse:
        """
        @summary 获取指定时间类型和表达式未来5次调度时间
        
        @param request: ListScheduleTimesRequest
        @return: ListScheduleTimesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_schedule_times_with_options_async(request, runtime)

    def operate_designate_executors_with_options(
        self,
        tmp_req: scheduler_x320240624_models.OperateDesignateExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateDesignateExecutorsResponse:
        """
        @summary 指定执行器
        
        @param tmp_req: OperateDesignateExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateDesignateExecutorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateDesignateExecutorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address_list):
            request.address_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address_list, 'AddressList', 'json')
        body = {}
        if not UtilClient.is_unset(request.address_list_shrink):
            body['AddressList'] = request.address_list_shrink
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.designate_type):
            body['DesignateType'] = request.designate_type
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.transferable):
            body['Transferable'] = request.transferable
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateDesignateExecutors',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateDesignateExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_designate_executors_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.OperateDesignateExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateDesignateExecutorsResponse:
        """
        @summary 指定执行器
        
        @param tmp_req: OperateDesignateExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateDesignateExecutorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateDesignateExecutorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address_list):
            request.address_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address_list, 'AddressList', 'json')
        body = {}
        if not UtilClient.is_unset(request.address_list_shrink):
            body['AddressList'] = request.address_list_shrink
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.designate_type):
            body['DesignateType'] = request.designate_type
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.transferable):
            body['Transferable'] = request.transferable
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateDesignateExecutors',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateDesignateExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_designate_executors(
        self,
        request: scheduler_x320240624_models.OperateDesignateExecutorsRequest,
    ) -> scheduler_x320240624_models.OperateDesignateExecutorsResponse:
        """
        @summary 指定执行器
        
        @param request: OperateDesignateExecutorsRequest
        @return: OperateDesignateExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_designate_executors_with_options(request, runtime)

    async def operate_designate_executors_async(
        self,
        request: scheduler_x320240624_models.OperateDesignateExecutorsRequest,
    ) -> scheduler_x320240624_models.OperateDesignateExecutorsResponse:
        """
        @summary 指定执行器
        
        @param request: OperateDesignateExecutorsRequest
        @return: OperateDesignateExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_designate_executors_with_options_async(request, runtime)

    def operate_disable_jobs_with_options(
        self,
        tmp_req: scheduler_x320240624_models.OperateDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateDisableJobsResponse:
        """
        @summary 批量禁用任务
        
        @param tmp_req: OperateDisableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateDisableJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateDisableJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateDisableJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_disable_jobs_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.OperateDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateDisableJobsResponse:
        """
        @summary 批量禁用任务
        
        @param tmp_req: OperateDisableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateDisableJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateDisableJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateDisableJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateDisableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_disable_jobs(
        self,
        request: scheduler_x320240624_models.OperateDisableJobsRequest,
    ) -> scheduler_x320240624_models.OperateDisableJobsResponse:
        """
        @summary 批量禁用任务
        
        @param request: OperateDisableJobsRequest
        @return: OperateDisableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_disable_jobs_with_options(request, runtime)

    async def operate_disable_jobs_async(
        self,
        request: scheduler_x320240624_models.OperateDisableJobsRequest,
    ) -> scheduler_x320240624_models.OperateDisableJobsResponse:
        """
        @summary 批量禁用任务
        
        @param request: OperateDisableJobsRequest
        @return: OperateDisableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_disable_jobs_with_options_async(request, runtime)

    def operate_enable_jobs_with_options(
        self,
        tmp_req: scheduler_x320240624_models.OperateEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateEnableJobsResponse:
        """
        @summary 批量启用任务
        
        @param tmp_req: OperateEnableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateEnableJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateEnableJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateEnableJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_enable_jobs_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.OperateEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateEnableJobsResponse:
        """
        @summary 批量启用任务
        
        @param tmp_req: OperateEnableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateEnableJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateEnableJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateEnableJobs',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateEnableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_enable_jobs(
        self,
        request: scheduler_x320240624_models.OperateEnableJobsRequest,
    ) -> scheduler_x320240624_models.OperateEnableJobsResponse:
        """
        @summary 批量启用任务
        
        @param request: OperateEnableJobsRequest
        @return: OperateEnableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_enable_jobs_with_options(request, runtime)

    async def operate_enable_jobs_async(
        self,
        request: scheduler_x320240624_models.OperateEnableJobsRequest,
    ) -> scheduler_x320240624_models.OperateEnableJobsResponse:
        """
        @summary 批量启用任务
        
        @param request: OperateEnableJobsRequest
        @return: OperateEnableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_enable_jobs_with_options_async(request, runtime)

    def operate_execute_job_with_options(
        self,
        request: scheduler_x320240624_models.OperateExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateExecuteJobResponse:
        """
        @summary 运行一次任务
        
        @param request: OperateExecuteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateExecuteJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_parameters):
            body['InstanceParameters'] = request.instance_parameters
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.worker):
            body['Worker'] = request.worker
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateExecuteJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_execute_job_with_options_async(
        self,
        request: scheduler_x320240624_models.OperateExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateExecuteJobResponse:
        """
        @summary 运行一次任务
        
        @param request: OperateExecuteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateExecuteJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_parameters):
            body['InstanceParameters'] = request.instance_parameters
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.worker):
            body['Worker'] = request.worker
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateExecuteJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateExecuteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_execute_job(
        self,
        request: scheduler_x320240624_models.OperateExecuteJobRequest,
    ) -> scheduler_x320240624_models.OperateExecuteJobResponse:
        """
        @summary 运行一次任务
        
        @param request: OperateExecuteJobRequest
        @return: OperateExecuteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_execute_job_with_options(request, runtime)

    async def operate_execute_job_async(
        self,
        request: scheduler_x320240624_models.OperateExecuteJobRequest,
    ) -> scheduler_x320240624_models.OperateExecuteJobResponse:
        """
        @summary 运行一次任务
        
        @param request: OperateExecuteJobRequest
        @return: OperateExecuteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_execute_job_with_options_async(request, runtime)

    def operate_rerun_job_with_options(
        self,
        request: scheduler_x320240624_models.OperateRerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateRerunJobResponse:
        """
        @summary 重刷任务历史数据
        
        @param request: OperateRerunJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateRerunJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_time):
            query['DataTime'] = request.data_time
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateRerunJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateRerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_rerun_job_with_options_async(
        self,
        request: scheduler_x320240624_models.OperateRerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateRerunJobResponse:
        """
        @summary 重刷任务历史数据
        
        @param request: OperateRerunJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateRerunJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_time):
            query['DataTime'] = request.data_time
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateRerunJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateRerunJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_rerun_job(
        self,
        request: scheduler_x320240624_models.OperateRerunJobRequest,
    ) -> scheduler_x320240624_models.OperateRerunJobResponse:
        """
        @summary 重刷任务历史数据
        
        @param request: OperateRerunJobRequest
        @return: OperateRerunJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_rerun_job_with_options(request, runtime)

    async def operate_rerun_job_async(
        self,
        request: scheduler_x320240624_models.OperateRerunJobRequest,
    ) -> scheduler_x320240624_models.OperateRerunJobResponse:
        """
        @summary 重刷任务历史数据
        
        @param request: OperateRerunJobRequest
        @return: OperateRerunJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_rerun_job_with_options_async(request, runtime)

    def operate_retry_job_execution_with_options(
        self,
        tmp_req: scheduler_x320240624_models.OperateRetryJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateRetryJobExecutionResponse:
        """
        @summary 重跑失败的任务实例
        
        @param tmp_req: OperateRetryJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateRetryJobExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateRetryJobExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_list):
            request.task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateRetryJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateRetryJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_retry_job_execution_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.OperateRetryJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateRetryJobExecutionResponse:
        """
        @summary 重跑失败的任务实例
        
        @param tmp_req: OperateRetryJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateRetryJobExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateRetryJobExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_list):
            request.task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateRetryJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateRetryJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_retry_job_execution(
        self,
        request: scheduler_x320240624_models.OperateRetryJobExecutionRequest,
    ) -> scheduler_x320240624_models.OperateRetryJobExecutionResponse:
        """
        @summary 重跑失败的任务实例
        
        @param request: OperateRetryJobExecutionRequest
        @return: OperateRetryJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_retry_job_execution_with_options(request, runtime)

    async def operate_retry_job_execution_async(
        self,
        request: scheduler_x320240624_models.OperateRetryJobExecutionRequest,
    ) -> scheduler_x320240624_models.OperateRetryJobExecutionResponse:
        """
        @summary 重跑失败的任务实例
        
        @param request: OperateRetryJobExecutionRequest
        @return: OperateRetryJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_retry_job_execution_with_options_async(request, runtime)

    def operate_stop_job_execution_with_options(
        self,
        tmp_req: scheduler_x320240624_models.OperateStopJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateStopJobExecutionResponse:
        """
        @summary 停止正在运行的任务实例
        
        @param tmp_req: OperateStopJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateStopJobExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateStopJobExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_list):
            request.task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateStopJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateStopJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_stop_job_execution_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.OperateStopJobExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.OperateStopJobExecutionResponse:
        """
        @summary 停止正在运行的任务实例
        
        @param tmp_req: OperateStopJobExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateStopJobExecutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.OperateStopJobExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_list):
            request.task_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not UtilClient.is_unset(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateStopJobExecution',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.OperateStopJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_stop_job_execution(
        self,
        request: scheduler_x320240624_models.OperateStopJobExecutionRequest,
    ) -> scheduler_x320240624_models.OperateStopJobExecutionResponse:
        """
        @summary 停止正在运行的任务实例
        
        @param request: OperateStopJobExecutionRequest
        @return: OperateStopJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_stop_job_execution_with_options(request, runtime)

    async def operate_stop_job_execution_async(
        self,
        request: scheduler_x320240624_models.OperateStopJobExecutionRequest,
    ) -> scheduler_x320240624_models.OperateStopJobExecutionResponse:
        """
        @summary 停止正在运行的任务实例
        
        @param request: OperateStopJobExecutionRequest
        @return: OperateStopJobExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_stop_job_execution_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: scheduler_x320240624_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateAppResponse:
        """
        @summary 更新应用分组
        
        @param request: UpdateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token):
            body['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not UtilClient.is_unset(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: scheduler_x320240624_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateAppResponse:
        """
        @summary 更新应用分组
        
        @param request: UpdateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token):
            body['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not UtilClient.is_unset(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: scheduler_x320240624_models.UpdateAppRequest,
    ) -> scheduler_x320240624_models.UpdateAppResponse:
        """
        @summary 更新应用分组
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: scheduler_x320240624_models.UpdateAppRequest,
    ) -> scheduler_x320240624_models.UpdateAppResponse:
        """
        @summary 更新应用分组
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        request: scheduler_x320240624_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateClusterResponse:
        """
        @summary 更新集群
        
        @param request: UpdateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        request: scheduler_x320240624_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateClusterResponse:
        """
        @summary 更新集群
        
        @param request: UpdateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: scheduler_x320240624_models.UpdateClusterRequest,
    ) -> scheduler_x320240624_models.UpdateClusterResponse:
        """
        @summary 更新集群
        
        @param request: UpdateClusterRequest
        @return: UpdateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: scheduler_x320240624_models.UpdateClusterRequest,
    ) -> scheduler_x320240624_models.UpdateClusterResponse:
        """
        @summary 更新集群
        
        @param request: UpdateClusterRequest
        @return: UpdateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        tmp_req: scheduler_x320240624_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateJobResponse:
        """
        @summary 更新任务信息
        
        @param tmp_req: UpdateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.UpdateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notice_config):
            request.notice_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notice_contacts):
            request.notice_contacts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not UtilClient.is_unset(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not UtilClient.is_unset(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        tmp_req: scheduler_x320240624_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateJobResponse:
        """
        @summary 更新任务信息
        
        @param tmp_req: UpdateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = scheduler_x320240624_models.UpdateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notice_config):
            request.notice_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notice_contacts):
            request.notice_contacts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not UtilClient.is_unset(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not UtilClient.is_unset(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: scheduler_x320240624_models.UpdateJobRequest,
    ) -> scheduler_x320240624_models.UpdateJobResponse:
        """
        @summary 更新任务信息
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: scheduler_x320240624_models.UpdateJobRequest,
    ) -> scheduler_x320240624_models.UpdateJobResponse:
        """
        @summary 更新任务信息
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)

    def update_job_script_with_options(
        self,
        request: scheduler_x320240624_models.UpdateJobScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateJobScriptResponse:
        """
        @summary 更新任务脚本内容
        
        @param request: UpdateJobScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.script_content):
            body['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJobScript',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateJobScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_script_with_options_async(
        self,
        request: scheduler_x320240624_models.UpdateJobScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scheduler_x320240624_models.UpdateJobScriptResponse:
        """
        @summary 更新任务脚本内容
        
        @param request: UpdateJobScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.script_content):
            body['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJobScript',
            version='2024-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scheduler_x320240624_models.UpdateJobScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job_script(
        self,
        request: scheduler_x320240624_models.UpdateJobScriptRequest,
    ) -> scheduler_x320240624_models.UpdateJobScriptResponse:
        """
        @summary 更新任务脚本内容
        
        @param request: UpdateJobScriptRequest
        @return: UpdateJobScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_job_script_with_options(request, runtime)

    async def update_job_script_async(
        self,
        request: scheduler_x320240624_models.UpdateJobScriptRequest,
    ) -> scheduler_x320240624_models.UpdateJobScriptResponse:
        """
        @summary 更新任务脚本内容
        
        @param request: UpdateJobScriptRequest
        @return: UpdateJobScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_job_script_with_options_async(request, runtime)
