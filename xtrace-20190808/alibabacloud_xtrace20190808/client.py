# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xtrace20190808 import models as xtrace_20190808_models
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
        self._endpoint = self.get_endpoint('xtrace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_tag_key_with_options(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['SpanName'] = request.span_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTagKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTagKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_key_with_options_async(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['SpanName'] = request.span_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTagKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTagKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_key(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_key_with_options(request, runtime)

    async def get_tag_key_async(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_key_with_options_async(request, runtime)

    def get_tag_val_with_options(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagValResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['SpanName'] = request.span_name
        query['TagKey'] = request.tag_key
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTagVal',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTagValResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_val_with_options_async(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagValResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['SpanName'] = request.span_name
        query['TagKey'] = request.tag_key
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTagVal',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTagValResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_val(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
    ) -> xtrace_20190808_models.GetTagValResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_val_with_options(request, runtime)

    async def get_tag_val_async(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
    ) -> xtrace_20190808_models.GetTagValResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_val_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: xtrace_20190808_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['AppType'] = request.app_type
        query['ProxyUserId'] = request.proxy_user_id
        query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: xtrace_20190808_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['AppType'] = request.app_type
        query['ProxyUserId'] = request.proxy_user_id
        query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: xtrace_20190808_models.GetTokenRequest,
    ) -> xtrace_20190808_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: xtrace_20190808_models.GetTokenRequest,
    ) -> xtrace_20190808_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TraceID'] = request.trace_id
        query['AppType'] = request.app_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TraceID'] = request.trace_id
        query['AppType'] = request.app_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
    ) -> xtrace_20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
    ) -> xtrace_20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def list_ip_or_hosts_with_options(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListIpOrHosts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListIpOrHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ip_or_hosts_with_options_async(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListIpOrHosts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListIpOrHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ip_or_hosts(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ip_or_hosts_with_options(request, runtime)

    async def list_ip_or_hosts_async(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ip_or_hosts_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
    ) -> xtrace_20190808_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
    ) -> xtrace_20190808_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def list_span_names_with_options(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSpanNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListSpanNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_span_names_with_options_async(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSpanNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.ListSpanNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_span_names(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_span_names_with_options(request, runtime)

    async def list_span_names_async(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_span_names_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IntervalInSec'] = request.interval_in_sec
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['OrderBy'] = request.order_by
        query['Limit'] = request.limit
        query['Metric'] = request.metric
        query['Order'] = request.order
        query['ProxyUserId'] = request.proxy_user_id
        query['Filters'] = request.filters
        query['Dimensions'] = request.dimensions
        query['Measures'] = request.measures
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.QueryMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IntervalInSec'] = request.interval_in_sec
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['OrderBy'] = request.order_by
        query['Limit'] = request.limit
        query['Metric'] = request.metric
        query['Order'] = request.order
        query['ProxyUserId'] = request.proxy_user_id
        query['Filters'] = request.filters
        query['Dimensions'] = request.dimensions
        query['Measures'] = request.measures
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.QueryMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['OperationName'] = request.operation_name
        query['MinDuration'] = request.min_duration
        query['AppType'] = request.app_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Reverse'] = request.reverse
        query['ServiceIp'] = request.service_ip
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['RegionId'] = request.region_id
        query['ServiceName'] = request.service_name
        query['OperationName'] = request.operation_name
        query['MinDuration'] = request.min_duration
        query['AppType'] = request.app_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Reverse'] = request.reverse
        query['ServiceIp'] = request.service_ip
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.SearchTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)
