# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eas20210701 import models as eas_20210701_models
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
        self._endpoint_map = {
            'cn-beijing': 'pai-eas.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'pai-eas.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'pai-eas.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai-eas.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai-eas.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai-eas.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai-eas.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'pai-eas.ap-southeast-5.aliyuncs.com',
            'us-east-1': 'pai-eas.us-east-1.aliyuncs.com',
            'us-west-1': 'pai-eas.us-west-1.aliyuncs.com',
            'eu-central-1': 'pai-eas.eu-central-1.aliyuncs.com',
            'ap-south-1': 'pai-eas.ap-south-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'pai-eas.cn-shanghai-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'pai-eas.cn-north-2-gov-1.aliyuncs.com',
            'cn-chengdu': 'pai-eas.cn-chengdu.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_benchmark_task(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_benchmark_task_with_options(request, headers, runtime)

    async def create_benchmark_task_async(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_benchmark_task_with_options_async(request, headers, runtime)

    def create_benchmark_task_with_options(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_benchmark_task_with_options_async(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: eas_20210701_models.CreateResourceRequest,
    ) -> eas_20210701_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request, headers, runtime)

    async def create_resource_async(
        self,
        request: eas_20210701_models.CreateResourceRequest,
    ) -> eas_20210701_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request, headers, runtime)

    def create_resource_with_options(
        self,
        request: eas_20210701_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: eas_20210701_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_log_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_log_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_store):
            body['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_store):
            body['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: eas_20210701_models.CreateServiceRequest,
    ) -> eas_20210701_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: eas_20210701_models.CreateServiceRequest,
    ) -> eas_20210701_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: eas_20210701_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: eas_20210701_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def delete_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def delete_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def delete_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def delete_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def delete_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def describe_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def describe_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task_report(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_report_with_options(cluster_id, task_name, request, headers, runtime)

    async def describe_benchmark_task_report_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_report_with_options_async(cluster_id, task_name, request, headers, runtime)

    def describe_benchmark_task_report_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTaskReport',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_report_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTaskReport',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group(
        self,
        cluster_id: str,
        group_name: str,
    ) -> eas_20210701_models.DescribeGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_group_with_options(cluster_id, group_name, headers, runtime)

    async def describe_group_async(
        self,
        cluster_id: str,
        group_name: str,
    ) -> eas_20210701_models.DescribeGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_group_with_options_async(cluster_id, group_name, headers, runtime)

    def describe_group_with_options(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(group_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(group_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_event(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_event_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_event_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_event_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_event_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceEvent',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_event_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceEvent',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_log(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_log_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_log_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_log_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_log_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_log_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_benchmark_task(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_benchmark_task_with_options(request, headers, runtime)

    async def list_benchmark_task_async(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_benchmark_task_with_options_async(request, headers, runtime)

    def list_benchmark_task_with_options(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_benchmark_task_with_options_async(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: eas_20210701_models.ListGroupsRequest,
    ) -> eas_20210701_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    async def list_groups_async(
        self,
        request: eas_20210701_models.ListGroupsRequest,
    ) -> eas_20210701_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_groups_with_options_async(request, headers, runtime)

    def list_groups_with_options(
        self,
        request: eas_20210701_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: eas_20210701_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instance_worker(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instance_worker_with_options(cluster_id, resource_id, instance_name, request, headers, runtime)

    async def list_resource_instance_worker_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_instance_worker_with_options_async(cluster_id, resource_id, instance_name, request, headers, runtime)

    def list_resource_instance_worker_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstanceWorker',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/workers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstanceWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instance_worker_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstanceWorker',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/workers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstanceWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_services(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_services_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_services_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_services_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resource_services_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_services_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: eas_20210701_models.ListResourcesRequest,
    ) -> eas_20210701_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: eas_20210701_models.ListResourcesRequest,
    ) -> eas_20210701_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: eas_20210701_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: eas_20210701_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_versions(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_versions_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_versions_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_versions_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_service_versions_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_versions_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: eas_20210701_models.ListServicesRequest,
    ) -> eas_20210701_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: eas_20210701_models.ListServicesRequest,
    ) -> eas_20210701_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        request: eas_20210701_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: eas_20210701_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def release_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def release_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/release',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReleaseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/release',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReleaseServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def start_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def start_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StartServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_service_with_options(cluster_id, service_name, headers, runtime)

    async def start_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StartServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_service_with_options_async(cluster_id, service_name, headers, runtime)

    def start_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def stop_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def stop_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StopServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_service_with_options(cluster_id, service_name, headers, runtime)

    async def stop_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StopServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_service_with_options_async(cluster_id, service_name, headers, runtime)

    def stop_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_benchmark_task_with_options(cluster_id, task_name, request, headers, runtime)

    async def update_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_benchmark_task_with_options_async(cluster_id, task_name, request, headers, runtime)

    def update_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
    ) -> eas_20210701_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
    ) -> eas_20210701_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_dlink_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_dlink_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_instance(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_instance_with_options(cluster_id, resource_id, instance_id, request, headers, runtime)

    async def update_resource_instance_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_instance_with_options_async(cluster_id, resource_id, instance_id, request, headers, runtime)

    def update_resource_instance_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['Action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_instance_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['Action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
    ) -> eas_20210701_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
    ) -> eas_20210701_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_safety_lock(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_safety_lock_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_safety_lock_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_safety_lock_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_safety_lock_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock):
            body['Lock'] = request.lock
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSafetyLock',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/lock',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceSafetyLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_safety_lock_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock):
            body['Lock'] = request.lock
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSafetyLock',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/lock',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceSafetyLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_version(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_version_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_version_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_version_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceVersion',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_version_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceVersion',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )
