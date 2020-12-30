# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
        return batch_compute_20151111_models.CancelImageResponse().from_map(
            self.do_roarequest('CancelImage', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.CancelImageResponse().from_map(
            await self.do_roarequest_async('CancelImage', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ChangeJobPriorityResponse().from_map(
            self.do_roarequest('ChangeJobPriority', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ChangeJobPriorityResponse().from_map(
            await self.do_roarequest_async('ChangeJobPriority', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateAppResponse().from_map(
            self.do_roarequest('CreateApp', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/apps', 'none', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.CreateAppResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return batch_compute_20151111_models.CreateAppResponse().from_map(
            await self.do_roarequest_async('CreateApp', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/apps', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateClusterResponse().from_map(
            self.do_roarequest('CreateCluster', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateClusterResponse().from_map(
            await self.do_roarequest_async('CreateCluster', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateImageResponse().from_map(
            self.do_roarequest('CreateImage', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/images', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateImageResponse().from_map(
            await self.do_roarequest_async('CreateImage', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/images', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateJobResponse().from_map(
            self.do_roarequest('CreateJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs', 'none', req, runtime)
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
        return batch_compute_20151111_models.CreateJobResponse().from_map(
            await self.do_roarequest_async('CreateJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteAppResponse().from_map(
            self.do_roarequest('DeleteApp', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteAppResponse().from_map(
            await self.do_roarequest_async('DeleteApp', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteClusterResponse().from_map(
            self.do_roarequest('DeleteCluster', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteClusterResponse().from_map(
            await self.do_roarequest_async('DeleteCluster', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteClusterInstanceResponse().from_map(
            self.do_roarequest('DeleteClusterInstance', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteClusterInstanceResponse().from_map(
            await self.do_roarequest_async('DeleteClusterInstance', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteImageResponse().from_map(
            self.do_roarequest('DeleteImage', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteImageResponse().from_map(
            await self.do_roarequest_async('DeleteImage', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteJobResponse().from_map(
            self.do_roarequest('DeleteJob', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteJobResponse().from_map(
            await self.do_roarequest_async('DeleteJob', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteProjectResponse().from_map(
            self.do_roarequest('DeleteProject', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/projects/{project_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.DeleteProjectResponse().from_map(
            await self.do_roarequest_async('DeleteProject', '2015-11-11', 'HTTPS', 'DELETE', 'AK', f'/projects/{project_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetAppResponse().from_map(
            self.do_roarequest('GetApp', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetAppResponse().from_map(
            await self.do_roarequest_async('GetApp', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetClusterResponse().from_map(
            self.do_roarequest('GetCluster', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetClusterResponse().from_map(
            await self.do_roarequest_async('GetCluster', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetClusterInstanceResponse().from_map(
            self.do_roarequest('GetClusterInstance', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetClusterInstanceResponse().from_map(
            await self.do_roarequest_async('GetClusterInstance', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetImageResponse().from_map(
            self.do_roarequest('GetImage', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetImageResponse().from_map(
            await self.do_roarequest_async('GetImage', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/images/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetInstanceResponse().from_map(
            self.do_roarequest('GetInstance', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetInstanceResponse().from_map(
            await self.do_roarequest_async('GetInstance', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}/instances/{{InstanceId}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetJobResponse().from_map(
            self.do_roarequest('GetJob', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetJobResponse().from_map(
            await self.do_roarequest_async('GetJob', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetJobDescriptionResponse().from_map(
            self.do_roarequest('GetJobDescription', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}?description', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetJobDescriptionResponse().from_map(
            await self.do_roarequest_async('GetJobDescription', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}?description', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetQuotaResponse().from_map(
            self.do_roarequest('GetQuota', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/quotas', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetQuotaResponse().from_map(
            await self.do_roarequest_async('GetQuota', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/quotas', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetTaskResponse().from_map(
            self.do_roarequest('GetTask', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.GetTaskResponse().from_map(
            await self.do_roarequest_async('GetTask', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListAppsResponse().from_map(
            self.do_roarequest('ListApps', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/apps', 'none', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAppsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return batch_compute_20151111_models.ListAppsResponse().from_map(
            await self.do_roarequest_async('ListApps', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/apps', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListAvailableInstanceTypeResponse().from_map(
            self.do_roarequest('ListAvailableInstanceType', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/available', 'none', req, runtime)
        )

    async def list_available_instance_type_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListAvailableInstanceTypeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return batch_compute_20151111_models.ListAvailableInstanceTypeResponse().from_map(
            await self.do_roarequest_async('ListAvailableInstanceType', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/available', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListClusterInstancesResponse().from_map(
            self.do_roarequest('ListClusterInstances', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListClusterInstancesResponse().from_map(
            await self.do_roarequest_async('ListClusterInstances', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListClustersResponse().from_map(
            self.do_roarequest('ListClusters', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListClustersResponse().from_map(
            await self.do_roarequest_async('ListClusters', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/clusters', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListImagesResponse().from_map(
            self.do_roarequest('ListImages', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/images', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListImagesResponse().from_map(
            await self.do_roarequest_async('ListImages', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/images', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListInstancesResponse().from_map(
            self.do_roarequest('ListInstances', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}/instances', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListInstancesResponse().from_map(
            await self.do_roarequest_async('ListInstances', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks/{{TaskName}}/instances', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListJobsResponse().from_map(
            self.do_roarequest('ListJobs', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListJobsResponse().from_map(
            await self.do_roarequest_async('ListJobs', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListRegionsResponse().from_map(
            self.do_roarequest('ListRegions', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20151111_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return batch_compute_20151111_models.ListRegionsResponse().from_map(
            await self.do_roarequest_async('ListRegions', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/regions', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListTasksResponse().from_map(
            self.do_roarequest('ListTasks', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks', 'none', req, runtime)
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
        return batch_compute_20151111_models.ListTasksResponse().from_map(
            await self.do_roarequest_async('ListTasks', '2015-11-11', 'HTTPS', 'GET', 'AK', f'/jobs/{resource_name}/tasks', 'none', req, runtime)
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
        return batch_compute_20151111_models.ModifyAppResponse().from_map(
            self.do_roarequest('ModifyApp', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ModifyAppResponse().from_map(
            await self.do_roarequest_async('ModifyApp', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/apps/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ModifyClusterResponse().from_map(
            self.do_roarequest('ModifyCluster', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.ModifyClusterResponse().from_map(
            await self.do_roarequest_async('ModifyCluster', '2015-11-11', 'HTTPS', 'PUT', 'AK', f'/clusters/{resource_name}', 'none', req, runtime)
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
        return batch_compute_20151111_models.PollForTaskResponse().from_map(
            self.do_roarequest('PollForTask', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/fetchTask', 'none', req, runtime)
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
        return batch_compute_20151111_models.PollForTaskResponse().from_map(
            await self.do_roarequest_async('PollForTask', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/fetchTask', 'none', req, runtime)
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
        return batch_compute_20151111_models.RecreateClusterInstanceResponse().from_map(
            self.do_roarequest('RecreateClusterInstance', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/recreate', 'none', req, runtime)
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
        return batch_compute_20151111_models.RecreateClusterInstanceResponse().from_map(
            await self.do_roarequest_async('RecreateClusterInstance', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/recreate', 'none', req, runtime)
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
        return batch_compute_20151111_models.RenewClusterInstanceResponse().from_map(
            self.do_roarequest('RenewClusterInstance', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/renew', 'none', req, runtime)
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
        return batch_compute_20151111_models.RenewClusterInstanceResponse().from_map(
            await self.do_roarequest_async('RenewClusterInstance', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/groups/{{GroupName}}/instances/{{InstanceId}}/renew', 'none', req, runtime)
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
        return batch_compute_20151111_models.ReportTaskStatusResponse().from_map(
            self.do_roarequest('ReportTaskStatus', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateTaskStatus', 'none', req, runtime)
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
        return batch_compute_20151111_models.ReportTaskStatusResponse().from_map(
            await self.do_roarequest_async('ReportTaskStatus', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateTaskStatus', 'none', req, runtime)
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
        return batch_compute_20151111_models.ReportWorkerStatusResponse().from_map(
            self.do_roarequest('ReportWorkerStatus', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateStatus', 'none', req, runtime)
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
        return batch_compute_20151111_models.ReportWorkerStatusResponse().from_map(
            await self.do_roarequest_async('ReportWorkerStatus', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/workers/{{WorkerId}}/updateStatus', 'none', req, runtime)
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
        return batch_compute_20151111_models.StartJobResponse().from_map(
            self.do_roarequest('StartJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs/{resource_name}/start', 'none', req, runtime)
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
        return batch_compute_20151111_models.StartJobResponse().from_map(
            await self.do_roarequest_async('StartJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs/{resource_name}/start', 'none', req, runtime)
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
        return batch_compute_20151111_models.StopJobResponse().from_map(
            self.do_roarequest('StopJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs/{resource_name}/stop', 'none', req, runtime)
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
        return batch_compute_20151111_models.StopJobResponse().from_map(
            await self.do_roarequest_async('StopJob', '2015-11-11', 'HTTPS', 'POST', 'AK', f'/jobs/{resource_name}/stop', 'none', req, runtime)
        )
