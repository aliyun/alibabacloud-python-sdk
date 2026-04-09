# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_httpdns20160201 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('httpdns', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_domain_with_options(
        self,
        request: main_models.AddDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomain',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: main_models.AddDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomain',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain(
        self,
        request: main_models.AddDomainRequest,
    ) -> main_models.AddDomainResponse:
        runtime = RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: main_models.AddDomainRequest,
    ) -> main_models.AddDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def get_account_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountInfo',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountInfo',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_info(self) -> main_models.GetAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.get_account_info_with_options(runtime)

    async def get_account_info_async(self) -> main_models.GetAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_account_info_with_options_async(runtime)

    def get_resolve_count_summary_with_options(
        self,
        request: main_models.GetResolveCountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResolveCountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.time_span):
            query['TimeSpan'] = request.time_span
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResolveCountSummary',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResolveCountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resolve_count_summary_with_options_async(
        self,
        request: main_models.GetResolveCountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResolveCountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.time_span):
            query['TimeSpan'] = request.time_span
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResolveCountSummary',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResolveCountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resolve_count_summary(
        self,
        request: main_models.GetResolveCountSummaryRequest,
    ) -> main_models.GetResolveCountSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_resolve_count_summary_with_options(request, runtime)

    async def get_resolve_count_summary_async(
        self,
        request: main_models.GetResolveCountSummaryRequest,
    ) -> main_models.GetResolveCountSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_resolve_count_summary_with_options_async(request, runtime)

    def get_resolve_statistics_with_options(
        self,
        request: main_models.GetResolveStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResolveStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.time_span):
            query['TimeSpan'] = request.time_span
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResolveStatistics',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResolveStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resolve_statistics_with_options_async(
        self,
        request: main_models.GetResolveStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResolveStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.time_span):
            query['TimeSpan'] = request.time_span
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResolveStatistics',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResolveStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resolve_statistics(
        self,
        request: main_models.GetResolveStatisticsRequest,
    ) -> main_models.GetResolveStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_resolve_statistics_with_options(request, runtime)

    async def get_resolve_statistics_async(
        self,
        request: main_models.GetResolveStatisticsRequest,
    ) -> main_models.GetResolveStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_resolve_statistics_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.without_metering_data):
            query['WithoutMeteringData'] = request.without_metering_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.without_metering_data):
            query['WithoutMeteringData'] = request.without_metering_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)

    def refresh_resolve_cache_with_options(
        self,
        tmp_req: main_models.RefreshResolveCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshResolveCacheResponse:
        tmp_req.validate()
        request = main_models.RefreshResolveCacheShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domains):
            request.domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.domains, 'Domains', 'json')
        query = {}
        if not DaraCore.is_null(request.domains_shrink):
            query['Domains'] = request.domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshResolveCache',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshResolveCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_resolve_cache_with_options_async(
        self,
        tmp_req: main_models.RefreshResolveCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshResolveCacheResponse:
        tmp_req.validate()
        request = main_models.RefreshResolveCacheShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domains):
            request.domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.domains, 'Domains', 'json')
        query = {}
        if not DaraCore.is_null(request.domains_shrink):
            query['Domains'] = request.domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshResolveCache',
            version = '2016-02-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshResolveCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_resolve_cache(
        self,
        request: main_models.RefreshResolveCacheRequest,
    ) -> main_models.RefreshResolveCacheResponse:
        runtime = RuntimeOptions()
        return self.refresh_resolve_cache_with_options(request, runtime)

    async def refresh_resolve_cache_async(
        self,
        request: main_models.RefreshResolveCacheRequest,
    ) -> main_models.RefreshResolveCacheResponse:
        runtime = RuntimeOptions()
        return await self.refresh_resolve_cache_with_options_async(request, runtime)
