# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_alidns20150109 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alidns', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_custom_line_with_options(
        self,
        request: main_models.AddCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_line_with_options_async(
        self,
        request: main_models.AddCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_line(
        self,
        request: main_models.AddCustomLineRequest,
    ) -> main_models.AddCustomLineResponse:
        runtime = RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    async def add_custom_line_async(
        self,
        request: main_models.AddCustomLineRequest,
    ) -> main_models.AddCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_line_with_options_async(request, runtime)

    def add_dns_cache_domain_with_options(
        self,
        request: main_models.AddDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not DaraCore.is_null(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not DaraCore.is_null(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not DaraCore.is_null(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_cache_domain_with_options_async(
        self,
        request: main_models.AddDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not DaraCore.is_null(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not DaraCore.is_null(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not DaraCore.is_null(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_cache_domain(
        self,
        request: main_models.AddDnsCacheDomainRequest,
    ) -> main_models.AddDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return self.add_dns_cache_domain_with_options(request, runtime)

    async def add_dns_cache_domain_async(
        self,
        request: main_models.AddDnsCacheDomainRequest,
    ) -> main_models.AddDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_dns_cache_domain_with_options_async(request, runtime)

    def add_dns_gtm_access_strategy_with_options(
        self,
        request: main_models.AddDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not DaraCore.is_null(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not DaraCore.is_null(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not DaraCore.is_null(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not DaraCore.is_null(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not DaraCore.is_null(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not DaraCore.is_null(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not DaraCore.is_null(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not DaraCore.is_null(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not DaraCore.is_null(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not DaraCore.is_null(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not DaraCore.is_null(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_access_strategy_with_options_async(
        self,
        request: main_models.AddDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not DaraCore.is_null(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not DaraCore.is_null(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not DaraCore.is_null(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not DaraCore.is_null(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not DaraCore.is_null(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not DaraCore.is_null(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not DaraCore.is_null(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not DaraCore.is_null(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not DaraCore.is_null(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not DaraCore.is_null(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not DaraCore.is_null(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_access_strategy(
        self,
        request: main_models.AddDnsGtmAccessStrategyRequest,
    ) -> main_models.AddDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.add_dns_gtm_access_strategy_with_options(request, runtime)

    async def add_dns_gtm_access_strategy_async(
        self,
        request: main_models.AddDnsGtmAccessStrategyRequest,
    ) -> main_models.AddDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.add_dns_gtm_access_strategy_with_options_async(request, runtime)

    def add_dns_gtm_address_pool_with_options(
        self,
        request: main_models.AddDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_address_pool_with_options_async(
        self,
        request: main_models.AddDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_address_pool(
        self,
        request: main_models.AddDnsGtmAddressPoolRequest,
    ) -> main_models.AddDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.add_dns_gtm_address_pool_with_options(request, runtime)

    async def add_dns_gtm_address_pool_async(
        self,
        request: main_models.AddDnsGtmAddressPoolRequest,
    ) -> main_models.AddDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.add_dns_gtm_address_pool_with_options_async(request, runtime)

    def add_dns_gtm_monitor_with_options(
        self,
        request: main_models.AddDnsGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_monitor_with_options_async(
        self,
        request: main_models.AddDnsGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_monitor(
        self,
        request: main_models.AddDnsGtmMonitorRequest,
    ) -> main_models.AddDnsGtmMonitorResponse:
        runtime = RuntimeOptions()
        return self.add_dns_gtm_monitor_with_options(request, runtime)

    async def add_dns_gtm_monitor_async(
        self,
        request: main_models.AddDnsGtmMonitorRequest,
    ) -> main_models.AddDnsGtmMonitorResponse:
        runtime = RuntimeOptions()
        return await self.add_dns_gtm_monitor_with_options_async(request, runtime)

    def add_domain_with_options(
        self,
        request: main_models.AddDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomain',
            version = '2015-01-09',
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
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomain',
            version = '2015-01-09',
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

    def add_domain_backup_with_options(
        self,
        request: main_models.AddDomainBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainBackup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_backup_with_options_async(
        self,
        request: main_models.AddDomainBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainBackup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_backup(
        self,
        request: main_models.AddDomainBackupRequest,
    ) -> main_models.AddDomainBackupResponse:
        runtime = RuntimeOptions()
        return self.add_domain_backup_with_options(request, runtime)

    async def add_domain_backup_async(
        self,
        request: main_models.AddDomainBackupRequest,
    ) -> main_models.AddDomainBackupResponse:
        runtime = RuntimeOptions()
        return await self.add_domain_backup_with_options_async(request, runtime)

    def add_domain_group_with_options(
        self,
        request: main_models.AddDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_group_with_options_async(
        self,
        request: main_models.AddDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_group(
        self,
        request: main_models.AddDomainGroupRequest,
    ) -> main_models.AddDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.add_domain_group_with_options(request, runtime)

    async def add_domain_group_async(
        self,
        request: main_models.AddDomainGroupRequest,
    ) -> main_models.AddDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_domain_group_with_options_async(request, runtime)

    def add_domain_record_with_options(
        self,
        request: main_models.AddDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['TTL'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_record_with_options_async(
        self,
        request: main_models.AddDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['TTL'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_record(
        self,
        request: main_models.AddDomainRecordRequest,
    ) -> main_models.AddDomainRecordResponse:
        runtime = RuntimeOptions()
        return self.add_domain_record_with_options(request, runtime)

    async def add_domain_record_async(
        self,
        request: main_models.AddDomainRecordRequest,
    ) -> main_models.AddDomainRecordResponse:
        runtime = RuntimeOptions()
        return await self.add_domain_record_with_options_async(request, runtime)

    def add_gtm_access_strategy_with_options(
        self,
        request: main_models.AddGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not DaraCore.is_null(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not DaraCore.is_null(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_access_strategy_with_options_async(
        self,
        request: main_models.AddGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not DaraCore.is_null(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not DaraCore.is_null(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_access_strategy(
        self,
        request: main_models.AddGtmAccessStrategyRequest,
    ) -> main_models.AddGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.add_gtm_access_strategy_with_options(request, runtime)

    async def add_gtm_access_strategy_async(
        self,
        request: main_models.AddGtmAccessStrategyRequest,
    ) -> main_models.AddGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.add_gtm_access_strategy_with_options_async(request, runtime)

    def add_gtm_address_pool_with_options(
        self,
        request: main_models.AddGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_address_pool_with_options_async(
        self,
        request: main_models.AddGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_address_pool(
        self,
        request: main_models.AddGtmAddressPoolRequest,
    ) -> main_models.AddGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.add_gtm_address_pool_with_options(request, runtime)

    async def add_gtm_address_pool_async(
        self,
        request: main_models.AddGtmAddressPoolRequest,
    ) -> main_models.AddGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.add_gtm_address_pool_with_options_async(request, runtime)

    def add_gtm_monitor_with_options(
        self,
        request: main_models.AddGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_monitor_with_options_async(
        self,
        request: main_models.AddGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_monitor(
        self,
        request: main_models.AddGtmMonitorRequest,
    ) -> main_models.AddGtmMonitorResponse:
        runtime = RuntimeOptions()
        return self.add_gtm_monitor_with_options(request, runtime)

    async def add_gtm_monitor_async(
        self,
        request: main_models.AddGtmMonitorRequest,
    ) -> main_models.AddGtmMonitorResponse:
        runtime = RuntimeOptions()
        return await self.add_gtm_monitor_with_options_async(request, runtime)

    def add_gtm_recovery_plan_with_options(
        self,
        request: main_models.AddGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.AddGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_recovery_plan(
        self,
        request: main_models.AddGtmRecoveryPlanRequest,
    ) -> main_models.AddGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.add_gtm_recovery_plan_with_options(request, runtime)

    async def add_gtm_recovery_plan_async(
        self,
        request: main_models.AddGtmRecoveryPlanRequest,
    ) -> main_models.AddGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.add_gtm_recovery_plan_with_options_async(request, runtime)

    def add_recursion_record_with_options(
        self,
        request: main_models.AddRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecursionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_recursion_record_with_options_async(
        self,
        request: main_models.AddRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecursionRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_recursion_record(
        self,
        request: main_models.AddRecursionRecordRequest,
    ) -> main_models.AddRecursionRecordResponse:
        runtime = RuntimeOptions()
        return self.add_recursion_record_with_options(request, runtime)

    async def add_recursion_record_async(
        self,
        request: main_models.AddRecursionRecordRequest,
    ) -> main_models.AddRecursionRecordResponse:
        runtime = RuntimeOptions()
        return await self.add_recursion_record_with_options_async(request, runtime)

    def add_recursion_zone_with_options(
        self,
        request: main_models.AddRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecursionZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_recursion_zone_with_options_async(
        self,
        request: main_models.AddRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecursionZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_recursion_zone(
        self,
        request: main_models.AddRecursionZoneRequest,
    ) -> main_models.AddRecursionZoneResponse:
        runtime = RuntimeOptions()
        return self.add_recursion_zone_with_options(request, runtime)

    async def add_recursion_zone_async(
        self,
        request: main_models.AddRecursionZoneRequest,
    ) -> main_models.AddRecursionZoneResponse:
        runtime = RuntimeOptions()
        return await self.add_recursion_zone_with_options_async(request, runtime)

    def add_rsp_domain_server_hold_status_for_gateway_with_options(
        self,
        request: main_models.AddRspDomainServerHoldStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRspDomainServerHoldStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.status_msg):
            query['StatusMsg'] = request.status_msg
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRspDomainServerHoldStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRspDomainServerHoldStatusForGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rsp_domain_server_hold_status_for_gateway_with_options_async(
        self,
        request: main_models.AddRspDomainServerHoldStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRspDomainServerHoldStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.status_msg):
            query['StatusMsg'] = request.status_msg
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRspDomainServerHoldStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRspDomainServerHoldStatusForGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rsp_domain_server_hold_status_for_gateway(
        self,
        request: main_models.AddRspDomainServerHoldStatusForGatewayRequest,
    ) -> main_models.AddRspDomainServerHoldStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return self.add_rsp_domain_server_hold_status_for_gateway_with_options(request, runtime)

    async def add_rsp_domain_server_hold_status_for_gateway_async(
        self,
        request: main_models.AddRspDomainServerHoldStatusForGatewayRequest,
    ) -> main_models.AddRspDomainServerHoldStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return await self.add_rsp_domain_server_hold_status_for_gateway_with_options_async(request, runtime)

    def bind_instance_domains_with_options(
        self,
        request: main_models.BindInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_instance_domains_with_options_async(
        self,
        request: main_models.BindInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_instance_domains(
        self,
        request: main_models.BindInstanceDomainsRequest,
    ) -> main_models.BindInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return self.bind_instance_domains_with_options(request, runtime)

    async def bind_instance_domains_async(
        self,
        request: main_models.BindInstanceDomainsRequest,
    ) -> main_models.BindInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return await self.bind_instance_domains_with_options_async(request, runtime)

    def change_domain_group_with_options(
        self,
        request: main_models.ChangeDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_group_with_options_async(
        self,
        request: main_models.ChangeDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_group(
        self,
        request: main_models.ChangeDomainGroupRequest,
    ) -> main_models.ChangeDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.change_domain_group_with_options(request, runtime)

    async def change_domain_group_async(
        self,
        request: main_models.ChangeDomainGroupRequest,
    ) -> main_models.ChangeDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_domain_group_with_options_async(request, runtime)

    def change_domain_of_dns_product_with_options(
        self,
        request: main_models.ChangeDomainOfDnsProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainOfDnsProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_domain):
            query['NewDomain'] = request.new_domain
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainOfDnsProduct',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainOfDnsProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_of_dns_product_with_options_async(
        self,
        request: main_models.ChangeDomainOfDnsProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDomainOfDnsProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_domain):
            query['NewDomain'] = request.new_domain
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDomainOfDnsProduct',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDomainOfDnsProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_of_dns_product(
        self,
        request: main_models.ChangeDomainOfDnsProductRequest,
    ) -> main_models.ChangeDomainOfDnsProductResponse:
        runtime = RuntimeOptions()
        return self.change_domain_of_dns_product_with_options(request, runtime)

    async def change_domain_of_dns_product_async(
        self,
        request: main_models.ChangeDomainOfDnsProductRequest,
    ) -> main_models.ChangeDomainOfDnsProductResponse:
        runtime = RuntimeOptions()
        return await self.change_domain_of_dns_product_with_options_async(request, runtime)

    def copy_gtm_config_with_options(
        self,
        request: main_models.CopyGtmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyGtmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.copy_type):
            query['CopyType'] = request.copy_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyGtmConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyGtmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_gtm_config_with_options_async(
        self,
        request: main_models.CopyGtmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyGtmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.copy_type):
            query['CopyType'] = request.copy_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyGtmConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyGtmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_gtm_config(
        self,
        request: main_models.CopyGtmConfigRequest,
    ) -> main_models.CopyGtmConfigResponse:
        runtime = RuntimeOptions()
        return self.copy_gtm_config_with_options(request, runtime)

    async def copy_gtm_config_async(
        self,
        request: main_models.CopyGtmConfigRequest,
    ) -> main_models.CopyGtmConfigResponse:
        runtime = RuntimeOptions()
        return await self.copy_gtm_config_with_options_async(request, runtime)

    def create_cloud_gtm_address_with_options(
        self,
        tmp_req: main_models.CreateCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmAddressResponse:
        tmp_req.validate()
        request = main_models.CreateCloudGtmAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_tasks):
            request.health_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not DaraCore.is_null(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not DaraCore.is_null(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_address_with_options_async(
        self,
        tmp_req: main_models.CreateCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmAddressResponse:
        tmp_req.validate()
        request = main_models.CreateCloudGtmAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_tasks):
            request.health_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not DaraCore.is_null(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not DaraCore.is_null(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_address(
        self,
        request: main_models.CreateCloudGtmAddressRequest,
    ) -> main_models.CreateCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_gtm_address_with_options(request, runtime)

    async def create_cloud_gtm_address_async(
        self,
        request: main_models.CreateCloudGtmAddressRequest,
    ) -> main_models.CreateCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_gtm_address_with_options_async(request, runtime)

    def create_cloud_gtm_address_pool_with_options(
        self,
        request: main_models.CreateCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_address_pool_with_options_async(
        self,
        request: main_models.CreateCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_address_pool(
        self,
        request: main_models.CreateCloudGtmAddressPoolRequest,
    ) -> main_models.CreateCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_gtm_address_pool_with_options(request, runtime)

    async def create_cloud_gtm_address_pool_async(
        self,
        request: main_models.CreateCloudGtmAddressPoolRequest,
    ) -> main_models.CreateCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_gtm_address_pool_with_options_async(request, runtime)

    def create_cloud_gtm_instance_config_with_options(
        self,
        request: main_models.CreateCloudGtmInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not DaraCore.is_null(request.schedule_rr_type):
            query['ScheduleRrType'] = request.schedule_rr_type
        if not DaraCore.is_null(request.schedule_zone_mode):
            query['ScheduleZoneMode'] = request.schedule_zone_mode
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_instance_config_with_options_async(
        self,
        request: main_models.CreateCloudGtmInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not DaraCore.is_null(request.schedule_rr_type):
            query['ScheduleRrType'] = request.schedule_rr_type
        if not DaraCore.is_null(request.schedule_zone_mode):
            query['ScheduleZoneMode'] = request.schedule_zone_mode
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_instance_config(
        self,
        request: main_models.CreateCloudGtmInstanceConfigRequest,
    ) -> main_models.CreateCloudGtmInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_gtm_instance_config_with_options(request, runtime)

    async def create_cloud_gtm_instance_config_async(
        self,
        request: main_models.CreateCloudGtmInstanceConfigRequest,
    ) -> main_models.CreateCloudGtmInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_gtm_instance_config_with_options_async(request, runtime)

    def create_cloud_gtm_monitor_template_with_options(
        self,
        tmp_req: main_models.CreateCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmMonitorTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCloudGtmMonitorTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_monitor_template_with_options_async(
        self,
        tmp_req: main_models.CreateCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudGtmMonitorTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCloudGtmMonitorTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_monitor_template(
        self,
        request: main_models.CreateCloudGtmMonitorTemplateRequest,
    ) -> main_models.CreateCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_gtm_monitor_template_with_options(request, runtime)

    async def create_cloud_gtm_monitor_template_async(
        self,
        request: main_models.CreateCloudGtmMonitorTemplateRequest,
    ) -> main_models.CreateCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def create_pdns_app_key_with_options(
        self,
        request: main_models.CreatePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdns_app_key_with_options_async(
        self,
        request: main_models.CreatePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdns_app_key(
        self,
        request: main_models.CreatePdnsAppKeyRequest,
    ) -> main_models.CreatePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return self.create_pdns_app_key_with_options(request, runtime)

    async def create_pdns_app_key_async(
        self,
        request: main_models.CreatePdnsAppKeyRequest,
    ) -> main_models.CreatePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_pdns_app_key_with_options_async(request, runtime)

    def create_pdns_udp_ip_segment_with_options(
        self,
        request: main_models.CreatePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_token):
            query['IpToken'] = request.ip_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdns_udp_ip_segment_with_options_async(
        self,
        request: main_models.CreatePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_token):
            query['IpToken'] = request.ip_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdns_udp_ip_segment(
        self,
        request: main_models.CreatePdnsUdpIpSegmentRequest,
    ) -> main_models.CreatePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return self.create_pdns_udp_ip_segment_with_options(request, runtime)

    async def create_pdns_udp_ip_segment_async(
        self,
        request: main_models.CreatePdnsUdpIpSegmentRequest,
    ) -> main_models.CreatePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return await self.create_pdns_udp_ip_segment_with_options_async(request, runtime)

    def delete_cloud_gtm_address_with_options(
        self,
        request: main_models.DeleteCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_address_with_options_async(
        self,
        request: main_models.DeleteCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_address(
        self,
        request: main_models.DeleteCloudGtmAddressRequest,
    ) -> main_models.DeleteCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_gtm_address_with_options(request, runtime)

    async def delete_cloud_gtm_address_async(
        self,
        request: main_models.DeleteCloudGtmAddressRequest,
    ) -> main_models.DeleteCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_gtm_address_with_options_async(request, runtime)

    def delete_cloud_gtm_address_pool_with_options(
        self,
        request: main_models.DeleteCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_address_pool_with_options_async(
        self,
        request: main_models.DeleteCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_address_pool(
        self,
        request: main_models.DeleteCloudGtmAddressPoolRequest,
    ) -> main_models.DeleteCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_gtm_address_pool_with_options(request, runtime)

    async def delete_cloud_gtm_address_pool_async(
        self,
        request: main_models.DeleteCloudGtmAddressPoolRequest,
    ) -> main_models.DeleteCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_gtm_address_pool_with_options_async(request, runtime)

    def delete_cloud_gtm_instance_config_with_options(
        self,
        request: main_models.DeleteCloudGtmInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_instance_config_with_options_async(
        self,
        request: main_models.DeleteCloudGtmInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_instance_config(
        self,
        request: main_models.DeleteCloudGtmInstanceConfigRequest,
    ) -> main_models.DeleteCloudGtmInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_gtm_instance_config_with_options(request, runtime)

    async def delete_cloud_gtm_instance_config_async(
        self,
        request: main_models.DeleteCloudGtmInstanceConfigRequest,
    ) -> main_models.DeleteCloudGtmInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_gtm_instance_config_with_options_async(request, runtime)

    def delete_cloud_gtm_monitor_template_with_options(
        self,
        request: main_models.DeleteCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmMonitorTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_monitor_template_with_options_async(
        self,
        request: main_models.DeleteCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudGtmMonitorTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_monitor_template(
        self,
        request: main_models.DeleteCloudGtmMonitorTemplateRequest,
    ) -> main_models.DeleteCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_gtm_monitor_template_with_options(request, runtime)

    async def delete_cloud_gtm_monitor_template_async(
        self,
        request: main_models.DeleteCloudGtmMonitorTemplateRequest,
    ) -> main_models.DeleteCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def delete_custom_lines_with_options(
        self,
        request: main_models.DeleteCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_ids):
            query['LineIds'] = request.line_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_lines_with_options_async(
        self,
        request: main_models.DeleteCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_ids):
            query['LineIds'] = request.line_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_lines(
        self,
        request: main_models.DeleteCustomLinesRequest,
    ) -> main_models.DeleteCustomLinesResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_lines_with_options(request, runtime)

    async def delete_custom_lines_async(
        self,
        request: main_models.DeleteCustomLinesRequest,
    ) -> main_models.DeleteCustomLinesResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_lines_with_options_async(request, runtime)

    def delete_dns_cache_domain_with_options(
        self,
        request: main_models.DeleteDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_cache_domain_with_options_async(
        self,
        request: main_models.DeleteDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_cache_domain(
        self,
        request: main_models.DeleteDnsCacheDomainRequest,
    ) -> main_models.DeleteDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_dns_cache_domain_with_options(request, runtime)

    async def delete_dns_cache_domain_async(
        self,
        request: main_models.DeleteDnsCacheDomainRequest,
    ) -> main_models.DeleteDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_dns_cache_domain_with_options_async(request, runtime)

    def delete_dns_gtm_access_strategy_with_options(
        self,
        request: main_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_gtm_access_strategy_with_options_async(
        self,
        request: main_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_gtm_access_strategy(
        self,
        request: main_models.DeleteDnsGtmAccessStrategyRequest,
    ) -> main_models.DeleteDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_dns_gtm_access_strategy_with_options(request, runtime)

    async def delete_dns_gtm_access_strategy_async(
        self,
        request: main_models.DeleteDnsGtmAccessStrategyRequest,
    ) -> main_models.DeleteDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_dns_gtm_access_strategy_with_options_async(request, runtime)

    def delete_dns_gtm_address_pool_with_options(
        self,
        request: main_models.DeleteDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_gtm_address_pool_with_options_async(
        self,
        request: main_models.DeleteDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_gtm_address_pool(
        self,
        request: main_models.DeleteDnsGtmAddressPoolRequest,
    ) -> main_models.DeleteDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_dns_gtm_address_pool_with_options(request, runtime)

    async def delete_dns_gtm_address_pool_async(
        self,
        request: main_models.DeleteDnsGtmAddressPoolRequest,
    ) -> main_models.DeleteDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_dns_gtm_address_pool_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2015-01-09',
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
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2015-01-09',
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

    def delete_domain_group_with_options(
        self,
        request: main_models.DeleteDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: main_models.DeleteDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_group(
        self,
        request: main_models.DeleteDomainGroupRequest,
    ) -> main_models.DeleteDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: main_models.DeleteDomainGroupRequest,
    ) -> main_models.DeleteDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_domain_record_with_options(
        self,
        request: main_models.DeleteDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_record_with_options_async(
        self,
        request: main_models.DeleteDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_record(
        self,
        request: main_models.DeleteDomainRecordRequest,
    ) -> main_models.DeleteDomainRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_record_with_options(request, runtime)

    async def delete_domain_record_async(
        self,
        request: main_models.DeleteDomainRecordRequest,
    ) -> main_models.DeleteDomainRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_record_with_options_async(request, runtime)

    def delete_gtm_access_strategy_with_options(
        self,
        request: main_models.DeleteGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_access_strategy_with_options_async(
        self,
        request: main_models.DeleteGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_access_strategy(
        self,
        request: main_models.DeleteGtmAccessStrategyRequest,
    ) -> main_models.DeleteGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_gtm_access_strategy_with_options(request, runtime)

    async def delete_gtm_access_strategy_async(
        self,
        request: main_models.DeleteGtmAccessStrategyRequest,
    ) -> main_models.DeleteGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_gtm_access_strategy_with_options_async(request, runtime)

    def delete_gtm_address_pool_with_options(
        self,
        request: main_models.DeleteGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_address_pool_with_options_async(
        self,
        request: main_models.DeleteGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_address_pool(
        self,
        request: main_models.DeleteGtmAddressPoolRequest,
    ) -> main_models.DeleteGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_gtm_address_pool_with_options(request, runtime)

    async def delete_gtm_address_pool_async(
        self,
        request: main_models.DeleteGtmAddressPoolRequest,
    ) -> main_models.DeleteGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_gtm_address_pool_with_options_async(request, runtime)

    def delete_gtm_recovery_plan_with_options(
        self,
        request: main_models.DeleteGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.DeleteGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_recovery_plan(
        self,
        request: main_models.DeleteGtmRecoveryPlanRequest,
    ) -> main_models.DeleteGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_gtm_recovery_plan_with_options(request, runtime)

    async def delete_gtm_recovery_plan_async(
        self,
        request: main_models.DeleteGtmRecoveryPlanRequest,
    ) -> main_models.DeleteGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_gtm_recovery_plan_with_options_async(request, runtime)

    def delete_recursion_record_with_options(
        self,
        request: main_models.DeleteRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecursionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recursion_record_with_options_async(
        self,
        request: main_models.DeleteRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecursionRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recursion_record(
        self,
        request: main_models.DeleteRecursionRecordRequest,
    ) -> main_models.DeleteRecursionRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_recursion_record_with_options(request, runtime)

    async def delete_recursion_record_async(
        self,
        request: main_models.DeleteRecursionRecordRequest,
    ) -> main_models.DeleteRecursionRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_recursion_record_with_options_async(request, runtime)

    def delete_recursion_zone_with_options(
        self,
        request: main_models.DeleteRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecursionZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recursion_zone_with_options_async(
        self,
        request: main_models.DeleteRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecursionZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recursion_zone(
        self,
        request: main_models.DeleteRecursionZoneRequest,
    ) -> main_models.DeleteRecursionZoneResponse:
        runtime = RuntimeOptions()
        return self.delete_recursion_zone_with_options(request, runtime)

    async def delete_recursion_zone_async(
        self,
        request: main_models.DeleteRecursionZoneRequest,
    ) -> main_models.DeleteRecursionZoneResponse:
        runtime = RuntimeOptions()
        return await self.delete_recursion_zone_with_options_async(request, runtime)

    def delete_sub_domain_records_with_options(
        self,
        request: main_models.DeleteSubDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_domain_records_with_options_async(
        self,
        request: main_models.DeleteSubDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub_domain_records(
        self,
        request: main_models.DeleteSubDomainRecordsRequest,
    ) -> main_models.DeleteSubDomainRecordsResponse:
        runtime = RuntimeOptions()
        return self.delete_sub_domain_records_with_options(request, runtime)

    async def delete_sub_domain_records_async(
        self,
        request: main_models.DeleteSubDomainRecordsRequest,
    ) -> main_models.DeleteSubDomainRecordsResponse:
        runtime = RuntimeOptions()
        return await self.delete_sub_domain_records_with_options_async(request, runtime)

    def describe_batch_result_count_with_options(
        self,
        request: main_models.DescribeBatchResultCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchResultCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchResultCount',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchResultCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_result_count_with_options_async(
        self,
        request: main_models.DescribeBatchResultCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchResultCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchResultCount',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchResultCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_result_count(
        self,
        request: main_models.DescribeBatchResultCountRequest,
    ) -> main_models.DescribeBatchResultCountResponse:
        runtime = RuntimeOptions()
        return self.describe_batch_result_count_with_options(request, runtime)

    async def describe_batch_result_count_async(
        self,
        request: main_models.DescribeBatchResultCountRequest,
    ) -> main_models.DescribeBatchResultCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_batch_result_count_with_options_async(request, runtime)

    def describe_batch_result_detail_with_options(
        self,
        request: main_models.DescribeBatchResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchResultDetail',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_result_detail_with_options_async(
        self,
        request: main_models.DescribeBatchResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchResultDetail',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_result_detail(
        self,
        request: main_models.DescribeBatchResultDetailRequest,
    ) -> main_models.DescribeBatchResultDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_batch_result_detail_with_options(request, runtime)

    async def describe_batch_result_detail_async(
        self,
        request: main_models.DescribeBatchResultDetailRequest,
    ) -> main_models.DescribeBatchResultDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_batch_result_detail_with_options_async(request, runtime)

    def describe_cloud_gtm_address_with_options(
        self,
        request: main_models.DescribeCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_with_options_async(
        self,
        request: main_models.DescribeCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address(
        self,
        request: main_models.DescribeCloudGtmAddressRequest,
    ) -> main_models.DescribeCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_address_with_options(request, runtime)

    async def describe_cloud_gtm_address_async(
        self,
        request: main_models.DescribeCloudGtmAddressRequest,
    ) -> main_models.DescribeCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_address_with_options_async(request, runtime)

    def describe_cloud_gtm_address_pool_with_options(
        self,
        request: main_models.DescribeCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_pool_with_options_async(
        self,
        request: main_models.DescribeCloudGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_pool(
        self,
        request: main_models.DescribeCloudGtmAddressPoolRequest,
    ) -> main_models.DescribeCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_address_pool_with_options(request, runtime)

    async def describe_cloud_gtm_address_pool_async(
        self,
        request: main_models.DescribeCloudGtmAddressPoolRequest,
    ) -> main_models.DescribeCloudGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_address_pool_with_options_async(request, runtime)

    def describe_cloud_gtm_address_pool_reference_with_options(
        self,
        request: main_models.DescribeCloudGtmAddressPoolReferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressPoolReferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressPoolReference',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressPoolReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_pool_reference_with_options_async(
        self,
        request: main_models.DescribeCloudGtmAddressPoolReferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressPoolReferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressPoolReference',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressPoolReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_pool_reference(
        self,
        request: main_models.DescribeCloudGtmAddressPoolReferenceRequest,
    ) -> main_models.DescribeCloudGtmAddressPoolReferenceResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_address_pool_reference_with_options(request, runtime)

    async def describe_cloud_gtm_address_pool_reference_async(
        self,
        request: main_models.DescribeCloudGtmAddressPoolReferenceRequest,
    ) -> main_models.DescribeCloudGtmAddressPoolReferenceResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_address_pool_reference_with_options_async(request, runtime)

    def describe_cloud_gtm_address_reference_with_options(
        self,
        request: main_models.DescribeCloudGtmAddressReferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressReferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressReference',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_reference_with_options_async(
        self,
        request: main_models.DescribeCloudGtmAddressReferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmAddressReferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmAddressReference',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmAddressReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_reference(
        self,
        request: main_models.DescribeCloudGtmAddressReferenceRequest,
    ) -> main_models.DescribeCloudGtmAddressReferenceResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_address_reference_with_options(request, runtime)

    async def describe_cloud_gtm_address_reference_async(
        self,
        request: main_models.DescribeCloudGtmAddressReferenceRequest,
    ) -> main_models.DescribeCloudGtmAddressReferenceResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_address_reference_with_options_async(request, runtime)

    def describe_cloud_gtm_global_alert_with_options(
        self,
        request: main_models.DescribeCloudGtmGlobalAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmGlobalAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmGlobalAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmGlobalAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_global_alert_with_options_async(
        self,
        request: main_models.DescribeCloudGtmGlobalAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmGlobalAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmGlobalAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmGlobalAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_global_alert(
        self,
        request: main_models.DescribeCloudGtmGlobalAlertRequest,
    ) -> main_models.DescribeCloudGtmGlobalAlertResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_global_alert_with_options(request, runtime)

    async def describe_cloud_gtm_global_alert_async(
        self,
        request: main_models.DescribeCloudGtmGlobalAlertRequest,
    ) -> main_models.DescribeCloudGtmGlobalAlertResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_global_alert_with_options_async(request, runtime)

    def describe_cloud_gtm_instance_config_alert_with_options(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmInstanceConfigAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmInstanceConfigAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmInstanceConfigAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_instance_config_alert_with_options_async(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmInstanceConfigAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmInstanceConfigAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmInstanceConfigAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_instance_config_alert(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigAlertRequest,
    ) -> main_models.DescribeCloudGtmInstanceConfigAlertResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_instance_config_alert_with_options(request, runtime)

    async def describe_cloud_gtm_instance_config_alert_async(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigAlertRequest,
    ) -> main_models.DescribeCloudGtmInstanceConfigAlertResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_instance_config_alert_with_options_async(request, runtime)

    def describe_cloud_gtm_instance_config_full_info_with_options(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmInstanceConfigFullInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmInstanceConfigFullInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_instance_config_full_info_with_options_async(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmInstanceConfigFullInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmInstanceConfigFullInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_instance_config_full_info(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
    ) -> main_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_instance_config_full_info_with_options(request, runtime)

    async def describe_cloud_gtm_instance_config_full_info_async(
        self,
        request: main_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
    ) -> main_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_instance_config_full_info_with_options_async(request, runtime)

    def describe_cloud_gtm_monitor_template_with_options(
        self,
        request: main_models.DescribeCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmMonitorTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_monitor_template_with_options_async(
        self,
        request: main_models.DescribeCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmMonitorTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_monitor_template(
        self,
        request: main_models.DescribeCloudGtmMonitorTemplateRequest,
    ) -> main_models.DescribeCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_monitor_template_with_options(request, runtime)

    async def describe_cloud_gtm_monitor_template_async(
        self,
        request: main_models.DescribeCloudGtmMonitorTemplateRequest,
    ) -> main_models.DescribeCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def describe_cloud_gtm_summary_with_options(
        self,
        request: main_models.DescribeCloudGtmSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_summary_with_options_async(
        self,
        request: main_models.DescribeCloudGtmSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_summary(
        self,
        request: main_models.DescribeCloudGtmSummaryRequest,
    ) -> main_models.DescribeCloudGtmSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_summary_with_options(request, runtime)

    async def describe_cloud_gtm_summary_async(
        self,
        request: main_models.DescribeCloudGtmSummaryRequest,
    ) -> main_models.DescribeCloudGtmSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_summary_with_options_async(request, runtime)

    def describe_cloud_gtm_system_lines_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmSystemLinesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmSystemLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmSystemLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_system_lines_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudGtmSystemLinesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCloudGtmSystemLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudGtmSystemLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_system_lines(self) -> main_models.DescribeCloudGtmSystemLinesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_gtm_system_lines_with_options(runtime)

    async def describe_cloud_gtm_system_lines_async(self) -> main_models.DescribeCloudGtmSystemLinesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_gtm_system_lines_with_options_async(runtime)

    def describe_custom_line_with_options(
        self,
        request: main_models.DescribeCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_line_with_options_async(
        self,
        request: main_models.DescribeCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_line(
        self,
        request: main_models.DescribeCustomLineRequest,
    ) -> main_models.DescribeCustomLineResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_line_with_options(request, runtime)

    async def describe_custom_line_async(
        self,
        request: main_models.DescribeCustomLineRequest,
    ) -> main_models.DescribeCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_line_with_options_async(request, runtime)

    def describe_custom_lines_with_options(
        self,
        request: main_models.DescribeCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_lines_with_options_async(
        self,
        request: main_models.DescribeCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_lines(
        self,
        request: main_models.DescribeCustomLinesRequest,
    ) -> main_models.DescribeCustomLinesResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    async def describe_custom_lines_async(
        self,
        request: main_models.DescribeCustomLinesRequest,
    ) -> main_models.DescribeCustomLinesResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_lines_with_options_async(request, runtime)

    def describe_dnsslbsub_domains_with_options(
        self,
        request: main_models.DescribeDNSSLBSubDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDNSSLBSubDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDNSSLBSubDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDNSSLBSubDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dnsslbsub_domains_with_options_async(
        self,
        request: main_models.DescribeDNSSLBSubDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDNSSLBSubDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDNSSLBSubDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDNSSLBSubDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dnsslbsub_domains(
        self,
        request: main_models.DescribeDNSSLBSubDomainsRequest,
    ) -> main_models.DescribeDNSSLBSubDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dnsslbsub_domains_with_options(request, runtime)

    async def describe_dnsslbsub_domains_async(
        self,
        request: main_models.DescribeDNSSLBSubDomainsRequest,
    ) -> main_models.DescribeDNSSLBSubDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dnsslbsub_domains_with_options_async(request, runtime)

    def describe_dns_cache_domains_with_options(
        self,
        request: main_models.DescribeDnsCacheDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsCacheDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsCacheDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsCacheDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_cache_domains_with_options_async(
        self,
        request: main_models.DescribeDnsCacheDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsCacheDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsCacheDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsCacheDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_cache_domains(
        self,
        request: main_models.DescribeDnsCacheDomainsRequest,
    ) -> main_models.DescribeDnsCacheDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_cache_domains_with_options(request, runtime)

    async def describe_dns_cache_domains_async(
        self,
        request: main_models.DescribeDnsCacheDomainsRequest,
    ) -> main_models.DescribeDnsCacheDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_cache_domains_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategies_with_options(
        self,
        request: main_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategies',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategies_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategies',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategies(
        self,
        request: main_models.DescribeDnsGtmAccessStrategiesRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategiesResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_access_strategies_with_options(request, runtime)

    async def describe_dns_gtm_access_strategies_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategiesRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_access_strategies_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_with_options(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategy_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_available_config_with_options(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategyAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategy_available_config_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAccessStrategyAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy_available_config(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_available_config_async(
        self,
        request: main_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_addr_attribute_info_with_options(
        self,
        request: main_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAddrAttributeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addrs):
            query['Addrs'] = request.addrs
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAddrAttributeInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAddrAttributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_addr_attribute_info_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAddrAttributeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addrs):
            query['Addrs'] = request.addrs
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAddrAttributeInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAddrAttributeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_addr_attribute_info(
        self,
        request: main_models.DescribeDnsGtmAddrAttributeInfoRequest,
    ) -> main_models.DescribeDnsGtmAddrAttributeInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_addr_attribute_info_with_options(request, runtime)

    async def describe_dns_gtm_addr_attribute_info_async(
        self,
        request: main_models.DescribeDnsGtmAddrAttributeInfoRequest,
    ) -> main_models.DescribeDnsGtmAddrAttributeInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_addr_attribute_info_with_options_async(request, runtime)

    def describe_dns_gtm_address_pool_available_config_with_options(
        self,
        request: main_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAddressPoolAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_address_pool_available_config_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAddressPoolAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_address_pool_available_config(
        self,
        request: main_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_address_pool_available_config_with_options(request, runtime)

    async def describe_dns_gtm_address_pool_available_config_async(
        self,
        request: main_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_address_pool_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_available_alert_group_with_options(
        self,
        request: main_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAvailableAlertGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAvailableAlertGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_available_alert_group_with_options_async(
        self,
        request: main_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmAvailableAlertGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmAvailableAlertGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmAvailableAlertGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_available_alert_group(
        self,
        request: main_models.DescribeDnsGtmAvailableAlertGroupRequest,
    ) -> main_models.DescribeDnsGtmAvailableAlertGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_available_alert_group_with_options(request, runtime)

    async def describe_dns_gtm_available_alert_group_async(
        self,
        request: main_models.DescribeDnsGtmAvailableAlertGroupRequest,
    ) -> main_models.DescribeDnsGtmAvailableAlertGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_dns_gtm_instance_with_options(
        self,
        request: main_models.DescribeDnsGtmInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance(
        self,
        request: main_models.DescribeDnsGtmInstanceRequest,
    ) -> main_models.DescribeDnsGtmInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instance_with_options(request, runtime)

    async def describe_dns_gtm_instance_async(
        self,
        request: main_models.DescribeDnsGtmInstanceRequest,
    ) -> main_models.DescribeDnsGtmInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instance_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pool_with_options(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_address_pool_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pool(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolRequest,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pool_async(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolRequest,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pools_with_options(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_address_pools_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pools(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolsRequest,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pools_async(
        self,
        request: main_models.DescribeDnsGtmInstanceAddressPoolsRequest,
    ) -> main_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_dns_gtm_instance_status_with_options(
        self,
        request: main_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_status_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_status(
        self,
        request: main_models.DescribeDnsGtmInstanceStatusRequest,
    ) -> main_models.DescribeDnsGtmInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instance_status_with_options(request, runtime)

    async def describe_dns_gtm_instance_status_async(
        self,
        request: main_models.DescribeDnsGtmInstanceStatusRequest,
    ) -> main_models.DescribeDnsGtmInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instance_status_with_options_async(request, runtime)

    def describe_dns_gtm_instance_system_cname_with_options(
        self,
        request: main_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceSystemCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceSystemCname',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_system_cname_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstanceSystemCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstanceSystemCname',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstanceSystemCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_system_cname(
        self,
        request: main_models.DescribeDnsGtmInstanceSystemCnameRequest,
    ) -> main_models.DescribeDnsGtmInstanceSystemCnameResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_dns_gtm_instance_system_cname_async(
        self,
        request: main_models.DescribeDnsGtmInstanceSystemCnameRequest,
    ) -> main_models.DescribeDnsGtmInstanceSystemCnameResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_dns_gtm_instances_with_options(
        self,
        request: main_models.DescribeDnsGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instances_with_options_async(
        self,
        request: main_models.DescribeDnsGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instances(
        self,
        request: main_models.DescribeDnsGtmInstancesRequest,
    ) -> main_models.DescribeDnsGtmInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_instances_with_options(request, runtime)

    async def describe_dns_gtm_instances_async(
        self,
        request: main_models.DescribeDnsGtmInstancesRequest,
    ) -> main_models.DescribeDnsGtmInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_instances_with_options_async(request, runtime)

    def describe_dns_gtm_logs_with_options(
        self,
        request: main_models.DescribeDnsGtmLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_logs_with_options_async(
        self,
        request: main_models.DescribeDnsGtmLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_logs(
        self,
        request: main_models.DescribeDnsGtmLogsRequest,
    ) -> main_models.DescribeDnsGtmLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_logs_with_options(request, runtime)

    async def describe_dns_gtm_logs_async(
        self,
        request: main_models.DescribeDnsGtmLogsRequest,
    ) -> main_models.DescribeDnsGtmLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_logs_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_available_config_with_options(
        self,
        request: main_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmMonitorAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_monitor_available_config_with_options_async(
        self,
        request: main_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmMonitorAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmMonitorAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_monitor_available_config(
        self,
        request: main_models.DescribeDnsGtmMonitorAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_available_config_async(
        self,
        request: main_models.DescribeDnsGtmMonitorAvailableConfigRequest,
    ) -> main_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_config_with_options(
        self,
        request: main_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmMonitorConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_monitor_config_with_options_async(
        self,
        request: main_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsGtmMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsGtmMonitorConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsGtmMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_monitor_config(
        self,
        request: main_models.DescribeDnsGtmMonitorConfigRequest,
    ) -> main_models.DescribeDnsGtmMonitorConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_gtm_monitor_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_config_async(
        self,
        request: main_models.DescribeDnsGtmMonitorConfigRequest,
    ) -> main_models.DescribeDnsGtmMonitorConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_gtm_monitor_config_with_options_async(request, runtime)

    def describe_dns_product_instance_with_options(
        self,
        request: main_models.DescribeDnsProductInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsProductInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsProductInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_product_instance_with_options_async(
        self,
        request: main_models.DescribeDnsProductInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsProductInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsProductInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsProductInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_product_instance(
        self,
        request: main_models.DescribeDnsProductInstanceRequest,
    ) -> main_models.DescribeDnsProductInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_product_instance_with_options(request, runtime)

    async def describe_dns_product_instance_async(
        self,
        request: main_models.DescribeDnsProductInstanceRequest,
    ) -> main_models.DescribeDnsProductInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_product_instance_with_options_async(request, runtime)

    def describe_dns_product_instances_with_options(
        self,
        request: main_models.DescribeDnsProductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsProductInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsProductInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_product_instances_with_options_async(
        self,
        request: main_models.DescribeDnsProductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsProductInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsProductInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsProductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_product_instances(
        self,
        request: main_models.DescribeDnsProductInstancesRequest,
    ) -> main_models.DescribeDnsProductInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_product_instances_with_options(request, runtime)

    async def describe_dns_product_instances_async(
        self,
        request: main_models.DescribeDnsProductInstancesRequest,
    ) -> main_models.DescribeDnsProductInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_product_instances_with_options_async(request, runtime)

    def describe_doh_account_statistics_with_options(
        self,
        request: main_models.DescribeDohAccountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohAccountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohAccountStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohAccountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_account_statistics_with_options_async(
        self,
        request: main_models.DescribeDohAccountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohAccountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohAccountStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohAccountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_account_statistics(
        self,
        request: main_models.DescribeDohAccountStatisticsRequest,
    ) -> main_models.DescribeDohAccountStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_account_statistics_with_options(request, runtime)

    async def describe_doh_account_statistics_async(
        self,
        request: main_models.DescribeDohAccountStatisticsRequest,
    ) -> main_models.DescribeDohAccountStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_account_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_with_options(
        self,
        request: main_models.DescribeDohDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_domain_statistics_with_options_async(
        self,
        request: main_models.DescribeDohDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_domain_statistics(
        self,
        request: main_models.DescribeDohDomainStatisticsRequest,
    ) -> main_models.DescribeDohDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_domain_statistics_with_options(request, runtime)

    async def describe_doh_domain_statistics_async(
        self,
        request: main_models.DescribeDohDomainStatisticsRequest,
    ) -> main_models.DescribeDohDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_domain_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_summary_with_options(
        self,
        request: main_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_domain_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_domain_statistics_summary(
        self,
        request: main_models.DescribeDohDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDohDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_domain_statistics_summary_async(
        self,
        request: main_models.DescribeDohDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDohDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_with_options(
        self,
        request: main_models.DescribeDohSubDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohSubDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohSubDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohSubDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_sub_domain_statistics_with_options_async(
        self,
        request: main_models.DescribeDohSubDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohSubDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohSubDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohSubDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics(
        self,
        request: main_models.DescribeDohSubDomainStatisticsRequest,
    ) -> main_models.DescribeDohSubDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_async(
        self,
        request: main_models.DescribeDohSubDomainStatisticsRequest,
    ) -> main_models.DescribeDohSubDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_summary_with_options(
        self,
        request: main_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohSubDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohSubDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohSubDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_sub_domain_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohSubDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohSubDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohSubDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics_summary(
        self,
        request: main_models.DescribeDohSubDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDohSubDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_summary_async(
        self,
        request: main_models.DescribeDohSubDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDohSubDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_user_info_with_options(
        self,
        request: main_models.DescribeDohUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohUserInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_user_info_with_options_async(
        self,
        request: main_models.DescribeDohUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDohUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDohUserInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDohUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_user_info(
        self,
        request: main_models.DescribeDohUserInfoRequest,
    ) -> main_models.DescribeDohUserInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_doh_user_info_with_options(request, runtime)

    async def describe_doh_user_info_async(
        self,
        request: main_models.DescribeDohUserInfoRequest,
    ) -> main_models.DescribeDohUserInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_doh_user_info_with_options_async(request, runtime)

    def describe_domain_dnssec_info_with_options(
        self,
        request: main_models.DescribeDomainDnssecInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDnssecInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDnssecInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDnssecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_dnssec_info_with_options_async(
        self,
        request: main_models.DescribeDomainDnssecInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDnssecInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDnssecInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDnssecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_dnssec_info(
        self,
        request: main_models.DescribeDomainDnssecInfoRequest,
    ) -> main_models.DescribeDomainDnssecInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_dnssec_info_with_options(request, runtime)

    async def describe_domain_dnssec_info_async(
        self,
        request: main_models.DescribeDomainDnssecInfoRequest,
    ) -> main_models.DescribeDomainDnssecInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_dnssec_info_with_options_async(request, runtime)

    def describe_domain_groups_with_options(
        self,
        request: main_models.DescribeDomainGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainGroups',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_groups_with_options_async(
        self,
        request: main_models.DescribeDomainGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainGroups',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_groups(
        self,
        request: main_models.DescribeDomainGroupsRequest,
    ) -> main_models.DescribeDomainGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_groups_with_options(request, runtime)

    async def describe_domain_groups_async(
        self,
        request: main_models.DescribeDomainGroupsRequest,
    ) -> main_models.DescribeDomainGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_groups_with_options_async(request, runtime)

    def describe_domain_info_with_options(
        self,
        request: main_models.DescribeDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_info_with_options_async(
        self,
        request: main_models.DescribeDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_info(
        self,
        request: main_models.DescribeDomainInfoRequest,
    ) -> main_models.DescribeDomainInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_info_with_options(request, runtime)

    async def describe_domain_info_async(
        self,
        request: main_models.DescribeDomainInfoRequest,
    ) -> main_models.DescribeDomainInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_info_with_options_async(request, runtime)

    def describe_domain_logs_with_options(
        self,
        request: main_models.DescribeDomainLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_logs_with_options_async(
        self,
        request: main_models.DescribeDomainLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_logs(
        self,
        request: main_models.DescribeDomainLogsRequest,
    ) -> main_models.DescribeDomainLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_logs_with_options(request, runtime)

    async def describe_domain_logs_async(
        self,
        request: main_models.DescribeDomainLogsRequest,
    ) -> main_models.DescribeDomainLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_logs_with_options_async(request, runtime)

    def describe_domain_ns_with_options(
        self,
        request: main_models.DescribeDomainNsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainNsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainNs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainNsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_ns_with_options_async(
        self,
        request: main_models.DescribeDomainNsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainNsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainNs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainNsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_ns(
        self,
        request: main_models.DescribeDomainNsRequest,
    ) -> main_models.DescribeDomainNsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_ns_with_options(request, runtime)

    async def describe_domain_ns_async(
        self,
        request: main_models.DescribeDomainNsRequest,
    ) -> main_models.DescribeDomainNsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_ns_with_options_async(request, runtime)

    def describe_domain_record_info_with_options(
        self,
        request: main_models.DescribeDomainRecordInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRecordInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRecordInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRecordInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_record_info_with_options_async(
        self,
        request: main_models.DescribeDomainRecordInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRecordInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRecordInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRecordInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_record_info(
        self,
        request: main_models.DescribeDomainRecordInfoRequest,
    ) -> main_models.DescribeDomainRecordInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_record_info_with_options(request, runtime)

    async def describe_domain_record_info_async(
        self,
        request: main_models.DescribeDomainRecordInfoRequest,
    ) -> main_models.DescribeDomainRecordInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_record_info_with_options_async(request, runtime)

    def describe_domain_records_with_options(
        self,
        request: main_models.DescribeDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rrkey_word):
            query['RRKeyWord'] = request.rrkey_word
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.type_key_word):
            query['TypeKeyWord'] = request.type_key_word
        if not DaraCore.is_null(request.value_key_word):
            query['ValueKeyWord'] = request.value_key_word
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_records_with_options_async(
        self,
        request: main_models.DescribeDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rrkey_word):
            query['RRKeyWord'] = request.rrkey_word
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.type_key_word):
            query['TypeKeyWord'] = request.type_key_word
        if not DaraCore.is_null(request.value_key_word):
            query['ValueKeyWord'] = request.value_key_word
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_records(
        self,
        request: main_models.DescribeDomainRecordsRequest,
    ) -> main_models.DescribeDomainRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_records_with_options(request, runtime)

    async def describe_domain_records_async(
        self,
        request: main_models.DescribeDomainRecordsRequest,
    ) -> main_models.DescribeDomainRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_records_with_options_async(request, runtime)

    def describe_domain_resolve_statistics_summary_with_options(
        self,
        request: main_models.DescribeDomainResolveStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResolveStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResolveStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolve_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeDomainResolveStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResolveStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResolveStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResolveStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resolve_statistics_summary(
        self,
        request: main_models.DescribeDomainResolveStatisticsSummaryRequest,
    ) -> main_models.DescribeDomainResolveStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_resolve_statistics_summary_with_options(request, runtime)

    async def describe_domain_resolve_statistics_summary_async(
        self,
        request: main_models.DescribeDomainResolveStatisticsSummaryRequest,
    ) -> main_models.DescribeDomainResolveStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_resolve_statistics_summary_with_options_async(request, runtime)

    def describe_domain_statistics_with_options(
        self,
        request: main_models.DescribeDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_statistics_with_options_async(
        self,
        request: main_models.DescribeDomainStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_statistics(
        self,
        request: main_models.DescribeDomainStatisticsRequest,
    ) -> main_models.DescribeDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_statistics_with_options(request, runtime)

    async def describe_domain_statistics_async(
        self,
        request: main_models.DescribeDomainStatisticsRequest,
    ) -> main_models.DescribeDomainStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_statistics_with_options_async(request, runtime)

    def describe_domain_statistics_summary_with_options(
        self,
        request: main_models.DescribeDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeDomainStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_statistics_summary(
        self,
        request: main_models.DescribeDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_statistics_summary_with_options(request, runtime)

    async def describe_domain_statistics_summary_async(
        self,
        request: main_models.DescribeDomainStatisticsSummaryRequest,
    ) -> main_models.DescribeDomainStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_statistics_summary_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.starmark):
            query['Starmark'] = request.starmark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2015-01-09',
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
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.starmark):
            query['Starmark'] = request.starmark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2015-01-09',
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

    def describe_gtm_access_strategies_with_options(
        self,
        request: main_models.DescribeGtmAccessStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategies',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategies_with_options_async(
        self,
        request: main_models.DescribeGtmAccessStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategies',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategies(
        self,
        request: main_models.DescribeGtmAccessStrategiesRequest,
    ) -> main_models.DescribeGtmAccessStrategiesResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_access_strategies_with_options(request, runtime)

    async def describe_gtm_access_strategies_async(
        self,
        request: main_models.DescribeGtmAccessStrategiesRequest,
    ) -> main_models.DescribeGtmAccessStrategiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_access_strategies_with_options_async(request, runtime)

    def describe_gtm_access_strategy_with_options(
        self,
        request: main_models.DescribeGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategy_with_options_async(
        self,
        request: main_models.DescribeGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategy(
        self,
        request: main_models.DescribeGtmAccessStrategyRequest,
    ) -> main_models.DescribeGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_access_strategy_with_options(request, runtime)

    async def describe_gtm_access_strategy_async(
        self,
        request: main_models.DescribeGtmAccessStrategyRequest,
    ) -> main_models.DescribeGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_access_strategy_with_options_async(request, runtime)

    def describe_gtm_access_strategy_available_config_with_options(
        self,
        request: main_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategyAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategy_available_config_with_options_async(
        self,
        request: main_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAccessStrategyAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAccessStrategyAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategy_available_config(
        self,
        request: main_models.DescribeGtmAccessStrategyAvailableConfigRequest,
    ) -> main_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_gtm_access_strategy_available_config_async(
        self,
        request: main_models.DescribeGtmAccessStrategyAvailableConfigRequest,
    ) -> main_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_gtm_available_alert_group_with_options(
        self,
        request: main_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAvailableAlertGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAvailableAlertGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_available_alert_group_with_options_async(
        self,
        request: main_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmAvailableAlertGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmAvailableAlertGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmAvailableAlertGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_available_alert_group(
        self,
        request: main_models.DescribeGtmAvailableAlertGroupRequest,
    ) -> main_models.DescribeGtmAvailableAlertGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_available_alert_group_with_options(request, runtime)

    async def describe_gtm_available_alert_group_async(
        self,
        request: main_models.DescribeGtmAvailableAlertGroupRequest,
    ) -> main_models.DescribeGtmAvailableAlertGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_gtm_instance_with_options(
        self,
        request: main_models.DescribeGtmInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_with_options_async(
        self,
        request: main_models.DescribeGtmInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstance',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance(
        self,
        request: main_models.DescribeGtmInstanceRequest,
    ) -> main_models.DescribeGtmInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instance_with_options(request, runtime)

    async def describe_gtm_instance_async(
        self,
        request: main_models.DescribeGtmInstanceRequest,
    ) -> main_models.DescribeGtmInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instance_with_options_async(request, runtime)

    def describe_gtm_instance_address_pool_with_options(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_address_pool_with_options_async(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_address_pool(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolRequest,
    ) -> main_models.DescribeGtmInstanceAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_gtm_instance_address_pool_async(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolRequest,
    ) -> main_models.DescribeGtmInstanceAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_gtm_instance_address_pools_with_options(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_address_pools_with_options_async(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_address_pools(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolsRequest,
    ) -> main_models.DescribeGtmInstanceAddressPoolsResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_gtm_instance_address_pools_async(
        self,
        request: main_models.DescribeGtmInstanceAddressPoolsRequest,
    ) -> main_models.DescribeGtmInstanceAddressPoolsResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_gtm_instance_status_with_options(
        self,
        request: main_models.DescribeGtmInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_status_with_options_async(
        self,
        request: main_models.DescribeGtmInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_status(
        self,
        request: main_models.DescribeGtmInstanceStatusRequest,
    ) -> main_models.DescribeGtmInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instance_status_with_options(request, runtime)

    async def describe_gtm_instance_status_async(
        self,
        request: main_models.DescribeGtmInstanceStatusRequest,
    ) -> main_models.DescribeGtmInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instance_status_with_options_async(request, runtime)

    def describe_gtm_instance_system_cname_with_options(
        self,
        request: main_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceSystemCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceSystemCname',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_system_cname_with_options_async(
        self,
        request: main_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstanceSystemCnameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstanceSystemCname',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstanceSystemCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_system_cname(
        self,
        request: main_models.DescribeGtmInstanceSystemCnameRequest,
    ) -> main_models.DescribeGtmInstanceSystemCnameResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_gtm_instance_system_cname_async(
        self,
        request: main_models.DescribeGtmInstanceSystemCnameRequest,
    ) -> main_models.DescribeGtmInstanceSystemCnameResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_gtm_instances_with_options(
        self,
        request: main_models.DescribeGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instances_with_options_async(
        self,
        request: main_models.DescribeGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instances(
        self,
        request: main_models.DescribeGtmInstancesRequest,
    ) -> main_models.DescribeGtmInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_instances_with_options(request, runtime)

    async def describe_gtm_instances_async(
        self,
        request: main_models.DescribeGtmInstancesRequest,
    ) -> main_models.DescribeGtmInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_instances_with_options_async(request, runtime)

    def describe_gtm_logs_with_options(
        self,
        request: main_models.DescribeGtmLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_logs_with_options_async(
        self,
        request: main_models.DescribeGtmLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_logs(
        self,
        request: main_models.DescribeGtmLogsRequest,
    ) -> main_models.DescribeGtmLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_logs_with_options(request, runtime)

    async def describe_gtm_logs_async(
        self,
        request: main_models.DescribeGtmLogsRequest,
    ) -> main_models.DescribeGtmLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_logs_with_options_async(request, runtime)

    def describe_gtm_monitor_available_config_with_options(
        self,
        request: main_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmMonitorAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmMonitorAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_monitor_available_config_with_options_async(
        self,
        request: main_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmMonitorAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmMonitorAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmMonitorAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_monitor_available_config(
        self,
        request: main_models.DescribeGtmMonitorAvailableConfigRequest,
    ) -> main_models.DescribeGtmMonitorAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_gtm_monitor_available_config_async(
        self,
        request: main_models.DescribeGtmMonitorAvailableConfigRequest,
    ) -> main_models.DescribeGtmMonitorAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_gtm_monitor_config_with_options(
        self,
        request: main_models.DescribeGtmMonitorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmMonitorConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_monitor_config_with_options_async(
        self,
        request: main_models.DescribeGtmMonitorConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmMonitorConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_monitor_config(
        self,
        request: main_models.DescribeGtmMonitorConfigRequest,
    ) -> main_models.DescribeGtmMonitorConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_monitor_config_with_options(request, runtime)

    async def describe_gtm_monitor_config_async(
        self,
        request: main_models.DescribeGtmMonitorConfigRequest,
    ) -> main_models.DescribeGtmMonitorConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_monitor_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_with_options(
        self,
        request: main_models.DescribeGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.DescribeGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plan(
        self,
        request: main_models.DescribeGtmRecoveryPlanRequest,
    ) -> main_models.DescribeGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_recovery_plan_with_options(request, runtime)

    async def describe_gtm_recovery_plan_async(
        self,
        request: main_models.DescribeGtmRecoveryPlanRequest,
    ) -> main_models.DescribeGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_recovery_plan_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_available_config_with_options(
        self,
        request: main_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlanAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlanAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plan_available_config_with_options_async(
        self,
        request: main_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlanAvailableConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlanAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plan_available_config(
        self,
        request: main_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
    ) -> main_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_recovery_plan_available_config_with_options(request, runtime)

    async def describe_gtm_recovery_plan_available_config_async(
        self,
        request: main_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
    ) -> main_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_recovery_plan_available_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plans_with_options(
        self,
        request: main_models.DescribeGtmRecoveryPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlans',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plans_with_options_async(
        self,
        request: main_models.DescribeGtmRecoveryPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGtmRecoveryPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGtmRecoveryPlans',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGtmRecoveryPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plans(
        self,
        request: main_models.DescribeGtmRecoveryPlansRequest,
    ) -> main_models.DescribeGtmRecoveryPlansResponse:
        runtime = RuntimeOptions()
        return self.describe_gtm_recovery_plans_with_options(request, runtime)

    async def describe_gtm_recovery_plans_async(
        self,
        request: main_models.DescribeGtmRecoveryPlansRequest,
    ) -> main_models.DescribeGtmRecoveryPlansResponse:
        runtime = RuntimeOptions()
        return await self.describe_gtm_recovery_plans_with_options_async(request, runtime)

    def describe_instance_domains_with_options(
        self,
        request: main_models.DescribeInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_domains_with_options_async(
        self,
        request: main_models.DescribeInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_domains(
        self,
        request: main_models.DescribeInstanceDomainsRequest,
    ) -> main_models.DescribeInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_domains_with_options(request, runtime)

    async def describe_instance_domains_async(
        self,
        request: main_models.DescribeInstanceDomainsRequest,
    ) -> main_models.DescribeInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_domains_with_options_async(request, runtime)

    def describe_internet_dns_logs_with_options(
        self,
        request: main_models.DescribeInternetDnsLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetDnsLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.recursion_protocol_type):
            query['RecursionProtocolType'] = request.recursion_protocol_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetDnsLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetDnsLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_dns_logs_with_options_async(
        self,
        request: main_models.DescribeInternetDnsLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetDnsLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.recursion_protocol_type):
            query['RecursionProtocolType'] = request.recursion_protocol_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetDnsLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetDnsLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_dns_logs(
        self,
        request: main_models.DescribeInternetDnsLogsRequest,
    ) -> main_models.DescribeInternetDnsLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_dns_logs_with_options(request, runtime)

    async def describe_internet_dns_logs_async(
        self,
        request: main_models.DescribeInternetDnsLogsRequest,
    ) -> main_models.DescribeInternetDnsLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_dns_logs_with_options_async(request, runtime)

    def describe_isp_flush_cache_instances_with_options(
        self,
        request: main_models.DescribeIspFlushCacheInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_instances_with_options_async(
        self,
        request: main_models.DescribeIspFlushCacheInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_instances(
        self,
        request: main_models.DescribeIspFlushCacheInstancesRequest,
    ) -> main_models.DescribeIspFlushCacheInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_isp_flush_cache_instances_with_options(request, runtime)

    async def describe_isp_flush_cache_instances_async(
        self,
        request: main_models.DescribeIspFlushCacheInstancesRequest,
    ) -> main_models.DescribeIspFlushCacheInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_isp_flush_cache_instances_with_options_async(request, runtime)

    def describe_isp_flush_cache_remain_quota_with_options(
        self,
        request: main_models.DescribeIspFlushCacheRemainQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheRemainQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheRemainQuota',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheRemainQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_remain_quota_with_options_async(
        self,
        request: main_models.DescribeIspFlushCacheRemainQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheRemainQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheRemainQuota',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheRemainQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_remain_quota(
        self,
        request: main_models.DescribeIspFlushCacheRemainQuotaRequest,
    ) -> main_models.DescribeIspFlushCacheRemainQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_isp_flush_cache_remain_quota_with_options(request, runtime)

    async def describe_isp_flush_cache_remain_quota_async(
        self,
        request: main_models.DescribeIspFlushCacheRemainQuotaRequest,
    ) -> main_models.DescribeIspFlushCacheRemainQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_isp_flush_cache_remain_quota_with_options_async(request, runtime)

    def describe_isp_flush_cache_task_with_options(
        self,
        request: main_models.DescribeIspFlushCacheTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheTask',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_task_with_options_async(
        self,
        request: main_models.DescribeIspFlushCacheTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheTask',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_task(
        self,
        request: main_models.DescribeIspFlushCacheTaskRequest,
    ) -> main_models.DescribeIspFlushCacheTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_isp_flush_cache_task_with_options(request, runtime)

    async def describe_isp_flush_cache_task_async(
        self,
        request: main_models.DescribeIspFlushCacheTaskRequest,
    ) -> main_models.DescribeIspFlushCacheTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_isp_flush_cache_task_with_options_async(request, runtime)

    def describe_isp_flush_cache_tasks_with_options(
        self,
        request: main_models.DescribeIspFlushCacheTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheTasks',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_tasks_with_options_async(
        self,
        request: main_models.DescribeIspFlushCacheTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspFlushCacheTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspFlushCacheTasks',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspFlushCacheTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_tasks(
        self,
        request: main_models.DescribeIspFlushCacheTasksRequest,
    ) -> main_models.DescribeIspFlushCacheTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_isp_flush_cache_tasks_with_options(request, runtime)

    async def describe_isp_flush_cache_tasks_async(
        self,
        request: main_models.DescribeIspFlushCacheTasksRequest,
    ) -> main_models.DescribeIspFlushCacheTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_isp_flush_cache_tasks_with_options_async(request, runtime)

    def describe_pdns_account_summary_with_options(
        self,
        request: main_models.DescribePdnsAccountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAccountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAccountSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_account_summary_with_options_async(
        self,
        request: main_models.DescribePdnsAccountSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAccountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAccountSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_account_summary(
        self,
        request: main_models.DescribePdnsAccountSummaryRequest,
    ) -> main_models.DescribePdnsAccountSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_account_summary_with_options(request, runtime)

    async def describe_pdns_account_summary_async(
        self,
        request: main_models.DescribePdnsAccountSummaryRequest,
    ) -> main_models.DescribePdnsAccountSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_account_summary_with_options_async(request, runtime)

    def describe_pdns_app_key_with_options(
        self,
        request: main_models.DescribePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_app_key_with_options_async(
        self,
        request: main_models.DescribePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_app_key(
        self,
        request: main_models.DescribePdnsAppKeyRequest,
    ) -> main_models.DescribePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_app_key_with_options(request, runtime)

    async def describe_pdns_app_key_async(
        self,
        request: main_models.DescribePdnsAppKeyRequest,
    ) -> main_models.DescribePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_app_key_with_options_async(request, runtime)

    def describe_pdns_app_keys_with_options(
        self,
        request: main_models.DescribePdnsAppKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAppKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAppKeys',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAppKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_app_keys_with_options_async(
        self,
        request: main_models.DescribePdnsAppKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsAppKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsAppKeys',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsAppKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_app_keys(
        self,
        request: main_models.DescribePdnsAppKeysRequest,
    ) -> main_models.DescribePdnsAppKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_app_keys_with_options(request, runtime)

    async def describe_pdns_app_keys_async(
        self,
        request: main_models.DescribePdnsAppKeysRequest,
    ) -> main_models.DescribePdnsAppKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_app_keys_with_options_async(request, runtime)

    def describe_pdns_operate_logs_with_options(
        self,
        request: main_models.DescribePdnsOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsOperateLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_operate_logs_with_options_async(
        self,
        request: main_models.DescribePdnsOperateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsOperateLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsOperateLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_operate_logs(
        self,
        request: main_models.DescribePdnsOperateLogsRequest,
    ) -> main_models.DescribePdnsOperateLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_operate_logs_with_options(request, runtime)

    async def describe_pdns_operate_logs_async(
        self,
        request: main_models.DescribePdnsOperateLogsRequest,
    ) -> main_models.DescribePdnsOperateLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_operate_logs_with_options_async(request, runtime)

    def describe_pdns_request_statistic_with_options(
        self,
        request: main_models.DescribePdnsRequestStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsRequestStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsRequestStatistic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsRequestStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_request_statistic_with_options_async(
        self,
        request: main_models.DescribePdnsRequestStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsRequestStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsRequestStatistic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsRequestStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_request_statistic(
        self,
        request: main_models.DescribePdnsRequestStatisticRequest,
    ) -> main_models.DescribePdnsRequestStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_request_statistic_with_options(request, runtime)

    async def describe_pdns_request_statistic_async(
        self,
        request: main_models.DescribePdnsRequestStatisticRequest,
    ) -> main_models.DescribePdnsRequestStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_request_statistic_with_options_async(request, runtime)

    def describe_pdns_request_statistics_with_options(
        self,
        request: main_models.DescribePdnsRequestStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsRequestStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsRequestStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsRequestStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_request_statistics_with_options_async(
        self,
        request: main_models.DescribePdnsRequestStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsRequestStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsRequestStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsRequestStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_request_statistics(
        self,
        request: main_models.DescribePdnsRequestStatisticsRequest,
    ) -> main_models.DescribePdnsRequestStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_request_statistics_with_options(request, runtime)

    async def describe_pdns_request_statistics_async(
        self,
        request: main_models.DescribePdnsRequestStatisticsRequest,
    ) -> main_models.DescribePdnsRequestStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_request_statistics_with_options_async(request, runtime)

    def describe_pdns_threat_logs_with_options(
        self,
        request: main_models.DescribePdnsThreatLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not DaraCore.is_null(request.threat_type):
            query['ThreatType'] = request.threat_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_logs_with_options_async(
        self,
        request: main_models.DescribePdnsThreatLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not DaraCore.is_null(request.threat_type):
            query['ThreatType'] = request.threat_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_logs(
        self,
        request: main_models.DescribePdnsThreatLogsRequest,
    ) -> main_models.DescribePdnsThreatLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_threat_logs_with_options(request, runtime)

    async def describe_pdns_threat_logs_async(
        self,
        request: main_models.DescribePdnsThreatLogsRequest,
    ) -> main_models.DescribePdnsThreatLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_threat_logs_with_options_async(request, runtime)

    def describe_pdns_threat_statistic_with_options(
        self,
        request: main_models.DescribePdnsThreatStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatStatistic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_statistic_with_options_async(
        self,
        request: main_models.DescribePdnsThreatStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatStatistic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_statistic(
        self,
        request: main_models.DescribePdnsThreatStatisticRequest,
    ) -> main_models.DescribePdnsThreatStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_threat_statistic_with_options(request, runtime)

    async def describe_pdns_threat_statistic_async(
        self,
        request: main_models.DescribePdnsThreatStatisticRequest,
    ) -> main_models.DescribePdnsThreatStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_threat_statistic_with_options_async(request, runtime)

    def describe_pdns_threat_statistics_with_options(
        self,
        request: main_models.DescribePdnsThreatStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not DaraCore.is_null(request.threat_type):
            query['ThreatType'] = request.threat_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_statistics_with_options_async(
        self,
        request: main_models.DescribePdnsThreatStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsThreatStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not DaraCore.is_null(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not DaraCore.is_null(request.threat_type):
            query['ThreatType'] = request.threat_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsThreatStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsThreatStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_statistics(
        self,
        request: main_models.DescribePdnsThreatStatisticsRequest,
    ) -> main_models.DescribePdnsThreatStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_threat_statistics_with_options(request, runtime)

    async def describe_pdns_threat_statistics_async(
        self,
        request: main_models.DescribePdnsThreatStatisticsRequest,
    ) -> main_models.DescribePdnsThreatStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_threat_statistics_with_options_async(request, runtime)

    def describe_pdns_udp_ip_segments_with_options(
        self,
        request: main_models.DescribePdnsUdpIpSegmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsUdpIpSegmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsUdpIpSegments',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsUdpIpSegmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_udp_ip_segments_with_options_async(
        self,
        request: main_models.DescribePdnsUdpIpSegmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsUdpIpSegmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsUdpIpSegments',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsUdpIpSegmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_udp_ip_segments(
        self,
        request: main_models.DescribePdnsUdpIpSegmentsRequest,
    ) -> main_models.DescribePdnsUdpIpSegmentsResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_udp_ip_segments_with_options(request, runtime)

    async def describe_pdns_udp_ip_segments_async(
        self,
        request: main_models.DescribePdnsUdpIpSegmentsRequest,
    ) -> main_models.DescribePdnsUdpIpSegmentsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_udp_ip_segments_with_options_async(request, runtime)

    def describe_pdns_user_info_with_options(
        self,
        request: main_models.DescribePdnsUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsUserInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_user_info_with_options_async(
        self,
        request: main_models.DescribePdnsUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePdnsUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePdnsUserInfo',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePdnsUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_user_info(
        self,
        request: main_models.DescribePdnsUserInfoRequest,
    ) -> main_models.DescribePdnsUserInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_pdns_user_info_with_options(request, runtime)

    async def describe_pdns_user_info_async(
        self,
        request: main_models.DescribePdnsUserInfoRequest,
    ) -> main_models.DescribePdnsUserInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_pdns_user_info_with_options_async(request, runtime)

    def describe_record_logs_with_options(
        self,
        request: main_models.DescribeRecordLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_logs_with_options_async(
        self,
        request: main_models.DescribeRecordLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_logs(
        self,
        request: main_models.DescribeRecordLogsRequest,
    ) -> main_models.DescribeRecordLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_record_logs_with_options(request, runtime)

    async def describe_record_logs_async(
        self,
        request: main_models.DescribeRecordLogsRequest,
    ) -> main_models.DescribeRecordLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_logs_with_options_async(request, runtime)

    def describe_record_resolve_statistics_summary_with_options(
        self,
        request: main_models.DescribeRecordResolveStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordResolveStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordResolveStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_resolve_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeRecordResolveStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordResolveStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordResolveStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordResolveStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_resolve_statistics_summary(
        self,
        request: main_models.DescribeRecordResolveStatisticsSummaryRequest,
    ) -> main_models.DescribeRecordResolveStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_record_resolve_statistics_summary_with_options(request, runtime)

    async def describe_record_resolve_statistics_summary_async(
        self,
        request: main_models.DescribeRecordResolveStatisticsSummaryRequest,
    ) -> main_models.DescribeRecordResolveStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_resolve_statistics_summary_with_options_async(request, runtime)

    def describe_record_statistics_with_options(
        self,
        request: main_models.DescribeRecordStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_statistics_with_options_async(
        self,
        request: main_models.DescribeRecordStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordStatistics',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_statistics(
        self,
        request: main_models.DescribeRecordStatisticsRequest,
    ) -> main_models.DescribeRecordStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_record_statistics_with_options(request, runtime)

    async def describe_record_statistics_async(
        self,
        request: main_models.DescribeRecordStatisticsRequest,
    ) -> main_models.DescribeRecordStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_statistics_with_options_async(request, runtime)

    def describe_record_statistics_summary_with_options(
        self,
        request: main_models.DescribeRecordStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_statistics_summary_with_options_async(
        self,
        request: main_models.DescribeRecordStatisticsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordStatisticsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecordStatisticsSummary',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_statistics_summary(
        self,
        request: main_models.DescribeRecordStatisticsSummaryRequest,
    ) -> main_models.DescribeRecordStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_record_statistics_summary_with_options(request, runtime)

    async def describe_record_statistics_summary_async(
        self,
        request: main_models.DescribeRecordStatisticsSummaryRequest,
    ) -> main_models.DescribeRecordStatisticsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_record_statistics_summary_with_options_async(request, runtime)

    def describe_recursion_record_with_options(
        self,
        request: main_models.DescribeRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecursionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recursion_record_with_options_async(
        self,
        request: main_models.DescribeRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecursionRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recursion_record(
        self,
        request: main_models.DescribeRecursionRecordRequest,
    ) -> main_models.DescribeRecursionRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_recursion_record_with_options(request, runtime)

    async def describe_recursion_record_async(
        self,
        request: main_models.DescribeRecursionRecordRequest,
    ) -> main_models.DescribeRecursionRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_recursion_record_with_options_async(request, runtime)

    def describe_recursion_zone_with_options(
        self,
        request: main_models.DescribeRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecursionZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recursion_zone_with_options_async(
        self,
        request: main_models.DescribeRecursionZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecursionZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecursionZone',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecursionZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recursion_zone(
        self,
        request: main_models.DescribeRecursionZoneRequest,
    ) -> main_models.DescribeRecursionZoneResponse:
        runtime = RuntimeOptions()
        return self.describe_recursion_zone_with_options(request, runtime)

    async def describe_recursion_zone_async(
        self,
        request: main_models.DescribeRecursionZoneRequest,
    ) -> main_models.DescribeRecursionZoneResponse:
        runtime = RuntimeOptions()
        return await self.describe_recursion_zone_with_options_async(request, runtime)

    def describe_sub_domain_records_with_options(
        self,
        request: main_models.DescribeSubDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sub_domain_records_with_options_async(
        self,
        request: main_models.DescribeSubDomainRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubDomainRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubDomainRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sub_domain_records(
        self,
        request: main_models.DescribeSubDomainRecordsRequest,
    ) -> main_models.DescribeSubDomainRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_sub_domain_records_with_options(request, runtime)

    async def describe_sub_domain_records_async(
        self,
        request: main_models.DescribeSubDomainRecordsRequest,
    ) -> main_models.DescribeSubDomainRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sub_domain_records_with_options_async(request, runtime)

    def describe_support_lines_with_options(
        self,
        request: main_models.DescribeSupportLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_lines_with_options_async(
        self,
        request: main_models.DescribeSupportLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportLines',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_lines(
        self,
        request: main_models.DescribeSupportLinesRequest,
    ) -> main_models.DescribeSupportLinesResponse:
        runtime = RuntimeOptions()
        return self.describe_support_lines_with_options(request, runtime)

    async def describe_support_lines_async(
        self,
        request: main_models.DescribeSupportLinesRequest,
    ) -> main_models.DescribeSupportLinesResponse:
        runtime = RuntimeOptions()
        return await self.describe_support_lines_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_transfer_domains_with_options(
        self,
        request: main_models.DescribeTransferDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransferDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.from_user_id):
            query['FromUserId'] = request.from_user_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransferDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransferDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_domains_with_options_async(
        self,
        request: main_models.DescribeTransferDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransferDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.from_user_id):
            query['FromUserId'] = request.from_user_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransferDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransferDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_domains(
        self,
        request: main_models.DescribeTransferDomainsRequest,
    ) -> main_models.DescribeTransferDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_transfer_domains_with_options(request, runtime)

    async def describe_transfer_domains_async(
        self,
        request: main_models.DescribeTransferDomainsRequest,
    ) -> main_models.DescribeTransferDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_transfer_domains_with_options_async(request, runtime)

    def execute_gtm_recovery_plan_with_options(
        self,
        request: main_models.ExecuteGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.ExecuteGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_gtm_recovery_plan(
        self,
        request: main_models.ExecuteGtmRecoveryPlanRequest,
    ) -> main_models.ExecuteGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.execute_gtm_recovery_plan_with_options(request, runtime)

    async def execute_gtm_recovery_plan_async(
        self,
        request: main_models.ExecuteGtmRecoveryPlanRequest,
    ) -> main_models.ExecuteGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.execute_gtm_recovery_plan_with_options_async(request, runtime)

    def get_main_domain_name_with_options(
        self,
        request: main_models.GetMainDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMainDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_string):
            query['InputString'] = request.input_string
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMainDomainName',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMainDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_main_domain_name_with_options_async(
        self,
        request: main_models.GetMainDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMainDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_string):
            query['InputString'] = request.input_string
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMainDomainName',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMainDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_main_domain_name(
        self,
        request: main_models.GetMainDomainNameRequest,
    ) -> main_models.GetMainDomainNameResponse:
        runtime = RuntimeOptions()
        return self.get_main_domain_name_with_options(request, runtime)

    async def get_main_domain_name_async(
        self,
        request: main_models.GetMainDomainNameRequest,
    ) -> main_models.GetMainDomainNameResponse:
        runtime = RuntimeOptions()
        return await self.get_main_domain_name_with_options_async(request, runtime)

    def get_txt_record_for_verify_with_options(
        self,
        request: main_models.GetTxtRecordForVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTxtRecordForVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTxtRecordForVerify',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTxtRecordForVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_txt_record_for_verify_with_options_async(
        self,
        request: main_models.GetTxtRecordForVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTxtRecordForVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTxtRecordForVerify',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTxtRecordForVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_txt_record_for_verify(
        self,
        request: main_models.GetTxtRecordForVerifyRequest,
    ) -> main_models.GetTxtRecordForVerifyResponse:
        runtime = RuntimeOptions()
        return self.get_txt_record_for_verify_with_options(request, runtime)

    async def get_txt_record_for_verify_async(
        self,
        request: main_models.GetTxtRecordForVerifyRequest,
    ) -> main_models.GetTxtRecordForVerifyResponse:
        runtime = RuntimeOptions()
        return await self.get_txt_record_for_verify_with_options_async(request, runtime)

    def list_cloud_gtm_address_pools_with_options(
        self,
        request: main_models.ListCloudGtmAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_address_pools_with_options_async(
        self,
        request: main_models.ListCloudGtmAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_address_pools(
        self,
        request: main_models.ListCloudGtmAddressPoolsRequest,
    ) -> main_models.ListCloudGtmAddressPoolsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_address_pools_with_options(request, runtime)

    async def list_cloud_gtm_address_pools_async(
        self,
        request: main_models.ListCloudGtmAddressPoolsRequest,
    ) -> main_models.ListCloudGtmAddressPoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_address_pools_with_options_async(request, runtime)

    def list_cloud_gtm_addresses_with_options(
        self,
        request: main_models.ListCloudGtmAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.monitor_template_id):
            query['MonitorTemplateId'] = request.monitor_template_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAddresses',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_addresses_with_options_async(
        self,
        request: main_models.ListCloudGtmAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.monitor_template_id):
            query['MonitorTemplateId'] = request.monitor_template_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAddresses',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_addresses(
        self,
        request: main_models.ListCloudGtmAddressesRequest,
    ) -> main_models.ListCloudGtmAddressesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_addresses_with_options(request, runtime)

    async def list_cloud_gtm_addresses_async(
        self,
        request: main_models.ListCloudGtmAddressesRequest,
    ) -> main_models.ListCloudGtmAddressesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_addresses_with_options_async(request, runtime)

    def list_cloud_gtm_alert_logs_with_options(
        self,
        request: main_models.ListCloudGtmAlertLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAlertLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAlertLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAlertLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_alert_logs_with_options_async(
        self,
        request: main_models.ListCloudGtmAlertLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAlertLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAlertLogs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAlertLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_alert_logs(
        self,
        request: main_models.ListCloudGtmAlertLogsRequest,
    ) -> main_models.ListCloudGtmAlertLogsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_alert_logs_with_options(request, runtime)

    async def list_cloud_gtm_alert_logs_async(
        self,
        request: main_models.ListCloudGtmAlertLogsRequest,
    ) -> main_models.ListCloudGtmAlertLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_alert_logs_with_options_async(request, runtime)

    def list_cloud_gtm_available_alert_groups_with_options(
        self,
        request: main_models.ListCloudGtmAvailableAlertGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAvailableAlertGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAvailableAlertGroups',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAvailableAlertGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_available_alert_groups_with_options_async(
        self,
        request: main_models.ListCloudGtmAvailableAlertGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmAvailableAlertGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmAvailableAlertGroups',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmAvailableAlertGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_available_alert_groups(
        self,
        request: main_models.ListCloudGtmAvailableAlertGroupsRequest,
    ) -> main_models.ListCloudGtmAvailableAlertGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_available_alert_groups_with_options(request, runtime)

    async def list_cloud_gtm_available_alert_groups_async(
        self,
        request: main_models.ListCloudGtmAvailableAlertGroupsRequest,
    ) -> main_models.ListCloudGtmAvailableAlertGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_available_alert_groups_with_options_async(request, runtime)

    def list_cloud_gtm_instance_configs_with_options(
        self,
        request: main_models.ListCloudGtmInstanceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmInstanceConfigs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_instance_configs_with_options_async(
        self,
        request: main_models.ListCloudGtmInstanceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmInstanceConfigs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_instance_configs(
        self,
        request: main_models.ListCloudGtmInstanceConfigsRequest,
    ) -> main_models.ListCloudGtmInstanceConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_instance_configs_with_options(request, runtime)

    async def list_cloud_gtm_instance_configs_async(
        self,
        request: main_models.ListCloudGtmInstanceConfigsRequest,
    ) -> main_models.ListCloudGtmInstanceConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_instance_configs_with_options_async(request, runtime)

    def list_cloud_gtm_instances_with_options(
        self,
        request: main_models.ListCloudGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_instances_with_options_async(
        self,
        request: main_models.ListCloudGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_instances(
        self,
        request: main_models.ListCloudGtmInstancesRequest,
    ) -> main_models.ListCloudGtmInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_instances_with_options(request, runtime)

    async def list_cloud_gtm_instances_async(
        self,
        request: main_models.ListCloudGtmInstancesRequest,
    ) -> main_models.ListCloudGtmInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_instances_with_options_async(request, runtime)

    def list_cloud_gtm_monitor_nodes_with_options(
        self,
        request: main_models.ListCloudGtmMonitorNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmMonitorNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmMonitorNodes',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmMonitorNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_monitor_nodes_with_options_async(
        self,
        request: main_models.ListCloudGtmMonitorNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmMonitorNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmMonitorNodes',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmMonitorNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_monitor_nodes(
        self,
        request: main_models.ListCloudGtmMonitorNodesRequest,
    ) -> main_models.ListCloudGtmMonitorNodesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_monitor_nodes_with_options(request, runtime)

    async def list_cloud_gtm_monitor_nodes_async(
        self,
        request: main_models.ListCloudGtmMonitorNodesRequest,
    ) -> main_models.ListCloudGtmMonitorNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_monitor_nodes_with_options_async(request, runtime)

    def list_cloud_gtm_monitor_templates_with_options(
        self,
        request: main_models.ListCloudGtmMonitorTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmMonitorTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmMonitorTemplates',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmMonitorTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_monitor_templates_with_options_async(
        self,
        request: main_models.ListCloudGtmMonitorTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudGtmMonitorTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudGtmMonitorTemplates',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudGtmMonitorTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_monitor_templates(
        self,
        request: main_models.ListCloudGtmMonitorTemplatesRequest,
    ) -> main_models.ListCloudGtmMonitorTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_gtm_monitor_templates_with_options(request, runtime)

    async def list_cloud_gtm_monitor_templates_async(
        self,
        request: main_models.ListCloudGtmMonitorTemplatesRequest,
    ) -> main_models.ListCloudGtmMonitorTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_gtm_monitor_templates_with_options_async(request, runtime)

    def list_recursion_records_with_options(
        self,
        request: main_models.ListRecursionRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecursionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecursionRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecursionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recursion_records_with_options_async(
        self,
        request: main_models.ListRecursionRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecursionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecursionRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecursionRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recursion_records(
        self,
        request: main_models.ListRecursionRecordsRequest,
    ) -> main_models.ListRecursionRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_recursion_records_with_options(request, runtime)

    async def list_recursion_records_async(
        self,
        request: main_models.ListRecursionRecordsRequest,
    ) -> main_models.ListRecursionRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_recursion_records_with_options_async(request, runtime)

    def list_recursion_zones_with_options(
        self,
        request: main_models.ListRecursionZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecursionZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecursionZones',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecursionZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recursion_zones_with_options_async(
        self,
        request: main_models.ListRecursionZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecursionZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecursionZones',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecursionZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recursion_zones(
        self,
        request: main_models.ListRecursionZonesRequest,
    ) -> main_models.ListRecursionZonesResponse:
        runtime = RuntimeOptions()
        return self.list_recursion_zones_with_options(request, runtime)

    async def list_recursion_zones_async(
        self,
        request: main_models.ListRecursionZonesRequest,
    ) -> main_models.ListRecursionZonesResponse:
        runtime = RuntimeOptions()
        return await self.list_recursion_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_hichina_domain_dnswith_options(
        self,
        request: main_models.ModifyHichinaDomainDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHichinaDomainDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHichinaDomainDNS',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHichinaDomainDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hichina_domain_dnswith_options_async(
        self,
        request: main_models.ModifyHichinaDomainDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHichinaDomainDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHichinaDomainDNS',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHichinaDomainDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hichina_domain_dns(
        self,
        request: main_models.ModifyHichinaDomainDNSRequest,
    ) -> main_models.ModifyHichinaDomainDNSResponse:
        runtime = RuntimeOptions()
        return self.modify_hichina_domain_dnswith_options(request, runtime)

    async def modify_hichina_domain_dns_async(
        self,
        request: main_models.ModifyHichinaDomainDNSRequest,
    ) -> main_models.ModifyHichinaDomainDNSResponse:
        runtime = RuntimeOptions()
        return await self.modify_hichina_domain_dnswith_options_async(request, runtime)

    def move_domain_resource_group_with_options(
        self,
        request: main_models.MoveDomainResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveDomainResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveDomainResourceGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveDomainResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_domain_resource_group_with_options_async(
        self,
        request: main_models.MoveDomainResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveDomainResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveDomainResourceGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveDomainResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_domain_resource_group(
        self,
        request: main_models.MoveDomainResourceGroupRequest,
    ) -> main_models.MoveDomainResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_domain_resource_group_with_options(request, runtime)

    async def move_domain_resource_group_async(
        self,
        request: main_models.MoveDomainResourceGroupRequest,
    ) -> main_models.MoveDomainResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_domain_resource_group_with_options_async(request, runtime)

    def move_gtm_resource_group_with_options(
        self,
        request: main_models.MoveGtmResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveGtmResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveGtmResourceGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveGtmResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_gtm_resource_group_with_options_async(
        self,
        request: main_models.MoveGtmResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveGtmResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveGtmResourceGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveGtmResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_gtm_resource_group(
        self,
        request: main_models.MoveGtmResourceGroupRequest,
    ) -> main_models.MoveGtmResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_gtm_resource_group_with_options(request, runtime)

    async def move_gtm_resource_group_async(
        self,
        request: main_models.MoveGtmResourceGroupRequest,
    ) -> main_models.MoveGtmResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_gtm_resource_group_with_options_async(request, runtime)

    def operate_batch_domain_with_options(
        self,
        request: main_models.OperateBatchDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBatchDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_record_info):
            query['DomainRecordInfo'] = request.domain_record_info
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBatchDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBatchDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_batch_domain_with_options_async(
        self,
        request: main_models.OperateBatchDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBatchDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_record_info):
            query['DomainRecordInfo'] = request.domain_record_info
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBatchDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBatchDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_batch_domain(
        self,
        request: main_models.OperateBatchDomainRequest,
    ) -> main_models.OperateBatchDomainResponse:
        runtime = RuntimeOptions()
        return self.operate_batch_domain_with_options(request, runtime)

    async def operate_batch_domain_async(
        self,
        request: main_models.OperateBatchDomainRequest,
    ) -> main_models.OperateBatchDomainResponse:
        runtime = RuntimeOptions()
        return await self.operate_batch_domain_with_options_async(request, runtime)

    def pause_pdns_service_with_options(
        self,
        request: main_models.PausePdnsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PausePdnsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PausePdnsService',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PausePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_pdns_service_with_options_async(
        self,
        request: main_models.PausePdnsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PausePdnsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PausePdnsService',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PausePdnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_pdns_service(
        self,
        request: main_models.PausePdnsServiceRequest,
    ) -> main_models.PausePdnsServiceResponse:
        runtime = RuntimeOptions()
        return self.pause_pdns_service_with_options(request, runtime)

    async def pause_pdns_service_async(
        self,
        request: main_models.PausePdnsServiceRequest,
    ) -> main_models.PausePdnsServiceResponse:
        runtime = RuntimeOptions()
        return await self.pause_pdns_service_with_options_async(request, runtime)

    def preview_gtm_recovery_plan_with_options(
        self,
        request: main_models.PreviewGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.PreviewGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreviewGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_gtm_recovery_plan(
        self,
        request: main_models.PreviewGtmRecoveryPlanRequest,
    ) -> main_models.PreviewGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.preview_gtm_recovery_plan_with_options(request, runtime)

    async def preview_gtm_recovery_plan_async(
        self,
        request: main_models.PreviewGtmRecoveryPlanRequest,
    ) -> main_models.PreviewGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.preview_gtm_recovery_plan_with_options_async(request, runtime)

    def remove_pdns_app_key_with_options(
        self,
        request: main_models.RemovePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_pdns_app_key_with_options_async(
        self,
        request: main_models.RemovePdnsAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePdnsAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePdnsAppKey',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_pdns_app_key(
        self,
        request: main_models.RemovePdnsAppKeyRequest,
    ) -> main_models.RemovePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return self.remove_pdns_app_key_with_options(request, runtime)

    async def remove_pdns_app_key_async(
        self,
        request: main_models.RemovePdnsAppKeyRequest,
    ) -> main_models.RemovePdnsAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.remove_pdns_app_key_with_options_async(request, runtime)

    def remove_pdns_udp_ip_segment_with_options(
        self,
        request: main_models.RemovePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_pdns_udp_ip_segment_with_options_async(
        self,
        request: main_models.RemovePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_pdns_udp_ip_segment(
        self,
        request: main_models.RemovePdnsUdpIpSegmentRequest,
    ) -> main_models.RemovePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return self.remove_pdns_udp_ip_segment_with_options(request, runtime)

    async def remove_pdns_udp_ip_segment_async(
        self,
        request: main_models.RemovePdnsUdpIpSegmentRequest,
    ) -> main_models.RemovePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return await self.remove_pdns_udp_ip_segment_with_options_async(request, runtime)

    def remove_rsp_domain_server_hold_status_for_gateway_with_options(
        self,
        request: main_models.RemoveRspDomainServerHoldStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveRspDomainServerHoldStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.status_msg):
            query['StatusMsg'] = request.status_msg
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveRspDomainServerHoldStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveRspDomainServerHoldStatusForGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_rsp_domain_server_hold_status_for_gateway_with_options_async(
        self,
        request: main_models.RemoveRspDomainServerHoldStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveRspDomainServerHoldStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.status_msg):
            query['StatusMsg'] = request.status_msg
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveRspDomainServerHoldStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveRspDomainServerHoldStatusForGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_rsp_domain_server_hold_status_for_gateway(
        self,
        request: main_models.RemoveRspDomainServerHoldStatusForGatewayRequest,
    ) -> main_models.RemoveRspDomainServerHoldStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return self.remove_rsp_domain_server_hold_status_for_gateway_with_options(request, runtime)

    async def remove_rsp_domain_server_hold_status_for_gateway_async(
        self,
        request: main_models.RemoveRspDomainServerHoldStatusForGatewayRequest,
    ) -> main_models.RemoveRspDomainServerHoldStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return await self.remove_rsp_domain_server_hold_status_for_gateway_with_options_async(request, runtime)

    def replace_cloud_gtm_address_pool_address_with_options(
        self,
        tmp_req: main_models.ReplaceCloudGtmAddressPoolAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceCloudGtmAddressPoolAddressResponse:
        tmp_req.validate()
        request = main_models.ReplaceCloudGtmAddressPoolAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.addresses_shrink):
            query['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceCloudGtmAddressPoolAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceCloudGtmAddressPoolAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_cloud_gtm_address_pool_address_with_options_async(
        self,
        tmp_req: main_models.ReplaceCloudGtmAddressPoolAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceCloudGtmAddressPoolAddressResponse:
        tmp_req.validate()
        request = main_models.ReplaceCloudGtmAddressPoolAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addresses):
            request.addresses_shrink = Utils.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.addresses_shrink):
            query['Addresses'] = request.addresses_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceCloudGtmAddressPoolAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceCloudGtmAddressPoolAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_cloud_gtm_address_pool_address(
        self,
        request: main_models.ReplaceCloudGtmAddressPoolAddressRequest,
    ) -> main_models.ReplaceCloudGtmAddressPoolAddressResponse:
        runtime = RuntimeOptions()
        return self.replace_cloud_gtm_address_pool_address_with_options(request, runtime)

    async def replace_cloud_gtm_address_pool_address_async(
        self,
        request: main_models.ReplaceCloudGtmAddressPoolAddressRequest,
    ) -> main_models.ReplaceCloudGtmAddressPoolAddressResponse:
        runtime = RuntimeOptions()
        return await self.replace_cloud_gtm_address_pool_address_with_options_async(request, runtime)

    def replace_cloud_gtm_instance_config_address_pool_with_options(
        self,
        tmp_req: main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        tmp_req.validate()
        request = main_models.ReplaceCloudGtmInstanceConfigAddressPoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address_pools):
            request.address_pools_shrink = Utils.array_to_string_with_specified_style(tmp_req.address_pools, 'AddressPools', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pools_shrink):
            query['AddressPools'] = request.address_pools_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceCloudGtmInstanceConfigAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_cloud_gtm_instance_config_address_pool_with_options_async(
        self,
        tmp_req: main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        tmp_req.validate()
        request = main_models.ReplaceCloudGtmInstanceConfigAddressPoolShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address_pools):
            request.address_pools_shrink = Utils.array_to_string_with_specified_style(tmp_req.address_pools, 'AddressPools', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pools_shrink):
            query['AddressPools'] = request.address_pools_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceCloudGtmInstanceConfigAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_cloud_gtm_instance_config_address_pool(
        self,
        request: main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
    ) -> main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.replace_cloud_gtm_instance_config_address_pool_with_options(request, runtime)

    async def replace_cloud_gtm_instance_config_address_pool_async(
        self,
        request: main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
    ) -> main_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.replace_cloud_gtm_instance_config_address_pool_with_options_async(request, runtime)

    def resume_pdns_service_with_options(
        self,
        request: main_models.ResumePdnsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumePdnsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumePdnsService',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_pdns_service_with_options_async(
        self,
        request: main_models.ResumePdnsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumePdnsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumePdnsService',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumePdnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_pdns_service(
        self,
        request: main_models.ResumePdnsServiceRequest,
    ) -> main_models.ResumePdnsServiceResponse:
        runtime = RuntimeOptions()
        return self.resume_pdns_service_with_options(request, runtime)

    async def resume_pdns_service_async(
        self,
        request: main_models.ResumePdnsServiceRequest,
    ) -> main_models.ResumePdnsServiceResponse:
        runtime = RuntimeOptions()
        return await self.resume_pdns_service_with_options_async(request, runtime)

    def retrieve_domain_with_options(
        self,
        request: main_models.RetrieveDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_domain_with_options_async(
        self,
        request: main_models.RetrieveDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_domain(
        self,
        request: main_models.RetrieveDomainRequest,
    ) -> main_models.RetrieveDomainResponse:
        runtime = RuntimeOptions()
        return self.retrieve_domain_with_options(request, runtime)

    async def retrieve_domain_async(
        self,
        request: main_models.RetrieveDomainRequest,
    ) -> main_models.RetrieveDomainResponse:
        runtime = RuntimeOptions()
        return await self.retrieve_domain_with_options_async(request, runtime)

    def rollback_gtm_recovery_plan_with_options(
        self,
        request: main_models.RollbackGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.RollbackGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_gtm_recovery_plan(
        self,
        request: main_models.RollbackGtmRecoveryPlanRequest,
    ) -> main_models.RollbackGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.rollback_gtm_recovery_plan_with_options(request, runtime)

    async def rollback_gtm_recovery_plan_async(
        self,
        request: main_models.RollbackGtmRecoveryPlanRequest,
    ) -> main_models.RollbackGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.rollback_gtm_recovery_plan_with_options_async(request, runtime)

    def search_cloud_gtm_address_pools_with_options(
        self,
        request: main_models.SearchCloudGtmAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_address_pools_with_options_async(
        self,
        request: main_models.SearchCloudGtmAddressPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmAddressPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmAddressPools',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_address_pools(
        self,
        request: main_models.SearchCloudGtmAddressPoolsRequest,
    ) -> main_models.SearchCloudGtmAddressPoolsResponse:
        runtime = RuntimeOptions()
        return self.search_cloud_gtm_address_pools_with_options(request, runtime)

    async def search_cloud_gtm_address_pools_async(
        self,
        request: main_models.SearchCloudGtmAddressPoolsRequest,
    ) -> main_models.SearchCloudGtmAddressPoolsResponse:
        runtime = RuntimeOptions()
        return await self.search_cloud_gtm_address_pools_with_options_async(request, runtime)

    def search_cloud_gtm_addresses_with_options(
        self,
        request: main_models.SearchCloudGtmAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.monitor_template_name):
            query['MonitorTemplateName'] = request.monitor_template_name
        if not DaraCore.is_null(request.name_search_condition):
            query['NameSearchCondition'] = request.name_search_condition
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark_search_condition):
            query['RemarkSearchCondition'] = request.remark_search_condition
        if not DaraCore.is_null(request.remarks):
            query['Remarks'] = request.remarks
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmAddresses',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_addresses_with_options_async(
        self,
        request: main_models.SearchCloudGtmAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.monitor_template_name):
            query['MonitorTemplateName'] = request.monitor_template_name
        if not DaraCore.is_null(request.name_search_condition):
            query['NameSearchCondition'] = request.name_search_condition
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark_search_condition):
            query['RemarkSearchCondition'] = request.remark_search_condition
        if not DaraCore.is_null(request.remarks):
            query['Remarks'] = request.remarks
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmAddresses',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_addresses(
        self,
        request: main_models.SearchCloudGtmAddressesRequest,
    ) -> main_models.SearchCloudGtmAddressesResponse:
        runtime = RuntimeOptions()
        return self.search_cloud_gtm_addresses_with_options(request, runtime)

    async def search_cloud_gtm_addresses_async(
        self,
        request: main_models.SearchCloudGtmAddressesRequest,
    ) -> main_models.SearchCloudGtmAddressesResponse:
        runtime = RuntimeOptions()
        return await self.search_cloud_gtm_addresses_with_options_async(request, runtime)

    def search_cloud_gtm_instance_configs_with_options(
        self,
        request: main_models.SearchCloudGtmInstanceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmInstanceConfigs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_instance_configs_with_options_async(
        self,
        request: main_models.SearchCloudGtmInstanceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmInstanceConfigs',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_instance_configs(
        self,
        request: main_models.SearchCloudGtmInstanceConfigsRequest,
    ) -> main_models.SearchCloudGtmInstanceConfigsResponse:
        runtime = RuntimeOptions()
        return self.search_cloud_gtm_instance_configs_with_options(request, runtime)

    async def search_cloud_gtm_instance_configs_async(
        self,
        request: main_models.SearchCloudGtmInstanceConfigsRequest,
    ) -> main_models.SearchCloudGtmInstanceConfigsResponse:
        runtime = RuntimeOptions()
        return await self.search_cloud_gtm_instance_configs_with_options_async(request, runtime)

    def search_cloud_gtm_instances_with_options(
        self,
        request: main_models.SearchCloudGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_instances_with_options_async(
        self,
        request: main_models.SearchCloudGtmInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmInstances',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_instances(
        self,
        request: main_models.SearchCloudGtmInstancesRequest,
    ) -> main_models.SearchCloudGtmInstancesResponse:
        runtime = RuntimeOptions()
        return self.search_cloud_gtm_instances_with_options(request, runtime)

    async def search_cloud_gtm_instances_async(
        self,
        request: main_models.SearchCloudGtmInstancesRequest,
    ) -> main_models.SearchCloudGtmInstancesResponse:
        runtime = RuntimeOptions()
        return await self.search_cloud_gtm_instances_with_options_async(request, runtime)

    def search_cloud_gtm_monitor_templates_with_options(
        self,
        request: main_models.SearchCloudGtmMonitorTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmMonitorTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmMonitorTemplates',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmMonitorTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_monitor_templates_with_options_async(
        self,
        request: main_models.SearchCloudGtmMonitorTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCloudGtmMonitorTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCloudGtmMonitorTemplates',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCloudGtmMonitorTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_monitor_templates(
        self,
        request: main_models.SearchCloudGtmMonitorTemplatesRequest,
    ) -> main_models.SearchCloudGtmMonitorTemplatesResponse:
        runtime = RuntimeOptions()
        return self.search_cloud_gtm_monitor_templates_with_options(request, runtime)

    async def search_cloud_gtm_monitor_templates_async(
        self,
        request: main_models.SearchCloudGtmMonitorTemplatesRequest,
    ) -> main_models.SearchCloudGtmMonitorTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.search_cloud_gtm_monitor_templates_with_options_async(request, runtime)

    def search_recursion_records_with_options(
        self,
        request: main_models.SearchRecursionRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRecursionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRecursionRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRecursionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_recursion_records_with_options_async(
        self,
        request: main_models.SearchRecursionRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRecursionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRecursionRecords',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRecursionRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_recursion_records(
        self,
        request: main_models.SearchRecursionRecordsRequest,
    ) -> main_models.SearchRecursionRecordsResponse:
        runtime = RuntimeOptions()
        return self.search_recursion_records_with_options(request, runtime)

    async def search_recursion_records_async(
        self,
        request: main_models.SearchRecursionRecordsRequest,
    ) -> main_models.SearchRecursionRecordsResponse:
        runtime = RuntimeOptions()
        return await self.search_recursion_records_with_options_async(request, runtime)

    def search_recursion_zones_with_options(
        self,
        tmp_req: main_models.SearchRecursionZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRecursionZonesResponse:
        tmp_req.validate()
        request = main_models.SearchRecursionZonesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.effective_scopes):
            request.effective_scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.effective_scopes, 'EffectiveScopes', 'json')
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.effective_scopes_shrink):
            query['EffectiveScopes'] = request.effective_scopes_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRecursionZones',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRecursionZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_recursion_zones_with_options_async(
        self,
        tmp_req: main_models.SearchRecursionZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRecursionZonesResponse:
        tmp_req.validate()
        request = main_models.SearchRecursionZonesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.effective_scopes):
            request.effective_scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.effective_scopes, 'EffectiveScopes', 'json')
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.effective_scopes_shrink):
            query['EffectiveScopes'] = request.effective_scopes_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRecursionZones',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRecursionZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_recursion_zones(
        self,
        request: main_models.SearchRecursionZonesRequest,
    ) -> main_models.SearchRecursionZonesResponse:
        runtime = RuntimeOptions()
        return self.search_recursion_zones_with_options(request, runtime)

    async def search_recursion_zones_async(
        self,
        request: main_models.SearchRecursionZonesRequest,
    ) -> main_models.SearchRecursionZonesResponse:
        runtime = RuntimeOptions()
        return await self.search_recursion_zones_with_options_async(request, runtime)

    def set_dnsslbstatus_with_options(
        self,
        request: main_models.SetDNSSLBStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDNSSLBStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.open):
            query['Open'] = request.open
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDNSSLBStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDNSSLBStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dnsslbstatus_with_options_async(
        self,
        request: main_models.SetDNSSLBStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDNSSLBStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.open):
            query['Open'] = request.open
        if not DaraCore.is_null(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDNSSLBStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDNSSLBStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dnsslbstatus(
        self,
        request: main_models.SetDNSSLBStatusRequest,
    ) -> main_models.SetDNSSLBStatusResponse:
        runtime = RuntimeOptions()
        return self.set_dnsslbstatus_with_options(request, runtime)

    async def set_dnsslbstatus_async(
        self,
        request: main_models.SetDNSSLBStatusRequest,
    ) -> main_models.SetDNSSLBStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_dnsslbstatus_with_options_async(request, runtime)

    def set_dns_gtm_access_mode_with_options(
        self,
        request: main_models.SetDnsGtmAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDnsGtmAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDnsGtmAccessMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDnsGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dns_gtm_access_mode_with_options_async(
        self,
        request: main_models.SetDnsGtmAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDnsGtmAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDnsGtmAccessMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDnsGtmAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dns_gtm_access_mode(
        self,
        request: main_models.SetDnsGtmAccessModeRequest,
    ) -> main_models.SetDnsGtmAccessModeResponse:
        runtime = RuntimeOptions()
        return self.set_dns_gtm_access_mode_with_options(request, runtime)

    async def set_dns_gtm_access_mode_async(
        self,
        request: main_models.SetDnsGtmAccessModeRequest,
    ) -> main_models.SetDnsGtmAccessModeResponse:
        runtime = RuntimeOptions()
        return await self.set_dns_gtm_access_mode_with_options_async(request, runtime)

    def set_dns_gtm_monitor_status_with_options(
        self,
        request: main_models.SetDnsGtmMonitorStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDnsGtmMonitorStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDnsGtmMonitorStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDnsGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dns_gtm_monitor_status_with_options_async(
        self,
        request: main_models.SetDnsGtmMonitorStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDnsGtmMonitorStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDnsGtmMonitorStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDnsGtmMonitorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dns_gtm_monitor_status(
        self,
        request: main_models.SetDnsGtmMonitorStatusRequest,
    ) -> main_models.SetDnsGtmMonitorStatusResponse:
        runtime = RuntimeOptions()
        return self.set_dns_gtm_monitor_status_with_options(request, runtime)

    async def set_dns_gtm_monitor_status_async(
        self,
        request: main_models.SetDnsGtmMonitorStatusRequest,
    ) -> main_models.SetDnsGtmMonitorStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_dns_gtm_monitor_status_with_options_async(request, runtime)

    def set_domain_dnssec_status_with_options(
        self,
        request: main_models.SetDomainDnssecStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainDnssecStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainDnssecStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainDnssecStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_dnssec_status_with_options_async(
        self,
        request: main_models.SetDomainDnssecStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainDnssecStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainDnssecStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainDnssecStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_dnssec_status(
        self,
        request: main_models.SetDomainDnssecStatusRequest,
    ) -> main_models.SetDomainDnssecStatusResponse:
        runtime = RuntimeOptions()
        return self.set_domain_dnssec_status_with_options(request, runtime)

    async def set_domain_dnssec_status_async(
        self,
        request: main_models.SetDomainDnssecStatusRequest,
    ) -> main_models.SetDomainDnssecStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_dnssec_status_with_options_async(request, runtime)

    def set_domain_record_status_with_options(
        self,
        request: main_models.SetDomainRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainRecordStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_record_status_with_options_async(
        self,
        request: main_models.SetDomainRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainRecordStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_record_status(
        self,
        request: main_models.SetDomainRecordStatusRequest,
    ) -> main_models.SetDomainRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.set_domain_record_status_with_options(request, runtime)

    async def set_domain_record_status_async(
        self,
        request: main_models.SetDomainRecordStatusRequest,
    ) -> main_models.SetDomainRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_record_status_with_options_async(request, runtime)

    def set_gtm_access_mode_with_options(
        self,
        request: main_models.SetGtmAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGtmAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGtmAccessMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gtm_access_mode_with_options_async(
        self,
        request: main_models.SetGtmAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGtmAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGtmAccessMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGtmAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gtm_access_mode(
        self,
        request: main_models.SetGtmAccessModeRequest,
    ) -> main_models.SetGtmAccessModeResponse:
        runtime = RuntimeOptions()
        return self.set_gtm_access_mode_with_options(request, runtime)

    async def set_gtm_access_mode_async(
        self,
        request: main_models.SetGtmAccessModeRequest,
    ) -> main_models.SetGtmAccessModeResponse:
        runtime = RuntimeOptions()
        return await self.set_gtm_access_mode_with_options_async(request, runtime)

    def set_gtm_monitor_status_with_options(
        self,
        request: main_models.SetGtmMonitorStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGtmMonitorStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGtmMonitorStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gtm_monitor_status_with_options_async(
        self,
        request: main_models.SetGtmMonitorStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGtmMonitorStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGtmMonitorStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGtmMonitorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gtm_monitor_status(
        self,
        request: main_models.SetGtmMonitorStatusRequest,
    ) -> main_models.SetGtmMonitorStatusResponse:
        runtime = RuntimeOptions()
        return self.set_gtm_monitor_status_with_options(request, runtime)

    async def set_gtm_monitor_status_async(
        self,
        request: main_models.SetGtmMonitorStatusRequest,
    ) -> main_models.SetGtmMonitorStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_gtm_monitor_status_with_options_async(request, runtime)

    def submit_isp_flush_cache_task_with_options(
        self,
        request: main_models.SubmitIspFlushCacheTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIspFlushCacheTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIspFlushCacheTask',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_isp_flush_cache_task_with_options_async(
        self,
        request: main_models.SubmitIspFlushCacheTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIspFlushCacheTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIspFlushCacheTask',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIspFlushCacheTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_isp_flush_cache_task(
        self,
        request: main_models.SubmitIspFlushCacheTaskRequest,
    ) -> main_models.SubmitIspFlushCacheTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_isp_flush_cache_task_with_options(request, runtime)

    async def submit_isp_flush_cache_task_async(
        self,
        request: main_models.SubmitIspFlushCacheTaskRequest,
    ) -> main_models.SubmitIspFlushCacheTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_isp_flush_cache_task_with_options_async(request, runtime)

    def switch_dns_gtm_instance_strategy_mode_with_options(
        self,
        request: main_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDnsGtmInstanceStrategyModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDnsGtmInstanceStrategyMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDnsGtmInstanceStrategyModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dns_gtm_instance_strategy_mode_with_options_async(
        self,
        request: main_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDnsGtmInstanceStrategyModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDnsGtmInstanceStrategyMode',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDnsGtmInstanceStrategyModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dns_gtm_instance_strategy_mode(
        self,
        request: main_models.SwitchDnsGtmInstanceStrategyModeRequest,
    ) -> main_models.SwitchDnsGtmInstanceStrategyModeResponse:
        runtime = RuntimeOptions()
        return self.switch_dns_gtm_instance_strategy_mode_with_options(request, runtime)

    async def switch_dns_gtm_instance_strategy_mode_async(
        self,
        request: main_models.SwitchDnsGtmInstanceStrategyModeRequest,
    ) -> main_models.SwitchDnsGtmInstanceStrategyModeResponse:
        runtime = RuntimeOptions()
        return await self.switch_dns_gtm_instance_strategy_mode_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_domain_with_options(
        self,
        request: main_models.TransferDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_domain_with_options_async(
        self,
        request: main_models.TransferDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_domain(
        self,
        request: main_models.TransferDomainRequest,
    ) -> main_models.TransferDomainResponse:
        runtime = RuntimeOptions()
        return self.transfer_domain_with_options(request, runtime)

    async def transfer_domain_async(
        self,
        request: main_models.TransferDomainRequest,
    ) -> main_models.TransferDomainResponse:
        runtime = RuntimeOptions()
        return await self.transfer_domain_with_options_async(request, runtime)

    def unbind_instance_domains_with_options(
        self,
        request: main_models.UnbindInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_instance_domains_with_options_async(
        self,
        request: main_models.UnbindInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInstanceDomains',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_instance_domains(
        self,
        request: main_models.UnbindInstanceDomainsRequest,
    ) -> main_models.UnbindInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return self.unbind_instance_domains_with_options(request, runtime)

    async def unbind_instance_domains_async(
        self,
        request: main_models.UnbindInstanceDomainsRequest,
    ) -> main_models.UnbindInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return await self.unbind_instance_domains_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_app_key_state_with_options(
        self,
        request: main_models.UpdateAppKeyStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppKeyStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppKeyState',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppKeyStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_key_state_with_options_async(
        self,
        request: main_models.UpdateAppKeyStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppKeyStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppKeyState',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppKeyStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_key_state(
        self,
        request: main_models.UpdateAppKeyStateRequest,
    ) -> main_models.UpdateAppKeyStateResponse:
        runtime = RuntimeOptions()
        return self.update_app_key_state_with_options(request, runtime)

    async def update_app_key_state_async(
        self,
        request: main_models.UpdateAppKeyStateRequest,
    ) -> main_models.UpdateAppKeyStateResponse:
        runtime = RuntimeOptions()
        return await self.update_app_key_state_with_options_async(request, runtime)

    def update_cloud_gtm_address_with_options(
        self,
        tmp_req: main_models.UpdateCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_tasks):
            request.health_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudGtmAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmAddressShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_tasks):
            request.health_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not DaraCore.is_null(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddress',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address(
        self,
        request: main_models.UpdateCloudGtmAddressRequest,
    ) -> main_models.UpdateCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_with_options(request, runtime)

    async def update_cloud_gtm_address_async(
        self,
        request: main_models.UpdateCloudGtmAddressRequest,
    ) -> main_models.UpdateCloudGtmAddressResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_with_options_async(request, runtime)

    def update_cloud_gtm_address_enable_status_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_enable_status_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_enable_status(
        self,
        request: main_models.UpdateCloudGtmAddressEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_address_enable_status_async(
        self,
        request: main_models.UpdateCloudGtmAddressEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_manual_available_status_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressManualAvailableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressManualAvailableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_manual_available_status_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressManualAvailableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressManualAvailableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_manual_available_status(
        self,
        request: main_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_manual_available_status_with_options(request, runtime)

    async def update_cloud_gtm_address_manual_available_status_async(
        self,
        request: main_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_manual_available_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_basic_config_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolBasicConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_basic_config_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolBasicConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_basic_config(
        self,
        request: main_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_pool_basic_config_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_basic_config_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_basic_config_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_enable_status_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_enable_status_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_enable_status(
        self,
        request: main_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_pool_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_enable_status_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_lb_strategy_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_lb_strategy):
            query['AddressLbStrategy'] = request.address_lb_strategy
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolLbStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolLbStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_lb_strategy_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_lb_strategy):
            query['AddressLbStrategy'] = request.address_lb_strategy
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolLbStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolLbStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_lb_strategy(
        self,
        request: main_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_pool_lb_strategy_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_lb_strategy_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_lb_strategy_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_remark_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressPoolRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_remark_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressPoolRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressPoolRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressPoolRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_remark(
        self,
        request: main_models.UpdateCloudGtmAddressPoolRemarkRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_pool_remark_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_remark_async(
        self,
        request: main_models.UpdateCloudGtmAddressPoolRemarkRequest,
    ) -> main_models.UpdateCloudGtmAddressPoolRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_remark_with_options_async(request, runtime)

    def update_cloud_gtm_address_remark_with_options(
        self,
        request: main_models.UpdateCloudGtmAddressRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_remark_with_options_async(
        self,
        request: main_models.UpdateCloudGtmAddressRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmAddressRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmAddressRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmAddressRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_remark(
        self,
        request: main_models.UpdateCloudGtmAddressRemarkRequest,
    ) -> main_models.UpdateCloudGtmAddressRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_address_remark_with_options(request, runtime)

    async def update_cloud_gtm_address_remark_async(
        self,
        request: main_models.UpdateCloudGtmAddressRemarkRequest,
    ) -> main_models.UpdateCloudGtmAddressRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_address_remark_with_options_async(request, runtime)

    def update_cloud_gtm_global_alert_with_options(
        self,
        tmp_req: main_models.UpdateCloudGtmGlobalAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmGlobalAlertResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmGlobalAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_config):
            request.alert_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not DaraCore.is_null(tmp_req.alert_group):
            request.alert_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not DaraCore.is_null(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmGlobalAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmGlobalAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_global_alert_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudGtmGlobalAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmGlobalAlertResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmGlobalAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_config):
            request.alert_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not DaraCore.is_null(tmp_req.alert_group):
            request.alert_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not DaraCore.is_null(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmGlobalAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmGlobalAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_global_alert(
        self,
        request: main_models.UpdateCloudGtmGlobalAlertRequest,
    ) -> main_models.UpdateCloudGtmGlobalAlertResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_global_alert_with_options(request, runtime)

    async def update_cloud_gtm_global_alert_async(
        self,
        request: main_models.UpdateCloudGtmGlobalAlertRequest,
    ) -> main_models.UpdateCloudGtmGlobalAlertResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_global_alert_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_alert_with_options(
        self,
        tmp_req: main_models.UpdateCloudGtmInstanceConfigAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigAlertResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmInstanceConfigAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_config):
            request.alert_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not DaraCore.is_null(tmp_req.alert_group):
            request.alert_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not DaraCore.is_null(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not DaraCore.is_null(request.alert_mode):
            query['AlertMode'] = request.alert_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_alert_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudGtmInstanceConfigAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigAlertResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmInstanceConfigAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_config):
            request.alert_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not DaraCore.is_null(tmp_req.alert_group):
            request.alert_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not DaraCore.is_null(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not DaraCore.is_null(request.alert_mode):
            query['AlertMode'] = request.alert_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigAlert',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_alert(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigAlertRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigAlertResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_config_alert_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_alert_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigAlertRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigAlertResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_alert_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_basic_with_options(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigBasicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigBasicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigBasic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigBasicResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_basic_with_options_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigBasicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigBasicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not DaraCore.is_null(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigBasic',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigBasicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_basic(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigBasicRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigBasicResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_config_basic_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_basic_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigBasicRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigBasicResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_basic_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_enable_status_with_options(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_enable_status_with_options_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_enable_status(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_config_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_enable_status_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_lb_strategy_with_options(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_lb_strategy):
            query['AddressPoolLbStrategy'] = request.address_pool_lb_strategy
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigLbStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_lb_strategy_with_options_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address_pool_lb_strategy):
            query['AddressPoolLbStrategy'] = request.address_pool_lb_strategy
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigLbStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_lb_strategy(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_config_lb_strategy_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_lb_strategy_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_lb_strategy_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_remark_with_options(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_remark_with_options_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceConfigRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceConfigRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_remark(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigRemarkRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_config_remark_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_remark_async(
        self,
        request: main_models.UpdateCloudGtmInstanceConfigRemarkRequest,
    ) -> main_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_remark_with_options_async(request, runtime)

    def update_cloud_gtm_instance_name_with_options(
        self,
        request: main_models.UpdateCloudGtmInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceName',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_name_with_options_async(
        self,
        request: main_models.UpdateCloudGtmInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmInstanceName',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_name(
        self,
        request: main_models.UpdateCloudGtmInstanceNameRequest,
    ) -> main_models.UpdateCloudGtmInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_instance_name_with_options(request, runtime)

    async def update_cloud_gtm_instance_name_async(
        self,
        request: main_models.UpdateCloudGtmInstanceNameRequest,
    ) -> main_models.UpdateCloudGtmInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_instance_name_with_options_async(request, runtime)

    def update_cloud_gtm_monitor_template_with_options(
        self,
        tmp_req: main_models.UpdateCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmMonitorTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmMonitorTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_monitor_template_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudGtmMonitorTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmMonitorTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudGtmMonitorTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not DaraCore.is_null(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmMonitorTemplate',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_monitor_template(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRequest,
    ) -> main_models.UpdateCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_monitor_template_with_options(request, runtime)

    async def update_cloud_gtm_monitor_template_async(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRequest,
    ) -> main_models.UpdateCloudGtmMonitorTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def update_cloud_gtm_monitor_template_remark_with_options(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmMonitorTemplateRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmMonitorTemplateRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_monitor_template_remark_with_options_async(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudGtmMonitorTemplateRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudGtmMonitorTemplateRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_monitor_template_remark(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
    ) -> main_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_gtm_monitor_template_remark_with_options(request, runtime)

    async def update_cloud_gtm_monitor_template_remark_async(
        self,
        request: main_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
    ) -> main_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_gtm_monitor_template_remark_with_options_async(request, runtime)

    def update_custom_line_with_options(
        self,
        request: main_models.UpdateCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        if not DaraCore.is_null(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_line_with_options_async(
        self,
        request: main_models.UpdateCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        if not DaraCore.is_null(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomLine',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_line(
        self,
        request: main_models.UpdateCustomLineRequest,
    ) -> main_models.UpdateCustomLineResponse:
        runtime = RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    async def update_custom_line_async(
        self,
        request: main_models.UpdateCustomLineRequest,
    ) -> main_models.UpdateCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_line_with_options_async(request, runtime)

    def update_dnsslbweight_with_options(
        self,
        request: main_models.UpdateDNSSLBWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDNSSLBWeightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDNSSLBWeight',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDNSSLBWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dnsslbweight_with_options_async(
        self,
        request: main_models.UpdateDNSSLBWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDNSSLBWeightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDNSSLBWeight',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDNSSLBWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dnsslbweight(
        self,
        request: main_models.UpdateDNSSLBWeightRequest,
    ) -> main_models.UpdateDNSSLBWeightResponse:
        runtime = RuntimeOptions()
        return self.update_dnsslbweight_with_options(request, runtime)

    async def update_dnsslbweight_async(
        self,
        request: main_models.UpdateDNSSLBWeightRequest,
    ) -> main_models.UpdateDNSSLBWeightResponse:
        runtime = RuntimeOptions()
        return await self.update_dnsslbweight_with_options_async(request, runtime)

    def update_dns_cache_domain_with_options(
        self,
        request: main_models.UpdateDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not DaraCore.is_null(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not DaraCore.is_null(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not DaraCore.is_null(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_cache_domain_with_options_async(
        self,
        request: main_models.UpdateDnsCacheDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsCacheDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not DaraCore.is_null(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not DaraCore.is_null(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not DaraCore.is_null(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsCacheDomain',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_cache_domain(
        self,
        request: main_models.UpdateDnsCacheDomainRequest,
    ) -> main_models.UpdateDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return self.update_dns_cache_domain_with_options(request, runtime)

    async def update_dns_cache_domain_async(
        self,
        request: main_models.UpdateDnsCacheDomainRequest,
    ) -> main_models.UpdateDnsCacheDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_cache_domain_with_options_async(request, runtime)

    def update_dns_cache_domain_remark_with_options(
        self,
        request: main_models.UpdateDnsCacheDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsCacheDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsCacheDomainRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsCacheDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_cache_domain_remark_with_options_async(
        self,
        request: main_models.UpdateDnsCacheDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsCacheDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsCacheDomainRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsCacheDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_cache_domain_remark(
        self,
        request: main_models.UpdateDnsCacheDomainRemarkRequest,
    ) -> main_models.UpdateDnsCacheDomainRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_dns_cache_domain_remark_with_options(request, runtime)

    async def update_dns_cache_domain_remark_async(
        self,
        request: main_models.UpdateDnsCacheDomainRemarkRequest,
    ) -> main_models.UpdateDnsCacheDomainRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_cache_domain_remark_with_options_async(request, runtime)

    def update_dns_gtm_access_strategy_with_options(
        self,
        request: main_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not DaraCore.is_null(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not DaraCore.is_null(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not DaraCore.is_null(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not DaraCore.is_null(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not DaraCore.is_null(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not DaraCore.is_null(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not DaraCore.is_null(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not DaraCore.is_null(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not DaraCore.is_null(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not DaraCore.is_null(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not DaraCore.is_null(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_access_strategy_with_options_async(
        self,
        request: main_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not DaraCore.is_null(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not DaraCore.is_null(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not DaraCore.is_null(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not DaraCore.is_null(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not DaraCore.is_null(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not DaraCore.is_null(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not DaraCore.is_null(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not DaraCore.is_null(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not DaraCore.is_null(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not DaraCore.is_null(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not DaraCore.is_null(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_access_strategy(
        self,
        request: main_models.UpdateDnsGtmAccessStrategyRequest,
    ) -> main_models.UpdateDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_dns_gtm_access_strategy_with_options(request, runtime)

    async def update_dns_gtm_access_strategy_async(
        self,
        request: main_models.UpdateDnsGtmAccessStrategyRequest,
    ) -> main_models.UpdateDnsGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_gtm_access_strategy_with_options_async(request, runtime)

    def update_dns_gtm_address_pool_with_options(
        self,
        request: main_models.UpdateDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_address_pool_with_options_async(
        self,
        request: main_models.UpdateDnsGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_address_pool(
        self,
        request: main_models.UpdateDnsGtmAddressPoolRequest,
    ) -> main_models.UpdateDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.update_dns_gtm_address_pool_with_options(request, runtime)

    async def update_dns_gtm_address_pool_async(
        self,
        request: main_models.UpdateDnsGtmAddressPoolRequest,
    ) -> main_models.UpdateDnsGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_gtm_address_pool_with_options_async(request, runtime)

    def update_dns_gtm_instance_global_config_with_options(
        self,
        request: main_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.cname_type):
            query['CnameType'] = request.cname_type
        if not DaraCore.is_null(request.force_update):
            query['ForceUpdate'] = request.force_update
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.public_cname_mode):
            query['PublicCnameMode'] = request.public_cname_mode
        if not DaraCore.is_null(request.public_rr):
            query['PublicRr'] = request.public_rr
        if not DaraCore.is_null(request.public_user_domain_name):
            query['PublicUserDomainName'] = request.public_user_domain_name
        if not DaraCore.is_null(request.public_zone_name):
            query['PublicZoneName'] = request.public_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmInstanceGlobalConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_instance_global_config_with_options_async(
        self,
        request: main_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.cname_type):
            query['CnameType'] = request.cname_type
        if not DaraCore.is_null(request.force_update):
            query['ForceUpdate'] = request.force_update
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.public_cname_mode):
            query['PublicCnameMode'] = request.public_cname_mode
        if not DaraCore.is_null(request.public_rr):
            query['PublicRr'] = request.public_rr
        if not DaraCore.is_null(request.public_user_domain_name):
            query['PublicUserDomainName'] = request.public_user_domain_name
        if not DaraCore.is_null(request.public_zone_name):
            query['PublicZoneName'] = request.public_zone_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmInstanceGlobalConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmInstanceGlobalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_instance_global_config(
        self,
        request: main_models.UpdateDnsGtmInstanceGlobalConfigRequest,
    ) -> main_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        runtime = RuntimeOptions()
        return self.update_dns_gtm_instance_global_config_with_options(request, runtime)

    async def update_dns_gtm_instance_global_config_async(
        self,
        request: main_models.UpdateDnsGtmInstanceGlobalConfigRequest,
    ) -> main_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_gtm_instance_global_config_with_options_async(request, runtime)

    def update_dns_gtm_monitor_with_options(
        self,
        request: main_models.UpdateDnsGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_monitor_with_options_async(
        self,
        request: main_models.UpdateDnsGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDnsGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDnsGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDnsGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_monitor(
        self,
        request: main_models.UpdateDnsGtmMonitorRequest,
    ) -> main_models.UpdateDnsGtmMonitorResponse:
        runtime = RuntimeOptions()
        return self.update_dns_gtm_monitor_with_options(request, runtime)

    async def update_dns_gtm_monitor_async(
        self,
        request: main_models.UpdateDnsGtmMonitorRequest,
    ) -> main_models.UpdateDnsGtmMonitorResponse:
        runtime = RuntimeOptions()
        return await self.update_dns_gtm_monitor_with_options_async(request, runtime)

    def update_domain_group_with_options(
        self,
        request: main_models.UpdateDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_group_with_options_async(
        self,
        request: main_models.UpdateDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainGroup',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_group(
        self,
        request: main_models.UpdateDomainGroupRequest,
    ) -> main_models.UpdateDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.update_domain_group_with_options(request, runtime)

    async def update_domain_group_async(
        self,
        request: main_models.UpdateDomainGroupRequest,
    ) -> main_models.UpdateDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_group_with_options_async(request, runtime)

    def update_domain_record_with_options(
        self,
        request: main_models.UpdateDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.ttl):
            query['TTL'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_record_with_options_async(
        self,
        request: main_models.UpdateDomainRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rr):
            query['RR'] = request.rr
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.ttl):
            query['TTL'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_record(
        self,
        request: main_models.UpdateDomainRecordRequest,
    ) -> main_models.UpdateDomainRecordResponse:
        runtime = RuntimeOptions()
        return self.update_domain_record_with_options(request, runtime)

    async def update_domain_record_async(
        self,
        request: main_models.UpdateDomainRecordRequest,
    ) -> main_models.UpdateDomainRecordResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_record_with_options_async(request, runtime)

    def update_domain_record_remark_with_options(
        self,
        request: main_models.UpdateDomainRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRecordRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_record_remark_with_options_async(
        self,
        request: main_models.UpdateDomainRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRecordRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_record_remark(
        self,
        request: main_models.UpdateDomainRecordRemarkRequest,
    ) -> main_models.UpdateDomainRecordRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_domain_record_remark_with_options(request, runtime)

    async def update_domain_record_remark_async(
        self,
        request: main_models.UpdateDomainRecordRemarkRequest,
    ) -> main_models.UpdateDomainRecordRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_record_remark_with_options_async(request, runtime)

    def update_domain_remark_with_options(
        self,
        request: main_models.UpdateDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_remark_with_options_async(
        self,
        request: main_models.UpdateDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_remark(
        self,
        request: main_models.UpdateDomainRemarkRequest,
    ) -> main_models.UpdateDomainRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_domain_remark_with_options(request, runtime)

    async def update_domain_remark_async(
        self,
        request: main_models.UpdateDomainRemarkRequest,
    ) -> main_models.UpdateDomainRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_remark_with_options_async(request, runtime)

    def update_gtm_access_strategy_with_options(
        self,
        request: main_models.UpdateGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not DaraCore.is_null(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not DaraCore.is_null(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_access_strategy_with_options_async(
        self,
        request: main_models.UpdateGtmAccessStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmAccessStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not DaraCore.is_null(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not DaraCore.is_null(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not DaraCore.is_null(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmAccessStrategy',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_access_strategy(
        self,
        request: main_models.UpdateGtmAccessStrategyRequest,
    ) -> main_models.UpdateGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_gtm_access_strategy_with_options(request, runtime)

    async def update_gtm_access_strategy_async(
        self,
        request: main_models.UpdateGtmAccessStrategyRequest,
    ) -> main_models.UpdateGtmAccessStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_gtm_access_strategy_with_options_async(request, runtime)

    def update_gtm_address_pool_with_options(
        self,
        request: main_models.UpdateGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_address_pool_with_options_async(
        self,
        request: main_models.UpdateGtmAddressPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmAddressPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addr):
            query['Addr'] = request.addr
        if not DaraCore.is_null(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmAddressPool',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_address_pool(
        self,
        request: main_models.UpdateGtmAddressPoolRequest,
    ) -> main_models.UpdateGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return self.update_gtm_address_pool_with_options(request, runtime)

    async def update_gtm_address_pool_async(
        self,
        request: main_models.UpdateGtmAddressPoolRequest,
    ) -> main_models.UpdateGtmAddressPoolResponse:
        runtime = RuntimeOptions()
        return await self.update_gtm_address_pool_with_options_async(request, runtime)

    def update_gtm_instance_global_config_with_options(
        self,
        request: main_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmInstanceGlobalConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.cname_custom_domain_name):
            query['CnameCustomDomainName'] = request.cname_custom_domain_name
        if not DaraCore.is_null(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.user_domain_name):
            query['UserDomainName'] = request.user_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmInstanceGlobalConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_instance_global_config_with_options_async(
        self,
        request: main_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmInstanceGlobalConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.cname_custom_domain_name):
            query['CnameCustomDomainName'] = request.cname_custom_domain_name
        if not DaraCore.is_null(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.user_domain_name):
            query['UserDomainName'] = request.user_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmInstanceGlobalConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmInstanceGlobalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_instance_global_config(
        self,
        request: main_models.UpdateGtmInstanceGlobalConfigRequest,
    ) -> main_models.UpdateGtmInstanceGlobalConfigResponse:
        runtime = RuntimeOptions()
        return self.update_gtm_instance_global_config_with_options(request, runtime)

    async def update_gtm_instance_global_config_async(
        self,
        request: main_models.UpdateGtmInstanceGlobalConfigRequest,
    ) -> main_models.UpdateGtmInstanceGlobalConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_gtm_instance_global_config_with_options_async(request, runtime)

    def update_gtm_monitor_with_options(
        self,
        request: main_models.UpdateGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_monitor_with_options_async(
        self,
        request: main_models.UpdateGtmMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not DaraCore.is_null(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmMonitor',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_monitor(
        self,
        request: main_models.UpdateGtmMonitorRequest,
    ) -> main_models.UpdateGtmMonitorResponse:
        runtime = RuntimeOptions()
        return self.update_gtm_monitor_with_options(request, runtime)

    async def update_gtm_monitor_async(
        self,
        request: main_models.UpdateGtmMonitorRequest,
    ) -> main_models.UpdateGtmMonitorResponse:
        runtime = RuntimeOptions()
        return await self.update_gtm_monitor_with_options_async(request, runtime)

    def update_gtm_recovery_plan_with_options(
        self,
        request: main_models.UpdateGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_recovery_plan_with_options_async(
        self,
        request: main_models.UpdateGtmRecoveryPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGtmRecoveryPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGtmRecoveryPlan',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_recovery_plan(
        self,
        request: main_models.UpdateGtmRecoveryPlanRequest,
    ) -> main_models.UpdateGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return self.update_gtm_recovery_plan_with_options(request, runtime)

    async def update_gtm_recovery_plan_async(
        self,
        request: main_models.UpdateGtmRecoveryPlanRequest,
    ) -> main_models.UpdateGtmRecoveryPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_gtm_recovery_plan_with_options_async(request, runtime)

    def update_isp_flush_cache_instance_config_with_options(
        self,
        request: main_models.UpdateIspFlushCacheInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIspFlushCacheInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIspFlushCacheInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIspFlushCacheInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_isp_flush_cache_instance_config_with_options_async(
        self,
        request: main_models.UpdateIspFlushCacheInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIspFlushCacheInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIspFlushCacheInstanceConfig',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIspFlushCacheInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_isp_flush_cache_instance_config(
        self,
        request: main_models.UpdateIspFlushCacheInstanceConfigRequest,
    ) -> main_models.UpdateIspFlushCacheInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.update_isp_flush_cache_instance_config_with_options(request, runtime)

    async def update_isp_flush_cache_instance_config_async(
        self,
        request: main_models.UpdateIspFlushCacheInstanceConfigRequest,
    ) -> main_models.UpdateIspFlushCacheInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_isp_flush_cache_instance_config_with_options_async(request, runtime)

    def update_recursion_record_with_options(
        self,
        request: main_models.UpdateRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_record_with_options_async(
        self,
        request: main_models.UpdateRecursionRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecord',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_record(
        self,
        request: main_models.UpdateRecursionRecordRequest,
    ) -> main_models.UpdateRecursionRecordResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_record_with_options(request, runtime)

    async def update_recursion_record_async(
        self,
        request: main_models.UpdateRecursionRecordRequest,
    ) -> main_models.UpdateRecursionRecordResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_record_with_options_async(request, runtime)

    def update_recursion_record_enable_status_with_options(
        self,
        request: main_models.UpdateRecursionRecordEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_record_enable_status_with_options_async(
        self,
        request: main_models.UpdateRecursionRecordEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_record_enable_status(
        self,
        request: main_models.UpdateRecursionRecordEnableStatusRequest,
    ) -> main_models.UpdateRecursionRecordEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_record_enable_status_with_options(request, runtime)

    async def update_recursion_record_enable_status_async(
        self,
        request: main_models.UpdateRecursionRecordEnableStatusRequest,
    ) -> main_models.UpdateRecursionRecordEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_record_enable_status_with_options_async(request, runtime)

    def update_recursion_record_remark_with_options(
        self,
        request: main_models.UpdateRecursionRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_record_remark_with_options_async(
        self,
        request: main_models.UpdateRecursionRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_record_remark(
        self,
        request: main_models.UpdateRecursionRecordRemarkRequest,
    ) -> main_models.UpdateRecursionRecordRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_record_remark_with_options(request, runtime)

    async def update_recursion_record_remark_async(
        self,
        request: main_models.UpdateRecursionRecordRemarkRequest,
    ) -> main_models.UpdateRecursionRecordRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_record_remark_with_options_async(request, runtime)

    def update_recursion_record_weight_with_options(
        self,
        request: main_models.UpdateRecursionRecordWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordWeightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordWeight',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_record_weight_with_options_async(
        self,
        request: main_models.UpdateRecursionRecordWeightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordWeightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordWeight',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_record_weight(
        self,
        request: main_models.UpdateRecursionRecordWeightRequest,
    ) -> main_models.UpdateRecursionRecordWeightResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_record_weight_with_options(request, runtime)

    async def update_recursion_record_weight_async(
        self,
        request: main_models.UpdateRecursionRecordWeightRequest,
    ) -> main_models.UpdateRecursionRecordWeightResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_record_weight_with_options_async(request, runtime)

    def update_recursion_record_weight_enable_status_with_options(
        self,
        request: main_models.UpdateRecursionRecordWeightEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordWeightEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordWeightEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordWeightEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_record_weight_enable_status_with_options_async(
        self,
        request: main_models.UpdateRecursionRecordWeightEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionRecordWeightEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.request_source):
            query['RequestSource'] = request.request_source
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionRecordWeightEnableStatus',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionRecordWeightEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_record_weight_enable_status(
        self,
        request: main_models.UpdateRecursionRecordWeightEnableStatusRequest,
    ) -> main_models.UpdateRecursionRecordWeightEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_record_weight_enable_status_with_options(request, runtime)

    async def update_recursion_record_weight_enable_status_async(
        self,
        request: main_models.UpdateRecursionRecordWeightEnableStatusRequest,
    ) -> main_models.UpdateRecursionRecordWeightEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_record_weight_enable_status_with_options_async(request, runtime)

    def update_recursion_zone_effective_scope_with_options(
        self,
        tmp_req: main_models.UpdateRecursionZoneEffectiveScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneEffectiveScopeResponse:
        tmp_req.validate()
        request = main_models.UpdateRecursionZoneEffectiveScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.effective_scopes):
            request.effective_scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.effective_scopes, 'EffectiveScopes', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.effective_scopes_shrink):
            query['EffectiveScopes'] = request.effective_scopes_shrink
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneEffectiveScope',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneEffectiveScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_zone_effective_scope_with_options_async(
        self,
        tmp_req: main_models.UpdateRecursionZoneEffectiveScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneEffectiveScopeResponse:
        tmp_req.validate()
        request = main_models.UpdateRecursionZoneEffectiveScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.effective_scopes):
            request.effective_scopes_shrink = Utils.array_to_string_with_specified_style(tmp_req.effective_scopes, 'EffectiveScopes', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.effective_scopes_shrink):
            query['EffectiveScopes'] = request.effective_scopes_shrink
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneEffectiveScope',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneEffectiveScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_zone_effective_scope(
        self,
        request: main_models.UpdateRecursionZoneEffectiveScopeRequest,
    ) -> main_models.UpdateRecursionZoneEffectiveScopeResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_zone_effective_scope_with_options(request, runtime)

    async def update_recursion_zone_effective_scope_async(
        self,
        request: main_models.UpdateRecursionZoneEffectiveScopeRequest,
    ) -> main_models.UpdateRecursionZoneEffectiveScopeResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_zone_effective_scope_with_options_async(request, runtime)

    def update_recursion_zone_proxy_pattern_with_options(
        self,
        request: main_models.UpdateRecursionZoneProxyPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneProxyPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneProxyPattern',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneProxyPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_zone_proxy_pattern_with_options_async(
        self,
        request: main_models.UpdateRecursionZoneProxyPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneProxyPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneProxyPattern',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneProxyPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_zone_proxy_pattern(
        self,
        request: main_models.UpdateRecursionZoneProxyPatternRequest,
    ) -> main_models.UpdateRecursionZoneProxyPatternResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_zone_proxy_pattern_with_options(request, runtime)

    async def update_recursion_zone_proxy_pattern_async(
        self,
        request: main_models.UpdateRecursionZoneProxyPatternRequest,
    ) -> main_models.UpdateRecursionZoneProxyPatternResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_zone_proxy_pattern_with_options_async(request, runtime)

    def update_recursion_zone_remark_with_options(
        self,
        request: main_models.UpdateRecursionZoneRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recursion_zone_remark_with_options_async(
        self,
        request: main_models.UpdateRecursionZoneRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecursionZoneRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecursionZoneRemark',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecursionZoneRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recursion_zone_remark(
        self,
        request: main_models.UpdateRecursionZoneRemarkRequest,
    ) -> main_models.UpdateRecursionZoneRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_recursion_zone_remark_with_options(request, runtime)

    async def update_recursion_zone_remark_async(
        self,
        request: main_models.UpdateRecursionZoneRemarkRequest,
    ) -> main_models.UpdateRecursionZoneRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_recursion_zone_remark_with_options_async(request, runtime)

    def update_rsp_domain_server_prohibit_status_for_gateway_with_options(
        self,
        request: main_models.UpdateRspDomainServerProhibitStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_status_list):
            query['AddStatusList'] = request.add_status_list
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_status_list):
            query['DeleteStatusList'] = request.delete_status_list
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRspDomainServerProhibitStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rsp_domain_server_prohibit_status_for_gateway_with_options_async(
        self,
        request: main_models.UpdateRspDomainServerProhibitStatusForGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_status_list):
            query['AddStatusList'] = request.add_status_list
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_status_list):
            query['DeleteStatusList'] = request.delete_status_list
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRspDomainServerProhibitStatusForGateway',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rsp_domain_server_prohibit_status_for_gateway(
        self,
        request: main_models.UpdateRspDomainServerProhibitStatusForGatewayRequest,
    ) -> main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return self.update_rsp_domain_server_prohibit_status_for_gateway_with_options(request, runtime)

    async def update_rsp_domain_server_prohibit_status_for_gateway_async(
        self,
        request: main_models.UpdateRspDomainServerProhibitStatusForGatewayRequest,
    ) -> main_models.UpdateRspDomainServerProhibitStatusForGatewayResponse:
        runtime = RuntimeOptions()
        return await self.update_rsp_domain_server_prohibit_status_for_gateway_with_options_async(request, runtime)

    def validate_dns_gtm_cname_rr_can_use_with_options(
        self,
        request: main_models.ValidateDnsGtmCnameRrCanUseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDnsGtmCnameRrCanUseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not DaraCore.is_null(request.cname_rr):
            query['CnameRr'] = request.cname_rr
        if not DaraCore.is_null(request.cname_type):
            query['CnameType'] = request.cname_type
        if not DaraCore.is_null(request.cname_zone):
            query['CnameZone'] = request.cname_zone
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDnsGtmCnameRrCanUse',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDnsGtmCnameRrCanUseResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_dns_gtm_cname_rr_can_use_with_options_async(
        self,
        request: main_models.ValidateDnsGtmCnameRrCanUseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDnsGtmCnameRrCanUseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not DaraCore.is_null(request.cname_rr):
            query['CnameRr'] = request.cname_rr
        if not DaraCore.is_null(request.cname_type):
            query['CnameType'] = request.cname_type
        if not DaraCore.is_null(request.cname_zone):
            query['CnameZone'] = request.cname_zone
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDnsGtmCnameRrCanUse',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDnsGtmCnameRrCanUseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_dns_gtm_cname_rr_can_use(
        self,
        request: main_models.ValidateDnsGtmCnameRrCanUseRequest,
    ) -> main_models.ValidateDnsGtmCnameRrCanUseResponse:
        runtime = RuntimeOptions()
        return self.validate_dns_gtm_cname_rr_can_use_with_options(request, runtime)

    async def validate_dns_gtm_cname_rr_can_use_async(
        self,
        request: main_models.ValidateDnsGtmCnameRrCanUseRequest,
    ) -> main_models.ValidateDnsGtmCnameRrCanUseResponse:
        runtime = RuntimeOptions()
        return await self.validate_dns_gtm_cname_rr_can_use_with_options_async(request, runtime)

    def validate_pdns_udp_ip_segment_with_options(
        self,
        request: main_models.ValidatePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidatePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_token):
            query['IpToken'] = request.ip_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidatePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_pdns_udp_ip_segment_with_options_async(
        self,
        request: main_models.ValidatePdnsUdpIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidatePdnsUdpIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_token):
            query['IpToken'] = request.ip_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidatePdnsUdpIpSegment',
            version = '2015-01-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidatePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_pdns_udp_ip_segment(
        self,
        request: main_models.ValidatePdnsUdpIpSegmentRequest,
    ) -> main_models.ValidatePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return self.validate_pdns_udp_ip_segment_with_options(request, runtime)

    async def validate_pdns_udp_ip_segment_async(
        self,
        request: main_models.ValidatePdnsUdpIpSegmentRequest,
    ) -> main_models.ValidatePdnsUdpIpSegmentResponse:
        runtime = RuntimeOptions()
        return await self.validate_pdns_udp_ip_segment_with_options_async(request, runtime)
