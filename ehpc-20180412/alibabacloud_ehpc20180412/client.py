# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20180412 import models as ehpc20180412_models
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
        self._endpoint = self.get_endpoint('ehpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_job_with_options(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            self.do_rpcrequest('DescribeJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            await self.do_rpcrequest_async('DescribeJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_job(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
    ) -> ehpc20180412_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
    ) -> ehpc20180412_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteImageResponse(),
            self.do_rpcrequest('DeleteImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteImageResponse(),
            await self.do_rpcrequest_async('DeleteImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_image(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
    ) -> ehpc20180412_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
    ) -> ehpc20180412_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_gwscluster_with_options(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSClusterResponse(),
            self.do_rpcrequest('DeleteGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_gwscluster_with_options_async(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSClusterResponse(),
            await self.do_rpcrequest_async('DeleteGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_gwscluster(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gwscluster_with_options(request, runtime)

    async def delete_gwscluster_async(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gwscluster_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            self.do_rpcrequest('DeleteUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            await self.do_rpcrequest_async('DeleteUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_users(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            self.do_rpcrequest('DescribeCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            await self.do_rpcrequest_async('DescribeCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_cluster(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ehpc20180412_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ehpc20180412_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: ehpc20180412_models.ListUsersRequest,
    ) -> ehpc20180412_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ehpc20180412_models.ListUsersRequest,
    ) -> ehpc20180412_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def describe_container_app_with_options(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeContainerAppResponse(),
            self.do_rpcrequest('DescribeContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_container_app_with_options_async(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeContainerAppResponse(),
            await self.do_rpcrequest_async('DescribeContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_container_app(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_app_with_options(request, runtime)

    async def describe_container_app_async(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_app_with_options_async(request, runtime)

    def pull_image_with_options(
        self,
        request: ehpc20180412_models.PullImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.PullImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            self.do_rpcrequest('PullImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def pull_image_with_options_async(
        self,
        request: ehpc20180412_models.PullImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.PullImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            await self.do_rpcrequest_async('PullImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def pull_image(
        self,
        request: ehpc20180412_models.PullImageRequest,
    ) -> ehpc20180412_models.PullImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.pull_image_with_options(request, runtime)

    async def pull_image_async(
        self,
        request: ehpc20180412_models.PullImageRequest,
    ) -> ehpc20180412_models.PullImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pull_image_with_options_async(request, runtime)

    def stop_nodes_with_options(
        self,
        request: ehpc20180412_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            self.do_rpcrequest('StopNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_nodes_with_options_async(
        self,
        request: ehpc20180412_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            await self.do_rpcrequest_async('StopNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_nodes(
        self,
        request: ehpc20180412_models.StopNodesRequest,
    ) -> ehpc20180412_models.StopNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    async def stop_nodes_async(
        self,
        request: ehpc20180412_models.StopNodesRequest,
    ) -> ehpc20180412_models.StopNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_nodes_with_options_async(request, runtime)

    def list_nodes_by_queue_with_options(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            self.do_rpcrequest('ListNodesByQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_nodes_by_queue_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            await self.do_rpcrequest_async('ListNodesByQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_queue(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_queue_with_options(request, runtime)

    async def list_nodes_by_queue_async(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_by_queue_with_options_async(request, runtime)

    def modify_container_app_attributes_with_options(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            self.do_rpcrequest('ModifyContainerAppAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_container_app_attributes_with_options_async(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            await self.do_rpcrequest_async('ModifyContainerAppAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_container_app_attributes(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_container_app_attributes_with_options(request, runtime)

    async def modify_container_app_attributes_async(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_container_app_attributes_with_options_async(request, runtime)

    def set_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            self.do_rpcrequest('SetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_scheduler_info_with_options_async(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            await self.do_rpcrequest_async('SetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scheduler_info(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scheduler_info_with_options(request, runtime)

    async def set_scheduler_info_async(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scheduler_info_with_options_async(request, runtime)

    def get_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            self.do_rpcrequest('GetCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_cloud_metric_profiling_with_options_async(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            await self.do_rpcrequest_async('GetCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cloud_metric_profiling(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_profiling_with_options(request, runtime)

    async def get_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_profiling_with_options_async(request, runtime)

    def describe_image_price_with_options(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            self.do_rpcrequest('DescribeImagePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_image_price_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            await self.do_rpcrequest_async('DescribeImagePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image_price(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_price_with_options(request, runtime)

    async def describe_image_price_async(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_price_with_options_async(request, runtime)

    def stop_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopGWSInstanceResponse(),
            self.do_rpcrequest('StopGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopGWSInstanceResponse(),
            await self.do_rpcrequest_async('StopGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_gwsinstance(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_gwsinstance_with_options(request, runtime)

    async def stop_gwsinstance_async(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_gwsinstance_with_options_async(request, runtime)

    def get_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            self.do_rpcrequest('GetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            await self.do_rpcrequest_async('GetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_auto_scale_config(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    async def get_auto_scale_config_async(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scale_config_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: ehpc20180412_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            self.do_rpcrequest('ListNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            await self.do_rpcrequest_async('ListNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes(
        self,
        request: ehpc20180412_models.ListNodesRequest,
    ) -> ehpc20180412_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: ehpc20180412_models.ListNodesRequest,
    ) -> ehpc20180412_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_commands_with_options(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            self.do_rpcrequest('ListCommands', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_commands_with_options_async(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            await self.do_rpcrequest_async('ListCommands', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_commands(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
    ) -> ehpc20180412_models.ListCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_commands_with_options(request, runtime)

    async def list_commands_async(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
    ) -> ehpc20180412_models.ListCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_commands_with_options_async(request, runtime)

    def create_gwsimage_with_options(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSImageResponse(),
            self.do_rpcrequest('CreateGWSImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_gwsimage_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSImageResponse(),
            await self.do_rpcrequest_async('CreateGWSImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwsimage(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwsimage_with_options(request, runtime)

    async def create_gwsimage_async(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwsimage_with_options_async(request, runtime)

    def invoke_shell_command_with_options(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            self.do_rpcrequest('InvokeShellCommand', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def invoke_shell_command_with_options_async(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            await self.do_rpcrequest_async('InvokeShellCommand', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def invoke_shell_command(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_shell_command_with_options(request, runtime)

    async def invoke_shell_command_async(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_shell_command_with_options_async(request, runtime)

    def list_file_system_with_mount_targets_with_options(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            self.do_rpcrequest('ListFileSystemWithMountTargets', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_file_system_with_mount_targets_with_options_async(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            await self.do_rpcrequest_async('ListFileSystemWithMountTargets', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_file_system_with_mount_targets(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_file_system_with_mount_targets_with_options(request, runtime)

    async def list_file_system_with_mount_targets_async(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_system_with_mount_targets_with_options_async(request, runtime)

    def modify_cluster_attributes_with_options(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            self.do_rpcrequest('ModifyClusterAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_attributes_with_options_async(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            await self.do_rpcrequest_async('ModifyClusterAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_cluster_attributes(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    async def modify_cluster_attributes_async(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_attributes_with_options_async(request, runtime)

    def delete_job_templates_with_options(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            self.do_rpcrequest('DeleteJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_job_templates_with_options_async(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            await self.do_rpcrequest_async('DeleteJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_job_templates(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    async def delete_job_templates_async(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_templates_with_options_async(request, runtime)

    def get_cloud_metric_logs_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            self.do_rpcrequest('GetCloudMetricLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_cloud_metric_logs_with_options_async(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            await self.do_rpcrequest_async('GetCloudMetricLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cloud_metric_logs(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_logs_with_options(request, runtime)

    async def get_cloud_metric_logs_async(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_logs_with_options_async(request, runtime)

    def create_job_template_with_options(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            self.do_rpcrequest('CreateJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_job_template_with_options_async(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            await self.do_rpcrequest_async('CreateJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_job_template(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    async def create_job_template_async(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_template_with_options_async(request, runtime)

    def get_hybrid_cluster_config_with_options(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            self.do_rpcrequest('GetHybridClusterConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_hybrid_cluster_config_with_options_async(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            await self.do_rpcrequest_async('GetHybridClusterConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hybrid_cluster_config(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hybrid_cluster_config_with_options(request, runtime)

    async def get_hybrid_cluster_config_async(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hybrid_cluster_config_with_options_async(request, runtime)

    def describe_gwsinstances_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            self.do_rpcrequest('DescribeGWSInstances', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_gwsinstances_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            await self.do_rpcrequest_async('DescribeGWSInstances', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsinstances(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsinstances_with_options(request, runtime)

    async def describe_gwsinstances_async(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsinstances_with_options_async(request, runtime)

    def reset_nodes_with_options(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ResetNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            self.do_rpcrequest('ResetNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def reset_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ResetNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            await self.do_rpcrequest_async('ResetNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def reset_nodes(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
    ) -> ehpc20180412_models.ResetNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    async def reset_nodes_async(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
    ) -> ehpc20180412_models.ResetNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_nodes_with_options_async(request, runtime)

    def uninstall_software_with_options(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            self.do_rpcrequest('UninstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def uninstall_software_with_options_async(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            await self.do_rpcrequest_async('UninstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def uninstall_software(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_software_with_options(request, runtime)

    async def uninstall_software_async(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_software_with_options_async(request, runtime)

    def apply_nodes_with_options(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            self.do_rpcrequest('ApplyNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def apply_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            await self.do_rpcrequest_async('ApplyNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def apply_nodes(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_nodes_with_options(request, runtime)

    async def apply_nodes_async(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_nodes_with_options_async(request, runtime)

    def describe_gwsclusters_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClustersResponse(),
            self.do_rpcrequest('DescribeGWSClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_gwsclusters_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClustersResponse(),
            await self.do_rpcrequest_async('DescribeGWSClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsclusters(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsclusters_with_options(request, runtime)

    async def describe_gwsclusters_async(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsclusters_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            self.do_rpcrequest('DeleteJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            await self.do_rpcrequest_async('DeleteJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_jobs(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def list_container_images_with_options(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerImagesResponse(),
            self.do_rpcrequest('ListContainerImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_container_images_with_options_async(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerImagesResponse(),
            await self.do_rpcrequest_async('ListContainerImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_container_images(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    async def list_container_images_async(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_images_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            self.do_rpcrequest('DeleteNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_nodes_with_options_async(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            await self.do_rpcrequest_async('DeleteNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_nodes(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: ehpc20180412_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            self.do_rpcrequest('ListJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: ehpc20180412_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            await self.do_rpcrequest_async('ListJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_jobs(
        self,
        request: ehpc20180412_models.ListJobsRequest,
    ) -> ehpc20180412_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc20180412_models.ListJobsRequest,
    ) -> ehpc20180412_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_cpfs_file_systems_with_options(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            self.do_rpcrequest('ListCpfsFileSystems', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_cpfs_file_systems_with_options_async(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            await self.do_rpcrequest_async('ListCpfsFileSystems', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cpfs_file_systems(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cpfs_file_systems_with_options(request, runtime)

    async def list_cpfs_file_systems_async(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cpfs_file_systems_with_options_async(request, runtime)

    def list_clusters_meta_with_options(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            self.do_rpcrequest('ListClustersMeta', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_clusters_meta_with_options_async(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            await self.do_rpcrequest_async('ListClustersMeta', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_clusters_meta(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_meta_with_options(request, runtime)

    async def list_clusters_meta_async(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_meta_with_options_async(request, runtime)

    def query_service_pack_and_price_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            self.do_rpcrequest('QueryServicePackAndPrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_service_pack_and_price_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            await self.do_rpcrequest_async('QueryServicePackAndPrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_service_pack_and_price(self) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_service_pack_and_price_with_options(runtime)

    async def query_service_pack_and_price_async(self) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_service_pack_and_price_with_options_async(runtime)

    def delete_container_apps_with_options(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteContainerAppsResponse(),
            self.do_rpcrequest('DeleteContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_container_apps_with_options_async(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteContainerAppsResponse(),
            await self.do_rpcrequest_async('DeleteContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_container_apps(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_container_apps_with_options(request, runtime)

    async def delete_container_apps_async(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_container_apps_with_options_async(request, runtime)

    def list_volumes_with_options(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            self.do_rpcrequest('ListVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_volumes_with_options_async(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            await self.do_rpcrequest_async('ListVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_volumes(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
    ) -> ehpc20180412_models.ListVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    async def list_volumes_async(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
    ) -> ehpc20180412_models.ListVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_volumes_with_options_async(request, runtime)

    def list_invocation_status_with_options(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            self.do_rpcrequest('ListInvocationStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_invocation_status_with_options_async(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            await self.do_rpcrequest_async('ListInvocationStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_invocation_status(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_status_with_options(request, runtime)

    async def list_invocation_status_async(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_status_with_options_async(request, runtime)

    def modify_image_gateway_config_with_options(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            self.do_rpcrequest('ModifyImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_image_gateway_config_with_options_async(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            await self.do_rpcrequest_async('ModifyImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_image_gateway_config(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_gateway_config_with_options(request, runtime)

    async def modify_image_gateway_config_async(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_gateway_config_with_options_async(request, runtime)

    def list_container_apps_with_options(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerAppsResponse(),
            self.do_rpcrequest('ListContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_container_apps_with_options_async(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerAppsResponse(),
            await self.do_rpcrequest_async('ListContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_container_apps(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_apps_with_options(request, runtime)

    async def list_container_apps_async(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_apps_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            self.do_rpcrequest('DeleteSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_security_group_with_options_async(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            await self.do_rpcrequest_async('DeleteSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_security_group(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def describe_nfsclient_status_with_options(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            self.do_rpcrequest('DescribeNFSClientStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_nfsclient_status_with_options_async(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            await self.do_rpcrequest_async('DescribeNFSClientStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_nfsclient_status(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nfsclient_status_with_options(request, runtime)

    async def describe_nfsclient_status_async(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nfsclient_status_with_options_async(request, runtime)

    def ecd_delete_desktops_with_options(
        self,
        request: ehpc20180412_models.EcdDeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EcdDeleteDesktopsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EcdDeleteDesktopsResponse(),
            self.do_rpcrequest('EcdDeleteDesktops', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def ecd_delete_desktops_with_options_async(
        self,
        request: ehpc20180412_models.EcdDeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EcdDeleteDesktopsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EcdDeleteDesktopsResponse(),
            await self.do_rpcrequest_async('EcdDeleteDesktops', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def ecd_delete_desktops(
        self,
        request: ehpc20180412_models.EcdDeleteDesktopsRequest,
    ) -> ehpc20180412_models.EcdDeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ecd_delete_desktops_with_options(request, runtime)

    async def ecd_delete_desktops_async(
        self,
        request: ehpc20180412_models.EcdDeleteDesktopsRequest,
    ) -> ehpc20180412_models.EcdDeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ecd_delete_desktops_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: ehpc20180412_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: ehpc20180412_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            await self.do_rpcrequest_async('ListClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_clusters(
        self,
        request: ehpc20180412_models.ListClustersRequest,
    ) -> ehpc20180412_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ehpc20180412_models.ListClustersRequest,
    ) -> ehpc20180412_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def submit_job_with_options(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            self.do_rpcrequest('SubmitJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def submit_job_with_options_async(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            await self.do_rpcrequest_async('SubmitJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_job(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
    ) -> ehpc20180412_models.SubmitJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    async def submit_job_async(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
    ) -> ehpc20180412_models.SubmitJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_job_with_options_async(request, runtime)

    def get_accounting_report_with_options(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            self.do_rpcrequest('GetAccountingReport', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_accounting_report_with_options_async(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            await self.do_rpcrequest_async('GetAccountingReport', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_accounting_report(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_accounting_report_with_options(request, runtime)

    async def get_accounting_report_async(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_accounting_report_with_options_async(request, runtime)

    def describe_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            self.do_rpcrequest('DescribeAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            await self.do_rpcrequest_async('DescribeAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_auto_scale_config(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scale_config_with_options(request, runtime)

    async def describe_auto_scale_config_async(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scale_config_with_options_async(request, runtime)

    def get_visual_service_status_with_options(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            self.do_rpcrequest('GetVisualServiceStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_visual_service_status_with_options_async(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            await self.do_rpcrequest_async('GetVisualServiceStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_visual_service_status(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_visual_service_status_with_options(request, runtime)

    async def get_visual_service_status_async(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_visual_service_status_with_options_async(request, runtime)

    def start_visual_service_with_options(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            self.do_rpcrequest('StartVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def start_visual_service_with_options_async(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            await self.do_rpcrequest_async('StartVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_visual_service(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_visual_service_with_options(request, runtime)

    async def start_visual_service_async(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_visual_service_with_options_async(request, runtime)

    def get_if_ecs_type_support_ht_config_with_options(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            self.do_rpcrequest('GetIfEcsTypeSupportHtConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_if_ecs_type_support_ht_config_with_options_async(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            await self.do_rpcrequest_async('GetIfEcsTypeSupportHtConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_if_ecs_type_support_ht_config(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_if_ecs_type_support_ht_config_with_options(request, runtime)

    async def get_if_ecs_type_support_ht_config_async(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_if_ecs_type_support_ht_config_with_options_async(request, runtime)

    def get_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            self.do_rpcrequest('GetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_scheduler_info_with_options_async(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            await self.do_rpcrequest_async('GetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_scheduler_info(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scheduler_info_with_options(request, runtime)

    async def get_scheduler_info_async(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scheduler_info_with_options_async(request, runtime)

    def set_gwsinstance_user_with_options(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            self.do_rpcrequest('SetGWSInstanceUser', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_gwsinstance_user_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            await self.do_rpcrequest_async('SetGWSInstanceUser', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_gwsinstance_user(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_user_with_options(request, runtime)

    async def set_gwsinstance_user_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwsinstance_user_with_options_async(request, runtime)

    def get_workbench_token_with_options(
        self,
        request: ehpc20180412_models.GetWorkbenchTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetWorkbenchTokenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetWorkbenchTokenResponse(),
            self.do_rpcrequest('GetWorkbenchToken', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_workbench_token_with_options_async(
        self,
        request: ehpc20180412_models.GetWorkbenchTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetWorkbenchTokenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetWorkbenchTokenResponse(),
            await self.do_rpcrequest_async('GetWorkbenchToken', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_workbench_token(
        self,
        request: ehpc20180412_models.GetWorkbenchTokenRequest,
    ) -> ehpc20180412_models.GetWorkbenchTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workbench_token_with_options(request, runtime)

    async def get_workbench_token_async(
        self,
        request: ehpc20180412_models.GetWorkbenchTokenRequest,
    ) -> ehpc20180412_models.GetWorkbenchTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workbench_token_with_options_async(request, runtime)

    def install_software_with_options(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            self.do_rpcrequest('InstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def install_software_with_options_async(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            await self.do_rpcrequest_async('InstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def install_software(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_software_with_options(request, runtime)

    async def install_software_async(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_software_with_options_async(request, runtime)

    def list_available_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            self.do_rpcrequest('ListAvailableEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_available_ecs_types_with_options_async(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            await self.do_rpcrequest_async('ListAvailableEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_available_ecs_types(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_available_ecs_types_with_options(request, runtime)

    async def list_available_ecs_types_async(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_available_ecs_types_with_options_async(request, runtime)

    def mount_nfswith_options(
        self,
        request: ehpc20180412_models.MountNFSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.MountNFSResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.MountNFSResponse(),
            self.do_rpcrequest('MountNFS', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def mount_nfswith_options_async(
        self,
        request: ehpc20180412_models.MountNFSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.MountNFSResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.MountNFSResponse(),
            await self.do_rpcrequest_async('MountNFS', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def mount_nfs(
        self,
        request: ehpc20180412_models.MountNFSRequest,
    ) -> ehpc20180412_models.MountNFSResponse:
        runtime = util_models.RuntimeOptions()
        return self.mount_nfswith_options(request, runtime)

    async def mount_nfs_async(
        self,
        request: ehpc20180412_models.MountNFSRequest,
    ) -> ehpc20180412_models.MountNFSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mount_nfswith_options_async(request, runtime)

    def add_queue_with_options(
        self,
        request: ehpc20180412_models.AddQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            self.do_rpcrequest('AddQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_queue_with_options_async(
        self,
        request: ehpc20180412_models.AddQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            await self.do_rpcrequest_async('AddQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_queue(
        self,
        request: ehpc20180412_models.AddQueueRequest,
    ) -> ehpc20180412_models.AddQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_queue_with_options(request, runtime)

    async def add_queue_async(
        self,
        request: ehpc20180412_models.AddQueueRequest,
    ) -> ehpc20180412_models.AddQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_queue_with_options_async(request, runtime)

    def create_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSInstanceResponse(),
            self.do_rpcrequest('CreateGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSInstanceResponse(),
            await self.do_rpcrequest_async('CreateGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwsinstance(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwsinstance_with_options(request, runtime)

    async def create_gwsinstance_async(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwsinstance_with_options_async(request, runtime)

    def list_current_client_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            self.do_rpcrequest('ListCurrentClientVersion', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_current_client_version_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            await self.do_rpcrequest_async('ListCurrentClientVersion', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_current_client_version(self) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    async def list_current_client_version_async(self) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_current_client_version_with_options_async(runtime)

    def update_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            self.do_rpcrequest('UpdateClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_cluster_volumes_with_options_async(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            await self.do_rpcrequest_async('UpdateClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_cluster_volumes(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_volumes_with_options(request, runtime)

    async def update_cluster_volumes_async(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_volumes_with_options_async(request, runtime)

    def start_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartGWSInstanceResponse(),
            self.do_rpcrequest('StartGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def start_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartGWSInstanceResponse(),
            await self.do_rpcrequest_async('StartGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_gwsinstance(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_gwsinstance_with_options(request, runtime)

    async def start_gwsinstance_async(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_gwsinstance_with_options_async(request, runtime)

    def list_invocation_results_with_options(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            self.do_rpcrequest('ListInvocationResults', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_invocation_results_with_options_async(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            await self.do_rpcrequest_async('ListInvocationResults', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_invocation_results(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_results_with_options(request, runtime)

    async def list_invocation_results_async(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_results_with_options_async(request, runtime)

    def set_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            self.do_rpcrequest('SetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            await self.do_rpcrequest_async('SetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_auto_scale_config(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    async def set_auto_scale_config_async(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_auto_scale_config_with_options_async(request, runtime)

    def add_nodes_with_options(
        self,
        request: ehpc20180412_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            self.do_rpcrequest('AddNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            await self.do_rpcrequest_async('AddNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_nodes(
        self,
        request: ehpc20180412_models.AddNodesRequest,
    ) -> ehpc20180412_models.AddNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    async def add_nodes_async(
        self,
        request: ehpc20180412_models.AddNodesRequest,
    ) -> ehpc20180412_models.AddNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_nodes_with_options_async(request, runtime)

    def list_softwares_with_options(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            self.do_rpcrequest('ListSoftwares', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_softwares_with_options_async(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            await self.do_rpcrequest_async('ListSoftwares', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_softwares(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_security_groups_with_options(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            self.do_rpcrequest('ListSecurityGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_security_groups_with_options_async(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            await self.do_rpcrequest_async('ListSecurityGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_security_groups(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_groups_with_options(request, runtime)

    async def list_security_groups_async(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_groups_with_options_async(request, runtime)

    def describe_gwsimages_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSImagesResponse(),
            self.do_rpcrequest('DescribeGWSImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_gwsimages_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSImagesResponse(),
            await self.do_rpcrequest_async('DescribeGWSImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsimages(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsimages_with_options(request, runtime)

    async def describe_gwsimages_async(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsimages_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        request: ehpc20180412_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            self.do_rpcrequest('StopJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        request: ehpc20180412_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            await self.do_rpcrequest_async('StopJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_jobs(
        self,
        request: ehpc20180412_models.StopJobsRequest,
    ) -> ehpc20180412_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: ehpc20180412_models.StopJobsRequest,
    ) -> ehpc20180412_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def start_nodes_with_options(
        self,
        request: ehpc20180412_models.StartNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            self.do_rpcrequest('StartNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def start_nodes_with_options_async(
        self,
        request: ehpc20180412_models.StartNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            await self.do_rpcrequest_async('StartNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_nodes(
        self,
        request: ehpc20180412_models.StartNodesRequest,
    ) -> ehpc20180412_models.StartNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_nodes_with_options(request, runtime)

    async def start_nodes_async(
        self,
        request: ehpc20180412_models.StartNodesRequest,
    ) -> ehpc20180412_models.StartNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_nodes_with_options_async(request, runtime)

    def modify_user_groups_with_options(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            self.do_rpcrequest('ModifyUserGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_user_groups_with_options_async(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            await self.do_rpcrequest_async('ModifyUserGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_user_groups(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    async def modify_user_groups_async(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_groups_with_options_async(request, runtime)

    def set_queue_with_options(
        self,
        request: ehpc20180412_models.SetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            self.do_rpcrequest('SetQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_queue_with_options_async(
        self,
        request: ehpc20180412_models.SetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            await self.do_rpcrequest_async('SetQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_queue(
        self,
        request: ehpc20180412_models.SetQueueRequest,
    ) -> ehpc20180412_models.SetQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_queue_with_options(request, runtime)

    async def set_queue_async(
        self,
        request: ehpc20180412_models.SetQueueRequest,
    ) -> ehpc20180412_models.SetQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_queue_with_options_async(request, runtime)

    def start_cluster_with_options(
        self,
        request: ehpc20180412_models.StartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            self.do_rpcrequest('StartCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def start_cluster_with_options_async(
        self,
        request: ehpc20180412_models.StartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            await self.do_rpcrequest_async('StartCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_cluster(
        self,
        request: ehpc20180412_models.StartClusterRequest,
    ) -> ehpc20180412_models.StartClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_cluster_with_options(request, runtime)

    async def start_cluster_async(
        self,
        request: ehpc20180412_models.StartClusterRequest,
    ) -> ehpc20180412_models.StartClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_cluster_with_options_async(request, runtime)

    def list_custom_images_with_options(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            self.do_rpcrequest('ListCustomImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_custom_images_with_options_async(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            await self.do_rpcrequest_async('ListCustomImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_custom_images(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def add_users_with_options(
        self,
        request: ehpc20180412_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            self.do_rpcrequest('AddUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_users_with_options_async(
        self,
        request: ehpc20180412_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            await self.do_rpcrequest_async('AddUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_users(
        self,
        request: ehpc20180412_models.AddUsersRequest,
    ) -> ehpc20180412_models.AddUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    async def add_users_async(
        self,
        request: ehpc20180412_models.AddUsersRequest,
    ) -> ehpc20180412_models.AddUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_with_options_async(request, runtime)

    def create_gwscluster_with_options(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSClusterResponse(),
            self.do_rpcrequest('CreateGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_gwscluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSClusterResponse(),
            await self.do_rpcrequest_async('CreateGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwscluster(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwscluster_with_options(request, runtime)

    async def create_gwscluster_async(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwscluster_with_options_async(request, runtime)

    def list_job_templates_with_options(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            self.do_rpcrequest('ListJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_job_templates_with_options_async(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            await self.do_rpcrequest_async('ListJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_job_templates(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    async def list_job_templates_async(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_templates_with_options_async(request, runtime)

    def describe_image_gateway_config_with_options(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            self.do_rpcrequest('DescribeImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_image_gateway_config_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            await self.do_rpcrequest_async('DescribeImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image_gateway_config(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_gateway_config_with_options(request, runtime)

    async def describe_image_gateway_config_async(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_gateway_config_with_options_async(request, runtime)

    def get_gwsconnect_ticket_with_options(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            self.do_rpcrequest('GetGWSConnectTicket', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_gwsconnect_ticket_with_options_async(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            await self.do_rpcrequest_async('GetGWSConnectTicket', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_gwsconnect_ticket(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_gwsconnect_ticket_with_options(request, runtime)

    async def get_gwsconnect_ticket_async(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_gwsconnect_ticket_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: ehpc20180412_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            self.do_rpcrequest('ListTasks', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: ehpc20180412_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            await self.do_rpcrequest_async('ListTasks', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tasks(
        self,
        request: ehpc20180412_models.ListTasksRequest,
    ) -> ehpc20180412_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: ehpc20180412_models.ListTasksRequest,
    ) -> ehpc20180412_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def stop_cluster_with_options(
        self,
        request: ehpc20180412_models.StopClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            self.do_rpcrequest('StopCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_cluster_with_options_async(
        self,
        request: ehpc20180412_models.StopClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            await self.do_rpcrequest_async('StopCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_cluster(
        self,
        request: ehpc20180412_models.StopClusterRequest,
    ) -> ehpc20180412_models.StopClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_cluster_with_options(request, runtime)

    async def stop_cluster_async(
        self,
        request: ehpc20180412_models.StopClusterRequest,
    ) -> ehpc20180412_models.StopClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_cluster_with_options_async(request, runtime)

    def add_security_group_with_options(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            self.do_rpcrequest('AddSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_security_group_with_options_async(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            await self.do_rpcrequest_async('AddSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_security_group(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_with_options(request, runtime)

    async def add_security_group_async(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_security_group_with_options_async(request, runtime)

    def list_nodes_no_paging_with_options(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            self.do_rpcrequest('ListNodesNoPaging', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_nodes_no_paging_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            await self.do_rpcrequest_async('ListNodesNoPaging', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes_no_paging(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    async def list_nodes_no_paging_async(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_no_paging_with_options_async(request, runtime)

    def set_gwsinstance_name_with_options(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            self.do_rpcrequest('SetGWSInstanceName', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_gwsinstance_name_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            await self.do_rpcrequest_async('SetGWSInstanceName', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_gwsinstance_name(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_name_with_options(request, runtime)

    async def set_gwsinstance_name_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwsinstance_name_with_options_async(request, runtime)

    def create_hybrid_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            self.do_rpcrequest('CreateHybridCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_hybrid_cluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            await self.do_rpcrequest_async('CreateHybridCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_hybrid_cluster(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_cluster_with_options(request, runtime)

    async def create_hybrid_cluster_async(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_cluster_with_options_async(request, runtime)

    def update_queue_config_with_options(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            self.do_rpcrequest('UpdateQueueConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_queue_config_with_options_async(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            await self.do_rpcrequest_async('UpdateQueueConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_queue_config(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_queue_config_with_options(request, runtime)

    async def update_queue_config_async(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_queue_config_with_options_async(request, runtime)

    def stop_visual_service_with_options(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            self.do_rpcrequest('StopVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_visual_service_with_options_async(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            await self.do_rpcrequest_async('StopVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_visual_service(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_visual_service_with_options(request, runtime)

    async def stop_visual_service_async(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_visual_service_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            self.do_rpcrequest('CreateCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            await self.do_rpcrequest_async('CreateCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_cluster(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
    ) -> ehpc20180412_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
    ) -> ehpc20180412_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def describe_image_with_options(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageResponse(),
            self.do_rpcrequest('DescribeImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_image_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageResponse(),
            await self.do_rpcrequest_async('DescribeImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
    ) -> ehpc20180412_models.DescribeImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_with_options(request, runtime)

    async def describe_image_async(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
    ) -> ehpc20180412_models.DescribeImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_with_options_async(request, runtime)

    def modify_user_passwords_with_options(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            self.do_rpcrequest('ModifyUserPasswords', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_user_passwords_with_options_async(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            await self.do_rpcrequest_async('ModifyUserPasswords', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_user_passwords(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    async def modify_user_passwords_async(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_passwords_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            self.do_rpcrequest('DeleteQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            await self.do_rpcrequest_async('DeleteQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_queue(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def list_installed_software_with_options(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            self.do_rpcrequest('ListInstalledSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_installed_software_with_options_async(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            await self.do_rpcrequest_async('ListInstalledSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_installed_software(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_installed_software_with_options(request, runtime)

    async def list_installed_software_async(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_installed_software_with_options_async(request, runtime)

    def get_health_monitor_logs_with_options(
        self,
        request: ehpc20180412_models.GetHealthMonitorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHealthMonitorLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHealthMonitorLogsResponse(),
            self.do_rpcrequest('GetHealthMonitorLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_health_monitor_logs_with_options_async(
        self,
        request: ehpc20180412_models.GetHealthMonitorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHealthMonitorLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHealthMonitorLogsResponse(),
            await self.do_rpcrequest_async('GetHealthMonitorLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_health_monitor_logs(
        self,
        request: ehpc20180412_models.GetHealthMonitorLogsRequest,
    ) -> ehpc20180412_models.GetHealthMonitorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_health_monitor_logs_with_options(request, runtime)

    async def get_health_monitor_logs_async(
        self,
        request: ehpc20180412_models.GetHealthMonitorLogsRequest,
    ) -> ehpc20180412_models.GetHealthMonitorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_health_monitor_logs_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            self.do_rpcrequest('UpgradeClient', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def upgrade_client_with_options_async(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            await self.do_rpcrequest_async('UpgradeClient', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def upgrade_client(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            self.do_rpcrequest('DeleteCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            await self.do_rpcrequest_async('DeleteCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_cluster(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: ehpc20180412_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            self.do_rpcrequest('ListImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: ehpc20180412_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            await self.do_rpcrequest_async('ListImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_images(
        self,
        request: ehpc20180412_models.ListImagesRequest,
    ) -> ehpc20180412_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: ehpc20180412_models.ListImagesRequest,
    ) -> ehpc20180412_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def set_gwscluster_policy_with_options(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            self.do_rpcrequest('SetGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_gwscluster_policy_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            await self.do_rpcrequest_async('SetGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_gwscluster_policy(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwscluster_policy_with_options(request, runtime)

    async def set_gwscluster_policy_async(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwscluster_policy_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            self.do_rpcrequest('ListQueues', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            await self.do_rpcrequest_async('ListQueues', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_queues(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
    ) -> ehpc20180412_models.ListQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
    ) -> ehpc20180412_models.ListQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def create_job_file_with_options(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            self.do_rpcrequest('CreateJobFile', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_job_file_with_options_async(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            await self.do_rpcrequest_async('CreateJobFile', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_job_file(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_file_with_options(request, runtime)

    async def create_job_file_async(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_file_with_options_async(request, runtime)

    def list_cloud_metric_profilings_with_options(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            self.do_rpcrequest('ListCloudMetricProfilings', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_cloud_metric_profilings_with_options_async(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            await self.do_rpcrequest_async('ListCloudMetricProfilings', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cloud_metric_profilings(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_metric_profilings_with_options(request, runtime)

    async def list_cloud_metric_profilings_async(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_metric_profilings_with_options_async(request, runtime)

    def get_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            self.do_rpcrequest('GetClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_cluster_volumes_with_options_async(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            await self.do_rpcrequest_async('GetClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cluster_volumes(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_volumes_with_options(request, runtime)

    async def get_cluster_volumes_async(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_volumes_with_options_async(request, runtime)

    def delete_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            self.do_rpcrequest('DeleteGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            await self.do_rpcrequest_async('DeleteGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_gwsinstance(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gwsinstance_with_options(request, runtime)

    async def delete_gwsinstance_async(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gwsinstance_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            await self.do_rpcrequest_async('ListRegions', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_regions(self) -> ehpc20180412_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> ehpc20180412_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def initialize_ehpcwith_options(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            self.do_rpcrequest('InitializeEHPC', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def initialize_ehpcwith_options_async(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            await self.do_rpcrequest_async('InitializeEHPC', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def initialize_ehpc(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_ehpcwith_options(request, runtime)

    async def initialize_ehpc_async(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_ehpcwith_options_async(request, runtime)

    def run_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            self.do_rpcrequest('RunCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def run_cloud_metric_profiling_with_options_async(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            await self.do_rpcrequest_async('RunCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def run_cloud_metric_profiling(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_metric_profiling_with_options(request, runtime)

    async def run_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cloud_metric_profiling_with_options_async(request, runtime)

    def add_existed_nodes_with_options(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            self.do_rpcrequest('AddExistedNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_existed_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            await self.do_rpcrequest_async('AddExistedNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_existed_nodes(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_existed_nodes_with_options(request, runtime)

    async def add_existed_nodes_async(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_existed_nodes_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            await self.do_rpcrequest_async('DescribePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
    ) -> ehpc20180412_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
    ) -> ehpc20180412_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def rerun_jobs_with_options(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RerunJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            self.do_rpcrequest('RerunJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def rerun_jobs_with_options_async(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RerunJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            await self.do_rpcrequest_async('RerunJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def rerun_jobs(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
    ) -> ehpc20180412_models.RerunJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    async def rerun_jobs_async(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
    ) -> ehpc20180412_models.RerunJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_jobs_with_options_async(request, runtime)

    def describe_gwscluster_policy_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            self.do_rpcrequest('DescribeGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gwscluster_policy_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            await self.do_rpcrequest_async('DescribeGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_gwscluster_policy(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwscluster_policy_with_options(request, runtime)

    async def describe_gwscluster_policy_async(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwscluster_policy_with_options_async(request, runtime)

    def add_local_nodes_with_options(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            self.do_rpcrequest('AddLocalNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_local_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            await self.do_rpcrequest_async('AddLocalNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_local_nodes(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_local_nodes_with_options(request, runtime)

    async def add_local_nodes_async(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_local_nodes_with_options_async(request, runtime)

    def edit_job_template_with_options(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            self.do_rpcrequest('EditJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def edit_job_template_with_options_async(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            await self.do_rpcrequest_async('EditJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def edit_job_template(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    async def edit_job_template_async(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_job_template_with_options_async(request, runtime)

    def modify_visual_service_passwd_with_options(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            self.do_rpcrequest('ModifyVisualServicePasswd', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_visual_service_passwd_with_options_async(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            await self.do_rpcrequest_async('ModifyVisualServicePasswd', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_visual_service_passwd(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_visual_service_passwd_with_options(request, runtime)

    async def modify_visual_service_passwd_async(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_visual_service_passwd_with_options_async(request, runtime)

    def list_preferred_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            self.do_rpcrequest('ListPreferredEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_preferred_ecs_types_with_options_async(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            await self.do_rpcrequest_async('ListPreferredEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_preferred_ecs_types(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    async def list_preferred_ecs_types_async(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_preferred_ecs_types_with_options_async(request, runtime)

    def add_container_app_with_options(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddContainerAppResponse(),
            self.do_rpcrequest('AddContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_container_app_with_options_async(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddContainerAppResponse(),
            await self.do_rpcrequest_async('AddContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_container_app(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_container_app_with_options(request, runtime)

    async def add_container_app_async(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_container_app_with_options_async(request, runtime)

    def list_cluster_logs_with_options(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            self.do_rpcrequest('ListClusterLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_cluster_logs_with_options_async(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            await self.do_rpcrequest_async('ListClusterLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cluster_logs(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    async def list_cluster_logs_async(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_logs_with_options_async(request, runtime)

    def recover_cluster_with_options(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            self.do_rpcrequest('RecoverCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recover_cluster_with_options_async(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            await self.do_rpcrequest_async('RecoverCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recover_cluster(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_cluster_with_options(request, runtime)

    async def recover_cluster_async(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_cluster_with_options_async(request, runtime)
