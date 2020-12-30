# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eci20180808 import models as eci_20180808_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eci', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_container_group_with_options(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.CreateContainerGroupResponse().from_map(
            self.do_rpcrequest('CreateContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_container_group_with_options_async(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.CreateContainerGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_container_group(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_container_group_with_options(request, runtime)

    async def create_container_group_async(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_container_group_with_options_async(request, runtime)

    def create_image_cache_with_options(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.CreateImageCacheResponse().from_map(
            self.do_rpcrequest('CreateImageCache', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_cache_with_options_async(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.CreateImageCacheResponse().from_map(
            await self.do_rpcrequest_async('CreateImageCache', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_cache(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    async def create_image_cache_async(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_cache_with_options_async(request, runtime)

    def delete_container_group_with_options(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DeleteContainerGroupResponse().from_map(
            self.do_rpcrequest('DeleteContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_container_group_with_options_async(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DeleteContainerGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_container_group(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_container_group_with_options(request, runtime)

    async def delete_container_group_async(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_container_group_with_options_async(request, runtime)

    def delete_image_cache_with_options(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DeleteImageCacheResponse().from_map(
            self.do_rpcrequest('DeleteImageCache', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_cache_with_options_async(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DeleteImageCacheResponse().from_map(
            await self.do_rpcrequest_async('DeleteImageCache', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_cache(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    async def delete_image_cache_async(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_cache_with_options_async(request, runtime)

    def describe_container_group_metric_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupMetricResponse().from_map(
            self.do_rpcrequest('DescribeContainerGroupMetric', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_container_group_metric_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupMetricResponse().from_map(
            await self.do_rpcrequest_async('DescribeContainerGroupMetric', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_container_group_metric(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_metric_with_options(request, runtime)

    async def describe_container_group_metric_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_group_metric_with_options_async(request, runtime)

    def describe_container_group_price_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupPriceResponse().from_map(
            self.do_rpcrequest('DescribeContainerGroupPrice', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_container_group_price_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupPriceResponse().from_map(
            await self.do_rpcrequest_async('DescribeContainerGroupPrice', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_container_group_price(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_price_with_options(request, runtime)

    async def describe_container_group_price_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_group_price_with_options_async(request, runtime)

    def describe_container_groups_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupsResponse().from_map(
            self.do_rpcrequest('DescribeContainerGroups', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_container_groups_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeContainerGroups', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_container_groups(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_groups_with_options(request, runtime)

    async def describe_container_groups_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_groups_with_options_async(request, runtime)

    def describe_container_log_with_options(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerLogResponse().from_map(
            self.do_rpcrequest('DescribeContainerLog', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_container_log_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeContainerLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeContainerLog', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_container_log(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_log_with_options(request, runtime)

    async def describe_container_log_async(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_log_with_options_async(request, runtime)

    def describe_image_caches_with_options(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeImageCachesResponse().from_map(
            self.do_rpcrequest('DescribeImageCaches', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_caches_with_options_async(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeImageCachesResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageCaches', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_caches(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_caches_with_options(request, runtime)

    async def describe_image_caches_async(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_caches_with_options_async(request, runtime)

    def describe_multi_container_group_metric_with_options(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeMultiContainerGroupMetricResponse().from_map(
            self.do_rpcrequest('DescribeMultiContainerGroupMetric', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_multi_container_group_metric_with_options_async(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeMultiContainerGroupMetricResponse().from_map(
            await self.do_rpcrequest_async('DescribeMultiContainerGroupMetric', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_multi_container_group_metric(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_container_group_metric_with_options(request, runtime)

    async def describe_multi_container_group_metric_async(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_container_group_metric_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def exec_container_command_with_options(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.ExecContainerCommandResponse().from_map(
            self.do_rpcrequest('ExecContainerCommand', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def exec_container_command_with_options_async(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.ExecContainerCommandResponse().from_map(
            await self.do_rpcrequest_async('ExecContainerCommand', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exec_container_command(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.exec_container_command_with_options(request, runtime)

    async def exec_container_command_async(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.exec_container_command_with_options_async(request, runtime)

    def list_usage_with_options(
        self,
        request: eci_20180808_models.ListUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ListUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.ListUsageResponse().from_map(
            self.do_rpcrequest('ListUsage', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_usage_with_options_async(
        self,
        request: eci_20180808_models.ListUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ListUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.ListUsageResponse().from_map(
            await self.do_rpcrequest_async('ListUsage', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_usage(
        self,
        request: eci_20180808_models.ListUsageRequest,
    ) -> eci_20180808_models.ListUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_usage_with_options(request, runtime)

    async def list_usage_async(
        self,
        request: eci_20180808_models.ListUsageRequest,
    ) -> eci_20180808_models.ListUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_usage_with_options_async(request, runtime)

    def restart_container_group_with_options(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.RestartContainerGroupResponse().from_map(
            self.do_rpcrequest('RestartContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_container_group_with_options_async(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.RestartContainerGroupResponse().from_map(
            await self.do_rpcrequest_async('RestartContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_container_group(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_container_group_with_options(request, runtime)

    async def restart_container_group_async(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_container_group_with_options_async(request, runtime)

    def update_container_group_with_options(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.UpdateContainerGroupResponse().from_map(
            self.do_rpcrequest('UpdateContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_container_group_with_options_async(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eci_20180808_models.UpdateContainerGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateContainerGroup', '2018-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_container_group(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_container_group_with_options(request, runtime)

    async def update_container_group_async(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_container_group_with_options_async(request, runtime)
