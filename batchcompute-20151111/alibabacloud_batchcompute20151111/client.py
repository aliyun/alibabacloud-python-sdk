# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_batchcompute20151111 import models as batch_compute_20151111_models
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
        self._endpoint = self.get_endpoint('batchcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_image(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.CancelImageRequest,
    ) -> batch_compute_20151111_models.CancelImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_image_with_options(resource_name, request, headers, runtime)

    async def cancel_image_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.CancelImageRequest,
    ) -> batch_compute_20151111_models.CancelImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_image_with_options_async(resource_name, request, headers, runtime)

    def cancel_image_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.CancelImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CancelImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CancelImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_image_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.CancelImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CancelImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CancelImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_job_priority(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ChangeJobPriorityRequest,
    ) -> batch_compute_20151111_models.ChangeJobPriorityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_job_priority_with_options(resource_name, request, headers, runtime)

    async def change_job_priority_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ChangeJobPriorityRequest,
    ) -> batch_compute_20151111_models.ChangeJobPriorityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_job_priority_with_options_async(resource_name, request, headers, runtime)

    def change_job_priority_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ChangeJobPriorityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ChangeJobPriorityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeJobPriority',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ChangeJobPriorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_job_priority_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ChangeJobPriorityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ChangeJobPriorityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeJobPriority',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ChangeJobPriorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(self) -> batch_compute_20151111_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(headers, runtime)

    async def create_app_async(self) -> batch_compute_20151111_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(headers, runtime)

    def create_app_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: batch_compute_20151111_models.CreateClusterRequest,
    ) -> batch_compute_20151111_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    async def create_cluster_async(
        self,
        request: batch_compute_20151111_models.CreateClusterRequest,
    ) -> batch_compute_20151111_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def create_cluster_with_options(
        self,
        request: batch_compute_20151111_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: batch_compute_20151111_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image(
        self,
        request: batch_compute_20151111_models.CreateImageRequest,
    ) -> batch_compute_20151111_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_image_with_options(request, headers, runtime)

    async def create_image_async(
        self,
        request: batch_compute_20151111_models.CreateImageRequest,
    ) -> batch_compute_20151111_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_image_with_options_async(request, headers, runtime)

    def create_image_with_options(
        self,
        request: batch_compute_20151111_models.CreateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: batch_compute_20151111_models.CreateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: batch_compute_20151111_models.CreateJobRequest,
    ) -> batch_compute_20151111_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: batch_compute_20151111_models.CreateJobRequest,
    ) -> batch_compute_20151111_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: batch_compute_20151111_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: batch_compute_20151111_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_with_options(resource_name, headers, runtime)

    async def delete_app_async(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_with_options_async(resource_name, headers, runtime)

    def delete_app_with_options(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteClusterRequest,
    ) -> batch_compute_20151111_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(resource_name, request, headers, runtime)

    async def delete_cluster_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteClusterRequest,
    ) -> batch_compute_20151111_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_with_options_async(resource_name, request, headers, runtime)

    def delete_cluster_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_instance(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.DeleteClusterInstanceRequest,
    ) -> batch_compute_20151111_models.DeleteClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_instance_with_options(cluster_id, group_name, instance_id, request, headers, runtime)

    async def delete_cluster_instance_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.DeleteClusterInstanceRequest,
    ) -> batch_compute_20151111_models.DeleteClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_instance_with_options_async(cluster_id, group_name, instance_id, request, headers, runtime)

    def delete_cluster_instance_with_options(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.DeleteClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteClusterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_instance_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.DeleteClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteClusterInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteImageRequest,
    ) -> batch_compute_20151111_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_image_with_options(resource_name, request, headers, runtime)

    async def delete_image_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteImageRequest,
    ) -> batch_compute_20151111_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_image_with_options_async(resource_name, request, headers, runtime)

    def delete_image_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteJobRequest,
    ) -> batch_compute_20151111_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(resource_name, request, headers, runtime)

    async def delete_job_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteJobRequest,
    ) -> batch_compute_20151111_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(resource_name, request, headers, runtime)

    def delete_job_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_name: str,
        request: batch_compute_20151111_models.DeleteProjectRequest,
    ) -> batch_compute_20151111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_name, request, headers, runtime)

    async def delete_project_async(
        self,
        project_name: str,
        request: batch_compute_20151111_models.DeleteProjectRequest,
    ) -> batch_compute_20151111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_name, request, headers, runtime)

    def delete_project_with_options(
        self,
        project_name: str,
        request: batch_compute_20151111_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/projects/{project_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_name: str,
        request: batch_compute_20151111_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/projects/{project_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_with_options(resource_name, headers, runtime)

    async def get_app_async(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_with_options_async(resource_name, headers, runtime)

    def get_app_with_options(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetClusterRequest,
    ) -> batch_compute_20151111_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(resource_name, request, headers, runtime)

    async def get_cluster_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetClusterRequest,
    ) -> batch_compute_20151111_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_with_options_async(resource_name, request, headers, runtime)

    def get_cluster_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_instance(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetClusterInstanceRequest,
    ) -> batch_compute_20151111_models.GetClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_instance_with_options(cluster_id, group_name, instance_id, request, headers, runtime)

    async def get_cluster_instance_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetClusterInstanceRequest,
    ) -> batch_compute_20151111_models.GetClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_instance_with_options_async(cluster_id, group_name, instance_id, request, headers, runtime)

    def get_cluster_instance_with_options(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetClusterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_instance_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetClusterInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetImageRequest,
    ) -> batch_compute_20151111_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_with_options(resource_name, request, headers, runtime)

    async def get_image_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetImageRequest,
    ) -> batch_compute_20151111_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_with_options_async(resource_name, request, headers, runtime)

    def get_image_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        resource_name: str,
        task_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetInstanceRequest,
    ) -> batch_compute_20151111_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(resource_name, task_name, instance_id, request, headers, runtime)

    async def get_instance_async(
        self,
        resource_name: str,
        task_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetInstanceRequest,
    ) -> batch_compute_20151111_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(resource_name, task_name, instance_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        resource_name: str,
        task_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}/instances/{{InstanceId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        resource_name: str,
        task_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}/instances/{{InstanceId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobRequest,
    ) -> batch_compute_20151111_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(resource_name, request, headers, runtime)

    async def get_job_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobRequest,
    ) -> batch_compute_20151111_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(resource_name, request, headers, runtime)

    def get_job_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_description(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobDescriptionRequest,
    ) -> batch_compute_20151111_models.GetJobDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_description_with_options(resource_name, request, headers, runtime)

    async def get_job_description_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobDescriptionRequest,
    ) -> batch_compute_20151111_models.GetJobDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_description_with_options_async(resource_name, request, headers, runtime)

    def get_job_description_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetJobDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobDescription',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}?description',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetJobDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_description_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.GetJobDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetJobDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobDescription',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}?description',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetJobDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        request: batch_compute_20151111_models.GetQuotaRequest,
    ) -> batch_compute_20151111_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(request, headers, runtime)

    async def get_quota_async(
        self,
        request: batch_compute_20151111_models.GetQuotaRequest,
    ) -> batch_compute_20151111_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(request, headers, runtime)

    def get_quota_with_options(
        self,
        request: batch_compute_20151111_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        request: batch_compute_20151111_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.GetTaskRequest,
    ) -> batch_compute_20151111_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(resource_name, task_name, request, headers, runtime)

    async def get_task_async(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.GetTaskRequest,
    ) -> batch_compute_20151111_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(resource_name, task_name, request, headers, runtime)

    def get_task_with_options(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.GetTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.GetTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(self) -> batch_compute_20151111_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(headers, runtime)

    async def list_apps_async(self) -> batch_compute_20151111_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_apps_with_options_async(headers, runtime)

    def list_apps_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAppsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAppsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_instance_type(self) -> batch_compute_20151111_models.ListAvailableInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_instance_type_with_options(headers, runtime)

    async def list_available_instance_type_async(self) -> batch_compute_20151111_models.ListAvailableInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_available_instance_type_with_options_async(headers, runtime)

    def list_available_instance_type_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAvailableInstanceTypeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableInstanceType',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/available',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListAvailableInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_instance_type_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAvailableInstanceTypeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableInstanceType',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/available',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListAvailableInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_instances(
        self,
        cluster_id: str,
        group_name: str,
        request: batch_compute_20151111_models.ListClusterInstancesRequest,
    ) -> batch_compute_20151111_models.ListClusterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_instances_with_options(cluster_id, group_name, request, headers, runtime)

    async def list_cluster_instances_async(
        self,
        cluster_id: str,
        group_name: str,
        request: batch_compute_20151111_models.ListClusterInstancesRequest,
    ) -> batch_compute_20151111_models.ListClusterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_instances_with_options_async(cluster_id, group_name, request, headers, runtime)

    def list_cluster_instances_with_options(
        self,
        cluster_id: str,
        group_name: str,
        request: batch_compute_20151111_models.ListClusterInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListClusterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterInstances',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListClusterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_instances_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        request: batch_compute_20151111_models.ListClusterInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListClusterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterInstances',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListClusterInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: batch_compute_20151111_models.ListClustersRequest,
    ) -> batch_compute_20151111_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_clusters_with_options(request, headers, runtime)

    async def list_clusters_async(
        self,
        request: batch_compute_20151111_models.ListClustersRequest,
    ) -> batch_compute_20151111_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_clusters_with_options_async(request, headers, runtime)

    def list_clusters_with_options(
        self,
        request: batch_compute_20151111_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: batch_compute_20151111_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: batch_compute_20151111_models.ListImagesRequest,
    ) -> batch_compute_20151111_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: batch_compute_20151111_models.ListImagesRequest,
    ) -> batch_compute_20151111_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: batch_compute_20151111_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: batch_compute_20151111_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.ListInstancesRequest,
    ) -> batch_compute_20151111_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(resource_name, task_name, request, headers, runtime)

    async def list_instances_async(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.ListInstancesRequest,
    ) -> batch_compute_20151111_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(resource_name, task_name, request, headers, runtime)

    def list_instances_with_options(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        resource_name: str,
        task_name: str,
        request: batch_compute_20151111_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks/{{TaskName}}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: batch_compute_20151111_models.ListJobsRequest,
    ) -> batch_compute_20151111_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: batch_compute_20151111_models.ListJobsRequest,
    ) -> batch_compute_20151111_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        request: batch_compute_20151111_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: batch_compute_20151111_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> batch_compute_20151111_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> batch_compute_20151111_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ListTasksRequest,
    ) -> batch_compute_20151111_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(resource_name, request, headers, runtime)

    async def list_tasks_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ListTasksRequest,
    ) -> batch_compute_20151111_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(resource_name, request, headers, runtime)

    def list_tasks_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_with_options(resource_name, headers, runtime)

    async def modify_app_async(
        self,
        resource_name: str,
    ) -> batch_compute_20151111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_app_with_options_async(resource_name, headers, runtime)

    def modify_app_with_options(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ModifyAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ModifyAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/apps/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ModifyClusterRequest,
    ) -> batch_compute_20151111_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_with_options(resource_name, request, headers, runtime)

    async def modify_cluster_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ModifyClusterRequest,
    ) -> batch_compute_20151111_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_with_options_async(resource_name, request, headers, runtime)

    def modify_cluster_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ModifyClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{resource_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ModifyClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_for_task(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.PollForTaskRequest,
    ) -> batch_compute_20151111_models.PollForTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.poll_for_task_with_options(cluster_id, worker_id, request, headers, runtime)

    async def poll_for_task_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.PollForTaskRequest,
    ) -> batch_compute_20151111_models.PollForTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.poll_for_task_with_options_async(cluster_id, worker_id, request, headers, runtime)

    def poll_for_task_with_options(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.PollForTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.PollForTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollForTask',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/fetchTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.PollForTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_for_task_with_options_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.PollForTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.PollForTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollForTask',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/fetchTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.PollForTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recreate_cluster_instance(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RecreateClusterInstanceRequest,
    ) -> batch_compute_20151111_models.RecreateClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recreate_cluster_instance_with_options(cluster_id, group_name, instance_id, request, headers, runtime)

    async def recreate_cluster_instance_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RecreateClusterInstanceRequest,
    ) -> batch_compute_20151111_models.RecreateClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recreate_cluster_instance_with_options_async(cluster_id, group_name, instance_id, request, headers, runtime)

    def recreate_cluster_instance_with_options(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RecreateClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.RecreateClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecreateClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/recreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.RecreateClusterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recreate_cluster_instance_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RecreateClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.RecreateClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecreateClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/recreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.RecreateClusterInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_cluster_instance(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RenewClusterInstanceRequest,
    ) -> batch_compute_20151111_models.RenewClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_cluster_instance_with_options(cluster_id, group_name, instance_id, request, headers, runtime)

    async def renew_cluster_instance_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RenewClusterInstanceRequest,
    ) -> batch_compute_20151111_models.RenewClusterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_cluster_instance_with_options_async(cluster_id, group_name, instance_id, request, headers, runtime)

    def renew_cluster_instance_with_options(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RenewClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.RenewClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.RenewClusterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_cluster_instance_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        instance_id: str,
        request: batch_compute_20151111_models.RenewClusterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.RenewClusterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewClusterInstance',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.RenewClusterInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_task_status(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportTaskStatusRequest,
    ) -> batch_compute_20151111_models.ReportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.report_task_status_with_options(cluster_id, worker_id, request, headers, runtime)

    async def report_task_status_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportTaskStatusRequest,
    ) -> batch_compute_20151111_models.ReportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.report_task_status_with_options_async(cluster_id, worker_id, request, headers, runtime)

    def report_task_status_with_options(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ReportTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportTaskStatus',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateTaskStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ReportTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_task_status_with_options_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ReportTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportTaskStatus',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateTaskStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ReportTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_worker_status(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportWorkerStatusRequest,
    ) -> batch_compute_20151111_models.ReportWorkerStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.report_worker_status_with_options(cluster_id, worker_id, request, headers, runtime)

    async def report_worker_status_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportWorkerStatusRequest,
    ) -> batch_compute_20151111_models.ReportWorkerStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.report_worker_status_with_options_async(cluster_id, worker_id, request, headers, runtime)

    def report_worker_status_with_options(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportWorkerStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ReportWorkerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportWorkerStatus',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ReportWorkerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_worker_status_with_options_async(
        self,
        cluster_id: str,
        worker_id: str,
        request: batch_compute_20151111_models.ReportWorkerStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ReportWorkerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportWorkerStatus',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.ReportWorkerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StartJobRequest,
    ) -> batch_compute_20151111_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_job_with_options(resource_name, request, headers, runtime)

    async def start_job_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StartJobRequest,
    ) -> batch_compute_20151111_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_job_with_options_async(resource_name, request, headers, runtime)

    def start_job_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StartJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.StartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StartJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.StartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StopJobRequest,
    ) -> batch_compute_20151111_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(resource_name, request, headers, runtime)

    async def stop_job_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StopJobRequest,
    ) -> batch_compute_20151111_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_job_with_options_async(resource_name, request, headers, runtime)

    def stop_job_with_options(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StopJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.StopJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        resource_name: str,
        request: batch_compute_20151111_models.StopJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.StopJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2015-11-11',
            protocol='HTTPS',
            pathname=f'/jobs/{resource_name}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            batch_compute_20151111_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )
