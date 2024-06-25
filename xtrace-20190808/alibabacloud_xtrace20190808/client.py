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

    def check_commercial_status_with_options(
        self,
        request: xtrace_20190808_models.CheckCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.CheckCommercialStatusResponse:
        """
        @summary 检查商业化状态
        
        @param request: CheckCommercialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCommercialStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.CheckCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_commercial_status_with_options_async(
        self,
        request: xtrace_20190808_models.CheckCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.CheckCommercialStatusResponse:
        """
        @summary 检查商业化状态
        
        @param request: CheckCommercialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCommercialStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.CheckCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_commercial_status(
        self,
        request: xtrace_20190808_models.CheckCommercialStatusRequest,
    ) -> xtrace_20190808_models.CheckCommercialStatusResponse:
        """
        @summary 检查商业化状态
        
        @param request: CheckCommercialStatusRequest
        @return: CheckCommercialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_commercial_status_with_options(request, runtime)

    async def check_commercial_status_async(
        self,
        request: xtrace_20190808_models.CheckCommercialStatusRequest,
    ) -> xtrace_20190808_models.CheckCommercialStatusResponse:
        """
        @summary 检查商业化状态
        
        @param request: CheckCommercialStatusRequest
        @return: CheckCommercialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_commercial_status_with_options_async(request, runtime)

    def get_tag_key_with_options(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        """
        @summary Queries tag keys.
        
        @param request: GetTagKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries tag keys.
        
        @param request: GetTagKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries tag keys.
        
        @param request: GetTagKeyRequest
        @return: GetTagKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tag_key_with_options(request, runtime)

    async def get_tag_key_async(
        self,
        request: xtrace_20190808_models.GetTagKeyRequest,
    ) -> xtrace_20190808_models.GetTagKeyResponse:
        """
        @summary Queries tag keys.
        
        @param request: GetTagKeyRequest
        @return: GetTagKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_key_with_options_async(request, runtime)

    def get_tag_val_with_options(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTagValResponse:
        """
        @summary Queries the tag values that correspond to a tag key.
        
        @param request: GetTagValRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagValResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagVal',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the tag values that correspond to a tag key.
        
        @param request: GetTagValRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTagValResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagVal',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the tag values that correspond to a tag key.
        
        @param request: GetTagValRequest
        @return: GetTagValResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tag_val_with_options(request, runtime)

    async def get_tag_val_async(
        self,
        request: xtrace_20190808_models.GetTagValRequest,
    ) -> xtrace_20190808_models.GetTagValResponse:
        """
        @summary Queries the tag values that correspond to a tag key.
        
        @param request: GetTagValRequest
        @return: GetTagValResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_val_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.GetTraceResponse:
        """
        @summary Queries the details of a trace.
        
        @param request: GetTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details of a trace.
        
        @param request: GetTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details of a trace.
        
        @param request: GetTraceRequest
        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: xtrace_20190808_models.GetTraceRequest,
    ) -> xtrace_20190808_models.GetTraceResponse:
        """
        @summary Queries the details of a trace.
        
        @param request: GetTraceRequest
        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def list_ip_or_hosts_with_options(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        """
        @summary Queries the IP addresses of an application.
        
        @param request: ListIpOrHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpOrHostsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpOrHosts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the IP addresses of an application.
        
        @param request: ListIpOrHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpOrHostsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpOrHosts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the IP addresses of an application.
        
        @param request: ListIpOrHostsRequest
        @return: ListIpOrHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ip_or_hosts_with_options(request, runtime)

    async def list_ip_or_hosts_async(
        self,
        request: xtrace_20190808_models.ListIpOrHostsRequest,
    ) -> xtrace_20190808_models.ListIpOrHostsResponse:
        """
        @summary Queries the IP addresses of an application.
        
        @param request: ListIpOrHostsRequest
        @return: ListIpOrHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ip_or_hosts_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListServicesResponse:
        """
        @summary Queries applications.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries applications.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries applications.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: xtrace_20190808_models.ListServicesRequest,
    ) -> xtrace_20190808_models.ListServicesResponse:
        """
        @summary Queries applications.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def list_span_names_with_options(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        """
        @summary Queries all span names in a specified region or all span names of a microservice.
        
        @param request: ListSpanNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSpanNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpanNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries all span names in a specified region or all span names of a microservice.
        
        @param request: ListSpanNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSpanNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpanNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries all span names in a specified region or all span names of a microservice.
        
        @param request: ListSpanNamesRequest
        @return: ListSpanNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_span_names_with_options(request, runtime)

    async def list_span_names_async(
        self,
        request: xtrace_20190808_models.ListSpanNamesRequest,
    ) -> xtrace_20190808_models.ListSpanNamesResponse:
        """
        @summary Queries all span names in a specified region or all span names of a microservice.
        
        @param request: ListSpanNamesRequest
        @return: ListSpanNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_span_names_with_options_async(request, runtime)

    def open_xtrace_service_with_options(
        self,
        request: xtrace_20190808_models.OpenXtraceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.OpenXtraceServiceResponse:
        """
        @summary 开通xtrace和对应的sls
        
        @param request: OpenXtraceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenXtraceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceService',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.OpenXtraceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_xtrace_service_with_options_async(
        self,
        request: xtrace_20190808_models.OpenXtraceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.OpenXtraceServiceResponse:
        """
        @summary 开通xtrace和对应的sls
        
        @param request: OpenXtraceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenXtraceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceService',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtrace_20190808_models.OpenXtraceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_xtrace_service(
        self,
        request: xtrace_20190808_models.OpenXtraceServiceRequest,
    ) -> xtrace_20190808_models.OpenXtraceServiceResponse:
        """
        @summary 开通xtrace和对应的sls
        
        @param request: OpenXtraceServiceRequest
        @return: OpenXtraceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_service_with_options(request, runtime)

    async def open_xtrace_service_async(
        self,
        request: xtrace_20190808_models.OpenXtraceServiceRequest,
    ) -> xtrace_20190808_models.OpenXtraceServiceResponse:
        """
        @summary 开通xtrace和对应的sls
        
        @param request: OpenXtraceServiceRequest
        @return: OpenXtraceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_xtrace_service_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        """
        @summary Queries a metric.
        
        @param request: QueryMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries a metric.
        
        @param request: QueryMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries a metric.
        
        @param request: QueryMetricRequest
        @return: QueryMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: xtrace_20190808_models.QueryMetricRequest,
    ) -> xtrace_20190808_models.QueryMetricResponse:
        """
        @summary Queries a metric.
        
        @param request: QueryMetricRequest
        @return: QueryMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        """
        @summary Queries traces by time, application name, IP address, span name, and tag.
        
        @param request: SearchTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries traces by time, application name, IP address, span name, and tag.
        
        @param request: SearchTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries traces by time, application name, IP address, span name, and tag.
        
        @param request: SearchTracesRequest
        @return: SearchTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: xtrace_20190808_models.SearchTracesRequest,
    ) -> xtrace_20190808_models.SearchTracesResponse:
        """
        @summary Queries traces by time, application name, IP address, span name, and tag.
        
        @param request: SearchTracesRequest
        @return: SearchTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)
