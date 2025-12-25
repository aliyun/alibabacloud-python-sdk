# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_schedulerx320240624 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_app_with_options(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_token):
            body['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_token):
            body['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_calendar_with_options(
        self,
        request: main_models.CreateCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_calendar_with_options_async(
        self,
        request: main_models.CreateCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_calendar(
        self,
        request: main_models.CreateCalendarRequest,
    ) -> main_models.CreateCalendarResponse:
        runtime = RuntimeOptions()
        return self.create_calendar_with_options(request, runtime)

    async def create_calendar_async(
        self,
        request: main_models.CreateCalendarRequest,
    ) -> main_models.CreateCalendarResponse:
        runtime = RuntimeOptions()
        return await self.create_calendar_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.v_switches):
            request.v_switches_shrink = Utils.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.engine_type):
            body['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.v_switches_shrink):
            body['VSwitches'] = request.v_switches_shrink
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.v_switches):
            request.v_switches_shrink = Utils.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.engine_type):
            body['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.v_switches_shrink):
            body['VSwitches'] = request.v_switches_shrink
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_executors_with_options(
        self,
        request: main_models.CreateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExecutorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.worker_type):
            body['WorkerType'] = request.worker_type
        if not DaraCore.is_null(request.workers):
            body['Workers'] = request.workers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_executors_with_options_async(
        self,
        request: main_models.CreateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExecutorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.worker_type):
            body['WorkerType'] = request.worker_type
        if not DaraCore.is_null(request.workers):
            body['Workers'] = request.workers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_executors(
        self,
        request: main_models.CreateExecutorsRequest,
    ) -> main_models.CreateExecutorsResponse:
        runtime = RuntimeOptions()
        return self.create_executors_with_options(request, runtime)

    async def create_executors_async(
        self,
        request: main_models.CreateExecutorsRequest,
    ) -> main_models.CreateExecutorsResponse:
        runtime = RuntimeOptions()
        return await self.create_executors_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        tmp_req.validate()
        request = main_models.CreateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.coordinate):
            request.coordinate_shrink = Utils.array_to_string_with_specified_style(tmp_req.coordinate, 'Coordinate', 'json')
        if not DaraCore.is_null(tmp_req.notice_config):
            request.notice_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not DaraCore.is_null(tmp_req.notice_contacts):
            request.notice_contacts_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.coordinate_shrink):
            body['Coordinate'] = request.coordinate_shrink
        if not DaraCore.is_null(request.dependent_strategy):
            body['DependentStrategy'] = request.dependent_strategy
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not DaraCore.is_null(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not DaraCore.is_null(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not DaraCore.is_null(request.script):
            body['Script'] = request.script
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_type):
            body['StartTimeType'] = request.start_time_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        tmp_req.validate()
        request = main_models.CreateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.coordinate):
            request.coordinate_shrink = Utils.array_to_string_with_specified_style(tmp_req.coordinate, 'Coordinate', 'json')
        if not DaraCore.is_null(tmp_req.notice_config):
            request.notice_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not DaraCore.is_null(tmp_req.notice_contacts):
            request.notice_contacts_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.coordinate_shrink):
            body['Coordinate'] = request.coordinate_shrink
        if not DaraCore.is_null(request.dependent_strategy):
            body['DependentStrategy'] = request.dependent_strategy
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not DaraCore.is_null(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not DaraCore.is_null(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not DaraCore.is_null(request.script):
            body['Script'] = request.script
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_type):
            body['StartTimeType'] = request.start_time_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_workflow_with_options(
        self,
        request: main_models.CreateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_with_options_async(
        self,
        request: main_models.CreateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow(
        self,
        request: main_models.CreateWorkflowRequest,
    ) -> main_models.CreateWorkflowResponse:
        runtime = RuntimeOptions()
        return self.create_workflow_with_options(request, runtime)

    async def create_workflow_async(
        self,
        request: main_models.CreateWorkflowRequest,
    ) -> main_models.CreateWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.create_workflow_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_calendar_with_options(
        self,
        request: main_models.DeleteCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_calendar_with_options_async(
        self,
        request: main_models.DeleteCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_calendar(
        self,
        request: main_models.DeleteCalendarRequest,
    ) -> main_models.DeleteCalendarResponse:
        runtime = RuntimeOptions()
        return self.delete_calendar_with_options(request, runtime)

    async def delete_calendar_async(
        self,
        request: main_models.DeleteCalendarRequest,
    ) -> main_models.DeleteCalendarResponse:
        runtime = RuntimeOptions()
        return await self.delete_calendar_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        tmp_req: main_models.DeleteJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobsResponse:
        tmp_req.validate()
        request = main_models.DeleteJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        tmp_req: main_models.DeleteJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobsResponse:
        tmp_req.validate()
        request = main_models.DeleteJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: main_models.DeleteJobsRequest,
    ) -> main_models.DeleteJobsResponse:
        runtime = RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: main_models.DeleteJobsRequest,
    ) -> main_models.DeleteJobsResponse:
        runtime = RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def delete_workflow_with_options(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.delete_jobs):
            body['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_with_options_async(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.delete_jobs):
            body['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    async def delete_workflow_async(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.delete_workflow_with_options_async(request, runtime)

    def delete_workflows_with_options(
        self,
        tmp_req: main_models.DeleteWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowsResponse:
        tmp_req.validate()
        request = main_models.DeleteWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.delete_jobs):
            body['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflows_with_options_async(
        self,
        tmp_req: main_models.DeleteWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowsResponse:
        tmp_req.validate()
        request = main_models.DeleteWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.delete_jobs):
            body['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflows(
        self,
        request: main_models.DeleteWorkflowsRequest,
    ) -> main_models.DeleteWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.delete_workflows_with_options(request, runtime)

    async def delete_workflows_async(
        self,
        request: main_models.DeleteWorkflowsRequest,
    ) -> main_models.DeleteWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.delete_workflows_with_options_async(request, runtime)

    def export_jobs_with_options(
        self,
        tmp_req: main_models.ExportJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportJobsResponse:
        tmp_req.validate()
        request = main_models.ExportJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.export_job_type):
            body['ExportJobType'] = request.export_job_type
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'byte'
        )
        return DaraCore.from_map(
            main_models.ExportJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_jobs_with_options_async(
        self,
        tmp_req: main_models.ExportJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportJobsResponse:
        tmp_req.validate()
        request = main_models.ExportJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.export_job_type):
            body['ExportJobType'] = request.export_job_type
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'byte'
        )
        return DaraCore.from_map(
            main_models.ExportJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_jobs(
        self,
        request: main_models.ExportJobsRequest,
    ) -> main_models.ExportJobsResponse:
        runtime = RuntimeOptions()
        return self.export_jobs_with_options(request, runtime)

    async def export_jobs_async(
        self,
        request: main_models.ExportJobsRequest,
    ) -> main_models.ExportJobsResponse:
        runtime = RuntimeOptions()
        return await self.export_jobs_with_options_async(request, runtime)

    def export_workflows_with_options(
        self,
        tmp_req: main_models.ExportWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportWorkflowsResponse:
        tmp_req.validate()
        request = main_models.ExportWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_id):
            request.workflow_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_id, 'WorkflowId', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id_shrink):
            body['WorkflowId'] = request.workflow_id_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'byte'
        )
        return DaraCore.from_map(
            main_models.ExportWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_workflows_with_options_async(
        self,
        tmp_req: main_models.ExportWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportWorkflowsResponse:
        tmp_req.validate()
        request = main_models.ExportWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_id):
            request.workflow_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_id, 'WorkflowId', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id_shrink):
            body['WorkflowId'] = request.workflow_id_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'byte'
        )
        return DaraCore.from_map(
            main_models.ExportWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_workflows(
        self,
        request: main_models.ExportWorkflowsRequest,
    ) -> main_models.ExportWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.export_workflows_with_options(request, runtime)

    async def export_workflows_async(
        self,
        request: main_models.ExportWorkflowsRequest,
    ) -> main_models.ExportWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.export_workflows_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: main_models.GetAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: main_models.GetAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: main_models.GetAppRequest,
    ) -> main_models.GetAppResponse:
        runtime = RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: main_models.GetAppRequest,
    ) -> main_models.GetAppResponse:
        runtime = RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_calendar_with_options(
        self,
        request: main_models.GetCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCalendarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_calendar_with_options_async(
        self,
        request: main_models.GetCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCalendarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_calendar(
        self,
        request: main_models.GetCalendarRequest,
    ) -> main_models.GetCalendarResponse:
        runtime = RuntimeOptions()
        return self.get_calendar_with_options(request, runtime)

    async def get_calendar_async(
        self,
        request: main_models.GetCalendarRequest,
    ) -> main_models.GetCalendarResponse:
        runtime = RuntimeOptions()
        return await self.get_calendar_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_desigate_info_with_options(
        self,
        request: main_models.GetDesigateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDesigateInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDesigateInfo',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDesigateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_desigate_info_with_options_async(
        self,
        request: main_models.GetDesigateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDesigateInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDesigateInfo',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDesigateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_desigate_info(
        self,
        request: main_models.GetDesigateInfoRequest,
    ) -> main_models.GetDesigateInfoResponse:
        runtime = RuntimeOptions()
        return self.get_desigate_info_with_options(request, runtime)

    async def get_desigate_info_async(
        self,
        request: main_models.GetDesigateInfoRequest,
    ) -> main_models.GetDesigateInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_desigate_info_with_options_async(request, runtime)

    def get_executor_config_with_options(
        self,
        request: main_models.GetExecutorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutorConfig',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_executor_config_with_options_async(
        self,
        request: main_models.GetExecutorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutorConfig',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_executor_config(
        self,
        request: main_models.GetExecutorConfigRequest,
    ) -> main_models.GetExecutorConfigResponse:
        runtime = RuntimeOptions()
        return self.get_executor_config_with_options(request, runtime)

    async def get_executor_config_async(
        self,
        request: main_models.GetExecutorConfigRequest,
    ) -> main_models.GetExecutorConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_executor_config_with_options_async(request, runtime)

    def get_job_execution_with_options(
        self,
        request: main_models.GetJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.mse_session_id):
            query['MseSessionId'] = request.mse_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_with_options_async(
        self,
        request: main_models.GetJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.mse_session_id):
            query['MseSessionId'] = request.mse_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution(
        self,
        request: main_models.GetJobExecutionRequest,
    ) -> main_models.GetJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.get_job_execution_with_options(request, runtime)

    async def get_job_execution_async(
        self,
        request: main_models.GetJobExecutionRequest,
    ) -> main_models.GetJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.get_job_execution_with_options_async(request, runtime)

    def get_job_execution_progress_with_options(
        self,
        request: main_models.GetJobExecutionProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecutionProgress',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_progress_with_options_async(
        self,
        request: main_models.GetJobExecutionProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecutionProgress',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution_progress(
        self,
        request: main_models.GetJobExecutionProgressRequest,
    ) -> main_models.GetJobExecutionProgressResponse:
        runtime = RuntimeOptions()
        return self.get_job_execution_progress_with_options(request, runtime)

    async def get_job_execution_progress_async(
        self,
        request: main_models.GetJobExecutionProgressRequest,
    ) -> main_models.GetJobExecutionProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_job_execution_progress_with_options_async(request, runtime)

    def get_job_execution_thread_dump_with_options(
        self,
        request: main_models.GetJobExecutionThreadDumpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionThreadDumpResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecutionThreadDump',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionThreadDumpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_execution_thread_dump_with_options_async(
        self,
        request: main_models.GetJobExecutionThreadDumpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobExecutionThreadDumpResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobExecutionThreadDump',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobExecutionThreadDumpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_execution_thread_dump(
        self,
        request: main_models.GetJobExecutionThreadDumpRequest,
    ) -> main_models.GetJobExecutionThreadDumpResponse:
        runtime = RuntimeOptions()
        return self.get_job_execution_thread_dump_with_options(request, runtime)

    async def get_job_execution_thread_dump_async(
        self,
        request: main_models.GetJobExecutionThreadDumpRequest,
    ) -> main_models.GetJobExecutionThreadDumpResponse:
        runtime = RuntimeOptions()
        return await self.get_job_execution_thread_dump_with_options_async(request, runtime)

    def get_log_with_options(
        self,
        request: main_models.GetLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLog',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_with_options_async(
        self,
        request: main_models.GetLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLog',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log(
        self,
        request: main_models.GetLogRequest,
    ) -> main_models.GetLogResponse:
        runtime = RuntimeOptions()
        return self.get_log_with_options(request, runtime)

    async def get_log_async(
        self,
        request: main_models.GetLogRequest,
    ) -> main_models.GetLogResponse:
        runtime = RuntimeOptions()
        return await self.get_log_with_options_async(request, runtime)

    def get_log_event_with_options(
        self,
        request: main_models.GetLogEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_event_with_options_async(
        self,
        request: main_models.GetLogEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_event(
        self,
        request: main_models.GetLogEventRequest,
    ) -> main_models.GetLogEventResponse:
        runtime = RuntimeOptions()
        return self.get_log_event_with_options(request, runtime)

    async def get_log_event_async(
        self,
        request: main_models.GetLogEventRequest,
    ) -> main_models.GetLogEventResponse:
        runtime = RuntimeOptions()
        return await self.get_log_event_with_options_async(request, runtime)

    def get_workflow_with_options(
        self,
        request: main_models.GetWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_with_options_async(
        self,
        request: main_models.GetWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow(
        self,
        request: main_models.GetWorkflowRequest,
    ) -> main_models.GetWorkflowResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_with_options(request, runtime)

    async def get_workflow_async(
        self,
        request: main_models.GetWorkflowRequest,
    ) -> main_models.GetWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_with_options_async(request, runtime)

    def get_workflow_dagwith_options(
        self,
        request: main_models.GetWorkflowDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDAGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDAGResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_dagwith_options_async(
        self,
        request: main_models.GetWorkflowDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDAGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDAGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_dag(
        self,
        request: main_models.GetWorkflowDAGRequest,
    ) -> main_models.GetWorkflowDAGResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_dagwith_options(request, runtime)

    async def get_workflow_dag_async(
        self,
        request: main_models.GetWorkflowDAGRequest,
    ) -> main_models.GetWorkflowDAGResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_dagwith_options_async(request, runtime)

    def get_workflow_dagpreview_with_options(
        self,
        request: main_models.GetWorkflowDAGPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDAGPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_version):
            query['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDAGPreview',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDAGPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_dagpreview_with_options_async(
        self,
        request: main_models.GetWorkflowDAGPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowDAGPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_version):
            query['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowDAGPreview',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowDAGPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_dagpreview(
        self,
        request: main_models.GetWorkflowDAGPreviewRequest,
    ) -> main_models.GetWorkflowDAGPreviewResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_dagpreview_with_options(request, runtime)

    async def get_workflow_dagpreview_async(
        self,
        request: main_models.GetWorkflowDAGPreviewRequest,
    ) -> main_models.GetWorkflowDAGPreviewResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_dagpreview_with_options_async(request, runtime)

    def get_workflow_execution_dagwith_options(
        self,
        request: main_models.GetWorkflowExecutionDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowExecutionDAGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowExecutionDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowExecutionDAGResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_execution_dagwith_options_async(
        self,
        request: main_models.GetWorkflowExecutionDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowExecutionDAGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowExecutionDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowExecutionDAGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_execution_dag(
        self,
        request: main_models.GetWorkflowExecutionDAGRequest,
    ) -> main_models.GetWorkflowExecutionDAGResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_execution_dagwith_options(request, runtime)

    async def get_workflow_execution_dag_async(
        self,
        request: main_models.GetWorkflowExecutionDAGRequest,
    ) -> main_models.GetWorkflowExecutionDAGResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_execution_dagwith_options_async(request, runtime)

    def import_calendar_with_options(
        self,
        request: main_models.ImportCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_calendar_with_options_async(
        self,
        request: main_models.ImportCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_calendar(
        self,
        request: main_models.ImportCalendarRequest,
    ) -> main_models.ImportCalendarResponse:
        runtime = RuntimeOptions()
        return self.import_calendar_with_options(request, runtime)

    async def import_calendar_async(
        self,
        request: main_models.ImportCalendarRequest,
    ) -> main_models.ImportCalendarResponse:
        runtime = RuntimeOptions()
        return await self.import_calendar_with_options_async(request, runtime)

    def import_jobs_with_options(
        self,
        request: main_models.ImportJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_jobs_with_options_async(
        self,
        request: main_models.ImportJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_jobs(
        self,
        request: main_models.ImportJobsRequest,
    ) -> main_models.ImportJobsResponse:
        runtime = RuntimeOptions()
        return self.import_jobs_with_options(request, runtime)

    async def import_jobs_async(
        self,
        request: main_models.ImportJobsRequest,
    ) -> main_models.ImportJobsResponse:
        runtime = RuntimeOptions()
        return await self.import_jobs_with_options_async(request, runtime)

    def import_workflows_with_options(
        self,
        request: main_models.ImportWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportWorkflowsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_workflows_with_options_async(
        self,
        request: main_models.ImportWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportWorkflowsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_app):
            body['AutoCreateApp'] = request.auto_create_app
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_workflows(
        self,
        request: main_models.ImportWorkflowsRequest,
    ) -> main_models.ImportWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.import_workflows_with_options(request, runtime)

    async def import_workflows_async(
        self,
        request: main_models.ImportWorkflowsRequest,
    ) -> main_models.ImportWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.import_workflows_with_options_async(request, runtime)

    def list_alarm_event_with_options(
        self,
        request: main_models.ListAlarmEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarmEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_event_with_options_async(
        self,
        request: main_models.ListAlarmEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarmEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_event(
        self,
        request: main_models.ListAlarmEventRequest,
    ) -> main_models.ListAlarmEventResponse:
        runtime = RuntimeOptions()
        return self.list_alarm_event_with_options(request, runtime)

    async def list_alarm_event_async(
        self,
        request: main_models.ListAlarmEventRequest,
    ) -> main_models.ListAlarmEventResponse:
        runtime = RuntimeOptions()
        return await self.list_alarm_event_with_options_async(request, runtime)

    def list_app_names_with_options(
        self,
        request: main_models.ListAppNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppNamesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppNames',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_names_with_options_async(
        self,
        request: main_models.ListAppNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppNamesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppNames',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_names(
        self,
        request: main_models.ListAppNamesRequest,
    ) -> main_models.ListAppNamesResponse:
        runtime = RuntimeOptions()
        return self.list_app_names_with_options(request, runtime)

    async def list_app_names_async(
        self,
        request: main_models.ListAppNamesRequest,
    ) -> main_models.ListAppNamesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_names_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: main_models.ListAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApps',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: main_models.ListAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApps',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: main_models.ListAppsRequest,
    ) -> main_models.ListAppsResponse:
        runtime = RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: main_models.ListAppsRequest,
    ) -> main_models.ListAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_calendar_names_with_options(
        self,
        request: main_models.ListCalendarNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCalendarNamesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalendarNames',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalendarNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calendar_names_with_options_async(
        self,
        request: main_models.ListCalendarNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCalendarNamesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalendarNames',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalendarNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calendar_names(
        self,
        request: main_models.ListCalendarNamesRequest,
    ) -> main_models.ListCalendarNamesResponse:
        runtime = RuntimeOptions()
        return self.list_calendar_names_with_options(request, runtime)

    async def list_calendar_names_async(
        self,
        request: main_models.ListCalendarNamesRequest,
    ) -> main_models.ListCalendarNamesResponse:
        runtime = RuntimeOptions()
        return await self.list_calendar_names_with_options_async(request, runtime)

    def list_calendars_with_options(
        self,
        request: main_models.ListCalendarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCalendarsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.fetch_calendar_detail):
            query['FetchCalendarDetail'] = request.fetch_calendar_detail
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalendars',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calendars_with_options_async(
        self,
        request: main_models.ListCalendarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCalendarsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.fetch_calendar_detail):
            query['FetchCalendarDetail'] = request.fetch_calendar_detail
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalendars',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalendarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calendars(
        self,
        request: main_models.ListCalendarsRequest,
    ) -> main_models.ListCalendarsResponse:
        runtime = RuntimeOptions()
        return self.list_calendars_with_options(request, runtime)

    async def list_calendars_async(
        self,
        request: main_models.ListCalendarsRequest,
    ) -> main_models.ListCalendarsResponse:
        runtime = RuntimeOptions()
        return await self.list_calendars_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_executors_with_options(
        self,
        request: main_models.ListExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executors_with_options_async(
        self,
        request: main_models.ListExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executors(
        self,
        request: main_models.ListExecutorsRequest,
    ) -> main_models.ListExecutorsResponse:
        runtime = RuntimeOptions()
        return self.list_executors_with_options(request, runtime)

    async def list_executors_async(
        self,
        request: main_models.ListExecutorsRequest,
    ) -> main_models.ListExecutorsResponse:
        runtime = RuntimeOptions()
        return await self.list_executors_with_options_async(request, runtime)

    def list_job_executions_with_options(
        self,
        request: main_models.ListJobExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_executions_with_options_async(
        self,
        request: main_models.ListJobExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_executions(
        self,
        request: main_models.ListJobExecutionsRequest,
    ) -> main_models.ListJobExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_job_executions_with_options(request, runtime)

    async def list_job_executions_async(
        self,
        request: main_models.ListJobExecutionsRequest,
    ) -> main_models.ListJobExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_job_executions_with_options_async(request, runtime)

    def list_job_script_history_with_options(
        self,
        request: main_models.ListJobScriptHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobScriptHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobScriptHistory',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobScriptHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_script_history_with_options_async(
        self,
        request: main_models.ListJobScriptHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobScriptHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobScriptHistory',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobScriptHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_script_history(
        self,
        request: main_models.ListJobScriptHistoryRequest,
    ) -> main_models.ListJobScriptHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_job_script_history_with_options(request, runtime)

    async def list_job_script_history_async(
        self,
        request: main_models.ListJobScriptHistoryRequest,
    ) -> main_models.ListJobScriptHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_job_script_history_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.job_handler):
            query['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.job_handler):
            query['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_k8s_resource_with_options(
        self,
        request: main_models.ListK8sResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sResource',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_resource_with_options_async(
        self,
        request: main_models.ListK8sResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sResource',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_resource(
        self,
        request: main_models.ListK8sResourceRequest,
    ) -> main_models.ListK8sResourceResponse:
        runtime = RuntimeOptions()
        return self.list_k8s_resource_with_options(request, runtime)

    async def list_k8s_resource_async(
        self,
        request: main_models.ListK8sResourceRequest,
    ) -> main_models.ListK8sResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_k8s_resource_with_options_async(request, runtime)

    def list_lables_with_options(
        self,
        request: main_models.ListLablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLablesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLables',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lables_with_options_async(
        self,
        request: main_models.ListLablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLablesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLables',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lables(
        self,
        request: main_models.ListLablesRequest,
    ) -> main_models.ListLablesResponse:
        runtime = RuntimeOptions()
        return self.list_lables_with_options(request, runtime)

    async def list_lables_async(
        self,
        request: main_models.ListLablesRequest,
    ) -> main_models.ListLablesResponse:
        runtime = RuntimeOptions()
        return await self.list_lables_with_options_async(request, runtime)

    def list_region_zone_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionZoneResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegionZone',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_region_zone_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionZoneResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegionZone',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_region_zone(self) -> main_models.ListRegionZoneResponse:
        runtime = RuntimeOptions()
        return self.list_region_zone_with_options(runtime)

    async def list_region_zone_async(self) -> main_models.ListRegionZoneResponse:
        runtime = RuntimeOptions()
        return await self.list_region_zone_with_options_async(runtime)

    def list_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_schedule_event_with_options(
        self,
        request: main_models.ListScheduleEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduleEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduleEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduleEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedule_event_with_options_async(
        self,
        request: main_models.ListScheduleEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduleEventResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduleEvent',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduleEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedule_event(
        self,
        request: main_models.ListScheduleEventRequest,
    ) -> main_models.ListScheduleEventResponse:
        runtime = RuntimeOptions()
        return self.list_schedule_event_with_options(request, runtime)

    async def list_schedule_event_async(
        self,
        request: main_models.ListScheduleEventRequest,
    ) -> main_models.ListScheduleEventResponse:
        runtime = RuntimeOptions()
        return await self.list_schedule_event_with_options_async(request, runtime)

    def list_schedule_times_with_options(
        self,
        request: main_models.ListScheduleTimesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduleTimesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduleTimes',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduleTimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedule_times_with_options_async(
        self,
        request: main_models.ListScheduleTimesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduleTimesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduleTimes',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduleTimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedule_times(
        self,
        request: main_models.ListScheduleTimesRequest,
    ) -> main_models.ListScheduleTimesResponse:
        runtime = RuntimeOptions()
        return self.list_schedule_times_with_options(request, runtime)

    async def list_schedule_times_async(
        self,
        request: main_models.ListScheduleTimesRequest,
    ) -> main_models.ListScheduleTimesResponse:
        runtime = RuntimeOptions()
        return await self.list_schedule_times_with_options_async(request, runtime)

    def list_workflow_executions_with_options(
        self,
        request: main_models.ListWorkflowExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_name):
            query['WorkflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowExecutions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_executions_with_options_async(
        self,
        request: main_models.ListWorkflowExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_execution_id):
            query['WorkflowExecutionId'] = request.workflow_execution_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        if not DaraCore.is_null(request.workflow_name):
            query['WorkflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowExecutions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_executions(
        self,
        request: main_models.ListWorkflowExecutionsRequest,
    ) -> main_models.ListWorkflowExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_workflow_executions_with_options(request, runtime)

    async def list_workflow_executions_async(
        self,
        request: main_models.ListWorkflowExecutionsRequest,
    ) -> main_models.ListWorkflowExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_workflow_executions_with_options_async(request, runtime)

    def list_workflow_versions_with_options(
        self,
        request: main_models.ListWorkflowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowVersions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_versions_with_options_async(
        self,
        request: main_models.ListWorkflowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowVersions',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_versions(
        self,
        request: main_models.ListWorkflowVersionsRequest,
    ) -> main_models.ListWorkflowVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_workflow_versions_with_options(request, runtime)

    async def list_workflow_versions_async(
        self,
        request: main_models.ListWorkflowVersionsRequest,
    ) -> main_models.ListWorkflowVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_workflow_versions_with_options_async(request, runtime)

    def list_workflows_with_options(
        self,
        request: main_models.ListWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflows_with_options_async(
        self,
        request: main_models.ListWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflows(
        self,
        request: main_models.ListWorkflowsRequest,
    ) -> main_models.ListWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.list_workflows_with_options(request, runtime)

    async def list_workflows_async(
        self,
        request: main_models.ListWorkflowsRequest,
    ) -> main_models.ListWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.list_workflows_with_options_async(request, runtime)

    def operate_backfill_workflow_with_options(
        self,
        request: main_models.OperateBackfillWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBackfillWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateBackfillWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBackfillWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_backfill_workflow_with_options_async(
        self,
        request: main_models.OperateBackfillWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBackfillWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateBackfillWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBackfillWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_backfill_workflow(
        self,
        request: main_models.OperateBackfillWorkflowRequest,
    ) -> main_models.OperateBackfillWorkflowResponse:
        runtime = RuntimeOptions()
        return self.operate_backfill_workflow_with_options(request, runtime)

    async def operate_backfill_workflow_async(
        self,
        request: main_models.OperateBackfillWorkflowRequest,
    ) -> main_models.OperateBackfillWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.operate_backfill_workflow_with_options_async(request, runtime)

    def operate_designate_executors_with_options(
        self,
        tmp_req: main_models.OperateDesignateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDesignateExecutorsResponse:
        tmp_req.validate()
        request = main_models.OperateDesignateExecutorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address_list):
            request.address_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.address_list, 'AddressList', 'json')
        body = {}
        if not DaraCore.is_null(request.address_list_shrink):
            body['AddressList'] = request.address_list_shrink
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.designate_type):
            body['DesignateType'] = request.designate_type
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.transferable):
            body['Transferable'] = request.transferable
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDesignateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDesignateExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_designate_executors_with_options_async(
        self,
        tmp_req: main_models.OperateDesignateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDesignateExecutorsResponse:
        tmp_req.validate()
        request = main_models.OperateDesignateExecutorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address_list):
            request.address_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.address_list, 'AddressList', 'json')
        body = {}
        if not DaraCore.is_null(request.address_list_shrink):
            body['AddressList'] = request.address_list_shrink
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.designate_type):
            body['DesignateType'] = request.designate_type
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.transferable):
            body['Transferable'] = request.transferable
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDesignateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDesignateExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_designate_executors(
        self,
        request: main_models.OperateDesignateExecutorsRequest,
    ) -> main_models.OperateDesignateExecutorsResponse:
        runtime = RuntimeOptions()
        return self.operate_designate_executors_with_options(request, runtime)

    async def operate_designate_executors_async(
        self,
        request: main_models.OperateDesignateExecutorsRequest,
    ) -> main_models.OperateDesignateExecutorsResponse:
        runtime = RuntimeOptions()
        return await self.operate_designate_executors_with_options_async(request, runtime)

    def operate_disable_jobs_with_options(
        self,
        tmp_req: main_models.OperateDisableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDisableJobsResponse:
        tmp_req.validate()
        request = main_models.OperateDisableJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDisableJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_disable_jobs_with_options_async(
        self,
        tmp_req: main_models.OperateDisableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDisableJobsResponse:
        tmp_req.validate()
        request = main_models.OperateDisableJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDisableJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDisableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_disable_jobs(
        self,
        request: main_models.OperateDisableJobsRequest,
    ) -> main_models.OperateDisableJobsResponse:
        runtime = RuntimeOptions()
        return self.operate_disable_jobs_with_options(request, runtime)

    async def operate_disable_jobs_async(
        self,
        request: main_models.OperateDisableJobsRequest,
    ) -> main_models.OperateDisableJobsResponse:
        runtime = RuntimeOptions()
        return await self.operate_disable_jobs_with_options_async(request, runtime)

    def operate_disable_workflows_with_options(
        self,
        tmp_req: main_models.OperateDisableWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDisableWorkflowsResponse:
        tmp_req.validate()
        request = main_models.OperateDisableWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDisableWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDisableWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_disable_workflows_with_options_async(
        self,
        tmp_req: main_models.OperateDisableWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateDisableWorkflowsResponse:
        tmp_req.validate()
        request = main_models.OperateDisableWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateDisableWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateDisableWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_disable_workflows(
        self,
        request: main_models.OperateDisableWorkflowsRequest,
    ) -> main_models.OperateDisableWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.operate_disable_workflows_with_options(request, runtime)

    async def operate_disable_workflows_async(
        self,
        request: main_models.OperateDisableWorkflowsRequest,
    ) -> main_models.OperateDisableWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.operate_disable_workflows_with_options_async(request, runtime)

    def operate_enable_jobs_with_options(
        self,
        tmp_req: main_models.OperateEnableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateEnableJobsResponse:
        tmp_req.validate()
        request = main_models.OperateEnableJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateEnableJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_enable_jobs_with_options_async(
        self,
        tmp_req: main_models.OperateEnableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateEnableJobsResponse:
        tmp_req.validate()
        request = main_models.OperateEnableJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateEnableJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateEnableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_enable_jobs(
        self,
        request: main_models.OperateEnableJobsRequest,
    ) -> main_models.OperateEnableJobsResponse:
        runtime = RuntimeOptions()
        return self.operate_enable_jobs_with_options(request, runtime)

    async def operate_enable_jobs_async(
        self,
        request: main_models.OperateEnableJobsRequest,
    ) -> main_models.OperateEnableJobsResponse:
        runtime = RuntimeOptions()
        return await self.operate_enable_jobs_with_options_async(request, runtime)

    def operate_enable_workflows_with_options(
        self,
        tmp_req: main_models.OperateEnableWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateEnableWorkflowsResponse:
        tmp_req.validate()
        request = main_models.OperateEnableWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateEnableWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateEnableWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_enable_workflows_with_options_async(
        self,
        tmp_req: main_models.OperateEnableWorkflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateEnableWorkflowsResponse:
        tmp_req.validate()
        request = main_models.OperateEnableWorkflowsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.workflow_ids):
            request.workflow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_ids_shrink):
            body['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateEnableWorkflows',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateEnableWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_enable_workflows(
        self,
        request: main_models.OperateEnableWorkflowsRequest,
    ) -> main_models.OperateEnableWorkflowsResponse:
        runtime = RuntimeOptions()
        return self.operate_enable_workflows_with_options(request, runtime)

    async def operate_enable_workflows_async(
        self,
        request: main_models.OperateEnableWorkflowsRequest,
    ) -> main_models.OperateEnableWorkflowsResponse:
        runtime = RuntimeOptions()
        return await self.operate_enable_workflows_with_options_async(request, runtime)

    def operate_execute_job_with_options(
        self,
        request: main_models.OperateExecuteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateExecuteJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_parameters):
            body['InstanceParameters'] = request.instance_parameters
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.worker):
            body['Worker'] = request.worker
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateExecuteJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_execute_job_with_options_async(
        self,
        request: main_models.OperateExecuteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateExecuteJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_parameters):
            body['InstanceParameters'] = request.instance_parameters
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.worker):
            body['Worker'] = request.worker
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateExecuteJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateExecuteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_execute_job(
        self,
        request: main_models.OperateExecuteJobRequest,
    ) -> main_models.OperateExecuteJobResponse:
        runtime = RuntimeOptions()
        return self.operate_execute_job_with_options(request, runtime)

    async def operate_execute_job_async(
        self,
        request: main_models.OperateExecuteJobRequest,
    ) -> main_models.OperateExecuteJobResponse:
        runtime = RuntimeOptions()
        return await self.operate_execute_job_with_options_async(request, runtime)

    def operate_execute_workflow_with_options(
        self,
        request: main_models.OperateExecuteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateExecuteWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateExecuteWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateExecuteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_execute_workflow_with_options_async(
        self,
        request: main_models.OperateExecuteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateExecuteWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateExecuteWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateExecuteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_execute_workflow(
        self,
        request: main_models.OperateExecuteWorkflowRequest,
    ) -> main_models.OperateExecuteWorkflowResponse:
        runtime = RuntimeOptions()
        return self.operate_execute_workflow_with_options(request, runtime)

    async def operate_execute_workflow_async(
        self,
        request: main_models.OperateExecuteWorkflowRequest,
    ) -> main_models.OperateExecuteWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.operate_execute_workflow_with_options_async(request, runtime)

    def operate_hold_job_execution_with_options(
        self,
        request: main_models.OperateHoldJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateHoldJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateHoldJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateHoldJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_hold_job_execution_with_options_async(
        self,
        request: main_models.OperateHoldJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateHoldJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateHoldJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateHoldJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_hold_job_execution(
        self,
        request: main_models.OperateHoldJobExecutionRequest,
    ) -> main_models.OperateHoldJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_hold_job_execution_with_options(request, runtime)

    async def operate_hold_job_execution_async(
        self,
        request: main_models.OperateHoldJobExecutionRequest,
    ) -> main_models.OperateHoldJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_hold_job_execution_with_options_async(request, runtime)

    def operate_hold_workflow_execution_with_options(
        self,
        request: main_models.OperateHoldWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateHoldWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateHoldWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateHoldWorkflowExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_hold_workflow_execution_with_options_async(
        self,
        request: main_models.OperateHoldWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateHoldWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateHoldWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateHoldWorkflowExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_hold_workflow_execution(
        self,
        request: main_models.OperateHoldWorkflowExecutionRequest,
    ) -> main_models.OperateHoldWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_hold_workflow_execution_with_options(request, runtime)

    async def operate_hold_workflow_execution_async(
        self,
        request: main_models.OperateHoldWorkflowExecutionRequest,
    ) -> main_models.OperateHoldWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_hold_workflow_execution_with_options_async(request, runtime)

    def operate_mark_success_job_execution_with_options(
        self,
        request: main_models.OperateMarkSuccessJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateMarkSuccessJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateMarkSuccessJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateMarkSuccessJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_mark_success_job_execution_with_options_async(
        self,
        request: main_models.OperateMarkSuccessJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateMarkSuccessJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateMarkSuccessJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateMarkSuccessJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_mark_success_job_execution(
        self,
        request: main_models.OperateMarkSuccessJobExecutionRequest,
    ) -> main_models.OperateMarkSuccessJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_mark_success_job_execution_with_options(request, runtime)

    async def operate_mark_success_job_execution_async(
        self,
        request: main_models.OperateMarkSuccessJobExecutionRequest,
    ) -> main_models.OperateMarkSuccessJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_mark_success_job_execution_with_options_async(request, runtime)

    def operate_mark_success_workflow_execution_with_options(
        self,
        request: main_models.OperateMarkSuccessWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateMarkSuccessWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateMarkSuccessWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateMarkSuccessWorkflowExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_mark_success_workflow_execution_with_options_async(
        self,
        request: main_models.OperateMarkSuccessWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateMarkSuccessWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateMarkSuccessWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateMarkSuccessWorkflowExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_mark_success_workflow_execution(
        self,
        request: main_models.OperateMarkSuccessWorkflowExecutionRequest,
    ) -> main_models.OperateMarkSuccessWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_mark_success_workflow_execution_with_options(request, runtime)

    async def operate_mark_success_workflow_execution_async(
        self,
        request: main_models.OperateMarkSuccessWorkflowExecutionRequest,
    ) -> main_models.OperateMarkSuccessWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_mark_success_workflow_execution_with_options_async(request, runtime)

    def operate_rerun_job_with_options(
        self,
        request: main_models.OperateRerunJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRerunJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_time):
            query['DataTime'] = request.data_time
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateRerunJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_rerun_job_with_options_async(
        self,
        request: main_models.OperateRerunJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRerunJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_time):
            query['DataTime'] = request.data_time
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateRerunJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRerunJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_rerun_job(
        self,
        request: main_models.OperateRerunJobRequest,
    ) -> main_models.OperateRerunJobResponse:
        runtime = RuntimeOptions()
        return self.operate_rerun_job_with_options(request, runtime)

    async def operate_rerun_job_async(
        self,
        request: main_models.OperateRerunJobRequest,
    ) -> main_models.OperateRerunJobResponse:
        runtime = RuntimeOptions()
        return await self.operate_rerun_job_with_options_async(request, runtime)

    def operate_retry_job_execution_with_options(
        self,
        tmp_req: main_models.OperateRetryJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRetryJobExecutionResponse:
        tmp_req.validate()
        request = main_models.OperateRetryJobExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_list):
            request.task_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        if not DaraCore.is_null(request.trigger_child):
            query['TriggerChild'] = request.trigger_child
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateRetryJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRetryJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_retry_job_execution_with_options_async(
        self,
        tmp_req: main_models.OperateRetryJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRetryJobExecutionResponse:
        tmp_req.validate()
        request = main_models.OperateRetryJobExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_list):
            request.task_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        if not DaraCore.is_null(request.trigger_child):
            query['TriggerChild'] = request.trigger_child
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateRetryJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRetryJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_retry_job_execution(
        self,
        request: main_models.OperateRetryJobExecutionRequest,
    ) -> main_models.OperateRetryJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_retry_job_execution_with_options(request, runtime)

    async def operate_retry_job_execution_async(
        self,
        request: main_models.OperateRetryJobExecutionRequest,
    ) -> main_models.OperateRetryJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_retry_job_execution_with_options_async(request, runtime)

    def operate_retry_workflow_execution_with_options(
        self,
        request: main_models.OperateRetryWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRetryWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.only_failed):
            body['OnlyFailed'] = request.only_failed
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateRetryWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRetryWorkflowExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_retry_workflow_execution_with_options_async(
        self,
        request: main_models.OperateRetryWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateRetryWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.only_failed):
            body['OnlyFailed'] = request.only_failed
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateRetryWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateRetryWorkflowExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_retry_workflow_execution(
        self,
        request: main_models.OperateRetryWorkflowExecutionRequest,
    ) -> main_models.OperateRetryWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_retry_workflow_execution_with_options(request, runtime)

    async def operate_retry_workflow_execution_async(
        self,
        request: main_models.OperateRetryWorkflowExecutionRequest,
    ) -> main_models.OperateRetryWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_retry_workflow_execution_with_options_async(request, runtime)

    def operate_skip_job_execution_with_options(
        self,
        request: main_models.OperateSkipJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateSkipJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateSkipJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateSkipJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_skip_job_execution_with_options_async(
        self,
        request: main_models.OperateSkipJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateSkipJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateSkipJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateSkipJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_skip_job_execution(
        self,
        request: main_models.OperateSkipJobExecutionRequest,
    ) -> main_models.OperateSkipJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_skip_job_execution_with_options(request, runtime)

    async def operate_skip_job_execution_async(
        self,
        request: main_models.OperateSkipJobExecutionRequest,
    ) -> main_models.OperateSkipJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_skip_job_execution_with_options_async(request, runtime)

    def operate_stop_job_execution_with_options(
        self,
        tmp_req: main_models.OperateStopJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateStopJobExecutionResponse:
        tmp_req.validate()
        request = main_models.OperateStopJobExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_list):
            request.task_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateStopJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateStopJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_stop_job_execution_with_options_async(
        self,
        tmp_req: main_models.OperateStopJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateStopJobExecutionResponse:
        tmp_req.validate()
        request = main_models.OperateStopJobExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_list):
            request.task_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_list, 'TaskList', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        if not DaraCore.is_null(request.task_list_shrink):
            query['TaskList'] = request.task_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateStopJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateStopJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_stop_job_execution(
        self,
        request: main_models.OperateStopJobExecutionRequest,
    ) -> main_models.OperateStopJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_stop_job_execution_with_options(request, runtime)

    async def operate_stop_job_execution_async(
        self,
        request: main_models.OperateStopJobExecutionRequest,
    ) -> main_models.OperateStopJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_stop_job_execution_with_options_async(request, runtime)

    def operate_stop_workflow_execution_with_options(
        self,
        request: main_models.OperateStopWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateStopWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateStopWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateStopWorkflowExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_stop_workflow_execution_with_options_async(
        self,
        request: main_models.OperateStopWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateStopWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateStopWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateStopWorkflowExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_stop_workflow_execution(
        self,
        request: main_models.OperateStopWorkflowExecutionRequest,
    ) -> main_models.OperateStopWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_stop_workflow_execution_with_options(request, runtime)

    async def operate_stop_workflow_execution_async(
        self,
        request: main_models.OperateStopWorkflowExecutionRequest,
    ) -> main_models.OperateStopWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_stop_workflow_execution_with_options_async(request, runtime)

    def operate_unhold_job_execution_with_options(
        self,
        request: main_models.OperateUnholdJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnholdJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnholdJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnholdJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_unhold_job_execution_with_options_async(
        self,
        request: main_models.OperateUnholdJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnholdJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnholdJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnholdJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_unhold_job_execution(
        self,
        request: main_models.OperateUnholdJobExecutionRequest,
    ) -> main_models.OperateUnholdJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_unhold_job_execution_with_options(request, runtime)

    async def operate_unhold_job_execution_async(
        self,
        request: main_models.OperateUnholdJobExecutionRequest,
    ) -> main_models.OperateUnholdJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_unhold_job_execution_with_options_async(request, runtime)

    def operate_unhold_workflow_execution_with_options(
        self,
        request: main_models.OperateUnholdWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnholdWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnholdWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnholdWorkflowExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_unhold_workflow_execution_with_options_async(
        self,
        request: main_models.OperateUnholdWorkflowExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnholdWorkflowExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.workflow_execution_id):
            body['WorkflowExecutionId'] = request.workflow_execution_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnholdWorkflowExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnholdWorkflowExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_unhold_workflow_execution(
        self,
        request: main_models.OperateUnholdWorkflowExecutionRequest,
    ) -> main_models.OperateUnholdWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_unhold_workflow_execution_with_options(request, runtime)

    async def operate_unhold_workflow_execution_async(
        self,
        request: main_models.OperateUnholdWorkflowExecutionRequest,
    ) -> main_models.OperateUnholdWorkflowExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_unhold_workflow_execution_with_options_async(request, runtime)

    def operate_unskip_job_execution_with_options(
        self,
        request: main_models.OperateUnskipJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnskipJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnskipJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnskipJobExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_unskip_job_execution_with_options_async(
        self,
        request: main_models.OperateUnskipJobExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateUnskipJobExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_execution_id):
            query['JobExecutionId'] = request.job_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateUnskipJobExecution',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateUnskipJobExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_unskip_job_execution(
        self,
        request: main_models.OperateUnskipJobExecutionRequest,
    ) -> main_models.OperateUnskipJobExecutionResponse:
        runtime = RuntimeOptions()
        return self.operate_unskip_job_execution_with_options(request, runtime)

    async def operate_unskip_job_execution_async(
        self,
        request: main_models.OperateUnskipJobExecutionRequest,
    ) -> main_models.OperateUnskipJobExecutionResponse:
        runtime = RuntimeOptions()
        return await self.operate_unskip_job_execution_with_options_async(request, runtime)

    def sync_jobs_with_options(
        self,
        tmp_req: main_models.SyncJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncJobsResponse:
        tmp_req.validate()
        request = main_models.SyncJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        if not DaraCore.is_null(request.original_app_name):
            body['OriginalAppName'] = request.original_app_name
        if not DaraCore.is_null(request.original_cluster_id):
            body['OriginalClusterId'] = request.original_cluster_id
        if not DaraCore.is_null(request.target_app_name):
            body['TargetAppName'] = request.target_app_name
        if not DaraCore.is_null(request.target_cluster_id):
            body['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_jobs_with_options_async(
        self,
        tmp_req: main_models.SyncJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncJobsResponse:
        tmp_req.validate()
        request = main_models.SyncJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not DaraCore.is_null(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        if not DaraCore.is_null(request.original_app_name):
            body['OriginalAppName'] = request.original_app_name
        if not DaraCore.is_null(request.original_cluster_id):
            body['OriginalClusterId'] = request.original_cluster_id
        if not DaraCore.is_null(request.target_app_name):
            body['TargetAppName'] = request.target_app_name
        if not DaraCore.is_null(request.target_cluster_id):
            body['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncJobs',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_jobs(
        self,
        request: main_models.SyncJobsRequest,
    ) -> main_models.SyncJobsResponse:
        runtime = RuntimeOptions()
        return self.sync_jobs_with_options(request, runtime)

    async def sync_jobs_async(
        self,
        request: main_models.SyncJobsRequest,
    ) -> main_models.SyncJobsResponse:
        runtime = RuntimeOptions()
        return await self.sync_jobs_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: main_models.UpdateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_token):
            body['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: main_models.UpdateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_token):
            body['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_log):
            body['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.label_route_strategy):
            body['LabelRouteStrategy'] = request.label_route_strategy
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApp',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: main_models.UpdateAppRequest,
    ) -> main_models.UpdateAppResponse:
        runtime = RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: main_models.UpdateAppRequest,
    ) -> main_models.UpdateAppResponse:
        runtime = RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_calendar_with_options(
        self,
        request: main_models.UpdateCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.incremental):
            body['Incremental'] = request.incremental
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_calendar_with_options_async(
        self,
        request: main_models.UpdateCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.incremental):
            body['Incremental'] = request.incremental
        if not DaraCore.is_null(request.months):
            body['Months'] = request.months
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCalendar',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_calendar(
        self,
        request: main_models.UpdateCalendarRequest,
    ) -> main_models.UpdateCalendarResponse:
        runtime = RuntimeOptions()
        return self.update_calendar_with_options(request, runtime)

    async def update_calendar_async(
        self,
        request: main_models.UpdateCalendarRequest,
    ) -> main_models.UpdateCalendarResponse:
        runtime = RuntimeOptions()
        return await self.update_calendar_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        request: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        request: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_executors_with_options(
        self,
        request: main_models.UpdateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExecutorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.worker_type):
            body['WorkerType'] = request.worker_type
        if not DaraCore.is_null(request.workers):
            body['Workers'] = request.workers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_executors_with_options_async(
        self,
        request: main_models.UpdateExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExecutorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.worker_type):
            body['WorkerType'] = request.worker_type
        if not DaraCore.is_null(request.workers):
            body['Workers'] = request.workers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExecutors',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_executors(
        self,
        request: main_models.UpdateExecutorsRequest,
    ) -> main_models.UpdateExecutorsResponse:
        runtime = RuntimeOptions()
        return self.update_executors_with_options(request, runtime)

    async def update_executors_async(
        self,
        request: main_models.UpdateExecutorsRequest,
    ) -> main_models.UpdateExecutorsResponse:
        runtime = RuntimeOptions()
        return await self.update_executors_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        tmp_req: main_models.UpdateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        tmp_req.validate()
        request = main_models.UpdateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notice_config):
            request.notice_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not DaraCore.is_null(tmp_req.notice_contacts):
            request.notice_contacts_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dependent_strategy):
            body['DependentStrategy'] = request.dependent_strategy
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not DaraCore.is_null(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not DaraCore.is_null(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not DaraCore.is_null(request.script):
            body['Script'] = request.script
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_type):
            body['StartTimeType'] = request.start_time_type
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        tmp_req: main_models.UpdateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        tmp_req.validate()
        request = main_models.UpdateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notice_config):
            request.notice_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_config, 'NoticeConfig', 'json')
        if not DaraCore.is_null(tmp_req.notice_contacts):
            request.notice_contacts_shrink = Utils.array_to_string_with_specified_style(tmp_req.notice_contacts, 'NoticeContacts', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.child_job_id):
            body['ChildJobId'] = request.child_job_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dependent_strategy):
            body['DependentStrategy'] = request.dependent_strategy
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.executor_block_strategy):
            body['ExecutorBlockStrategy'] = request.executor_block_strategy
        if not DaraCore.is_null(request.job_handler):
            body['JobHandler'] = request.job_handler
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notice_config_shrink):
            body['NoticeConfig'] = request.notice_config_shrink
        if not DaraCore.is_null(request.notice_contacts_shrink):
            body['NoticeContacts'] = request.notice_contacts_shrink
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.route_strategy):
            body['RouteStrategy'] = request.route_strategy
        if not DaraCore.is_null(request.script):
            body['Script'] = request.script
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_type):
            body['StartTimeType'] = request.start_time_type
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)

    def update_job_script_with_options(
        self,
        request: main_models.UpdateJobScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.script_content):
            body['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobScript',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_script_with_options_async(
        self,
        request: main_models.UpdateJobScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.script_content):
            body['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobScript',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job_script(
        self,
        request: main_models.UpdateJobScriptRequest,
    ) -> main_models.UpdateJobScriptResponse:
        runtime = RuntimeOptions()
        return self.update_job_script_with_options(request, runtime)

    async def update_job_script_async(
        self,
        request: main_models.UpdateJobScriptRequest,
    ) -> main_models.UpdateJobScriptResponse:
        runtime = RuntimeOptions()
        return await self.update_job_script_with_options_async(request, runtime)

    def update_workflow_with_options(
        self,
        request: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_with_options_async(
        self,
        request: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_with_options(request, runtime)

    async def update_workflow_async(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_with_options_async(request, runtime)

    def update_workflow_dagwith_options(
        self,
        tmp_req: main_models.UpdateWorkflowDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDAGResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkflowDAGShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dag):
            request.dag_shrink = Utils.array_to_string_with_specified_style(tmp_req.dag, 'Dag', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_shrink):
            body['Dag'] = request.dag_shrink
        if not DaraCore.is_null(request.dag_version):
            body['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDAGResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_dagwith_options_async(
        self,
        tmp_req: main_models.UpdateWorkflowDAGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDAGResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkflowDAGShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dag):
            request.dag_shrink = Utils.array_to_string_with_specified_style(tmp_req.dag, 'Dag', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_shrink):
            body['Dag'] = request.dag_shrink
        if not DaraCore.is_null(request.dag_version):
            body['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDAG',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDAGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_dag(
        self,
        request: main_models.UpdateWorkflowDAGRequest,
    ) -> main_models.UpdateWorkflowDAGResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_dagwith_options(request, runtime)

    async def update_workflow_dag_async(
        self,
        request: main_models.UpdateWorkflowDAGRequest,
    ) -> main_models.UpdateWorkflowDAGResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_dagwith_options_async(request, runtime)

    def update_workflow_dagversion_with_options(
        self,
        request: main_models.UpdateWorkflowDAGVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDAGVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_version):
            body['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDAGVersion',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDAGVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_dagversion_with_options_async(
        self,
        request: main_models.UpdateWorkflowDAGVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDAGVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dag_version):
            body['DagVersion'] = request.dag_version
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDAGVersion',
            version = '2024-06-24',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDAGVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_dagversion(
        self,
        request: main_models.UpdateWorkflowDAGVersionRequest,
    ) -> main_models.UpdateWorkflowDAGVersionResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_dagversion_with_options(request, runtime)

    async def update_workflow_dagversion_async(
        self,
        request: main_models.UpdateWorkflowDAGVersionRequest,
    ) -> main_models.UpdateWorkflowDAGVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_dagversion_with_options_async(request, runtime)
