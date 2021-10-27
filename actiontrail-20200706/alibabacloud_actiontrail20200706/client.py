# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_actiontrail20200706 import models as actiontrail_20200706_models
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
            'ap-northeast-2-pop': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-beijing-gov-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-nu16-b01': 'actiontrail.aliyuncs.com',
            'cn-edge-1': 'actiontrail.aliyuncs.com',
            'cn-fujian': 'actiontrail.aliyuncs.com',
            'cn-haidian-cm12-c01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-finance': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-test-306': 'actiontrail.aliyuncs.com',
            'cn-hongkong-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-qingdao-nebula': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et15-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et2-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-inner': 'actiontrail.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-finance-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-inner': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'actiontrail.aliyuncs.com',
            'cn-wuhan': 'actiontrail.aliyuncs.com',
            'cn-yushanfang': 'actiontrail.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'actiontrail.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'actiontrail.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'actiontrail.aliyuncs.com',
            'eu-west-1-oxs': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'actiontrail.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('actiontrail', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            self.do_rpcrequest('CreateDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            await self.do_rpcrequest_async('CreateDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_delivery_history_job(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_delivery_history_job_with_options(request, runtime)

    async def create_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_delivery_history_job_with_options_async(request, runtime)

    def create_trail_with_options(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            self.do_rpcrequest('CreateTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            await self.do_rpcrequest_async('CreateTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_trail(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trail_with_options(request, runtime)

    async def create_trail_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trail_with_options_async(request, runtime)

    def delete_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            self.do_rpcrequest('DeleteDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            await self.do_rpcrequest_async('DeleteDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_delivery_history_job(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_history_job_with_options(request, runtime)

    async def delete_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_delivery_history_job_with_options_async(request, runtime)

    def delete_trail_with_options(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            self.do_rpcrequest('DeleteTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            await self.do_rpcrequest_async('DeleteTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trail(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trail_with_options(request, runtime)

    async def delete_trail_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trail_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_trails_with_options(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            self.do_rpcrequest('DescribeTrails', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_trails_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            await self.do_rpcrequest_async('DescribeTrails', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_trails(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trails_with_options(request, runtime)

    async def describe_trails_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trails_with_options_async(request, runtime)

    def get_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            self.do_rpcrequest('GetDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            await self.do_rpcrequest_async('GetDeliveryHistoryJob', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_delivery_history_job(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_delivery_history_job_with_options(request, runtime)

    async def get_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_delivery_history_job_with_options_async(request, runtime)

    def get_trail_status_with_options(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            self.do_rpcrequest('GetTrailStatus', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trail_status_with_options_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            await self.do_rpcrequest_async('GetTrailStatus', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trail_status(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trail_status_with_options(request, runtime)

    async def get_trail_status_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trail_status_with_options_async(request, runtime)

    def list_delivery_history_jobs_with_options(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            self.do_rpcrequest('ListDeliveryHistoryJobs', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_delivery_history_jobs_with_options_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            await self.do_rpcrequest_async('ListDeliveryHistoryJobs', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_delivery_history_jobs(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_history_jobs_with_options(request, runtime)

    async def list_delivery_history_jobs_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delivery_history_jobs_with_options_async(request, runtime)

    def lookup_events_with_options(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            self.do_rpcrequest('LookupEvents', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lookup_events_with_options_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            await self.do_rpcrequest_async('LookupEvents', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lookup_events(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    async def lookup_events_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lookup_events_with_options_async(request, runtime)

    def start_logging_with_options(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            self.do_rpcrequest('StartLogging', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            await self.do_rpcrequest_async('StartLogging', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_logging(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_logging_with_options(request, runtime)

    async def start_logging_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_logging_with_options_async(request, runtime)

    def stop_logging_with_options(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            self.do_rpcrequest('StopLogging', '2020-07-06', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def stop_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            await self.do_rpcrequest_async('StopLogging', '2020-07-06', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_logging(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_logging_with_options(request, runtime)

    async def stop_logging_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_logging_with_options_async(request, runtime)

    def update_trail_with_options(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            self.do_rpcrequest('UpdateTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            await self.do_rpcrequest_async('UpdateTrail', '2020-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trail(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trail_with_options(request, runtime)

    async def update_trail_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trail_with_options_async(request, runtime)
