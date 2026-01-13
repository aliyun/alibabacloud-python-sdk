# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ehpcinstant20230701 import models as main_models
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
        self._endpoint = self.get_endpoint('ehpcinstant', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image_with_options(
        self,
        tmp_req: main_models.AddImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        tmp_req.validate()
        request = main_models.AddImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.container_image_spec):
            request.container_image_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.container_image_spec, 'ContainerImageSpec', 'json')
        if not DaraCore.is_null(tmp_req.vmimage_spec):
            request.vmimage_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.vmimage_spec, 'VMImageSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.container_image_spec_shrink):
            query['ContainerImageSpec'] = request.container_image_spec_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.image_version):
            query['ImageVersion'] = request.image_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.vmimage_spec_shrink):
            query['VMImageSpec'] = request.vmimage_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        tmp_req: main_models.AddImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageResponse:
        tmp_req.validate()
        request = main_models.AddImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.container_image_spec):
            request.container_image_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.container_image_spec, 'ContainerImageSpec', 'json')
        if not DaraCore.is_null(tmp_req.vmimage_spec):
            request.vmimage_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.vmimage_spec, 'VMImageSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.container_image_spec_shrink):
            query['ContainerImageSpec'] = request.container_image_spec_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.image_version):
            query['ImageVersion'] = request.image_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.vmimage_spec_shrink):
            query['VMImageSpec'] = request.vmimage_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    async def add_image_async(
        self,
        request: main_models.AddImageRequest,
    ) -> main_models.AddImageResponse:
        runtime = RuntimeOptions()
        return await self.add_image_with_options_async(request, runtime)

    def create_action_plan_with_options(
        self,
        tmp_req: main_models.CreateActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateActionPlanResponse:
        tmp_req.validate()
        request = main_models.CreateActionPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.regions):
            request.regions_shrink = Utils.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        query = {}
        if not DaraCore.is_null(request.action_plan_name):
            query['ActionPlanName'] = request.action_plan_name
        if not DaraCore.is_null(request.allocation_spec):
            query['AllocationSpec'] = request.allocation_spec
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.interval_minutes):
            query['IntervalMinutes'] = request.interval_minutes
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.prolog_script):
            query['PrologScript'] = request.prolog_script
        if not DaraCore.is_null(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resources_shrink):
            query['Resources'] = request.resources_shrink
        if not DaraCore.is_null(request.script):
            query['Script'] = request.script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_action_plan_with_options_async(
        self,
        tmp_req: main_models.CreateActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateActionPlanResponse:
        tmp_req.validate()
        request = main_models.CreateActionPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.regions):
            request.regions_shrink = Utils.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        if not DaraCore.is_null(tmp_req.resources):
            request.resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        query = {}
        if not DaraCore.is_null(request.action_plan_name):
            query['ActionPlanName'] = request.action_plan_name
        if not DaraCore.is_null(request.allocation_spec):
            query['AllocationSpec'] = request.allocation_spec
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.interval_minutes):
            query['IntervalMinutes'] = request.interval_minutes
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.prolog_script):
            query['PrologScript'] = request.prolog_script
        if not DaraCore.is_null(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resources_shrink):
            query['Resources'] = request.resources_shrink
        if not DaraCore.is_null(request.script):
            query['Script'] = request.script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_action_plan(
        self,
        request: main_models.CreateActionPlanRequest,
    ) -> main_models.CreateActionPlanResponse:
        runtime = RuntimeOptions()
        return self.create_action_plan_with_options(request, runtime)

    async def create_action_plan_async(
        self,
        request: main_models.CreateActionPlanRequest,
    ) -> main_models.CreateActionPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_action_plan_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        tmp_req.validate()
        request = main_models.CreateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dependency_policy):
            request.dependency_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependency_policy, 'DependencyPolicy', 'json')
        if not DaraCore.is_null(tmp_req.deployment_policy):
            request.deployment_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_policy, 'DeploymentPolicy', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        query = {}
        if not DaraCore.is_null(request.dependency_policy_shrink):
            query['DependencyPolicy'] = request.dependency_policy_shrink
        if not DaraCore.is_null(request.deployment_policy_shrink):
            query['DeploymentPolicy'] = request.deployment_policy_shrink
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not DaraCore.is_null(request.security_policy_shrink):
            query['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.tasks_shrink):
            query['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2023-07-01',
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
        if not DaraCore.is_null(tmp_req.dependency_policy):
            request.dependency_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dependency_policy, 'DependencyPolicy', 'json')
        if not DaraCore.is_null(tmp_req.deployment_policy):
            request.deployment_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_policy, 'DeploymentPolicy', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        query = {}
        if not DaraCore.is_null(request.dependency_policy_shrink):
            query['DependencyPolicy'] = request.dependency_policy_shrink
        if not DaraCore.is_null(request.deployment_policy_shrink):
            query['DeploymentPolicy'] = request.deployment_policy_shrink
        if not DaraCore.is_null(request.job_description):
            query['JobDescription'] = request.job_description
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not DaraCore.is_null(request.security_policy_shrink):
            query['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.tasks_shrink):
            query['Tasks'] = request.tasks_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2023-07-01',
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

    def create_pool_with_options(
        self,
        tmp_req: main_models.CreatePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePoolResponse:
        tmp_req.validate()
        request = main_models.CreatePoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_limits):
            request.resource_limits_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pool_with_options_async(
        self,
        tmp_req: main_models.CreatePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePoolResponse:
        tmp_req.validate()
        request = main_models.CreatePoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_limits):
            request.resource_limits_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pool(
        self,
        request: main_models.CreatePoolRequest,
    ) -> main_models.CreatePoolResponse:
        runtime = RuntimeOptions()
        return self.create_pool_with_options(request, runtime)

    async def create_pool_async(
        self,
        request: main_models.CreatePoolRequest,
    ) -> main_models.CreatePoolResponse:
        runtime = RuntimeOptions()
        return await self.create_pool_with_options_async(request, runtime)

    def delete_action_plan_with_options(
        self,
        request: main_models.DeleteActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_action_plan_with_options_async(
        self,
        request: main_models.DeleteActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_action_plan(
        self,
        request: main_models.DeleteActionPlanRequest,
    ) -> main_models.DeleteActionPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_action_plan_with_options(request, runtime)

    async def delete_action_plan_async(
        self,
        request: main_models.DeleteActionPlanRequest,
    ) -> main_models.DeleteActionPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_action_plan_with_options_async(request, runtime)

    def delete_job_records_with_options(
        self,
        tmp_req: main_models.DeleteJobRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobRecordsResponse:
        tmp_req.validate()
        request = main_models.DeleteJobRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not DaraCore.is_null(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobRecords',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_records_with_options_async(
        self,
        tmp_req: main_models.DeleteJobRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobRecordsResponse:
        tmp_req.validate()
        request = main_models.DeleteJobRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not DaraCore.is_null(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobRecords',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_records(
        self,
        request: main_models.DeleteJobRecordsRequest,
    ) -> main_models.DeleteJobRecordsResponse:
        runtime = RuntimeOptions()
        return self.delete_job_records_with_options(request, runtime)

    async def delete_job_records_async(
        self,
        request: main_models.DeleteJobRecordsRequest,
    ) -> main_models.DeleteJobRecordsResponse:
        runtime = RuntimeOptions()
        return await self.delete_job_records_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        tmp_req: main_models.DeleteJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobsResponse:
        tmp_req.validate()
        request = main_models.DeleteJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.executor_ids):
            request.executor_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.executor_ids, 'ExecutorIds', 'json')
        if not DaraCore.is_null(tmp_req.job_spec):
            request.job_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.executor_ids_shrink):
            query['ExecutorIds'] = request.executor_ids_shrink
        if not DaraCore.is_null(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not DaraCore.is_null(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobs',
            version = '2023-07-01',
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
        if not DaraCore.is_null(tmp_req.executor_ids):
            request.executor_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.executor_ids, 'ExecutorIds', 'json')
        if not DaraCore.is_null(tmp_req.job_spec):
            request.job_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.executor_ids_shrink):
            query['ExecutorIds'] = request.executor_ids_shrink
        if not DaraCore.is_null(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not DaraCore.is_null(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobs',
            version = '2023-07-01',
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

    def delete_pool_with_options(
        self,
        request: main_models.DeletePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pool_with_options_async(
        self,
        request: main_models.DeletePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pool(
        self,
        request: main_models.DeletePoolRequest,
    ) -> main_models.DeletePoolResponse:
        runtime = RuntimeOptions()
        return self.delete_pool_with_options(request, runtime)

    async def delete_pool_async(
        self,
        request: main_models.DeletePoolRequest,
    ) -> main_models.DeletePoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_pool_with_options_async(request, runtime)

    def describe_job_metric_data_with_options(
        self,
        tmp_req: main_models.DescribeJobMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMetricDataResponse:
        tmp_req.validate()
        request = main_models.DescribeJobMetricDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.array_index):
            request.array_index_shrink = Utils.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not DaraCore.is_null(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMetricData',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_metric_data_with_options_async(
        self,
        tmp_req: main_models.DescribeJobMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMetricDataResponse:
        tmp_req.validate()
        request = main_models.DescribeJobMetricDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.array_index):
            request.array_index_shrink = Utils.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not DaraCore.is_null(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMetricData',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_metric_data(
        self,
        request: main_models.DescribeJobMetricDataRequest,
    ) -> main_models.DescribeJobMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_job_metric_data_with_options(request, runtime)

    async def describe_job_metric_data_async(
        self,
        request: main_models.DescribeJobMetricDataRequest,
    ) -> main_models.DescribeJobMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_metric_data_with_options_async(request, runtime)

    def describe_job_metric_last_with_options(
        self,
        tmp_req: main_models.DescribeJobMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMetricLastResponse:
        tmp_req.validate()
        request = main_models.DescribeJobMetricLastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.array_index):
            request.array_index_shrink = Utils.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not DaraCore.is_null(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMetricLast',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_metric_last_with_options_async(
        self,
        tmp_req: main_models.DescribeJobMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobMetricLastResponse:
        tmp_req.validate()
        request = main_models.DescribeJobMetricLastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.array_index):
            request.array_index_shrink = Utils.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not DaraCore.is_null(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobMetricLast',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_metric_last(
        self,
        request: main_models.DescribeJobMetricLastRequest,
    ) -> main_models.DescribeJobMetricLastResponse:
        runtime = RuntimeOptions()
        return self.describe_job_metric_last_with_options(request, runtime)

    async def describe_job_metric_last_async(
        self,
        request: main_models.DescribeJobMetricLastRequest,
    ) -> main_models.DescribeJobMetricLastResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_metric_last_with_options_async(request, runtime)

    def get_action_plan_with_options(
        self,
        request: main_models.GetActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_action_plan_with_options_async(
        self,
        request: main_models.GetActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_action_plan(
        self,
        request: main_models.GetActionPlanRequest,
    ) -> main_models.GetActionPlanResponse:
        runtime = RuntimeOptions()
        return self.get_action_plan_with_options(request, runtime)

    async def get_action_plan_async(
        self,
        request: main_models.GetActionPlanRequest,
    ) -> main_models.GetActionPlanResponse:
        runtime = RuntimeOptions()
        return await self.get_action_plan_with_options_async(request, runtime)

    def get_app_versions_with_options(
        self,
        request: main_models.GetAppVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppVersions',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_versions_with_options_async(
        self,
        request: main_models.GetAppVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppVersions',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_versions(
        self,
        request: main_models.GetAppVersionsRequest,
    ) -> main_models.GetAppVersionsResponse:
        runtime = RuntimeOptions()
        return self.get_app_versions_with_options(request, runtime)

    async def get_app_versions_async(
        self,
        request: main_models.GetAppVersionsRequest,
    ) -> main_models.GetAppVersionsResponse:
        runtime = RuntimeOptions()
        return await self.get_app_versions_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        tmp_req: main_models.GetImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        tmp_req.validate()
        request = main_models.GetImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_region_ids):
            request.additional_region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_region_ids, 'AdditionalRegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.additional_region_ids_shrink):
            query['AdditionalRegionIds'] = request.additional_region_ids_shrink
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        tmp_req: main_models.GetImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        tmp_req.validate()
        request = main_models.GetImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_region_ids):
            request.additional_region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_region_ids, 'AdditionalRegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.additional_region_ids_shrink):
            query['AdditionalRegionIds'] = request.additional_region_ids_shrink
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: main_models.GetJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: main_models.GetJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_pool_with_options(
        self,
        request: main_models.GetPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pool_with_options_async(
        self,
        request: main_models.GetPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pool(
        self,
        request: main_models.GetPoolRequest,
    ) -> main_models.GetPoolResponse:
        runtime = RuntimeOptions()
        return self.get_pool_with_options(request, runtime)

    async def get_pool_async(
        self,
        request: main_models.GetPoolRequest,
    ) -> main_models.GetPoolResponse:
        runtime = RuntimeOptions()
        return await self.get_pool_with_options_async(request, runtime)

    def list_action_plan_activities_with_options(
        self,
        request: main_models.ListActionPlanActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionPlanActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionPlanActivities',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionPlanActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_action_plan_activities_with_options_async(
        self,
        request: main_models.ListActionPlanActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionPlanActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionPlanActivities',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionPlanActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_action_plan_activities(
        self,
        request: main_models.ListActionPlanActivitiesRequest,
    ) -> main_models.ListActionPlanActivitiesResponse:
        runtime = RuntimeOptions()
        return self.list_action_plan_activities_with_options(request, runtime)

    async def list_action_plan_activities_async(
        self,
        request: main_models.ListActionPlanActivitiesRequest,
    ) -> main_models.ListActionPlanActivitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_action_plan_activities_with_options_async(request, runtime)

    def list_action_plans_with_options(
        self,
        tmp_req: main_models.ListActionPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionPlansResponse:
        tmp_req.validate()
        request = main_models.ListActionPlansShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_plan_ids):
            request.action_plan_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_plan_ids, 'ActionPlanIds', 'json')
        query = {}
        if not DaraCore.is_null(request.action_plan_ids_shrink):
            query['ActionPlanIds'] = request.action_plan_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionPlans',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_action_plans_with_options_async(
        self,
        tmp_req: main_models.ListActionPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionPlansResponse:
        tmp_req.validate()
        request = main_models.ListActionPlansShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_plan_ids):
            request.action_plan_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_plan_ids, 'ActionPlanIds', 'json')
        query = {}
        if not DaraCore.is_null(request.action_plan_ids_shrink):
            query['ActionPlanIds'] = request.action_plan_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionPlans',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_action_plans(
        self,
        request: main_models.ListActionPlansRequest,
    ) -> main_models.ListActionPlansResponse:
        runtime = RuntimeOptions()
        return self.list_action_plans_with_options(request, runtime)

    async def list_action_plans_async(
        self,
        request: main_models.ListActionPlansRequest,
    ) -> main_models.ListActionPlansResponse:
        runtime = RuntimeOptions()
        return await self.list_action_plans_with_options_async(request, runtime)

    def list_executor_events_with_options(
        self,
        tmp_req: main_models.ListExecutorEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorEventsResponse:
        tmp_req.validate()
        request = main_models.ListExecutorEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutorEvents',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutorEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executor_events_with_options_async(
        self,
        tmp_req: main_models.ListExecutorEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorEventsResponse:
        tmp_req.validate()
        request = main_models.ListExecutorEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutorEvents',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutorEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executor_events(
        self,
        request: main_models.ListExecutorEventsRequest,
    ) -> main_models.ListExecutorEventsResponse:
        runtime = RuntimeOptions()
        return self.list_executor_events_with_options(request, runtime)

    async def list_executor_events_async(
        self,
        request: main_models.ListExecutorEventsRequest,
    ) -> main_models.ListExecutorEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_executor_events_with_options_async(request, runtime)

    def list_executors_with_options(
        self,
        tmp_req: main_models.ListExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorsResponse:
        tmp_req.validate()
        request = main_models.ListExecutorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutors',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        tmp_req: main_models.ListExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutorsResponse:
        tmp_req.validate()
        request = main_models.ListExecutorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutors',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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

    def list_images_with_options(
        self,
        tmp_req: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        tmp_req.validate()
        request = main_models.ListImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_ids):
            request.image_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'json')
        query = {}
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ids_shrink):
            query['ImageIds'] = request.image_ids_shrink
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        tmp_req: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        tmp_req.validate()
        request = main_models.ListImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_ids):
            request.image_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        if not DaraCore.is_null(tmp_req.image_names):
            request.image_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'json')
        query = {}
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ids_shrink):
            query['ImageIds'] = request.image_ids_shrink
        if not DaraCore.is_null(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_job_executors_with_options(
        self,
        request: main_models.ListJobExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutors',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_executors_with_options_async(
        self,
        request: main_models.ListJobExecutorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutors',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_executors(
        self,
        request: main_models.ListJobExecutorsRequest,
    ) -> main_models.ListJobExecutorsResponse:
        runtime = RuntimeOptions()
        return self.list_job_executors_with_options(request, runtime)

    async def list_job_executors_async(
        self,
        request: main_models.ListJobExecutorsRequest,
    ) -> main_models.ListJobExecutorsResponse:
        runtime = RuntimeOptions()
        return await self.list_job_executors_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.sort_by):
            request.sort_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_by, 'SortBy', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by_shrink):
            query['SortBy'] = request.sort_by_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2023-07-01',
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
        tmp_req: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.sort_by):
            request.sort_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_by, 'SortBy', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by_shrink):
            query['SortBy'] = request.sort_by_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2023-07-01',
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

    def list_pools_with_options(
        self,
        tmp_req: main_models.ListPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoolsResponse:
        tmp_req.validate()
        request = main_models.ListPoolsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPools',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pools_with_options_async(
        self,
        tmp_req: main_models.ListPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoolsResponse:
        tmp_req.validate()
        request = main_models.ListPoolsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPools',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pools(
        self,
        request: main_models.ListPoolsRequest,
    ) -> main_models.ListPoolsResponse:
        runtime = RuntimeOptions()
        return self.list_pools_with_options(request, runtime)

    async def list_pools_async(
        self,
        request: main_models.ListPoolsRequest,
    ) -> main_models.ListPoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_pools_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def remove_image_with_options(
        self,
        request: main_models.RemoveImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_with_options_async(
        self,
        request: main_models.RemoveImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveImage',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image(
        self,
        request: main_models.RemoveImageRequest,
    ) -> main_models.RemoveImageResponse:
        runtime = RuntimeOptions()
        return self.remove_image_with_options(request, runtime)

    async def remove_image_async(
        self,
        request: main_models.RemoveImageRequest,
    ) -> main_models.RemoveImageResponse:
        runtime = RuntimeOptions()
        return await self.remove_image_with_options_async(request, runtime)

    def synchronize_app_with_options(
        self,
        tmp_req: main_models.SynchronizeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeAppResponse:
        tmp_req.validate()
        request = main_models.SynchronizeAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.target_region_ids):
            request.target_region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_region_ids, 'TargetRegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.target_region_ids_shrink):
            query['TargetRegionIds'] = request.target_region_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeApp',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_app_with_options_async(
        self,
        tmp_req: main_models.SynchronizeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeAppResponse:
        tmp_req.validate()
        request = main_models.SynchronizeAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.target_region_ids):
            request.target_region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_region_ids, 'TargetRegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.target_region_ids_shrink):
            query['TargetRegionIds'] = request.target_region_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeApp',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_app(
        self,
        request: main_models.SynchronizeAppRequest,
    ) -> main_models.SynchronizeAppResponse:
        runtime = RuntimeOptions()
        return self.synchronize_app_with_options(request, runtime)

    async def synchronize_app_async(
        self,
        request: main_models.SynchronizeAppRequest,
    ) -> main_models.SynchronizeAppResponse:
        runtime = RuntimeOptions()
        return await self.synchronize_app_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_action_plan_with_options(
        self,
        request: main_models.UpdateActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.interval_minutes):
            query['IntervalMinutes'] = request.interval_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_action_plan_with_options_async(
        self,
        request: main_models.UpdateActionPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateActionPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.interval_minutes):
            query['IntervalMinutes'] = request.interval_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateActionPlan',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_action_plan(
        self,
        request: main_models.UpdateActionPlanRequest,
    ) -> main_models.UpdateActionPlanResponse:
        runtime = RuntimeOptions()
        return self.update_action_plan_with_options(request, runtime)

    async def update_action_plan_async(
        self,
        request: main_models.UpdateActionPlanRequest,
    ) -> main_models.UpdateActionPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_action_plan_with_options_async(request, runtime)

    def update_pool_with_options(
        self,
        tmp_req: main_models.UpdatePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePoolResponse:
        tmp_req.validate()
        request = main_models.UpdatePoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_limits):
            request.resource_limits_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pool_with_options_async(
        self,
        tmp_req: main_models.UpdatePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePoolResponse:
        tmp_req.validate()
        request = main_models.UpdatePoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_limits):
            request.resource_limits_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePool',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pool(
        self,
        request: main_models.UpdatePoolRequest,
    ) -> main_models.UpdatePoolResponse:
        runtime = RuntimeOptions()
        return self.update_pool_with_options(request, runtime)

    async def update_pool_async(
        self,
        request: main_models.UpdatePoolRequest,
    ) -> main_models.UpdatePoolResponse:
        runtime = RuntimeOptions()
        return await self.update_pool_with_options_async(request, runtime)
