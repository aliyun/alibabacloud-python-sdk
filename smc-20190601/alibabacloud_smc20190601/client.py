# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_smc20190601 import models as smc_20190601_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('smc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_replication_job_with_options(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.CreateReplicationJobResponse().from_map(
            self.do_rpcrequest('CreateReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_replication_job_with_options_async(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.CreateReplicationJobResponse().from_map(
            await self.do_rpcrequest_async('CreateReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_replication_job(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_replication_job_with_options(request, runtime)

    async def create_replication_job_async(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_replication_job_with_options_async(request, runtime)

    def cut_over_replication_job_with_options(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.CutOverReplicationJobResponse().from_map(
            self.do_rpcrequest('CutOverReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cut_over_replication_job_with_options_async(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.CutOverReplicationJobResponse().from_map(
            await self.do_rpcrequest_async('CutOverReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cut_over_replication_job(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cut_over_replication_job_with_options(request, runtime)

    async def cut_over_replication_job_async(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cut_over_replication_job_with_options_async(request, runtime)

    def delete_replication_job_with_options(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DeleteReplicationJobResponse().from_map(
            self.do_rpcrequest('DeleteReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_replication_job_with_options_async(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DeleteReplicationJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_replication_job(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_replication_job_with_options(request, runtime)

    async def delete_replication_job_async(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_replication_job_with_options_async(request, runtime)

    def delete_source_server_with_options(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DeleteSourceServerResponse().from_map(
            self.do_rpcrequest('DeleteSourceServer', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_source_server_with_options_async(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DeleteSourceServerResponse().from_map(
            await self.do_rpcrequest_async('DeleteSourceServer', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_source_server(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_source_server_with_options(request, runtime)

    async def delete_source_server_async(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_source_server_with_options_async(request, runtime)

    def describe_replication_jobs_with_options(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DescribeReplicationJobsResponse().from_map(
            self.do_rpcrequest('DescribeReplicationJobs', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_replication_jobs_with_options_async(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DescribeReplicationJobsResponse().from_map(
            await self.do_rpcrequest_async('DescribeReplicationJobs', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_replication_jobs(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_replication_jobs_with_options(request, runtime)

    async def describe_replication_jobs_async(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_replication_jobs_with_options_async(request, runtime)

    def describe_source_servers_with_options(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DescribeSourceServersResponse().from_map(
            self.do_rpcrequest('DescribeSourceServers', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_source_servers_with_options_async(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.DescribeSourceServersResponse().from_map(
            await self.do_rpcrequest_async('DescribeSourceServers', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_source_servers(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_source_servers_with_options(request, runtime)

    async def describe_source_servers_async(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_source_servers_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_replication_job_attribute_with_options(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ModifyReplicationJobAttributeResponse().from_map(
            self.do_rpcrequest('ModifyReplicationJobAttribute', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_replication_job_attribute_with_options_async(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ModifyReplicationJobAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyReplicationJobAttribute', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_replication_job_attribute(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_replication_job_attribute_with_options(request, runtime)

    async def modify_replication_job_attribute_async(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_replication_job_attribute_with_options_async(request, runtime)

    def modify_source_server_attribute_with_options(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ModifySourceServerAttributeResponse().from_map(
            self.do_rpcrequest('ModifySourceServerAttribute', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_source_server_attribute_with_options_async(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.ModifySourceServerAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifySourceServerAttribute', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_source_server_attribute(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_source_server_attribute_with_options(request, runtime)

    async def modify_source_server_attribute_async(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_source_server_attribute_with_options_async(request, runtime)

    def start_replication_job_with_options(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.StartReplicationJobResponse().from_map(
            self.do_rpcrequest('StartReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_replication_job_with_options_async(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.StartReplicationJobResponse().from_map(
            await self.do_rpcrequest_async('StartReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_replication_job(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_replication_job_with_options(request, runtime)

    async def start_replication_job_async(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_replication_job_with_options_async(request, runtime)

    def stop_replication_job_with_options(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.StopReplicationJobResponse().from_map(
            self.do_rpcrequest('StopReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_replication_job_with_options_async(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.StopReplicationJobResponse().from_map(
            await self.do_rpcrequest_async('StopReplicationJob', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_replication_job(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_replication_job_with_options(request, runtime)

    async def stop_replication_job_async(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_replication_job_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: smc_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: smc_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: smc_20190601_models.TagResourcesRequest,
    ) -> smc_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: smc_20190601_models.TagResourcesRequest,
    ) -> smc_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smc_20190601_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
    ) -> smc_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
    ) -> smc_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
