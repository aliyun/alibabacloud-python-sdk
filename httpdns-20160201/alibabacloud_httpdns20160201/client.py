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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'httpdns-api.aliyuncs.com'
        }
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

    def create_sdns_rule_category_with_options(
        self,
        tmp_req: main_models.CreateSdnsRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSdnsRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.CreateSdnsRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ip_ranges):
            request.client_ip_ranges_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ip_ranges, 'ClientIpRanges', 'json')
        if not DaraCore.is_null(tmp_req.paths):
            request.paths_shrink = Utils.array_to_string_with_specified_style(tmp_req.paths, 'Paths', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.client_ip_ranges_shrink):
            body['ClientIpRanges'] = request.client_ip_ranges_shrink
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.line_id):
            body['LineId'] = request.line_id
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.paths_shrink):
            body['Paths'] = request.paths_shrink
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSdnsRuleCategory',
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
            main_models.CreateSdnsRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sdns_rule_category_with_options_async(
        self,
        tmp_req: main_models.CreateSdnsRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSdnsRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.CreateSdnsRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ip_ranges):
            request.client_ip_ranges_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ip_ranges, 'ClientIpRanges', 'json')
        if not DaraCore.is_null(tmp_req.paths):
            request.paths_shrink = Utils.array_to_string_with_specified_style(tmp_req.paths, 'Paths', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.client_ip_ranges_shrink):
            body['ClientIpRanges'] = request.client_ip_ranges_shrink
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.line_id):
            body['LineId'] = request.line_id
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.paths_shrink):
            body['Paths'] = request.paths_shrink
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSdnsRuleCategory',
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
            main_models.CreateSdnsRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sdns_rule_category(
        self,
        request: main_models.CreateSdnsRuleCategoryRequest,
    ) -> main_models.CreateSdnsRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.create_sdns_rule_category_with_options(request, runtime)

    async def create_sdns_rule_category_async(
        self,
        request: main_models.CreateSdnsRuleCategoryRequest,
    ) -> main_models.CreateSdnsRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.create_sdns_rule_category_with_options_async(request, runtime)

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

    def sdns_delete_rule_category_with_options(
        self,
        request: main_models.SdnsDeleteRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsDeleteRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsDeleteRuleCategory',
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
            main_models.SdnsDeleteRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdns_delete_rule_category_with_options_async(
        self,
        request: main_models.SdnsDeleteRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsDeleteRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsDeleteRuleCategory',
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
            main_models.SdnsDeleteRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdns_delete_rule_category(
        self,
        request: main_models.SdnsDeleteRuleCategoryRequest,
    ) -> main_models.SdnsDeleteRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.sdns_delete_rule_category_with_options(request, runtime)

    async def sdns_delete_rule_category_async(
        self,
        request: main_models.SdnsDeleteRuleCategoryRequest,
    ) -> main_models.SdnsDeleteRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.sdns_delete_rule_category_with_options_async(request, runtime)

    def sdns_get_rule_category_with_options(
        self,
        request: main_models.SdnsGetRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsGetRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsGetRuleCategory',
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
            main_models.SdnsGetRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdns_get_rule_category_with_options_async(
        self,
        request: main_models.SdnsGetRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsGetRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsGetRuleCategory',
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
            main_models.SdnsGetRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdns_get_rule_category(
        self,
        request: main_models.SdnsGetRuleCategoryRequest,
    ) -> main_models.SdnsGetRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.sdns_get_rule_category_with_options(request, runtime)

    async def sdns_get_rule_category_async(
        self,
        request: main_models.SdnsGetRuleCategoryRequest,
    ) -> main_models.SdnsGetRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.sdns_get_rule_category_with_options_async(request, runtime)

    def sdns_list_rule_categories_with_options(
        self,
        request: main_models.SdnsListRuleCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsListRuleCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsListRuleCategories',
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
            main_models.SdnsListRuleCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdns_list_rule_categories_with_options_async(
        self,
        request: main_models.SdnsListRuleCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsListRuleCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsListRuleCategories',
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
            main_models.SdnsListRuleCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdns_list_rule_categories(
        self,
        request: main_models.SdnsListRuleCategoriesRequest,
    ) -> main_models.SdnsListRuleCategoriesResponse:
        runtime = RuntimeOptions()
        return self.sdns_list_rule_categories_with_options(request, runtime)

    async def sdns_list_rule_categories_async(
        self,
        request: main_models.SdnsListRuleCategoriesRequest,
    ) -> main_models.SdnsListRuleCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.sdns_list_rule_categories_with_options_async(request, runtime)

    def sdns_switch_rule_category_with_options(
        self,
        request: main_models.SdnsSwitchRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsSwitchRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsSwitchRuleCategory',
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
            main_models.SdnsSwitchRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdns_switch_rule_category_with_options_async(
        self,
        request: main_models.SdnsSwitchRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsSwitchRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdnsSwitchRuleCategory',
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
            main_models.SdnsSwitchRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdns_switch_rule_category(
        self,
        request: main_models.SdnsSwitchRuleCategoryRequest,
    ) -> main_models.SdnsSwitchRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.sdns_switch_rule_category_with_options(request, runtime)

    async def sdns_switch_rule_category_async(
        self,
        request: main_models.SdnsSwitchRuleCategoryRequest,
    ) -> main_models.SdnsSwitchRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.sdns_switch_rule_category_with_options_async(request, runtime)

    def sdns_verify_rule_category_with_options(
        self,
        tmp_req: main_models.SdnsVerifyRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsVerifyRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.SdnsVerifyRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.args):
            request.args_shrink = Utils.array_to_string_with_specified_style(tmp_req.args, 'Args', 'json')
        if not DaraCore.is_null(tmp_req.client_ip_ranges):
            request.client_ip_ranges_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ip_ranges, 'ClientIpRanges', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.args_shrink):
            body['Args'] = request.args_shrink
        if not DaraCore.is_null(request.cip):
            body['Cip'] = request.cip
        if not DaraCore.is_null(request.client_ip_ranges_shrink):
            body['ClientIpRanges'] = request.client_ip_ranges_shrink
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SdnsVerifyRuleCategory',
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
            main_models.SdnsVerifyRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdns_verify_rule_category_with_options_async(
        self,
        tmp_req: main_models.SdnsVerifyRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdnsVerifyRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.SdnsVerifyRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.args):
            request.args_shrink = Utils.array_to_string_with_specified_style(tmp_req.args, 'Args', 'json')
        if not DaraCore.is_null(tmp_req.client_ip_ranges):
            request.client_ip_ranges_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ip_ranges, 'ClientIpRanges', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.args_shrink):
            body['Args'] = request.args_shrink
        if not DaraCore.is_null(request.cip):
            body['Cip'] = request.cip
        if not DaraCore.is_null(request.client_ip_ranges_shrink):
            body['ClientIpRanges'] = request.client_ip_ranges_shrink
        if not DaraCore.is_null(request.match_type):
            body['MatchType'] = request.match_type
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SdnsVerifyRuleCategory',
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
            main_models.SdnsVerifyRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdns_verify_rule_category(
        self,
        request: main_models.SdnsVerifyRuleCategoryRequest,
    ) -> main_models.SdnsVerifyRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.sdns_verify_rule_category_with_options(request, runtime)

    async def sdns_verify_rule_category_async(
        self,
        request: main_models.SdnsVerifyRuleCategoryRequest,
    ) -> main_models.SdnsVerifyRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.sdns_verify_rule_category_with_options_async(request, runtime)

    def update_sdns_rule_category_with_options(
        self,
        tmp_req: main_models.UpdateSdnsRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSdnsRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.UpdateSdnsRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.client_ip_ranges):
            body['ClientIpRanges'] = request.client_ip_ranges
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSdnsRuleCategory',
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
            main_models.UpdateSdnsRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sdns_rule_category_with_options_async(
        self,
        tmp_req: main_models.UpdateSdnsRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSdnsRuleCategoryResponse:
        tmp_req.validate()
        request = main_models.UpdateSdnsRuleCategoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.client_ip_ranges):
            body['ClientIpRanges'] = request.client_ip_ranges
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSdnsRuleCategory',
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
            main_models.UpdateSdnsRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sdns_rule_category(
        self,
        request: main_models.UpdateSdnsRuleCategoryRequest,
    ) -> main_models.UpdateSdnsRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_sdns_rule_category_with_options(request, runtime)

    async def update_sdns_rule_category_async(
        self,
        request: main_models.UpdateSdnsRuleCategoryRequest,
    ) -> main_models.UpdateSdnsRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_sdns_rule_category_with_options_async(request, runtime)
