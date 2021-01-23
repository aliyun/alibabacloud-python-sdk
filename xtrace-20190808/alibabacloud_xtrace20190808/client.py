# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xtrace20190808 import models as xtrace_20190808_models
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTagKeyResponse().from_map(
            self.do_rpcrequest('GetTagKey', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_tag_key_with_options_async(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTagKeyResponse().from_map(
            await self.do_rpcrequest_async('GetTagKey', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTagValResponse().from_map(
            self.do_rpcrequest('GetTagVal', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_tag_val_with_options_async(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagValResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTagValResponse().from_map(
            await self.do_rpcrequest_async('GetTagVal', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTokenResponse().from_map(
            self.do_rpcrequest('GetToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: xtrace_20190808_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTokenResponse().from_map(
            await self.do_rpcrequest_async('GetToken', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTraceResponse().from_map(
            self.do_rpcrequest('GetTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTraceResponse().from_map(
            await self.do_rpcrequest_async('GetTrace', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_trace_analysis_with_options(
        self,
        request: xtrace_20190808_models.GetTraceAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceAnalysisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTraceAnalysisResponse().from_map(
            self.do_rpcrequest('GetTraceAnalysis', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_analysis_with_options_async(
        self,
        request: xtrace_20190808_models.GetTraceAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceAnalysisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.GetTraceAnalysisResponse().from_map(
            await self.do_rpcrequest_async('GetTraceAnalysis', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trace_analysis(
        self,
        request: xtrace_20190808_models.GetTraceAnalysisRequest,
    ) -> xtrace_20190808_models.GetTraceAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_analysis_with_options(request, runtime)

    async def get_trace_analysis_async(
        self,
        request: xtrace_20190808_models.GetTraceAnalysisRequest,
    ) -> xtrace_20190808_models.GetTraceAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_analysis_with_options_async(request, runtime)

    def list_ip_or_hosts_with_options(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListIpOrHostsResponse().from_map(
            self.do_rpcrequest('ListIpOrHosts', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ip_or_hosts_with_options_async(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListIpOrHostsResponse().from_map(
            await self.do_rpcrequest_async('ListIpOrHosts', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListServicesResponse().from_map(
            self.do_rpcrequest('ListServices', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListServicesResponse().from_map(
            await self.do_rpcrequest_async('ListServices', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListSpanNamesResponse().from_map(
            self.do_rpcrequest('ListSpanNames', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_span_names_with_options_async(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.ListSpanNamesResponse().from_map(
            await self.do_rpcrequest_async('ListSpanNames', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.QueryMetricResponse().from_map(
            self.do_rpcrequest('QueryMetric', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.QueryMetricResponse().from_map(
            await self.do_rpcrequest_async('QueryMetric', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.SearchTracesResponse().from_map(
            self.do_rpcrequest('SearchTraces', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return xtrace_20190808_models.SearchTracesResponse().from_map(
            await self.do_rpcrequest_async('SearchTraces', '2019-08-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
