# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alidns20150109 import models as alidns_20150109_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_custom_line_with_options(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        """
        @summary Adds a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: AddCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        """
        @summary Adds a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: AddCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_line(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        """
        @summary Adds a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: AddCustomLineRequest
        @return: AddCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    async def add_custom_line_async(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        """
        @summary Adds a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: AddCustomLineRequest
        @return: AddCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_line_with_options_async(request, runtime)

    def add_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        """
        @param request: AddDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_cache_domain_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        """
        @param request: AddDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_cache_domain(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        """
        @param request: AddDnsCacheDomainRequest
        @return: AddDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dns_cache_domain_with_options(request, runtime)

    async def add_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        """
        @param request: AddDnsCacheDomainRequest
        @return: AddDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_cache_domain_with_options_async(request, runtime)

    def add_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        """
        @summary Creates an access policy.
        
        @param request: AddDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        """
        @summary Creates an access policy.
        
        @param request: AddDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_access_strategy(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        """
        @summary Creates an access policy.
        
        @param request: AddDnsGtmAccessStrategyRequest
        @return: AddDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_access_strategy_with_options(request, runtime)

    async def add_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        """
        @summary Creates an access policy.
        
        @param request: AddDnsGtmAccessStrategyRequest
        @return: AddDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_access_strategy_with_options_async(request, runtime)

    def add_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_address_pool(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddDnsGtmAddressPoolRequest
        @return: AddDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_address_pool_with_options(request, runtime)

    async def add_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddDnsGtmAddressPoolRequest
        @return: AddDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_address_pool_with_options_async(request, runtime)

    def add_dns_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @description **\
        
        @param request: AddDnsGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @description **\
        
        @param request: AddDnsGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDnsGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_gtm_monitor(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @description **\
        
        @param request: AddDnsGtmMonitorRequest
        @return: AddDnsGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_monitor_with_options(request, runtime)

    async def add_dns_gtm_monitor_async(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @description **\
        
        @param request: AddDnsGtmMonitorRequest
        @return: AddDnsGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_monitor_with_options_async(request, runtime)

    def add_domain_with_options(
        self,
        request: alidns_20150109_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainResponse:
        """
        @summary Adds a domain name based on the specified parameters.
        
        @description For more information about how to check whether a domain name is valid, see
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm).
        
        @param request: AddDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainResponse:
        """
        @summary Adds a domain name based on the specified parameters.
        
        @description For more information about how to check whether a domain name is valid, see
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm).
        
        @param request: AddDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain(
        self,
        request: alidns_20150109_models.AddDomainRequest,
    ) -> alidns_20150109_models.AddDomainResponse:
        """
        @summary Adds a domain name based on the specified parameters.
        
        @description For more information about how to check whether a domain name is valid, see
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm).
        
        @param request: AddDomainRequest
        @return: AddDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: alidns_20150109_models.AddDomainRequest,
    ) -> alidns_20150109_models.AddDomainResponse:
        """
        @summary Adds a domain name based on the specified parameters.
        
        @description For more information about how to check whether a domain name is valid, see
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm).
        
        @param request: AddDomainRequest
        @return: AddDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def add_domain_backup_with_options(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        """
        @summary Creates a backup task for a domain name.
        
        @param request: AddDomainBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainBackup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_backup_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        """
        @summary Creates a backup task for a domain name.
        
        @param request: AddDomainBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainBackup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_backup(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        """
        @summary Creates a backup task for a domain name.
        
        @param request: AddDomainBackupRequest
        @return: AddDomainBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_backup_with_options(request, runtime)

    async def add_domain_backup_async(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        """
        @summary Creates a backup task for a domain name.
        
        @param request: AddDomainBackupRequest
        @return: AddDomainBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_backup_with_options_async(request, runtime)

    def add_domain_group_with_options(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        """
        @summary Creates a domain name group based on the specified parameters.
        
        @param request: AddDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        """
        @summary Creates a domain name group based on the specified parameters.
        
        @param request: AddDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_group(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        """
        @summary Creates a domain name group based on the specified parameters.
        
        @param request: AddDomainGroupRequest
        @return: AddDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_group_with_options(request, runtime)

    async def add_domain_group_async(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        """
        @summary Creates a domain name group based on the specified parameters.
        
        @param request: AddDomainGroupRequest
        @return: AddDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_group_with_options_async(request, runtime)

    def add_domain_record_with_options(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: AddDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: AddDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_record(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: AddDomainRecordRequest
        @return: AddDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_record_with_options(request, runtime)

    async def add_domain_record_async(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        """
        @summary Adds a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: AddDomainRecordRequest
        @return: AddDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_record_with_options_async(request, runtime)

    def add_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        """
        @param request: AddGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        """
        @param request: AddGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_access_strategy(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        """
        @param request: AddGtmAccessStrategyRequest
        @return: AddGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_access_strategy_with_options(request, runtime)

    async def add_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        """
        @param request: AddGtmAccessStrategyRequest
        @return: AddGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_access_strategy_with_options_async(request, runtime)

    def add_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_address_pool(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddGtmAddressPoolRequest
        @return: AddGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_address_pool_with_options(request, runtime)

    async def add_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        """
        @summary Creates an address pool.
        
        @param request: AddGtmAddressPoolRequest
        @return: AddGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_address_pool_with_options_async(request, runtime)

    def add_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @param request: AddGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @param request: AddGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_monitor(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @param request: AddGtmMonitorRequest
        @return: AddGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_monitor_with_options(request, runtime)

    async def add_gtm_monitor_async(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        """
        @summary Creates a health check task.
        
        @param request: AddGtmMonitorRequest
        @return: AddGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_monitor_with_options_async(request, runtime)

    def add_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        """
        @param request: AddGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        """
        @param request: AddGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        """
        @param request: AddGtmRecoveryPlanRequest
        @return: AddGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_recovery_plan_with_options(request, runtime)

    async def add_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        """
        @param request: AddGtmRecoveryPlanRequest
        @return: AddGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_recovery_plan_with_options_async(request, runtime)

    def bind_instance_domains_with_options(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        """
        @summary Binds one or more domain names to a paid Alibaba Cloud DNS instance.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call this API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call this API operation to bind only one domain name to the instance. However, if the instance is already bound to a domain name, you must unbind the original domain name from the instance and bind the desired domain name to the instance.
        
        @param request: BindInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.BindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        """
        @summary Binds one or more domain names to a paid Alibaba Cloud DNS instance.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call this API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call this API operation to bind only one domain name to the instance. However, if the instance is already bound to a domain name, you must unbind the original domain name from the instance and bind the desired domain name to the instance.
        
        @param request: BindInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.BindInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_instance_domains(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        """
        @summary Binds one or more domain names to a paid Alibaba Cloud DNS instance.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call this API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call this API operation to bind only one domain name to the instance. However, if the instance is already bound to a domain name, you must unbind the original domain name from the instance and bind the desired domain name to the instance.
        
        @param request: BindInstanceDomainsRequest
        @return: BindInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_instance_domains_with_options(request, runtime)

    async def bind_instance_domains_async(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        """
        @summary Binds one or more domain names to a paid Alibaba Cloud DNS instance.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call this API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call this API operation to bind only one domain name to the instance. However, if the instance is already bound to a domain name, you must unbind the original domain name from the instance and bind the desired domain name to the instance.
        
        @param request: BindInstanceDomainsRequest
        @return: BindInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_instance_domains_with_options_async(request, runtime)

    def change_domain_group_with_options(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        """
        @summary Moves a domain name from the original group to the new group based on the specified parameters.
        
        @description You can specify GroupId to move a domain name to a specific domain name group. You can move the domain name to the group that contains all domain names or the default group.
        
        @param request: ChangeDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        """
        @summary Moves a domain name from the original group to the new group based on the specified parameters.
        
        @description You can specify GroupId to move a domain name to a specific domain name group. You can move the domain name to the group that contains all domain names or the default group.
        
        @param request: ChangeDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_group(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        """
        @summary Moves a domain name from the original group to the new group based on the specified parameters.
        
        @description You can specify GroupId to move a domain name to a specific domain name group. You can move the domain name to the group that contains all domain names or the default group.
        
        @param request: ChangeDomainGroupRequest
        @return: ChangeDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_domain_group_with_options(request, runtime)

    async def change_domain_group_async(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        """
        @summary Moves a domain name from the original group to the new group based on the specified parameters.
        
        @description You can specify GroupId to move a domain name to a specific domain name group. You can move the domain name to the group that contains all domain names or the default group.
        
        @param request: ChangeDomainGroupRequest
        @return: ChangeDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_domain_group_with_options_async(request, runtime)

    def change_domain_of_dns_product_with_options(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        """
        @summary Changes the domain name bound to an Alibaba Cloud DNS instance.
        
        @description >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        
        @param request: ChangeDomainOfDnsProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainOfDnsProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_domain):
            query['NewDomain'] = request.new_domain
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainOfDnsProduct',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainOfDnsProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_domain_of_dns_product_with_options_async(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        """
        @summary Changes the domain name bound to an Alibaba Cloud DNS instance.
        
        @description >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        
        @param request: ChangeDomainOfDnsProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDomainOfDnsProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_domain):
            query['NewDomain'] = request.new_domain
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainOfDnsProduct',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainOfDnsProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_domain_of_dns_product(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        """
        @summary Changes the domain name bound to an Alibaba Cloud DNS instance.
        
        @description >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        
        @param request: ChangeDomainOfDnsProductRequest
        @return: ChangeDomainOfDnsProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_domain_of_dns_product_with_options(request, runtime)

    async def change_domain_of_dns_product_async(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        """
        @summary Changes the domain name bound to an Alibaba Cloud DNS instance.
        
        @description >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        
        @param request: ChangeDomainOfDnsProductRequest
        @return: ChangeDomainOfDnsProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_domain_of_dns_product_with_options_async(request, runtime)

    def copy_gtm_config_with_options(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        """
        @param request: CopyGtmConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyGtmConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copy_type):
            query['CopyType'] = request.copy_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyGtmConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CopyGtmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_gtm_config_with_options_async(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        """
        @param request: CopyGtmConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyGtmConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copy_type):
            query['CopyType'] = request.copy_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyGtmConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CopyGtmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_gtm_config(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        """
        @param request: CopyGtmConfigRequest
        @return: CopyGtmConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_gtm_config_with_options(request, runtime)

    async def copy_gtm_config_async(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        """
        @param request: CopyGtmConfigRequest
        @return: CopyGtmConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_gtm_config_with_options_async(request, runtime)

    def create_cloud_gtm_address_with_options(
        self,
        tmp_req: alidns_20150109_models.CreateCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmAddressResponse:
        """
        @param tmp_req: CreateCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.CreateCloudGtmAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.health_tasks):
            request.health_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not UtilClient.is_unset(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not UtilClient.is_unset(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_address_with_options_async(
        self,
        tmp_req: alidns_20150109_models.CreateCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmAddressResponse:
        """
        @param tmp_req: CreateCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.CreateCloudGtmAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.health_tasks):
            request.health_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not UtilClient.is_unset(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not UtilClient.is_unset(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_address(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressRequest,
    ) -> alidns_20150109_models.CreateCloudGtmAddressResponse:
        """
        @param request: CreateCloudGtmAddressRequest
        @return: CreateCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_gtm_address_with_options(request, runtime)

    async def create_cloud_gtm_address_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressRequest,
    ) -> alidns_20150109_models.CreateCloudGtmAddressResponse:
        """
        @param request: CreateCloudGtmAddressRequest
        @return: CreateCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_gtm_address_with_options_async(request, runtime)

    def create_cloud_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmAddressPoolResponse:
        """
        @param request: CreateCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmAddressPoolResponse:
        """
        @param request: CreateCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_address_pool(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.CreateCloudGtmAddressPoolResponse:
        """
        @param request: CreateCloudGtmAddressPoolRequest
        @return: CreateCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_gtm_address_pool_with_options(request, runtime)

    async def create_cloud_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.CreateCloudGtmAddressPoolResponse:
        """
        @param request: CreateCloudGtmAddressPoolRequest
        @return: CreateCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_gtm_address_pool_with_options_async(request, runtime)

    def create_cloud_gtm_instance_config_with_options(
        self,
        request: alidns_20150109_models.CreateCloudGtmInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmInstanceConfigResponse:
        """
        @param request: CreateCloudGtmInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not UtilClient.is_unset(request.schedule_rr_type):
            query['ScheduleRrType'] = request.schedule_rr_type
        if not UtilClient.is_unset(request.schedule_zone_mode):
            query['ScheduleZoneMode'] = request.schedule_zone_mode
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_instance_config_with_options_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmInstanceConfigResponse:
        """
        @param request: CreateCloudGtmInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not UtilClient.is_unset(request.schedule_rr_type):
            query['ScheduleRrType'] = request.schedule_rr_type
        if not UtilClient.is_unset(request.schedule_zone_mode):
            query['ScheduleZoneMode'] = request.schedule_zone_mode
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_instance_config(
        self,
        request: alidns_20150109_models.CreateCloudGtmInstanceConfigRequest,
    ) -> alidns_20150109_models.CreateCloudGtmInstanceConfigResponse:
        """
        @param request: CreateCloudGtmInstanceConfigRequest
        @return: CreateCloudGtmInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_gtm_instance_config_with_options(request, runtime)

    async def create_cloud_gtm_instance_config_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmInstanceConfigRequest,
    ) -> alidns_20150109_models.CreateCloudGtmInstanceConfigResponse:
        """
        @param request: CreateCloudGtmInstanceConfigRequest
        @return: CreateCloudGtmInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_gtm_instance_config_with_options_async(request, runtime)

    def create_cloud_gtm_monitor_template_with_options(
        self,
        tmp_req: alidns_20150109_models.CreateCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse:
        """
        @param tmp_req: CreateCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.CreateCloudGtmMonitorTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_gtm_monitor_template_with_options_async(
        self,
        tmp_req: alidns_20150109_models.CreateCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse:
        """
        @param tmp_req: CreateCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.CreateCloudGtmMonitorTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_gtm_monitor_template(
        self,
        request: alidns_20150109_models.CreateCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse:
        """
        @param request: CreateCloudGtmMonitorTemplateRequest
        @return: CreateCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_gtm_monitor_template_with_options(request, runtime)

    async def create_cloud_gtm_monitor_template_async(
        self,
        request: alidns_20150109_models.CreateCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.CreateCloudGtmMonitorTemplateResponse:
        """
        @param request: CreateCloudGtmMonitorTemplateRequest
        @return: CreateCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def create_pdns_app_key_with_options(
        self,
        request: alidns_20150109_models.CreatePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreatePdnsAppKeyResponse:
        """
        @summary 创建公共DNS AppKey
        
        @param request: CreatePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdns_app_key_with_options_async(
        self,
        request: alidns_20150109_models.CreatePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreatePdnsAppKeyResponse:
        """
        @summary 创建公共DNS AppKey
        
        @param request: CreatePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdns_app_key(
        self,
        request: alidns_20150109_models.CreatePdnsAppKeyRequest,
    ) -> alidns_20150109_models.CreatePdnsAppKeyResponse:
        """
        @summary 创建公共DNS AppKey
        
        @param request: CreatePdnsAppKeyRequest
        @return: CreatePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pdns_app_key_with_options(request, runtime)

    async def create_pdns_app_key_async(
        self,
        request: alidns_20150109_models.CreatePdnsAppKeyRequest,
    ) -> alidns_20150109_models.CreatePdnsAppKeyResponse:
        """
        @summary 创建公共DNS AppKey
        
        @param request: CreatePdnsAppKeyRequest
        @return: CreatePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pdns_app_key_with_options_async(request, runtime)

    def create_pdns_udp_ip_segment_with_options(
        self,
        request: alidns_20150109_models.CreatePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreatePdnsUdpIpSegmentResponse:
        """
        @summary 创建公共DNS Udp Ip地址段
        
        @param request: CreatePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdns_udp_ip_segment_with_options_async(
        self,
        request: alidns_20150109_models.CreatePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CreatePdnsUdpIpSegmentResponse:
        """
        @summary 创建公共DNS Udp Ip地址段
        
        @param request: CreatePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdns_udp_ip_segment(
        self,
        request: alidns_20150109_models.CreatePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.CreatePdnsUdpIpSegmentResponse:
        """
        @summary 创建公共DNS Udp Ip地址段
        
        @param request: CreatePdnsUdpIpSegmentRequest
        @return: CreatePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pdns_udp_ip_segment_with_options(request, runtime)

    async def create_pdns_udp_ip_segment_async(
        self,
        request: alidns_20150109_models.CreatePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.CreatePdnsUdpIpSegmentResponse:
        """
        @summary 创建公共DNS Udp Ip地址段
        
        @param request: CreatePdnsUdpIpSegmentRequest
        @return: CreatePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pdns_udp_ip_segment_with_options_async(request, runtime)

    def delete_cloud_gtm_address_with_options(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressResponse:
        """
        @param request: DeleteCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_address_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressResponse:
        """
        @param request: DeleteCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_address(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressResponse:
        """
        @param request: DeleteCloudGtmAddressRequest
        @return: DeleteCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_gtm_address_with_options(request, runtime)

    async def delete_cloud_gtm_address_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressResponse:
        """
        @param request: DeleteCloudGtmAddressRequest
        @return: DeleteCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_gtm_address_with_options_async(request, runtime)

    def delete_cloud_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressPoolResponse:
        """
        @param request: DeleteCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressPoolResponse:
        """
        @param request: DeleteCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_address_pool(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressPoolResponse:
        """
        @param request: DeleteCloudGtmAddressPoolRequest
        @return: DeleteCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_gtm_address_pool_with_options(request, runtime)

    async def delete_cloud_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmAddressPoolResponse:
        """
        @param request: DeleteCloudGtmAddressPoolRequest
        @return: DeleteCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_gtm_address_pool_with_options_async(request, runtime)

    def delete_cloud_gtm_instance_config_with_options(
        self,
        request: alidns_20150109_models.DeleteCloudGtmInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse:
        """
        @param request: DeleteCloudGtmInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_instance_config_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse:
        """
        @param request: DeleteCloudGtmInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_instance_config(
        self,
        request: alidns_20150109_models.DeleteCloudGtmInstanceConfigRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse:
        """
        @param request: DeleteCloudGtmInstanceConfigRequest
        @return: DeleteCloudGtmInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_gtm_instance_config_with_options(request, runtime)

    async def delete_cloud_gtm_instance_config_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmInstanceConfigRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmInstanceConfigResponse:
        """
        @param request: DeleteCloudGtmInstanceConfigRequest
        @return: DeleteCloudGtmInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_gtm_instance_config_with_options_async(request, runtime)

    def delete_cloud_gtm_monitor_template_with_options(
        self,
        request: alidns_20150109_models.DeleteCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse:
        """
        @param request: DeleteCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_gtm_monitor_template_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse:
        """
        @param request: DeleteCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_gtm_monitor_template(
        self,
        request: alidns_20150109_models.DeleteCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse:
        """
        @param request: DeleteCloudGtmMonitorTemplateRequest
        @return: DeleteCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_gtm_monitor_template_with_options(request, runtime)

    async def delete_cloud_gtm_monitor_template_async(
        self,
        request: alidns_20150109_models.DeleteCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.DeleteCloudGtmMonitorTemplateResponse:
        """
        @param request: DeleteCloudGtmMonitorTemplateRequest
        @return: DeleteCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def delete_custom_lines_with_options(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        """
        @summary Deletes multiple custom lines at a time.
        
        @param request: DeleteCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_ids):
            query['LineIds'] = request.line_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_lines_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        """
        @summary Deletes multiple custom lines at a time.
        
        @param request: DeleteCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_ids):
            query['LineIds'] = request.line_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_lines(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        """
        @summary Deletes multiple custom lines at a time.
        
        @param request: DeleteCustomLinesRequest
        @return: DeleteCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_lines_with_options(request, runtime)

    async def delete_custom_lines_async(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        """
        @summary Deletes multiple custom lines at a time.
        
        @param request: DeleteCustomLinesRequest
        @return: DeleteCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_lines_with_options_async(request, runtime)

    def delete_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        """
        @param request: DeleteDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_cache_domain_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        """
        @param request: DeleteDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_cache_domain(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        """
        @param request: DeleteDnsCacheDomainRequest
        @return: DeleteDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_cache_domain_with_options(request, runtime)

    async def delete_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        """
        @param request: DeleteDnsCacheDomainRequest
        @return: DeleteDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_cache_domain_with_options_async(request, runtime)

    def delete_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        """
        @param request: DeleteDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        """
        @param request: DeleteDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_gtm_access_strategy(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        """
        @param request: DeleteDnsGtmAccessStrategyRequest
        @return: DeleteDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_access_strategy_with_options(request, runtime)

    async def delete_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        """
        @param request: DeleteDnsGtmAccessStrategyRequest
        @return: DeleteDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_gtm_access_strategy_with_options_async(request, runtime)

    def delete_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        """
        @param request: DeleteDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        """
        @param request: DeleteDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_gtm_address_pool(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        """
        @param request: DeleteDnsGtmAddressPoolRequest
        @return: DeleteDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_address_pool_with_options(request, runtime)

    async def delete_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        """
        @param request: DeleteDnsGtmAddressPoolRequest
        @return: DeleteDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_gtm_address_pool_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name based on the specified parameters.
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name based on the specified parameters.
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name based on the specified parameters.
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        """
        @summary Deletes a domain name based on the specified parameters.
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_group_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        """
        @summary Deletes a domain name group. After you delete the domain name group, the domain names in the group are moved to the default group.
        
        @description >  The default group cannot be deleted.
        
        @param request: DeleteDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        """
        @summary Deletes a domain name group. After you delete the domain name group, the domain names in the group are moved to the default group.
        
        @description >  The default group cannot be deleted.
        
        @param request: DeleteDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_group(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        """
        @summary Deletes a domain name group. After you delete the domain name group, the domain names in the group are moved to the default group.
        
        @description >  The default group cannot be deleted.
        
        @param request: DeleteDomainGroupRequest
        @return: DeleteDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        """
        @summary Deletes a domain name group. After you delete the domain name group, the domain names in the group are moved to the default group.
        
        @description >  The default group cannot be deleted.
        
        @param request: DeleteDomainGroupRequest
        @return: DeleteDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_domain_record_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: DeleteDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: DeleteDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_record(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: DeleteDomainRecordRequest
        @return: DeleteDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_record_with_options(request, runtime)

    async def delete_domain_record_async(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        """
        @summary Deletes a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: DeleteDomainRecordRequest
        @return: DeleteDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_record_with_options_async(request, runtime)

    def delete_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        """
        @param request: DeleteGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        """
        @param request: DeleteGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_access_strategy(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        """
        @param request: DeleteGtmAccessStrategyRequest
        @return: DeleteGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_access_strategy_with_options(request, runtime)

    async def delete_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        """
        @param request: DeleteGtmAccessStrategyRequest
        @return: DeleteGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_access_strategy_with_options_async(request, runtime)

    def delete_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        """
        @param request: DeleteGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        """
        @param request: DeleteGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_address_pool(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        """
        @param request: DeleteGtmAddressPoolRequest
        @return: DeleteGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_address_pool_with_options(request, runtime)

    async def delete_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        """
        @param request: DeleteGtmAddressPoolRequest
        @return: DeleteGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_address_pool_with_options_async(request, runtime)

    def delete_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        """
        @param request: DeleteGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        """
        @param request: DeleteGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        """
        @param request: DeleteGtmRecoveryPlanRequest
        @return: DeleteGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_recovery_plan_with_options(request, runtime)

    async def delete_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        """
        @param request: DeleteGtmRecoveryPlanRequest
        @return: DeleteGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_recovery_plan_with_options_async(request, runtime)

    def delete_sub_domain_records_with_options(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        """
        @description If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        
        @param request: DeleteSubDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        """
        @description If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        
        @param request: DeleteSubDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteSubDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub_domain_records(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        """
        @description If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        
        @param request: DeleteSubDomainRecordsRequest
        @return: DeleteSubDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_domain_records_with_options(request, runtime)

    async def delete_sub_domain_records_async(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        """
        @description If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        
        @param request: DeleteSubDomainRecordsRequest
        @return: DeleteSubDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sub_domain_records_with_options_async(request, runtime)

    def describe_batch_result_count_with_options(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        """
        @param request: DescribeBatchResultCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchResultCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultCount',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_result_count_with_options_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        """
        @param request: DescribeBatchResultCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchResultCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultCount',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_result_count(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        """
        @param request: DescribeBatchResultCountRequest
        @return: DescribeBatchResultCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_count_with_options(request, runtime)

    async def describe_batch_result_count_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        """
        @param request: DescribeBatchResultCountRequest
        @return: DescribeBatchResultCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_result_count_with_options_async(request, runtime)

    def describe_batch_result_detail_with_options(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        """
        @summary Queries the detailed results of a batch operation task.
        
        @description Before you call this operation, make sure that the batch operation task is complete.
        
        @param request: DescribeBatchResultDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchResultDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultDetail',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_result_detail_with_options_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        """
        @summary Queries the detailed results of a batch operation task.
        
        @description Before you call this operation, make sure that the batch operation task is complete.
        
        @param request: DescribeBatchResultDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchResultDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultDetail',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_result_detail(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        """
        @summary Queries the detailed results of a batch operation task.
        
        @description Before you call this operation, make sure that the batch operation task is complete.
        
        @param request: DescribeBatchResultDetailRequest
        @return: DescribeBatchResultDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_detail_with_options(request, runtime)

    async def describe_batch_result_detail_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        """
        @summary Queries the detailed results of a batch operation task.
        
        @description Before you call this operation, make sure that the batch operation task is complete.
        
        @param request: DescribeBatchResultDetailRequest
        @return: DescribeBatchResultDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_result_detail_with_options_async(request, runtime)

    def describe_cloud_gtm_address_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressResponse:
        """
        @param request: DescribeCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressResponse:
        """
        @param request: DescribeCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressResponse:
        """
        @param request: DescribeCloudGtmAddressRequest
        @return: DescribeCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_address_with_options(request, runtime)

    async def describe_cloud_gtm_address_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressResponse:
        """
        @param request: DescribeCloudGtmAddressRequest
        @return: DescribeCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_address_with_options_async(request, runtime)

    def describe_cloud_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolResponse:
        """
        @param request: DescribeCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolResponse:
        """
        @param request: DescribeCloudGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_pool(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolResponse:
        """
        @param request: DescribeCloudGtmAddressPoolRequest
        @return: DescribeCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_address_pool_with_options(request, runtime)

    async def describe_cloud_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolResponse:
        """
        @param request: DescribeCloudGtmAddressPoolRequest
        @return: DescribeCloudGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_address_pool_with_options_async(request, runtime)

    def describe_cloud_gtm_address_pool_reference_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressPoolReferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressPoolReferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressPoolReference',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_pool_reference_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressPoolReferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressPoolReferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressPoolReference',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_pool_reference(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressPoolReferenceRequest
        @return: DescribeCloudGtmAddressPoolReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_address_pool_reference_with_options(request, runtime)

    async def describe_cloud_gtm_address_pool_reference_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressPoolReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressPoolReferenceRequest
        @return: DescribeCloudGtmAddressPoolReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_address_pool_reference_with_options_async(request, runtime)

    def describe_cloud_gtm_address_reference_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressReferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressReferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressReferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressReference',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_address_reference_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressReferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressReferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmAddressReferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmAddressReference',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_address_reference(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressReferenceRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressReferenceRequest
        @return: DescribeCloudGtmAddressReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_address_reference_with_options(request, runtime)

    async def describe_cloud_gtm_address_reference_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmAddressReferenceRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmAddressReferenceResponse:
        """
        @param request: DescribeCloudGtmAddressReferenceRequest
        @return: DescribeCloudGtmAddressReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_address_reference_with_options_async(request, runtime)

    def describe_cloud_gtm_global_alert_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmGlobalAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse:
        """
        @param request: DescribeCloudGtmGlobalAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmGlobalAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmGlobalAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_global_alert_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmGlobalAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse:
        """
        @param request: DescribeCloudGtmGlobalAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmGlobalAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmGlobalAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_global_alert(
        self,
        request: alidns_20150109_models.DescribeCloudGtmGlobalAlertRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse:
        """
        @param request: DescribeCloudGtmGlobalAlertRequest
        @return: DescribeCloudGtmGlobalAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_global_alert_with_options(request, runtime)

    async def describe_cloud_gtm_global_alert_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmGlobalAlertRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmGlobalAlertResponse:
        """
        @param request: DescribeCloudGtmGlobalAlertRequest
        @return: DescribeCloudGtmGlobalAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_global_alert_with_options_async(request, runtime)

    def describe_cloud_gtm_instance_config_alert_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmInstanceConfigAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmInstanceConfigAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_instance_config_alert_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmInstanceConfigAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmInstanceConfigAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_instance_config_alert(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigAlertRequest
        @return: DescribeCloudGtmInstanceConfigAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_instance_config_alert_with_options(request, runtime)

    async def describe_cloud_gtm_instance_config_alert_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigAlertResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigAlertRequest
        @return: DescribeCloudGtmInstanceConfigAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_instance_config_alert_with_options_async(request, runtime)

    def describe_cloud_gtm_instance_config_full_info_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigFullInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmInstanceConfigFullInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmInstanceConfigFullInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_instance_config_full_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigFullInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmInstanceConfigFullInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmInstanceConfigFullInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_instance_config_full_info(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigFullInfoRequest
        @return: DescribeCloudGtmInstanceConfigFullInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_instance_config_full_info_with_options(request, runtime)

    async def describe_cloud_gtm_instance_config_full_info_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmInstanceConfigFullInfoResponse:
        """
        @param request: DescribeCloudGtmInstanceConfigFullInfoRequest
        @return: DescribeCloudGtmInstanceConfigFullInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_instance_config_full_info_with_options_async(request, runtime)

    def describe_cloud_gtm_monitor_template_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse:
        """
        @param request: DescribeCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_monitor_template_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse:
        """
        @param request: DescribeCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_monitor_template(
        self,
        request: alidns_20150109_models.DescribeCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse:
        """
        @param request: DescribeCloudGtmMonitorTemplateRequest
        @return: DescribeCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_monitor_template_with_options(request, runtime)

    async def describe_cloud_gtm_monitor_template_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmMonitorTemplateResponse:
        """
        @param request: DescribeCloudGtmMonitorTemplateRequest
        @return: DescribeCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def describe_cloud_gtm_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeCloudGtmSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmSummaryResponse:
        """
        @param request: DescribeCloudGtmSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmSummaryResponse:
        """
        @param request: DescribeCloudGtmSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudGtmSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_summary(
        self,
        request: alidns_20150109_models.DescribeCloudGtmSummaryRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmSummaryResponse:
        """
        @param request: DescribeCloudGtmSummaryRequest
        @return: DescribeCloudGtmSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_summary_with_options(request, runtime)

    async def describe_cloud_gtm_summary_async(
        self,
        request: alidns_20150109_models.DescribeCloudGtmSummaryRequest,
    ) -> alidns_20150109_models.DescribeCloudGtmSummaryResponse:
        """
        @param request: DescribeCloudGtmSummaryRequest
        @return: DescribeCloudGtmSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_summary_with_options_async(request, runtime)

    def describe_cloud_gtm_system_lines_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmSystemLinesResponse:
        """
        @param request: DescribeCloudGtmSystemLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmSystemLinesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudGtmSystemLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmSystemLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_gtm_system_lines_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCloudGtmSystemLinesResponse:
        """
        @param request: DescribeCloudGtmSystemLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudGtmSystemLinesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudGtmSystemLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCloudGtmSystemLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_gtm_system_lines(self) -> alidns_20150109_models.DescribeCloudGtmSystemLinesResponse:
        """
        @return: DescribeCloudGtmSystemLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_gtm_system_lines_with_options(runtime)

    async def describe_cloud_gtm_system_lines_async(self) -> alidns_20150109_models.DescribeCloudGtmSystemLinesResponse:
        """
        @return: DescribeCloudGtmSystemLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_gtm_system_lines_with_options_async(runtime)

    def describe_custom_line_with_options(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        """
        @summary Queries a custom line.
        
        @param request: DescribeCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        """
        @summary Queries a custom line.
        
        @param request: DescribeCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_line(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        """
        @summary Queries a custom line.
        
        @param request: DescribeCustomLineRequest
        @return: DescribeCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_line_with_options(request, runtime)

    async def describe_custom_line_async(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        """
        @summary Queries a custom line.
        
        @param request: DescribeCustomLineRequest
        @return: DescribeCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_line_with_options_async(request, runtime)

    def describe_custom_lines_with_options(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        """
        @summary Queries custom lines.
        
        @param request: DescribeCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_lines_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        """
        @summary Queries custom lines.
        
        @param request: DescribeCustomLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_lines(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        """
        @summary Queries custom lines.
        
        @param request: DescribeCustomLinesRequest
        @return: DescribeCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    async def describe_custom_lines_async(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        """
        @summary Queries custom lines.
        
        @param request: DescribeCustomLinesRequest
        @return: DescribeCustomLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_lines_with_options_async(request, runtime)

    def describe_dnsslbsub_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        """
        @summary Queries the subdomains for which weighted round-robin is enabled based on the specified parameters.
        
        @param request: DescribeDNSSLBSubDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDNSSLBSubDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDNSSLBSubDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDNSSLBSubDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dnsslbsub_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        """
        @summary Queries the subdomains for which weighted round-robin is enabled based on the specified parameters.
        
        @param request: DescribeDNSSLBSubDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDNSSLBSubDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDNSSLBSubDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDNSSLBSubDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dnsslbsub_domains(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        """
        @summary Queries the subdomains for which weighted round-robin is enabled based on the specified parameters.
        
        @param request: DescribeDNSSLBSubDomainsRequest
        @return: DescribeDNSSLBSubDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dnsslbsub_domains_with_options(request, runtime)

    async def describe_dnsslbsub_domains_async(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        """
        @summary Queries the subdomains for which weighted round-robin is enabled based on the specified parameters.
        
        @param request: DescribeDNSSLBSubDomainsRequest
        @return: DescribeDNSSLBSubDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dnsslbsub_domains_with_options_async(request, runtime)

    def describe_dns_cache_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        """
        @param request: DescribeDnsCacheDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsCacheDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsCacheDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsCacheDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_cache_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        """
        @param request: DescribeDnsCacheDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsCacheDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsCacheDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsCacheDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_cache_domains(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        """
        @param request: DescribeDnsCacheDomainsRequest
        @return: DescribeDnsCacheDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_cache_domains_with_options(request, runtime)

    async def describe_dns_cache_domains_async(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        """
        @param request: DescribeDnsCacheDomainsRequest
        @return: DescribeDnsCacheDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_cache_domains_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategies_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        """
        @summary Queries access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategies_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        """
        @summary Queries access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategies(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        """
        @summary Queries access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategiesRequest
        @return: DescribeDnsGtmAccessStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategies_with_options(request, runtime)

    async def describe_dns_gtm_access_strategies_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        """
        @summary Queries access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategiesRequest
        @return: DescribeDnsGtmAccessStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategies_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        """
        @summary Queries detailed information about an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        """
        @summary Queries detailed information about an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        """
        @summary Queries detailed information about an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyRequest
        @return: DescribeDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        """
        @summary Queries detailed information about an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyRequest
        @return: DescribeDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the available configurations of an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategyAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_access_strategy_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the available configurations of an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAccessStrategyAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy_available_config(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the available configurations of an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyAvailableConfigRequest
        @return: DescribeDnsGtmAccessStrategyAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the available configurations of an access policy of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAccessStrategyAvailableConfigRequest
        @return: DescribeDnsGtmAccessStrategyAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_addr_attribute_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        """
        @param request: DescribeDnsGtmAddrAttributeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAddrAttributeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addrs):
            query['Addrs'] = request.addrs
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddrAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_addr_attribute_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        """
        @param request: DescribeDnsGtmAddrAttributeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAddrAttributeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addrs):
            query['Addrs'] = request.addrs
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddrAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_addr_attribute_info(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        """
        @param request: DescribeDnsGtmAddrAttributeInfoRequest
        @return: DescribeDnsGtmAddrAttributeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_addr_attribute_info_with_options(request, runtime)

    async def describe_dns_gtm_addr_attribute_info_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        """
        @param request: DescribeDnsGtmAddrAttributeInfoRequest
        @return: DescribeDnsGtmAddrAttributeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_addr_attribute_info_with_options_async(request, runtime)

    def describe_dns_gtm_address_pool_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        """
        @summary Queries the available configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAddressPoolAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAddressPoolAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddressPoolAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_address_pool_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        """
        @summary Queries the available configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAddressPoolAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAddressPoolAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddressPoolAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_address_pool_available_config(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        """
        @summary Queries the available configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAddressPoolAvailableConfigRequest
        @return: DescribeDnsGtmAddressPoolAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_address_pool_available_config_with_options(request, runtime)

    async def describe_dns_gtm_address_pool_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        """
        @summary Queries the available configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmAddressPoolAvailableConfigRequest
        @return: DescribeDnsGtmAddressPoolAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_address_pool_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_available_alert_group_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeDnsGtmAvailableAlertGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAvailableAlertGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_available_alert_group_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeDnsGtmAvailableAlertGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmAvailableAlertGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_available_alert_group(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeDnsGtmAvailableAlertGroupRequest
        @return: DescribeDnsGtmAvailableAlertGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_available_alert_group_with_options(request, runtime)

    async def describe_dns_gtm_available_alert_group_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeDnsGtmAvailableAlertGroupRequest
        @return: DescribeDnsGtmAvailableAlertGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_dns_gtm_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        """
        @summary Queries detailed information about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        """
        @summary Queries detailed information about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        """
        @summary Queries detailed information about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceRequest
        @return: DescribeDnsGtmInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_with_options(request, runtime)

    async def describe_dns_gtm_instance_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        """
        @summary Queries detailed information about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceRequest
        @return: DescribeDnsGtmInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pool_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        """
        @summary Queries detailed information about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        """
        @summary Queries detailed information about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pool(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        """
        @summary Queries detailed information about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolRequest
        @return: DescribeDnsGtmInstanceAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pool_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        """
        @summary Queries detailed information about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolRequest
        @return: DescribeDnsGtmInstanceAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pools_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        """
        @summary Queries the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        """
        @summary Queries the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pools(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        """
        @summary Queries the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolsRequest
        @return: DescribeDnsGtmInstanceAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pools_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        """
        @summary Queries the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceAddressPoolsRequest
        @return: DescribeDnsGtmInstanceAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_dns_gtm_instance_status_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        """
        @summary Queries the status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_status_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        """
        @summary Queries the status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_status(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        """
        @summary Queries the status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceStatusRequest
        @return: DescribeDnsGtmInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_status_with_options(request, runtime)

    async def describe_dns_gtm_instance_status_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        """
        @summary Queries the status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceStatusRequest
        @return: DescribeDnsGtmInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_status_with_options_async(request, runtime)

    def describe_dns_gtm_instance_system_cname_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        """
        @summary Queries the CNAME domain name assigned by the system for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceSystemCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceSystemCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instance_system_cname_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        """
        @summary Queries the CNAME domain name assigned by the system for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceSystemCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstanceSystemCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instance_system_cname(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        """
        @summary Queries the CNAME domain name assigned by the system for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceSystemCnameRequest
        @return: DescribeDnsGtmInstanceSystemCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_dns_gtm_instance_system_cname_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        """
        @summary Queries the CNAME domain name assigned by the system for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmInstanceSystemCnameRequest
        @return: DescribeDnsGtmInstanceSystemCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_dns_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        """
        @param request: DescribeDnsGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        """
        @param request: DescribeDnsGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_instances(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        """
        @param request: DescribeDnsGtmInstancesRequest
        @return: DescribeDnsGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instances_with_options(request, runtime)

    async def describe_dns_gtm_instances_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        """
        @param request: DescribeDnsGtmInstancesRequest
        @return: DescribeDnsGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instances_with_options_async(request, runtime)

    def describe_dns_gtm_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        """
        @summary Queries operation logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        """
        @summary Queries operation logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_logs(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        """
        @summary Queries operation logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmLogsRequest
        @return: DescribeDnsGtmLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_logs_with_options(request, runtime)

    async def describe_dns_gtm_logs_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        """
        @summary Queries operation logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmLogsRequest
        @return: DescribeDnsGtmLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_logs_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeDnsGtmMonitorAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmMonitorAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_monitor_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeDnsGtmMonitorAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmMonitorAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_monitor_available_config(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeDnsGtmMonitorAvailableConfigRequest
        @return: DescribeDnsGtmMonitorAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeDnsGtmMonitorAvailableConfigRequest
        @return: DescribeDnsGtmMonitorAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        """
        @summary Queries the health check configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmMonitorConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmMonitorConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_gtm_monitor_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        """
        @summary Queries the health check configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmMonitorConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsGtmMonitorConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_gtm_monitor_config(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        """
        @summary Queries the health check configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmMonitorConfigRequest
        @return: DescribeDnsGtmMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        """
        @summary Queries the health check configurations of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeDnsGtmMonitorConfigRequest
        @return: DescribeDnsGtmMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_monitor_config_with_options_async(request, runtime)

    def describe_dns_product_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        """
        @summary Queries the details about a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @param request: DescribeDnsProductInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsProductInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_product_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        """
        @summary Queries the details about a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @param request: DescribeDnsProductInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsProductInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_product_instance(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        """
        @summary Queries the details about a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @param request: DescribeDnsProductInstanceRequest
        @return: DescribeDnsProductInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instance_with_options(request, runtime)

    async def describe_dns_product_instance_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        """
        @summary Queries the details about a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @param request: DescribeDnsProductInstanceRequest
        @return: DescribeDnsProductInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_product_instance_with_options_async(request, runtime)

    def describe_dns_product_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        """
        @summary Calls the DescribeDnsProductInstances operation to query the list of paid Alibaba Cloud DNS instances based on input parameters.
        
        @description >  If the response parameters of an Alibaba Cloud DNS instance do not contain domain names, no domain names are bound to the instance.
        
        @param request: DescribeDnsProductInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsProductInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_product_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        """
        @summary Calls the DescribeDnsProductInstances operation to query the list of paid Alibaba Cloud DNS instances based on input parameters.
        
        @description >  If the response parameters of an Alibaba Cloud DNS instance do not contain domain names, no domain names are bound to the instance.
        
        @param request: DescribeDnsProductInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDnsProductInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_product_instances(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        """
        @summary Calls the DescribeDnsProductInstances operation to query the list of paid Alibaba Cloud DNS instances based on input parameters.
        
        @description >  If the response parameters of an Alibaba Cloud DNS instance do not contain domain names, no domain names are bound to the instance.
        
        @param request: DescribeDnsProductInstancesRequest
        @return: DescribeDnsProductInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instances_with_options(request, runtime)

    async def describe_dns_product_instances_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        """
        @summary Calls the DescribeDnsProductInstances operation to query the list of paid Alibaba Cloud DNS instances based on input parameters.
        
        @description >  If the response parameters of an Alibaba Cloud DNS instance do not contain domain names, no domain names are bound to the instance.
        
        @param request: DescribeDnsProductInstancesRequest
        @return: DescribeDnsProductInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_product_instances_with_options_async(request, runtime)

    def describe_doh_account_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        """
        @param request: DescribeDohAccountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohAccountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohAccountStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohAccountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_account_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        """
        @param request: DescribeDohAccountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohAccountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohAccountStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohAccountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_account_statistics(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        """
        @param request: DescribeDohAccountStatisticsRequest
        @return: DescribeDohAccountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_account_statistics_with_options(request, runtime)

    async def describe_doh_account_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        """
        @param request: DescribeDohAccountStatisticsRequest
        @return: DescribeDohAccountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_account_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        """
        @param request: DescribeDohDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        """
        @param request: DescribeDohDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_domain_statistics(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        """
        @param request: DescribeDohDomainStatisticsRequest
        @return: DescribeDohDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_with_options(request, runtime)

    async def describe_doh_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        """
        @param request: DescribeDohDomainStatisticsRequest
        @return: DescribeDohDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_domain_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_domain_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohDomainStatisticsSummaryRequest
        @return: DescribeDohDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohDomainStatisticsSummaryRequest
        @return: DescribeDohDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        """
        @param request: DescribeDohSubDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohSubDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_sub_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        """
        @param request: DescribeDohSubDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohSubDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        """
        @param request: DescribeDohSubDomainStatisticsRequest
        @return: DescribeDohSubDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        """
        @param request: DescribeDohSubDomainStatisticsRequest
        @return: DescribeDohSubDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohSubDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohSubDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_sub_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohSubDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohSubDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohSubDomainStatisticsSummaryRequest
        @return: DescribeDohSubDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        """
        @param request: DescribeDohSubDomainStatisticsSummaryRequest
        @return: DescribeDohSubDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_user_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        """
        @summary Queries the numbers of accessed domains and subdomains by using DNS over HTTPS (DoH).
        
        @param request: DescribeDohUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doh_user_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        """
        @summary Queries the numbers of accessed domains and subdomains by using DNS over HTTPS (DoH).
        
        @param request: DescribeDohUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDohUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doh_user_info(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        """
        @summary Queries the numbers of accessed domains and subdomains by using DNS over HTTPS (DoH).
        
        @param request: DescribeDohUserInfoRequest
        @return: DescribeDohUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_user_info_with_options(request, runtime)

    async def describe_doh_user_info_async(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        """
        @summary Queries the numbers of accessed domains and subdomains by using DNS over HTTPS (DoH).
        
        @param request: DescribeDohUserInfoRequest
        @return: DescribeDohUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_user_info_with_options_async(request, runtime)

    def describe_domain_dnssec_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        """
        @summary Queries the Domain Name System Security Extensions (DNSSEC) configurations of a domain name based on the specified parameters.
        
        @param request: DescribeDomainDnssecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDnssecInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDnssecInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainDnssecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_dnssec_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        """
        @summary Queries the Domain Name System Security Extensions (DNSSEC) configurations of a domain name based on the specified parameters.
        
        @param request: DescribeDomainDnssecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDnssecInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDnssecInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainDnssecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_dnssec_info(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        """
        @summary Queries the Domain Name System Security Extensions (DNSSEC) configurations of a domain name based on the specified parameters.
        
        @param request: DescribeDomainDnssecInfoRequest
        @return: DescribeDomainDnssecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_dnssec_info_with_options(request, runtime)

    async def describe_domain_dnssec_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        """
        @summary Queries the Domain Name System Security Extensions (DNSSEC) configurations of a domain name based on the specified parameters.
        
        @param request: DescribeDomainDnssecInfoRequest
        @return: DescribeDomainDnssecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_dnssec_info_with_options_async(request, runtime)

    def describe_domain_groups_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        """
        @summary Queries all domain name groups based on the specified parameters.
        
        @param request: DescribeDomainGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_groups_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        """
        @summary Queries all domain name groups based on the specified parameters.
        
        @param request: DescribeDomainGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_groups(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        """
        @summary Queries all domain name groups based on the specified parameters.
        
        @param request: DescribeDomainGroupsRequest
        @return: DescribeDomainGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_groups_with_options(request, runtime)

    async def describe_domain_groups_async(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        """
        @summary Queries all domain name groups based on the specified parameters.
        
        @param request: DescribeDomainGroupsRequest
        @return: DescribeDomainGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_groups_with_options_async(request, runtime)

    def describe_domain_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        """
        @summary Queries the information about a domain name based on specified parameters.
        
        @description In this example, the domain name is bound to an instance of Alibaba Cloud DNS Enterprise Ultimate Edition. For more information about valid Domain Name System (DNS) request lines, see the return values of the RecordLines parameter.
        
        @param request: DescribeDomainInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        """
        @summary Queries the information about a domain name based on specified parameters.
        
        @description In this example, the domain name is bound to an instance of Alibaba Cloud DNS Enterprise Ultimate Edition. For more information about valid Domain Name System (DNS) request lines, see the return values of the RecordLines parameter.
        
        @param request: DescribeDomainInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_info(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        """
        @summary Queries the information about a domain name based on specified parameters.
        
        @description In this example, the domain name is bound to an instance of Alibaba Cloud DNS Enterprise Ultimate Edition. For more information about valid Domain Name System (DNS) request lines, see the return values of the RecordLines parameter.
        
        @param request: DescribeDomainInfoRequest
        @return: DescribeDomainInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_info_with_options(request, runtime)

    async def describe_domain_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        """
        @summary Queries the information about a domain name based on specified parameters.
        
        @description In this example, the domain name is bound to an instance of Alibaba Cloud DNS Enterprise Ultimate Edition. For more information about valid Domain Name System (DNS) request lines, see the return values of the RecordLines parameter.
        
        @param request: DescribeDomainInfoRequest
        @return: DescribeDomainInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_info_with_options_async(request, runtime)

    def describe_domain_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        """
        @summary Queries the operation logs of domain names based on the specified parameters.
        
        @param request: DescribeDomainLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        """
        @summary Queries the operation logs of domain names based on the specified parameters.
        
        @param request: DescribeDomainLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_logs(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        """
        @summary Queries the operation logs of domain names based on the specified parameters.
        
        @param request: DescribeDomainLogsRequest
        @return: DescribeDomainLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_logs_with_options(request, runtime)

    async def describe_domain_logs_async(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        """
        @summary Queries the operation logs of domain names based on the specified parameters.
        
        @param request: DescribeDomainLogsRequest
        @return: DescribeDomainLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_logs_with_options_async(request, runtime)

    def describe_domain_ns_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        """
        @summary Queries the name servers configured for a specified domain name and checks whether all the name servers are Alibaba Cloud Domain Name System (DNS) servers.
        
        @description >  You can call this operation to query the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        
        @param request: DescribeDomainNsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainNsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainNsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_ns_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        """
        @summary Queries the name servers configured for a specified domain name and checks whether all the name servers are Alibaba Cloud Domain Name System (DNS) servers.
        
        @description >  You can call this operation to query the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        
        @param request: DescribeDomainNsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainNsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainNsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_ns(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        """
        @summary Queries the name servers configured for a specified domain name and checks whether all the name servers are Alibaba Cloud Domain Name System (DNS) servers.
        
        @description >  You can call this operation to query the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        
        @param request: DescribeDomainNsRequest
        @return: DescribeDomainNsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ns_with_options(request, runtime)

    async def describe_domain_ns_async(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        """
        @summary Queries the name servers configured for a specified domain name and checks whether all the name servers are Alibaba Cloud Domain Name System (DNS) servers.
        
        @description >  You can call this operation to query the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        
        @param request: DescribeDomainNsRequest
        @return: DescribeDomainNsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_ns_with_options_async(request, runtime)

    def describe_domain_record_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        """
        @summary Queries the information about a Domain Name System (DNS) record.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Alidns\\&api=DescribeDomainRecordInfo\\&type=RPC\\&version=2015-01-09)
        
        @param request: DescribeDomainRecordInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRecordInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecordInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_record_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        """
        @summary Queries the information about a Domain Name System (DNS) record.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Alidns\\&api=DescribeDomainRecordInfo\\&type=RPC\\&version=2015-01-09)
        
        @param request: DescribeDomainRecordInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRecordInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecordInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_record_info(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        """
        @summary Queries the information about a Domain Name System (DNS) record.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Alidns\\&api=DescribeDomainRecordInfo\\&type=RPC\\&version=2015-01-09)
        
        @param request: DescribeDomainRecordInfoRequest
        @return: DescribeDomainRecordInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_record_info_with_options(request, runtime)

    async def describe_domain_record_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        """
        @summary Queries the information about a Domain Name System (DNS) record.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Alidns\\&api=DescribeDomainRecordInfo\\&type=RPC\\&version=2015-01-09)
        
        @param request: DescribeDomainRecordInfoRequest
        @return: DescribeDomainRecordInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_record_info_with_options_async(request, runtime)

    def describe_domain_records_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of the specified primary domain names based on the specified parameters.
        
        @description    You can specify DomainName, PageNumber, and PageSize to query the DNS records of the specified domain names.
        You can also specify RRKeyWord, TypeKeyWord, or ValueKeyWord to query the DNS records that contain the specified keyword.
        By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        You can specify GroupId to query the DNS records of the specified domain names based on the group ID. You can query the DNS records of all domain names and the domain names in the default group.
        
        @param request: DescribeDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rrkey_word):
            query['RRKeyWord'] = request.rrkey_word
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.type_key_word):
            query['TypeKeyWord'] = request.type_key_word
        if not UtilClient.is_unset(request.value_key_word):
            query['ValueKeyWord'] = request.value_key_word
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of the specified primary domain names based on the specified parameters.
        
        @description    You can specify DomainName, PageNumber, and PageSize to query the DNS records of the specified domain names.
        You can also specify RRKeyWord, TypeKeyWord, or ValueKeyWord to query the DNS records that contain the specified keyword.
        By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        You can specify GroupId to query the DNS records of the specified domain names based on the group ID. You can query the DNS records of all domain names and the domain names in the default group.
        
        @param request: DescribeDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rrkey_word):
            query['RRKeyWord'] = request.rrkey_word
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.type_key_word):
            query['TypeKeyWord'] = request.type_key_word
        if not UtilClient.is_unset(request.value_key_word):
            query['ValueKeyWord'] = request.value_key_word
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_records(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of the specified primary domain names based on the specified parameters.
        
        @description    You can specify DomainName, PageNumber, and PageSize to query the DNS records of the specified domain names.
        You can also specify RRKeyWord, TypeKeyWord, or ValueKeyWord to query the DNS records that contain the specified keyword.
        By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        You can specify GroupId to query the DNS records of the specified domain names based on the group ID. You can query the DNS records of all domain names and the domain names in the default group.
        
        @param request: DescribeDomainRecordsRequest
        @return: DescribeDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_records_with_options(request, runtime)

    async def describe_domain_records_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of the specified primary domain names based on the specified parameters.
        
        @description    You can specify DomainName, PageNumber, and PageSize to query the DNS records of the specified domain names.
        You can also specify RRKeyWord, TypeKeyWord, or ValueKeyWord to query the DNS records that contain the specified keyword.
        By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        You can specify GroupId to query the DNS records of the specified domain names based on the group ID. You can query the DNS records of all domain names and the domain names in the default group.
        
        @param request: DescribeDomainRecordsRequest
        @return: DescribeDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_records_with_options_async(request, runtime)

    def describe_domain_resolve_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainResolveStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse:
        """
        @summary Queries the resolution requests of all paid domain names within your account.
        
        @param request: DescribeDomainResolveStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolve_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainResolveStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse:
        """
        @summary Queries the resolution requests of all paid domain names within your account.
        
        @param request: DescribeDomainResolveStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resolve_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeDomainResolveStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse:
        """
        @summary Queries the resolution requests of all paid domain names within your account.
        
        @param request: DescribeDomainResolveStatisticsSummaryRequest
        @return: DescribeDomainResolveStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolve_statistics_summary_with_options(request, runtime)

    async def describe_domain_resolve_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDomainResolveStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse:
        """
        @summary Queries the resolution requests of all paid domain names within your account.
        
        @param request: DescribeDomainResolveStatisticsSummaryRequest
        @return: DescribeDomainResolveStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolve_statistics_summary_with_options_async(request, runtime)

    def describe_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a primary domain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a primary domain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeDomainStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_statistics(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a primary domain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeDomainStatisticsRequest
        @return: DescribeDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_with_options(request, runtime)

    async def describe_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a primary domain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeDomainStatisticsRequest
        @return: DescribeDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_statistics_with_options_async(request, runtime)

    def describe_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        """
        @summary Calls the DescribeDomainStatisticsSummary operation to obtain the query volume of all paid domain names under your account.
        
        @param request: DescribeDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        """
        @summary Calls the DescribeDomainStatisticsSummary operation to obtain the query volume of all paid domain names under your account.
        
        @param request: DescribeDomainStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        """
        @summary Calls the DescribeDomainStatisticsSummary operation to obtain the query volume of all paid domain names under your account.
        
        @param request: DescribeDomainStatisticsSummaryRequest
        @return: DescribeDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_summary_with_options(request, runtime)

    async def describe_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        """
        @summary Calls the DescribeDomainStatisticsSummary operation to obtain the query volume of all paid domain names under your account.
        
        @param request: DescribeDomainStatisticsSummaryRequest
        @return: DescribeDomainStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_statistics_summary_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        """
        @summary Calls the DescribeDomains operation to query domain names of a user based on input parameters.
        
        @description    You can specify the PageNumber and PageSize parameters to query domain names.
        You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        By default, the domain names in a list are sorted in descending order of the time they were added.
        You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.starmark):
            query['Starmark'] = request.starmark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        """
        @summary Calls the DescribeDomains operation to query domain names of a user based on input parameters.
        
        @description    You can specify the PageNumber and PageSize parameters to query domain names.
        You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        By default, the domain names in a list are sorted in descending order of the time they were added.
        You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.starmark):
            query['Starmark'] = request.starmark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        """
        @summary Calls the DescribeDomains operation to query domain names of a user based on input parameters.
        
        @description    You can specify the PageNumber and PageSize parameters to query domain names.
        You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        By default, the domain names in a list are sorted in descending order of the time they were added.
        You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        """
        @summary Calls the DescribeDomains operation to query domain names of a user based on input parameters.
        
        @description    You can specify the PageNumber and PageSize parameters to query domain names.
        You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        By default, the domain names in a list are sorted in descending order of the time they were added.
        You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_gtm_access_strategies_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        """
        @summary You can call this operation to query the access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmAccessStrategiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategies_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        """
        @summary You can call this operation to query the access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmAccessStrategiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategies(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        """
        @summary You can call this operation to query the access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmAccessStrategiesRequest
        @return: DescribeGtmAccessStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategies_with_options(request, runtime)

    async def describe_gtm_access_strategies_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        """
        @summary You can call this operation to query the access policies of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmAccessStrategiesRequest
        @return: DescribeGtmAccessStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategies_with_options_async(request, runtime)

    def describe_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        """
        @summary You can call this operation to query the details about an access policy of a Global Traffic Manager (GTM) instance based on the policy ID.
        
        @param request: DescribeGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        """
        @summary You can call this operation to query the details about an access policy of a Global Traffic Manager (GTM) instance based on the policy ID.
        
        @param request: DescribeGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategy(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        """
        @summary You can call this operation to query the details about an access policy of a Global Traffic Manager (GTM) instance based on the policy ID.
        
        @param request: DescribeGtmAccessStrategyRequest
        @return: DescribeGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_with_options(request, runtime)

    async def describe_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        """
        @summary You can call this operation to query the details about an access policy of a Global Traffic Manager (GTM) instance based on the policy ID.
        
        @param request: DescribeGtmAccessStrategyRequest
        @return: DescribeGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategy_with_options_async(request, runtime)

    def describe_gtm_access_strategy_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the configuration items that can be set for an access policy.
        
        @param request: DescribeGtmAccessStrategyAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategyAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_access_strategy_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the configuration items that can be set for an access policy.
        
        @param request: DescribeGtmAccessStrategyAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAccessStrategyAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_access_strategy_available_config(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the configuration items that can be set for an access policy.
        
        @param request: DescribeGtmAccessStrategyAvailableConfigRequest
        @return: DescribeGtmAccessStrategyAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_gtm_access_strategy_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        """
        @summary Queries the configuration items that can be set for an access policy.
        
        @param request: DescribeGtmAccessStrategyAvailableConfigRequest
        @return: DescribeGtmAccessStrategyAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_gtm_available_alert_group_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeGtmAvailableAlertGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAvailableAlertGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_available_alert_group_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeGtmAvailableAlertGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmAvailableAlertGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_available_alert_group(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeGtmAvailableAlertGroupRequest
        @return: DescribeGtmAvailableAlertGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_available_alert_group_with_options(request, runtime)

    async def describe_gtm_available_alert_group_async(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        """
        @param request: DescribeGtmAvailableAlertGroupRequest
        @return: DescribeGtmAvailableAlertGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_gtm_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        """
        @summary Queries the details about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        """
        @summary Queries the details about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        """
        @summary Queries the details about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceRequest
        @return: DescribeGtmInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_with_options(request, runtime)

    async def describe_gtm_instance_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        """
        @summary Queries the details about a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceRequest
        @return: DescribeGtmInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_with_options_async(request, runtime)

    def describe_gtm_instance_address_pool_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        """
        @summary You can call this operation to query the details about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        """
        @summary You can call this operation to query the details about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_address_pool(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        """
        @summary You can call this operation to query the details about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolRequest
        @return: DescribeGtmInstanceAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_gtm_instance_address_pool_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        """
        @summary You can call this operation to query the details about an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolRequest
        @return: DescribeGtmInstanceAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_gtm_instance_address_pools_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        """
        @summary You can call this operation to query the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        """
        @summary You can call this operation to query the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_address_pools(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        """
        @summary You can call this operation to query the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolsRequest
        @return: DescribeGtmInstanceAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_gtm_instance_address_pools_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        """
        @summary You can call this operation to query the address pools of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceAddressPoolsRequest
        @return: DescribeGtmInstanceAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_gtm_instance_status_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        """
        @summary Queries the current status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_status_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        """
        @summary Queries the current status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_status(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        """
        @summary Queries the current status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceStatusRequest
        @return: DescribeGtmInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_status_with_options(request, runtime)

    async def describe_gtm_instance_status_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        """
        @summary Queries the current status of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmInstanceStatusRequest
        @return: DescribeGtmInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_status_with_options_async(request, runtime)

    def describe_gtm_instance_system_cname_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        """
        @param request: DescribeGtmInstanceSystemCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceSystemCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instance_system_cname_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        """
        @param request: DescribeGtmInstanceSystemCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstanceSystemCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instance_system_cname(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        """
        @param request: DescribeGtmInstanceSystemCnameRequest
        @return: DescribeGtmInstanceSystemCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_gtm_instance_system_cname_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        """
        @param request: DescribeGtmInstanceSystemCnameRequest
        @return: DescribeGtmInstanceSystemCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        """
        @summary Queries the Global Traffic Manager (GTM) instances under your account.
        
        @param request: DescribeGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        """
        @summary Queries the Global Traffic Manager (GTM) instances under your account.
        
        @param request: DescribeGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_instances(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        """
        @summary Queries the Global Traffic Manager (GTM) instances under your account.
        
        @param request: DescribeGtmInstancesRequest
        @return: DescribeGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instances_with_options(request, runtime)

    async def describe_gtm_instances_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        """
        @summary Queries the Global Traffic Manager (GTM) instances under your account.
        
        @param request: DescribeGtmInstancesRequest
        @return: DescribeGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instances_with_options_async(request, runtime)

    def describe_gtm_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        """
        @summary You can call this operation to query logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        """
        @summary You can call this operation to query logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_logs(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        """
        @summary You can call this operation to query logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmLogsRequest
        @return: DescribeGtmLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_logs_with_options(request, runtime)

    async def describe_gtm_logs_async(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        """
        @summary You can call this operation to query logs of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmLogsRequest
        @return: DescribeGtmLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_logs_with_options_async(request, runtime)

    def describe_gtm_monitor_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeGtmMonitorAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmMonitorAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_monitor_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeGtmMonitorAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmMonitorAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_monitor_available_config(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeGtmMonitorAvailableConfigRequest
        @return: DescribeGtmMonitorAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_gtm_monitor_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        """
        @summary Queries available monitored nodes.
        
        @param request: DescribeGtmMonitorAvailableConfigRequest
        @return: DescribeGtmMonitorAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_gtm_monitor_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        """
        @summary Queries the health check configuration of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmMonitorConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmMonitorConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_monitor_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        """
        @summary Queries the health check configuration of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmMonitorConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmMonitorConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_monitor_config(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        """
        @summary Queries the health check configuration of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmMonitorConfigRequest
        @return: DescribeGtmMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_config_with_options(request, runtime)

    async def describe_gtm_monitor_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        """
        @summary Queries the health check configuration of an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmMonitorConfigRequest
        @return: DescribeGtmMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_monitor_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to query the detailed information of a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to query the detailed information of a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to query the detailed information of a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanRequest
        @return: DescribeGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_with_options(request, runtime)

    async def describe_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to query the detailed information of a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanRequest
        @return: DescribeGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plan_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        """
        @summary You can call this operation to query the available configurations of a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlanAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlanAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plan_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        """
        @summary You can call this operation to query the available configurations of a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanAvailableConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlanAvailableConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlanAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plan_available_config(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        """
        @summary You can call this operation to query the available configurations of a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanAvailableConfigRequest
        @return: DescribeGtmRecoveryPlanAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_available_config_with_options(request, runtime)

    async def describe_gtm_recovery_plan_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        """
        @summary You can call this operation to query the available configurations of a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlanAvailableConfigRequest
        @return: DescribeGtmRecoveryPlanAvailableConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plan_available_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plans_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        """
        @summary Queries the disaster recovery plans for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlans',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gtm_recovery_plans_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        """
        @summary Queries the disaster recovery plans for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGtmRecoveryPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlans',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gtm_recovery_plans(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        """
        @summary Queries the disaster recovery plans for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlansRequest
        @return: DescribeGtmRecoveryPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plans_with_options(request, runtime)

    async def describe_gtm_recovery_plans_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        """
        @summary Queries the disaster recovery plans for a Global Traffic Manager (GTM) instance.
        
        @param request: DescribeGtmRecoveryPlansRequest
        @return: DescribeGtmRecoveryPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plans_with_options_async(request, runtime)

    def describe_instance_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        """
        @summary Queries the domain names that are bound to an Alibaba Cloud DNS instance.
        
        @param request: DescribeInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        """
        @summary Queries the domain names that are bound to an Alibaba Cloud DNS instance.
        
        @param request: DescribeInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_domains(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        """
        @summary Queries the domain names that are bound to an Alibaba Cloud DNS instance.
        
        @param request: DescribeInstanceDomainsRequest
        @return: DescribeInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_domains_with_options(request, runtime)

    async def describe_instance_domains_async(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        """
        @summary Queries the domain names that are bound to an Alibaba Cloud DNS instance.
        
        @param request: DescribeInstanceDomainsRequest
        @return: DescribeInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_domains_with_options_async(request, runtime)

    def describe_internet_dns_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeInternetDnsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInternetDnsLogsResponse:
        """
        @param request: DescribeInternetDnsLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetDnsLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetDnsLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeInternetDnsLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_dns_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeInternetDnsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInternetDnsLogsResponse:
        """
        @param request: DescribeInternetDnsLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetDnsLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetDnsLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeInternetDnsLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_dns_logs(
        self,
        request: alidns_20150109_models.DescribeInternetDnsLogsRequest,
    ) -> alidns_20150109_models.DescribeInternetDnsLogsResponse:
        """
        @param request: DescribeInternetDnsLogsRequest
        @return: DescribeInternetDnsLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_internet_dns_logs_with_options(request, runtime)

    async def describe_internet_dns_logs_async(
        self,
        request: alidns_20150109_models.DescribeInternetDnsLogsRequest,
    ) -> alidns_20150109_models.DescribeInternetDnsLogsResponse:
        """
        @param request: DescribeInternetDnsLogsRequest
        @return: DescribeInternetDnsLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_internet_dns_logs_with_options_async(request, runtime)

    def describe_isp_flush_cache_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheInstancesResponse:
        """
        @summary 获取缓存刷新套餐包列表
        
        @param request: DescribeIspFlushCacheInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheInstancesResponse:
        """
        @summary 获取缓存刷新套餐包列表
        
        @param request: DescribeIspFlushCacheInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_instances(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheInstancesRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheInstancesResponse:
        """
        @summary 获取缓存刷新套餐包列表
        
        @param request: DescribeIspFlushCacheInstancesRequest
        @return: DescribeIspFlushCacheInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_instances_with_options(request, runtime)

    async def describe_isp_flush_cache_instances_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheInstancesRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheInstancesResponse:
        """
        @summary 获取缓存刷新套餐包列表
        
        @param request: DescribeIspFlushCacheInstancesRequest
        @return: DescribeIspFlushCacheInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_isp_flush_cache_instances_with_options_async(request, runtime)

    def describe_isp_flush_cache_remain_quota_with_options(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheRemainQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse:
        """
        @summary 获取剩余可缓存刷新次数
        
        @param request: DescribeIspFlushCacheRemainQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheRemainQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheRemainQuota',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_remain_quota_with_options_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheRemainQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse:
        """
        @summary 获取剩余可缓存刷新次数
        
        @param request: DescribeIspFlushCacheRemainQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheRemainQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheRemainQuota',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_remain_quota(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheRemainQuotaRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse:
        """
        @summary 获取剩余可缓存刷新次数
        
        @param request: DescribeIspFlushCacheRemainQuotaRequest
        @return: DescribeIspFlushCacheRemainQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_remain_quota_with_options(request, runtime)

    async def describe_isp_flush_cache_remain_quota_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheRemainQuotaRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse:
        """
        @summary 获取剩余可缓存刷新次数
        
        @param request: DescribeIspFlushCacheRemainQuotaRequest
        @return: DescribeIspFlushCacheRemainQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_isp_flush_cache_remain_quota_with_options_async(request, runtime)

    def describe_isp_flush_cache_task_with_options(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTaskResponse:
        """
        @summary 获取缓存刷新任务详情
        
        @param request: DescribeIspFlushCacheTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_task_with_options_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTaskResponse:
        """
        @summary 获取缓存刷新任务详情
        
        @param request: DescribeIspFlushCacheTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_task(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTaskRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTaskResponse:
        """
        @summary 获取缓存刷新任务详情
        
        @param request: DescribeIspFlushCacheTaskRequest
        @return: DescribeIspFlushCacheTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_task_with_options(request, runtime)

    async def describe_isp_flush_cache_task_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTaskRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTaskResponse:
        """
        @summary 获取缓存刷新任务详情
        
        @param request: DescribeIspFlushCacheTaskRequest
        @return: DescribeIspFlushCacheTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_isp_flush_cache_task_with_options_async(request, runtime)

    def describe_isp_flush_cache_tasks_with_options(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTasksResponse:
        """
        @summary 获取缓存刷新任务列表
        
        @param request: DescribeIspFlushCacheTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTasks',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_flush_cache_tasks_with_options_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTasksResponse:
        """
        @summary 获取缓存刷新任务列表
        
        @param request: DescribeIspFlushCacheTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIspFlushCacheTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTasks',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_flush_cache_tasks(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTasksRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTasksResponse:
        """
        @summary 获取缓存刷新任务列表
        
        @param request: DescribeIspFlushCacheTasksRequest
        @return: DescribeIspFlushCacheTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_tasks_with_options(request, runtime)

    async def describe_isp_flush_cache_tasks_async(
        self,
        request: alidns_20150109_models.DescribeIspFlushCacheTasksRequest,
    ) -> alidns_20150109_models.DescribeIspFlushCacheTasksResponse:
        """
        @summary 获取缓存刷新任务列表
        
        @param request: DescribeIspFlushCacheTasksRequest
        @return: DescribeIspFlushCacheTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_isp_flush_cache_tasks_with_options_async(request, runtime)

    def describe_pdns_account_summary_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAccountSummaryResponse:
        """
        @summary 获取公共DNS用户数据概览
        
        @param request: DescribePdnsAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAccountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAccountSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_account_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAccountSummaryResponse:
        """
        @summary 获取公共DNS用户数据概览
        
        @param request: DescribePdnsAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAccountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAccountSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_account_summary(
        self,
        request: alidns_20150109_models.DescribePdnsAccountSummaryRequest,
    ) -> alidns_20150109_models.DescribePdnsAccountSummaryResponse:
        """
        @summary 获取公共DNS用户数据概览
        
        @param request: DescribePdnsAccountSummaryRequest
        @return: DescribePdnsAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_account_summary_with_options(request, runtime)

    async def describe_pdns_account_summary_async(
        self,
        request: alidns_20150109_models.DescribePdnsAccountSummaryRequest,
    ) -> alidns_20150109_models.DescribePdnsAccountSummaryResponse:
        """
        @summary 获取公共DNS用户数据概览
        
        @param request: DescribePdnsAccountSummaryRequest
        @return: DescribePdnsAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_account_summary_with_options_async(request, runtime)

    def describe_pdns_app_key_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAppKeyResponse:
        """
        @summary 获取公共DNS AppKey 详情
        
        @param request: DescribePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_app_key_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAppKeyResponse:
        """
        @summary 获取公共DNS AppKey 详情
        
        @param request: DescribePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_app_key(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeyRequest,
    ) -> alidns_20150109_models.DescribePdnsAppKeyResponse:
        """
        @summary 获取公共DNS AppKey 详情
        
        @param request: DescribePdnsAppKeyRequest
        @return: DescribePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_app_key_with_options(request, runtime)

    async def describe_pdns_app_key_async(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeyRequest,
    ) -> alidns_20150109_models.DescribePdnsAppKeyResponse:
        """
        @summary 获取公共DNS AppKey 详情
        
        @param request: DescribePdnsAppKeyRequest
        @return: DescribePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_app_key_with_options_async(request, runtime)

    def describe_pdns_app_keys_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAppKeysResponse:
        """
        @summary 获取公共DNS AppKey 列表
        
        @param request: DescribePdnsAppKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAppKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKeys',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_app_keys_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsAppKeysResponse:
        """
        @summary 获取公共DNS AppKey 列表
        
        @param request: DescribePdnsAppKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsAppKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKeys',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_app_keys(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeysRequest,
    ) -> alidns_20150109_models.DescribePdnsAppKeysResponse:
        """
        @summary 获取公共DNS AppKey 列表
        
        @param request: DescribePdnsAppKeysRequest
        @return: DescribePdnsAppKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_app_keys_with_options(request, runtime)

    async def describe_pdns_app_keys_async(
        self,
        request: alidns_20150109_models.DescribePdnsAppKeysRequest,
    ) -> alidns_20150109_models.DescribePdnsAppKeysResponse:
        """
        @summary 获取公共DNS AppKey 列表
        
        @param request: DescribePdnsAppKeysRequest
        @return: DescribePdnsAppKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_app_keys_with_options_async(request, runtime)

    def describe_pdns_operate_logs_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsOperateLogsResponse:
        """
        @summary 获取公共DNS 操作日志列表
        
        @param request: DescribePdnsOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsOperateLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_operate_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsOperateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsOperateLogsResponse:
        """
        @summary 获取公共DNS 操作日志列表
        
        @param request: DescribePdnsOperateLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsOperateLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsOperateLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsOperateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_operate_logs(
        self,
        request: alidns_20150109_models.DescribePdnsOperateLogsRequest,
    ) -> alidns_20150109_models.DescribePdnsOperateLogsResponse:
        """
        @summary 获取公共DNS 操作日志列表
        
        @param request: DescribePdnsOperateLogsRequest
        @return: DescribePdnsOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_operate_logs_with_options(request, runtime)

    async def describe_pdns_operate_logs_async(
        self,
        request: alidns_20150109_models.DescribePdnsOperateLogsRequest,
    ) -> alidns_20150109_models.DescribePdnsOperateLogsResponse:
        """
        @summary 获取公共DNS 操作日志列表
        
        @param request: DescribePdnsOperateLogsRequest
        @return: DescribePdnsOperateLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_operate_logs_with_options_async(request, runtime)

    def describe_pdns_request_statistic_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticResponse:
        """
        @summary 获取公共DNS 请求统计
        
        @param request: DescribePdnsRequestStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsRequestStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_request_statistic_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticResponse:
        """
        @summary 获取公共DNS 请求统计
        
        @param request: DescribePdnsRequestStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsRequestStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_request_statistic(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticRequest,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticResponse:
        """
        @summary 获取公共DNS 请求统计
        
        @param request: DescribePdnsRequestStatisticRequest
        @return: DescribePdnsRequestStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_request_statistic_with_options(request, runtime)

    async def describe_pdns_request_statistic_async(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticRequest,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticResponse:
        """
        @summary 获取公共DNS 请求统计
        
        @param request: DescribePdnsRequestStatisticRequest
        @return: DescribePdnsRequestStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_request_statistic_with_options_async(request, runtime)

    def describe_pdns_request_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticsResponse:
        """
        @summary 获取公共DNS 请求统计列表
        
        @param request: DescribePdnsRequestStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsRequestStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_request_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticsResponse:
        """
        @summary 获取公共DNS 请求统计列表
        
        @param request: DescribePdnsRequestStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsRequestStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_request_statistics(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticsRequest,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticsResponse:
        """
        @summary 获取公共DNS 请求统计列表
        
        @param request: DescribePdnsRequestStatisticsRequest
        @return: DescribePdnsRequestStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_request_statistics_with_options(request, runtime)

    async def describe_pdns_request_statistics_async(
        self,
        request: alidns_20150109_models.DescribePdnsRequestStatisticsRequest,
    ) -> alidns_20150109_models.DescribePdnsRequestStatisticsResponse:
        """
        @summary 获取公共DNS 请求统计列表
        
        @param request: DescribePdnsRequestStatisticsRequest
        @return: DescribePdnsRequestStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_request_statistics_with_options_async(request, runtime)

    def describe_pdns_threat_logs_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsThreatLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatLogsResponse:
        """
        @summary 获取公共DNS 威胁日志列表
        
        @param request: DescribePdnsThreatLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatLogsResponse:
        """
        @summary 获取公共DNS 威胁日志列表
        
        @param request: DescribePdnsThreatLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_logs(
        self,
        request: alidns_20150109_models.DescribePdnsThreatLogsRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatLogsResponse:
        """
        @summary 获取公共DNS 威胁日志列表
        
        @param request: DescribePdnsThreatLogsRequest
        @return: DescribePdnsThreatLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_logs_with_options(request, runtime)

    async def describe_pdns_threat_logs_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatLogsRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatLogsResponse:
        """
        @summary 获取公共DNS 威胁日志列表
        
        @param request: DescribePdnsThreatLogsRequest
        @return: DescribePdnsThreatLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_threat_logs_with_options_async(request, runtime)

    def describe_pdns_threat_statistic_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticResponse:
        """
        @summary 获取公共DNS 威胁统计
        
        @param request: DescribePdnsThreatStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_statistic_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticResponse:
        """
        @summary 获取公共DNS 威胁统计
        
        @param request: DescribePdnsThreatStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_statistic(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticResponse:
        """
        @summary 获取公共DNS 威胁统计
        
        @param request: DescribePdnsThreatStatisticRequest
        @return: DescribePdnsThreatStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_statistic_with_options(request, runtime)

    async def describe_pdns_threat_statistic_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticResponse:
        """
        @summary 获取公共DNS 威胁统计
        
        @param request: DescribePdnsThreatStatisticRequest
        @return: DescribePdnsThreatStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_threat_statistic_with_options_async(request, runtime)

    def describe_pdns_threat_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticsResponse:
        """
        @summary 获取公共DNS 威胁统计列表
        
        @param request: DescribePdnsThreatStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_threat_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticsResponse:
        """
        @summary 获取公共DNS 威胁统计列表
        
        @param request: DescribePdnsThreatStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsThreatStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_threat_statistics(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticsRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticsResponse:
        """
        @summary 获取公共DNS 威胁统计列表
        
        @param request: DescribePdnsThreatStatisticsRequest
        @return: DescribePdnsThreatStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_statistics_with_options(request, runtime)

    async def describe_pdns_threat_statistics_async(
        self,
        request: alidns_20150109_models.DescribePdnsThreatStatisticsRequest,
    ) -> alidns_20150109_models.DescribePdnsThreatStatisticsResponse:
        """
        @summary 获取公共DNS 威胁统计列表
        
        @param request: DescribePdnsThreatStatisticsRequest
        @return: DescribePdnsThreatStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_threat_statistics_with_options_async(request, runtime)

    def describe_pdns_udp_ip_segments_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsUdpIpSegmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse:
        """
        @summary 获取公共DNS Udp IP段列表
        
        @param request: DescribePdnsUdpIpSegmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsUdpIpSegmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUdpIpSegments',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_udp_ip_segments_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsUdpIpSegmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse:
        """
        @summary 获取公共DNS Udp IP段列表
        
        @param request: DescribePdnsUdpIpSegmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsUdpIpSegmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUdpIpSegments',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_udp_ip_segments(
        self,
        request: alidns_20150109_models.DescribePdnsUdpIpSegmentsRequest,
    ) -> alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse:
        """
        @summary 获取公共DNS Udp IP段列表
        
        @param request: DescribePdnsUdpIpSegmentsRequest
        @return: DescribePdnsUdpIpSegmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_udp_ip_segments_with_options(request, runtime)

    async def describe_pdns_udp_ip_segments_async(
        self,
        request: alidns_20150109_models.DescribePdnsUdpIpSegmentsRequest,
    ) -> alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse:
        """
        @summary 获取公共DNS Udp IP段列表
        
        @param request: DescribePdnsUdpIpSegmentsRequest
        @return: DescribePdnsUdpIpSegmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_udp_ip_segments_with_options_async(request, runtime)

    def describe_pdns_user_info_with_options(
        self,
        request: alidns_20150109_models.DescribePdnsUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsUserInfoResponse:
        """
        @summary 获取公共DNS用户信息
        
        @param request: DescribePdnsUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pdns_user_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribePdnsUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribePdnsUserInfoResponse:
        """
        @summary 获取公共DNS用户信息
        
        @param request: DescribePdnsUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePdnsUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pdns_user_info(
        self,
        request: alidns_20150109_models.DescribePdnsUserInfoRequest,
    ) -> alidns_20150109_models.DescribePdnsUserInfoResponse:
        """
        @summary 获取公共DNS用户信息
        
        @param request: DescribePdnsUserInfoRequest
        @return: DescribePdnsUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_user_info_with_options(request, runtime)

    async def describe_pdns_user_info_async(
        self,
        request: alidns_20150109_models.DescribePdnsUserInfoRequest,
    ) -> alidns_20150109_models.DescribePdnsUserInfoResponse:
        """
        @summary 获取公共DNS用户信息
        
        @param request: DescribePdnsUserInfoRequest
        @return: DescribePdnsUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pdns_user_info_with_options_async(request, runtime)

    def describe_record_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        """
        @summary Queries the operation logs of a domain name based on the specified parameters.
        
        @param request: DescribeRecordLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        """
        @summary Queries the operation logs of a domain name based on the specified parameters.
        
        @param request: DescribeRecordLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_logs(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        """
        @summary Queries the operation logs of a domain name based on the specified parameters.
        
        @param request: DescribeRecordLogsRequest
        @return: DescribeRecordLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_logs_with_options(request, runtime)

    async def describe_record_logs_async(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        """
        @summary Queries the operation logs of a domain name based on the specified parameters.
        
        @param request: DescribeRecordLogsRequest
        @return: DescribeRecordLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_logs_with_options_async(request, runtime)

    def describe_record_resolve_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordResolveStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse:
        """
        @summary Queries the number of resolution requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordResolveStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordResolveStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_resolve_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordResolveStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse:
        """
        @summary Queries the number of resolution requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordResolveStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordResolveStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_resolve_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeRecordResolveStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse:
        """
        @summary Queries the number of resolution requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordResolveStatisticsSummaryRequest
        @return: DescribeRecordResolveStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_resolve_statistics_summary_with_options(request, runtime)

    async def describe_record_resolve_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeRecordResolveStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse:
        """
        @summary Queries the number of resolution requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordResolveStatisticsSummaryRequest
        @return: DescribeRecordResolveStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_resolve_statistics_summary_with_options_async(request, runtime)

    def describe_record_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a subdomain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeRecordStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a subdomain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeRecordStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_statistics(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a subdomain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeRecordStatisticsRequest
        @return: DescribeRecordStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_with_options(request, runtime)

    async def describe_record_statistics_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        """
        @summary Queries the real-time statistics on the Domain Name System (DNS) requests for a subdomain name.
        
        @description Real-time data is collected per hour.
        
        @param request: DescribeRecordStatisticsRequest
        @return: DescribeRecordStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_statistics_with_options_async(request, runtime)

    def describe_record_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        """
        @summary Queries the number of Domain Name System (DNS) requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        """
        @summary Queries the number of Domain Name System (DNS) requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordStatisticsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordStatisticsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_statistics_summary(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        """
        @summary Queries the number of Domain Name System (DNS) requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordStatisticsSummaryRequest
        @return: DescribeRecordStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_summary_with_options(request, runtime)

    async def describe_record_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        """
        @summary Queries the number of Domain Name System (DNS) requests for all subdomain names of a specified domain name.
        
        @param request: DescribeRecordStatisticsSummaryRequest
        @return: DescribeRecordStatisticsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_statistics_summary_with_options_async(request, runtime)

    def describe_sub_domain_records_with_options(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of a subdomain name based on the specified parameters.
        
        @param request: DescribeSubDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sub_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of a subdomain name based on the specified parameters.
        
        @param request: DescribeSubDomainRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSubDomainRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sub_domain_records(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of a subdomain name based on the specified parameters.
        
        @param request: DescribeSubDomainRecordsRequest
        @return: DescribeSubDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_domain_records_with_options(request, runtime)

    async def describe_sub_domain_records_async(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        """
        @summary Queries all Domain Name System (DNS) records of a subdomain name based on the specified parameters.
        
        @param request: DescribeSubDomainRecordsRequest
        @return: DescribeSubDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sub_domain_records_with_options_async(request, runtime)

    def describe_support_lines_with_options(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        """
        @summary 查询云解析支持的所有线路列表。
        
        @param request: DescribeSupportLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSupportLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_lines_with_options_async(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        """
        @summary 查询云解析支持的所有线路列表。
        
        @param request: DescribeSupportLinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportLinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSupportLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_lines(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        """
        @summary 查询云解析支持的所有线路列表。
        
        @param request: DescribeSupportLinesRequest
        @return: DescribeSupportLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_support_lines_with_options(request, runtime)

    async def describe_support_lines_async(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        """
        @summary 查询云解析支持的所有线路列表。
        
        @param request: DescribeSupportLinesRequest
        @return: DescribeSupportLinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_support_lines_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        """
        @summary Queries existing tags.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        """
        @summary Queries existing tags.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        """
        @summary Queries existing tags.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        """
        @summary Queries existing tags.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_transfer_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        """
        @summary Queries the domain names that were transferred between the current account and another account based on the specified parameters.
        
        @param request: DescribeTransferDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransferDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.from_user_id):
            query['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTransferDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        """
        @summary Queries the domain names that were transferred between the current account and another account based on the specified parameters.
        
        @param request: DescribeTransferDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransferDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.from_user_id):
            query['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTransferDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_domains(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        """
        @summary Queries the domain names that were transferred between the current account and another account based on the specified parameters.
        
        @param request: DescribeTransferDomainsRequest
        @return: DescribeTransferDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_domains_with_options(request, runtime)

    async def describe_transfer_domains_async(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        """
        @summary Queries the domain names that were transferred between the current account and another account based on the specified parameters.
        
        @param request: DescribeTransferDomainsRequest
        @return: DescribeTransferDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_transfer_domains_with_options_async(request, runtime)

    def execute_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        """
        @param request: ExecuteGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ExecuteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        """
        @param request: ExecuteGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ExecuteGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        """
        @param request: ExecuteGtmRecoveryPlanRequest
        @return: ExecuteGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_gtm_recovery_plan_with_options(request, runtime)

    async def execute_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        """
        @param request: ExecuteGtmRecoveryPlanRequest
        @return: ExecuteGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_gtm_recovery_plan_with_options_async(request, runtime)

    def get_main_domain_name_with_options(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        """
        @summary Queries a primary domain name based on the specified parameters.
        
        @description For more information about the difference between primary domain names and subdomain names, see
        [Subdomain levels](https://www.alibabacloud.com/help/zh/faq-detail/39803.htm). For example, if you enter `www.abc.com`, abc.com is obtained.
        
        @param request: GetMainDomainNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMainDomainNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_string):
            query['InputString'] = request.input_string
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainDomainName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetMainDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_main_domain_name_with_options_async(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        """
        @summary Queries a primary domain name based on the specified parameters.
        
        @description For more information about the difference between primary domain names and subdomain names, see
        [Subdomain levels](https://www.alibabacloud.com/help/zh/faq-detail/39803.htm). For example, if you enter `www.abc.com`, abc.com is obtained.
        
        @param request: GetMainDomainNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMainDomainNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_string):
            query['InputString'] = request.input_string
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainDomainName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetMainDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_main_domain_name(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        """
        @summary Queries a primary domain name based on the specified parameters.
        
        @description For more information about the difference between primary domain names and subdomain names, see
        [Subdomain levels](https://www.alibabacloud.com/help/zh/faq-detail/39803.htm). For example, if you enter `www.abc.com`, abc.com is obtained.
        
        @param request: GetMainDomainNameRequest
        @return: GetMainDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_main_domain_name_with_options(request, runtime)

    async def get_main_domain_name_async(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        """
        @summary Queries a primary domain name based on the specified parameters.
        
        @description For more information about the difference between primary domain names and subdomain names, see
        [Subdomain levels](https://www.alibabacloud.com/help/zh/faq-detail/39803.htm). For example, if you enter `www.abc.com`, abc.com is obtained.
        
        @param request: GetMainDomainNameRequest
        @return: GetMainDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_main_domain_name_with_options_async(request, runtime)

    def get_txt_record_for_verify_with_options(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        """
        @summary Generates a text (TXT) record. TXT records are used to retrieve domain names and subdomain names, enable the subdomain name verification feature, and perform batch retrievals.
        
        @param request: GetTxtRecordForVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTxtRecordForVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTxtRecordForVerify',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetTxtRecordForVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_txt_record_for_verify_with_options_async(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        """
        @summary Generates a text (TXT) record. TXT records are used to retrieve domain names and subdomain names, enable the subdomain name verification feature, and perform batch retrievals.
        
        @param request: GetTxtRecordForVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTxtRecordForVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTxtRecordForVerify',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetTxtRecordForVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_txt_record_for_verify(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        """
        @summary Generates a text (TXT) record. TXT records are used to retrieve domain names and subdomain names, enable the subdomain name verification feature, and perform batch retrievals.
        
        @param request: GetTxtRecordForVerifyRequest
        @return: GetTxtRecordForVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_txt_record_for_verify_with_options(request, runtime)

    async def get_txt_record_for_verify_async(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        """
        @summary Generates a text (TXT) record. TXT records are used to retrieve domain names and subdomain names, enable the subdomain name verification feature, and perform batch retrievals.
        
        @param request: GetTxtRecordForVerifyRequest
        @return: GetTxtRecordForVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_txt_record_for_verify_with_options_async(request, runtime)

    def list_cloud_gtm_address_pools_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAddressPoolsResponse:
        """
        @param request: ListCloudGtmAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAddressPoolsResponse:
        """
        @param request: ListCloudGtmAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_address_pools(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressPoolsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAddressPoolsResponse:
        """
        @param request: ListCloudGtmAddressPoolsRequest
        @return: ListCloudGtmAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_address_pools_with_options(request, runtime)

    async def list_cloud_gtm_address_pools_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressPoolsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAddressPoolsResponse:
        """
        @param request: ListCloudGtmAddressPoolsRequest
        @return: ListCloudGtmAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_address_pools_with_options_async(request, runtime)

    def list_cloud_gtm_addresses_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAddressesResponse:
        """
        @param request: ListCloudGtmAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.monitor_template_id):
            query['MonitorTemplateId'] = request.monitor_template_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAddresses',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_addresses_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAddressesResponse:
        """
        @param request: ListCloudGtmAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.monitor_template_id):
            query['MonitorTemplateId'] = request.monitor_template_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAddresses',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_addresses(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressesRequest,
    ) -> alidns_20150109_models.ListCloudGtmAddressesResponse:
        """
        @param request: ListCloudGtmAddressesRequest
        @return: ListCloudGtmAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_addresses_with_options(request, runtime)

    async def list_cloud_gtm_addresses_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAddressesRequest,
    ) -> alidns_20150109_models.ListCloudGtmAddressesResponse:
        """
        @param request: ListCloudGtmAddressesRequest
        @return: ListCloudGtmAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_addresses_with_options_async(request, runtime)

    def list_cloud_gtm_alert_logs_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmAlertLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAlertLogsResponse:
        """
        @param request: ListCloudGtmAlertLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAlertLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAlertLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAlertLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_alert_logs_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAlertLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAlertLogsResponse:
        """
        @param request: ListCloudGtmAlertLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAlertLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAlertLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAlertLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_alert_logs(
        self,
        request: alidns_20150109_models.ListCloudGtmAlertLogsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAlertLogsResponse:
        """
        @param request: ListCloudGtmAlertLogsRequest
        @return: ListCloudGtmAlertLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_alert_logs_with_options(request, runtime)

    async def list_cloud_gtm_alert_logs_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAlertLogsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAlertLogsResponse:
        """
        @param request: ListCloudGtmAlertLogsRequest
        @return: ListCloudGtmAlertLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_alert_logs_with_options_async(request, runtime)

    def list_cloud_gtm_available_alert_groups_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmAvailableAlertGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse:
        """
        @param request: ListCloudGtmAvailableAlertGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAvailableAlertGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAvailableAlertGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_available_alert_groups_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAvailableAlertGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse:
        """
        @param request: ListCloudGtmAvailableAlertGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmAvailableAlertGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmAvailableAlertGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_available_alert_groups(
        self,
        request: alidns_20150109_models.ListCloudGtmAvailableAlertGroupsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse:
        """
        @param request: ListCloudGtmAvailableAlertGroupsRequest
        @return: ListCloudGtmAvailableAlertGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_available_alert_groups_with_options(request, runtime)

    async def list_cloud_gtm_available_alert_groups_async(
        self,
        request: alidns_20150109_models.ListCloudGtmAvailableAlertGroupsRequest,
    ) -> alidns_20150109_models.ListCloudGtmAvailableAlertGroupsResponse:
        """
        @param request: ListCloudGtmAvailableAlertGroupsRequest
        @return: ListCloudGtmAvailableAlertGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_available_alert_groups_with_options_async(request, runtime)

    def list_cloud_gtm_instance_configs_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmInstanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmInstanceConfigsResponse:
        """
        @param request: ListCloudGtmInstanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmInstanceConfigs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_instance_configs_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmInstanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmInstanceConfigsResponse:
        """
        @param request: ListCloudGtmInstanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmInstanceConfigs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_instance_configs(
        self,
        request: alidns_20150109_models.ListCloudGtmInstanceConfigsRequest,
    ) -> alidns_20150109_models.ListCloudGtmInstanceConfigsResponse:
        """
        @param request: ListCloudGtmInstanceConfigsRequest
        @return: ListCloudGtmInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_instance_configs_with_options(request, runtime)

    async def list_cloud_gtm_instance_configs_async(
        self,
        request: alidns_20150109_models.ListCloudGtmInstanceConfigsRequest,
    ) -> alidns_20150109_models.ListCloudGtmInstanceConfigsResponse:
        """
        @param request: ListCloudGtmInstanceConfigsRequest
        @return: ListCloudGtmInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_instance_configs_with_options_async(request, runtime)

    def list_cloud_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmInstancesResponse:
        """
        @param request: ListCloudGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmInstancesResponse:
        """
        @param request: ListCloudGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_instances(
        self,
        request: alidns_20150109_models.ListCloudGtmInstancesRequest,
    ) -> alidns_20150109_models.ListCloudGtmInstancesResponse:
        """
        @param request: ListCloudGtmInstancesRequest
        @return: ListCloudGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_instances_with_options(request, runtime)

    async def list_cloud_gtm_instances_async(
        self,
        request: alidns_20150109_models.ListCloudGtmInstancesRequest,
    ) -> alidns_20150109_models.ListCloudGtmInstancesResponse:
        """
        @param request: ListCloudGtmInstancesRequest
        @return: ListCloudGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_instances_with_options_async(request, runtime)

    def list_cloud_gtm_monitor_nodes_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmMonitorNodesResponse:
        """
        @param request: ListCloudGtmMonitorNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmMonitorNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmMonitorNodes',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmMonitorNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_monitor_nodes_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmMonitorNodesResponse:
        """
        @param request: ListCloudGtmMonitorNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmMonitorNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmMonitorNodes',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmMonitorNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_monitor_nodes(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorNodesRequest,
    ) -> alidns_20150109_models.ListCloudGtmMonitorNodesResponse:
        """
        @param request: ListCloudGtmMonitorNodesRequest
        @return: ListCloudGtmMonitorNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_monitor_nodes_with_options(request, runtime)

    async def list_cloud_gtm_monitor_nodes_async(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorNodesRequest,
    ) -> alidns_20150109_models.ListCloudGtmMonitorNodesResponse:
        """
        @param request: ListCloudGtmMonitorNodesRequest
        @return: ListCloudGtmMonitorNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_monitor_nodes_with_options_async(request, runtime)

    def list_cloud_gtm_monitor_templates_with_options(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse:
        """
        @param request: ListCloudGtmMonitorTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmMonitorTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmMonitorTemplates',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_gtm_monitor_templates_with_options_async(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse:
        """
        @param request: ListCloudGtmMonitorTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudGtmMonitorTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudGtmMonitorTemplates',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_gtm_monitor_templates(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorTemplatesRequest,
    ) -> alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse:
        """
        @param request: ListCloudGtmMonitorTemplatesRequest
        @return: ListCloudGtmMonitorTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_gtm_monitor_templates_with_options(request, runtime)

    async def list_cloud_gtm_monitor_templates_async(
        self,
        request: alidns_20150109_models.ListCloudGtmMonitorTemplatesRequest,
    ) -> alidns_20150109_models.ListCloudGtmMonitorTemplatesResponse:
        """
        @param request: ListCloudGtmMonitorTemplatesRequest
        @return: ListCloudGtmMonitorTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_gtm_monitor_templates_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a specified resource.
        
        @description    Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a specified resource.
        
        @description    Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a specified resource.
        
        @description    Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to a specified resource.
        
        @description    Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_hichina_domain_dnswith_options(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        """
        @summary Calls the ModifyHichinaDomainDNS operation to change the name of a DNS server based on input parameters.
        
        @description If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        
        @param request: ModifyHichinaDomainDNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHichinaDomainDNSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHichinaDomainDNS',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ModifyHichinaDomainDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hichina_domain_dnswith_options_async(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        """
        @summary Calls the ModifyHichinaDomainDNS operation to change the name of a DNS server based on input parameters.
        
        @description If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        
        @param request: ModifyHichinaDomainDNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHichinaDomainDNSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHichinaDomainDNS',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ModifyHichinaDomainDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hichina_domain_dns(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        """
        @summary Calls the ModifyHichinaDomainDNS operation to change the name of a DNS server based on input parameters.
        
        @description If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        
        @param request: ModifyHichinaDomainDNSRequest
        @return: ModifyHichinaDomainDNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hichina_domain_dnswith_options(request, runtime)

    async def modify_hichina_domain_dns_async(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        """
        @summary Calls the ModifyHichinaDomainDNS operation to change the name of a DNS server based on input parameters.
        
        @description If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        
        @param request: ModifyHichinaDomainDNSRequest
        @return: ModifyHichinaDomainDNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hichina_domain_dnswith_options_async(request, runtime)

    def move_domain_resource_group_with_options(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        """
        @summary Moves a domain name to another resource group.
        
        @param request: MoveDomainResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveDomainResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveDomainResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveDomainResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_domain_resource_group_with_options_async(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        """
        @summary Moves a domain name to another resource group.
        
        @param request: MoveDomainResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveDomainResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveDomainResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveDomainResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_domain_resource_group(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        """
        @summary Moves a domain name to another resource group.
        
        @param request: MoveDomainResourceGroupRequest
        @return: MoveDomainResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_domain_resource_group_with_options(request, runtime)

    async def move_domain_resource_group_async(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        """
        @summary Moves a domain name to another resource group.
        
        @param request: MoveDomainResourceGroupRequest
        @return: MoveDomainResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_domain_resource_group_with_options_async(request, runtime)

    def move_gtm_resource_group_with_options(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        """
        @param request: MoveGtmResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveGtmResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveGtmResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveGtmResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_gtm_resource_group_with_options_async(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        """
        @param request: MoveGtmResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveGtmResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveGtmResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveGtmResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_gtm_resource_group(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        """
        @param request: MoveGtmResourceGroupRequest
        @return: MoveGtmResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_gtm_resource_group_with_options(request, runtime)

    async def move_gtm_resource_group_async(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        """
        @param request: MoveGtmResourceGroupRequest
        @return: MoveGtmResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_gtm_resource_group_with_options_async(request, runtime)

    def operate_batch_domain_with_options(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        """
        @summary Submits a batch operation task to add or delete multiple domain names or multiple Domain Name System (DNS) records at a time.
        
        @description Scenario: You need to execute a large number of tasks related to DNS resolution and you do not have high requirements for efficiency.
        
        @param request: OperateBatchDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBatchDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_record_info):
            query['DomainRecordInfo'] = request.domain_record_info
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBatchDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.OperateBatchDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_batch_domain_with_options_async(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        """
        @summary Submits a batch operation task to add or delete multiple domain names or multiple Domain Name System (DNS) records at a time.
        
        @description Scenario: You need to execute a large number of tasks related to DNS resolution and you do not have high requirements for efficiency.
        
        @param request: OperateBatchDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBatchDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_record_info):
            query['DomainRecordInfo'] = request.domain_record_info
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBatchDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.OperateBatchDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_batch_domain(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        """
        @summary Submits a batch operation task to add or delete multiple domain names or multiple Domain Name System (DNS) records at a time.
        
        @description Scenario: You need to execute a large number of tasks related to DNS resolution and you do not have high requirements for efficiency.
        
        @param request: OperateBatchDomainRequest
        @return: OperateBatchDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_batch_domain_with_options(request, runtime)

    async def operate_batch_domain_async(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        """
        @summary Submits a batch operation task to add or delete multiple domain names or multiple Domain Name System (DNS) records at a time.
        
        @description Scenario: You need to execute a large number of tasks related to DNS resolution and you do not have high requirements for efficiency.
        
        @param request: OperateBatchDomainRequest
        @return: OperateBatchDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_batch_domain_with_options_async(request, runtime)

    def pause_pdns_service_with_options(
        self,
        request: alidns_20150109_models.PausePdnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PausePdnsServiceResponse:
        """
        @summary 暂停公共DNS服务
        
        @param request: PausePdnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PausePdnsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PausePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PausePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_pdns_service_with_options_async(
        self,
        request: alidns_20150109_models.PausePdnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PausePdnsServiceResponse:
        """
        @summary 暂停公共DNS服务
        
        @param request: PausePdnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PausePdnsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PausePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PausePdnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_pdns_service(
        self,
        request: alidns_20150109_models.PausePdnsServiceRequest,
    ) -> alidns_20150109_models.PausePdnsServiceResponse:
        """
        @summary 暂停公共DNS服务
        
        @param request: PausePdnsServiceRequest
        @return: PausePdnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_pdns_service_with_options(request, runtime)

    async def pause_pdns_service_async(
        self,
        request: alidns_20150109_models.PausePdnsServiceRequest,
    ) -> alidns_20150109_models.PausePdnsServiceResponse:
        """
        @summary 暂停公共DNS服务
        
        @param request: PausePdnsServiceRequest
        @return: PausePdnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_pdns_service_with_options_async(request, runtime)

    def preview_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to preview a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: PreviewGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PreviewGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to preview a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: PreviewGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PreviewGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to preview a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: PreviewGtmRecoveryPlanRequest
        @return: PreviewGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preview_gtm_recovery_plan_with_options(request, runtime)

    async def preview_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        """
        @summary You can call this operation to preview a disaster recovery plan of a Global Traffic Manager (GTM) instance.
        
        @param request: PreviewGtmRecoveryPlanRequest
        @return: PreviewGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preview_gtm_recovery_plan_with_options_async(request, runtime)

    def remove_pdns_app_key_with_options(
        self,
        request: alidns_20150109_models.RemovePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RemovePdnsAppKeyResponse:
        """
        @summary 删除公共DNS AppKey
        
        @param request: RemovePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_pdns_app_key_with_options_async(
        self,
        request: alidns_20150109_models.RemovePdnsAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RemovePdnsAppKeyResponse:
        """
        @summary 删除公共DNS AppKey
        
        @param request: RemovePdnsAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePdnsAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_pdns_app_key(
        self,
        request: alidns_20150109_models.RemovePdnsAppKeyRequest,
    ) -> alidns_20150109_models.RemovePdnsAppKeyResponse:
        """
        @summary 删除公共DNS AppKey
        
        @param request: RemovePdnsAppKeyRequest
        @return: RemovePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_pdns_app_key_with_options(request, runtime)

    async def remove_pdns_app_key_async(
        self,
        request: alidns_20150109_models.RemovePdnsAppKeyRequest,
    ) -> alidns_20150109_models.RemovePdnsAppKeyResponse:
        """
        @summary 删除公共DNS AppKey
        
        @param request: RemovePdnsAppKeyRequest
        @return: RemovePdnsAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_pdns_app_key_with_options_async(request, runtime)

    def remove_pdns_udp_ip_segment_with_options(
        self,
        request: alidns_20150109_models.RemovePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RemovePdnsUdpIpSegmentResponse:
        """
        @summary 删除公共DNS Udp Ip地址段
        
        @param request: RemovePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_pdns_udp_ip_segment_with_options_async(
        self,
        request: alidns_20150109_models.RemovePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RemovePdnsUdpIpSegmentResponse:
        """
        @summary 删除公共DNS Udp Ip地址段
        
        @param request: RemovePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_pdns_udp_ip_segment(
        self,
        request: alidns_20150109_models.RemovePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.RemovePdnsUdpIpSegmentResponse:
        """
        @summary 删除公共DNS Udp Ip地址段
        
        @param request: RemovePdnsUdpIpSegmentRequest
        @return: RemovePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_pdns_udp_ip_segment_with_options(request, runtime)

    async def remove_pdns_udp_ip_segment_async(
        self,
        request: alidns_20150109_models.RemovePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.RemovePdnsUdpIpSegmentResponse:
        """
        @summary 删除公共DNS Udp Ip地址段
        
        @param request: RemovePdnsUdpIpSegmentRequest
        @return: RemovePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_pdns_udp_ip_segment_with_options_async(request, runtime)

    def replace_cloud_gtm_address_pool_address_with_options(
        self,
        tmp_req: alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse:
        """
        @param tmp_req: ReplaceCloudGtmAddressPoolAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceCloudGtmAddressPoolAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.addresses_shrink):
            query['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceCloudGtmAddressPoolAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_cloud_gtm_address_pool_address_with_options_async(
        self,
        tmp_req: alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse:
        """
        @param tmp_req: ReplaceCloudGtmAddressPoolAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceCloudGtmAddressPoolAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.addresses_shrink):
            query['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceCloudGtmAddressPoolAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_cloud_gtm_address_pool_address(
        self,
        request: alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressRequest,
    ) -> alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse:
        """
        @param request: ReplaceCloudGtmAddressPoolAddressRequest
        @return: ReplaceCloudGtmAddressPoolAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_cloud_gtm_address_pool_address_with_options(request, runtime)

    async def replace_cloud_gtm_address_pool_address_async(
        self,
        request: alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressRequest,
    ) -> alidns_20150109_models.ReplaceCloudGtmAddressPoolAddressResponse:
        """
        @param request: ReplaceCloudGtmAddressPoolAddressRequest
        @return: ReplaceCloudGtmAddressPoolAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.replace_cloud_gtm_address_pool_address_with_options_async(request, runtime)

    def replace_cloud_gtm_instance_config_address_pool_with_options(
        self,
        tmp_req: alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        """
        @param tmp_req: ReplaceCloudGtmInstanceConfigAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceCloudGtmInstanceConfigAddressPoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address_pools):
            request.address_pools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address_pools, 'AddressPools', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pools_shrink):
            query['AddressPools'] = request.address_pools_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceCloudGtmInstanceConfigAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_cloud_gtm_instance_config_address_pool_with_options_async(
        self,
        tmp_req: alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        """
        @param tmp_req: ReplaceCloudGtmInstanceConfigAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceCloudGtmInstanceConfigAddressPoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address_pools):
            request.address_pools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address_pools, 'AddressPools', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pools_shrink):
            query['AddressPools'] = request.address_pools_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceCloudGtmInstanceConfigAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_cloud_gtm_instance_config_address_pool(
        self,
        request: alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
    ) -> alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        """
        @param request: ReplaceCloudGtmInstanceConfigAddressPoolRequest
        @return: ReplaceCloudGtmInstanceConfigAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_cloud_gtm_instance_config_address_pool_with_options(request, runtime)

    async def replace_cloud_gtm_instance_config_address_pool_async(
        self,
        request: alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolRequest,
    ) -> alidns_20150109_models.ReplaceCloudGtmInstanceConfigAddressPoolResponse:
        """
        @param request: ReplaceCloudGtmInstanceConfigAddressPoolRequest
        @return: ReplaceCloudGtmInstanceConfigAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.replace_cloud_gtm_instance_config_address_pool_with_options_async(request, runtime)

    def resume_pdns_service_with_options(
        self,
        request: alidns_20150109_models.ResumePdnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ResumePdnsServiceResponse:
        """
        @summary 恢复公共DNS服务
        
        @param request: ResumePdnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumePdnsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ResumePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_pdns_service_with_options_async(
        self,
        request: alidns_20150109_models.ResumePdnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ResumePdnsServiceResponse:
        """
        @summary 恢复公共DNS服务
        
        @param request: ResumePdnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumePdnsServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ResumePdnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_pdns_service(
        self,
        request: alidns_20150109_models.ResumePdnsServiceRequest,
    ) -> alidns_20150109_models.ResumePdnsServiceResponse:
        """
        @summary 恢复公共DNS服务
        
        @param request: ResumePdnsServiceRequest
        @return: ResumePdnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_pdns_service_with_options(request, runtime)

    async def resume_pdns_service_async(
        self,
        request: alidns_20150109_models.ResumePdnsServiceRequest,
    ) -> alidns_20150109_models.ResumePdnsServiceResponse:
        """
        @summary 恢复公共DNS服务
        
        @param request: ResumePdnsServiceRequest
        @return: ResumePdnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_pdns_service_with_options_async(request, runtime)

    def retrieve_domain_with_options(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        """
        @summary Retrieves a domain name.
        
        @description To retrieve a domain name, you must verify a text (TXT) record. Therefore, before you call this API operation to retrieve a domain name, call the [GetTxtRecordForVerify](https://www.alibabacloud.com/help/zh/alibaba-cloud-dns/latest/generating-a-txt-record) operation to generate a TXT record.
        
        @param request: RetrieveDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RetrieveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_domain_with_options_async(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        """
        @summary Retrieves a domain name.
        
        @description To retrieve a domain name, you must verify a text (TXT) record. Therefore, before you call this API operation to retrieve a domain name, call the [GetTxtRecordForVerify](https://www.alibabacloud.com/help/zh/alibaba-cloud-dns/latest/generating-a-txt-record) operation to generate a TXT record.
        
        @param request: RetrieveDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RetrieveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_domain(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        """
        @summary Retrieves a domain name.
        
        @description To retrieve a domain name, you must verify a text (TXT) record. Therefore, before you call this API operation to retrieve a domain name, call the [GetTxtRecordForVerify](https://www.alibabacloud.com/help/zh/alibaba-cloud-dns/latest/generating-a-txt-record) operation to generate a TXT record.
        
        @param request: RetrieveDomainRequest
        @return: RetrieveDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retrieve_domain_with_options(request, runtime)

    async def retrieve_domain_async(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        """
        @summary Retrieves a domain name.
        
        @description To retrieve a domain name, you must verify a text (TXT) record. Therefore, before you call this API operation to retrieve a domain name, call the [GetTxtRecordForVerify](https://www.alibabacloud.com/help/zh/alibaba-cloud-dns/latest/generating-a-txt-record) operation to generate a TXT record.
        
        @param request: RetrieveDomainRequest
        @return: RetrieveDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_domain_with_options_async(request, runtime)

    def rollback_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        """
        @param request: RollbackGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RollbackGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        """
        @param request: RollbackGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RollbackGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        """
        @param request: RollbackGtmRecoveryPlanRequest
        @return: RollbackGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_gtm_recovery_plan_with_options(request, runtime)

    async def rollback_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        """
        @param request: RollbackGtmRecoveryPlanRequest
        @return: RollbackGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_gtm_recovery_plan_with_options_async(request, runtime)

    def search_cloud_gtm_address_pools_with_options(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmAddressPoolsResponse:
        """
        @param request: SearchCloudGtmAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmAddressPoolsResponse:
        """
        @param request: SearchCloudGtmAddressPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmAddressPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.address_pool_type):
            query['AddressPoolType'] = request.address_pool_type
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmAddressPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_address_pools(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressPoolsRequest,
    ) -> alidns_20150109_models.SearchCloudGtmAddressPoolsResponse:
        """
        @param request: SearchCloudGtmAddressPoolsRequest
        @return: SearchCloudGtmAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_cloud_gtm_address_pools_with_options(request, runtime)

    async def search_cloud_gtm_address_pools_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressPoolsRequest,
    ) -> alidns_20150109_models.SearchCloudGtmAddressPoolsResponse:
        """
        @param request: SearchCloudGtmAddressPoolsRequest
        @return: SearchCloudGtmAddressPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_cloud_gtm_address_pools_with_options_async(request, runtime)

    def search_cloud_gtm_addresses_with_options(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmAddressesResponse:
        """
        @param request: SearchCloudGtmAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.monitor_template_name):
            query['MonitorTemplateName'] = request.monitor_template_name
        if not UtilClient.is_unset(request.name_search_condition):
            query['NameSearchCondition'] = request.name_search_condition
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark_search_condition):
            query['RemarkSearchCondition'] = request.remark_search_condition
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmAddresses',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_addresses_with_options_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmAddressesResponse:
        """
        @param request: SearchCloudGtmAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmAddressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.monitor_template_name):
            query['MonitorTemplateName'] = request.monitor_template_name
        if not UtilClient.is_unset(request.name_search_condition):
            query['NameSearchCondition'] = request.name_search_condition
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark_search_condition):
            query['RemarkSearchCondition'] = request.remark_search_condition
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmAddresses',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_addresses(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmAddressesResponse:
        """
        @param request: SearchCloudGtmAddressesRequest
        @return: SearchCloudGtmAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_cloud_gtm_addresses_with_options(request, runtime)

    async def search_cloud_gtm_addresses_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmAddressesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmAddressesResponse:
        """
        @param request: SearchCloudGtmAddressesRequest
        @return: SearchCloudGtmAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_cloud_gtm_addresses_with_options_async(request, runtime)

    def search_cloud_gtm_instance_configs_with_options(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse:
        """
        @param request: SearchCloudGtmInstanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmInstanceConfigs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_instance_configs_with_options_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse:
        """
        @param request: SearchCloudGtmInstanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.available_status):
            query['AvailableStatus'] = request.available_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.schedule_domain_name):
            query['ScheduleDomainName'] = request.schedule_domain_name
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmInstanceConfigs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_instance_configs(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstanceConfigsRequest,
    ) -> alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse:
        """
        @param request: SearchCloudGtmInstanceConfigsRequest
        @return: SearchCloudGtmInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_cloud_gtm_instance_configs_with_options(request, runtime)

    async def search_cloud_gtm_instance_configs_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstanceConfigsRequest,
    ) -> alidns_20150109_models.SearchCloudGtmInstanceConfigsResponse:
        """
        @param request: SearchCloudGtmInstanceConfigsRequest
        @return: SearchCloudGtmInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_cloud_gtm_instance_configs_with_options_async(request, runtime)

    def search_cloud_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmInstancesResponse:
        """
        @param request: SearchCloudGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmInstancesResponse:
        """
        @param request: SearchCloudGtmInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_instances(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstancesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmInstancesResponse:
        """
        @param request: SearchCloudGtmInstancesRequest
        @return: SearchCloudGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_cloud_gtm_instances_with_options(request, runtime)

    async def search_cloud_gtm_instances_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmInstancesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmInstancesResponse:
        """
        @param request: SearchCloudGtmInstancesRequest
        @return: SearchCloudGtmInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_cloud_gtm_instances_with_options_async(request, runtime)

    def search_cloud_gtm_monitor_templates_with_options(
        self,
        request: alidns_20150109_models.SearchCloudGtmMonitorTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse:
        """
        @param request: SearchCloudGtmMonitorTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmMonitorTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmMonitorTemplates',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cloud_gtm_monitor_templates_with_options_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmMonitorTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse:
        """
        @param request: SearchCloudGtmMonitorTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchCloudGtmMonitorTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchCloudGtmMonitorTemplates',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cloud_gtm_monitor_templates(
        self,
        request: alidns_20150109_models.SearchCloudGtmMonitorTemplatesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse:
        """
        @param request: SearchCloudGtmMonitorTemplatesRequest
        @return: SearchCloudGtmMonitorTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_cloud_gtm_monitor_templates_with_options(request, runtime)

    async def search_cloud_gtm_monitor_templates_async(
        self,
        request: alidns_20150109_models.SearchCloudGtmMonitorTemplatesRequest,
    ) -> alidns_20150109_models.SearchCloudGtmMonitorTemplatesResponse:
        """
        @param request: SearchCloudGtmMonitorTemplatesRequest
        @return: SearchCloudGtmMonitorTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_cloud_gtm_monitor_templates_with_options_async(request, runtime)

    def set_dnsslbstatus_with_options(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        """
        @summary Enables or disables weighted round-robin based on the specified parameters.
        
        @param request: SetDNSSLBStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDNSSLBStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDNSSLBStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDNSSLBStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dnsslbstatus_with_options_async(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        """
        @summary Enables or disables weighted round-robin based on the specified parameters.
        
        @param request: SetDNSSLBStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDNSSLBStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDNSSLBStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDNSSLBStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dnsslbstatus(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        """
        @summary Enables or disables weighted round-robin based on the specified parameters.
        
        @param request: SetDNSSLBStatusRequest
        @return: SetDNSSLBStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dnsslbstatus_with_options(request, runtime)

    async def set_dnsslbstatus_async(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        """
        @summary Enables or disables weighted round-robin based on the specified parameters.
        
        @param request: SetDNSSLBStatusRequest
        @return: SetDNSSLBStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dnsslbstatus_with_options_async(request, runtime)

    def set_dns_gtm_access_mode_with_options(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        """
        @description ***\
        
        @param request: SetDnsGtmAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDnsGtmAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dns_gtm_access_mode_with_options_async(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        """
        @description ***\
        
        @param request: SetDnsGtmAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDnsGtmAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dns_gtm_access_mode(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        """
        @description ***\
        
        @param request: SetDnsGtmAccessModeRequest
        @return: SetDnsGtmAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_access_mode_with_options(request, runtime)

    async def set_dns_gtm_access_mode_async(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        """
        @description ***\
        
        @param request: SetDnsGtmAccessModeRequest
        @return: SetDnsGtmAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dns_gtm_access_mode_with_options_async(request, runtime)

    def set_dns_gtm_monitor_status_with_options(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        """
        @summary Specifies the health check status of an address pool.
        
        @param request: SetDnsGtmMonitorStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDnsGtmMonitorStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dns_gtm_monitor_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        """
        @summary Specifies the health check status of an address pool.
        
        @param request: SetDnsGtmMonitorStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDnsGtmMonitorStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmMonitorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dns_gtm_monitor_status(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        """
        @summary Specifies the health check status of an address pool.
        
        @param request: SetDnsGtmMonitorStatusRequest
        @return: SetDnsGtmMonitorStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_monitor_status_with_options(request, runtime)

    async def set_dns_gtm_monitor_status_async(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        """
        @summary Specifies the health check status of an address pool.
        
        @param request: SetDnsGtmMonitorStatusRequest
        @return: SetDnsGtmMonitorStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dns_gtm_monitor_status_with_options_async(request, runtime)

    def set_domain_dnssec_status_with_options(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        """
        @summary Sets the Domain Name System Security Extensions (DNSSEC) status of a domain name.
        
        @param request: SetDomainDnssecStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainDnssecStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainDnssecStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainDnssecStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_dnssec_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        """
        @summary Sets the Domain Name System Security Extensions (DNSSEC) status of a domain name.
        
        @param request: SetDomainDnssecStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainDnssecStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainDnssecStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainDnssecStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_dnssec_status(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        """
        @summary Sets the Domain Name System Security Extensions (DNSSEC) status of a domain name.
        
        @param request: SetDomainDnssecStatusRequest
        @return: SetDomainDnssecStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_dnssec_status_with_options(request, runtime)

    async def set_domain_dnssec_status_async(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        """
        @summary Sets the Domain Name System Security Extensions (DNSSEC) status of a domain name.
        
        @param request: SetDomainDnssecStatusRequest
        @return: SetDomainDnssecStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_dnssec_status_with_options_async(request, runtime)

    def set_domain_record_status_with_options(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: SetDomainRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainRecordStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_record_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: SetDomainRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainRecordStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_record_status(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: SetDomainRecordStatusRequest
        @return: SetDomainRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_record_status_with_options(request, runtime)

    async def set_domain_record_status_async(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        """
        @summary Specifies the status of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: SetDomainRecordStatusRequest
        @return: SetDomainRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_record_status_with_options_async(request, runtime)

    def set_gtm_access_mode_with_options(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        """
        @param request: SetGtmAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGtmAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gtm_access_mode_with_options_async(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        """
        @param request: SetGtmAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGtmAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gtm_access_mode(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        """
        @param request: SetGtmAccessModeRequest
        @return: SetGtmAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_access_mode_with_options(request, runtime)

    async def set_gtm_access_mode_async(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        """
        @param request: SetGtmAccessModeRequest
        @return: SetGtmAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_gtm_access_mode_with_options_async(request, runtime)

    def set_gtm_monitor_status_with_options(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        """
        @param request: SetGtmMonitorStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGtmMonitorStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gtm_monitor_status_with_options_async(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        """
        @param request: SetGtmMonitorStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGtmMonitorStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmMonitorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gtm_monitor_status(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        """
        @param request: SetGtmMonitorStatusRequest
        @return: SetGtmMonitorStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_monitor_status_with_options(request, runtime)

    async def set_gtm_monitor_status_async(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        """
        @param request: SetGtmMonitorStatusRequest
        @return: SetGtmMonitorStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_gtm_monitor_status_with_options_async(request, runtime)

    def submit_isp_flush_cache_task_with_options(
        self,
        request: alidns_20150109_models.SubmitIspFlushCacheTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SubmitIspFlushCacheTaskResponse:
        """
        @summary 提交缓存刷新任务
        
        @param request: SubmitIspFlushCacheTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIspFlushCacheTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SubmitIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_isp_flush_cache_task_with_options_async(
        self,
        request: alidns_20150109_models.SubmitIspFlushCacheTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SubmitIspFlushCacheTaskResponse:
        """
        @summary 提交缓存刷新任务
        
        @param request: SubmitIspFlushCacheTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIspFlushCacheTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SubmitIspFlushCacheTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_isp_flush_cache_task(
        self,
        request: alidns_20150109_models.SubmitIspFlushCacheTaskRequest,
    ) -> alidns_20150109_models.SubmitIspFlushCacheTaskResponse:
        """
        @summary 提交缓存刷新任务
        
        @param request: SubmitIspFlushCacheTaskRequest
        @return: SubmitIspFlushCacheTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_isp_flush_cache_task_with_options(request, runtime)

    async def submit_isp_flush_cache_task_async(
        self,
        request: alidns_20150109_models.SubmitIspFlushCacheTaskRequest,
    ) -> alidns_20150109_models.SubmitIspFlushCacheTaskResponse:
        """
        @summary 提交缓存刷新任务
        
        @param request: SubmitIspFlushCacheTaskRequest
        @return: SubmitIspFlushCacheTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_isp_flush_cache_task_with_options_async(request, runtime)

    def switch_dns_gtm_instance_strategy_mode_with_options(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        """
        @summary Changes the access policy type for a Global Traffic Manager (GTM) instance.
        
        @param request: SwitchDnsGtmInstanceStrategyModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDnsGtmInstanceStrategyModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDnsGtmInstanceStrategyMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dns_gtm_instance_strategy_mode_with_options_async(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        """
        @summary Changes the access policy type for a Global Traffic Manager (GTM) instance.
        
        @param request: SwitchDnsGtmInstanceStrategyModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDnsGtmInstanceStrategyModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDnsGtmInstanceStrategyMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dns_gtm_instance_strategy_mode(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        """
        @summary Changes the access policy type for a Global Traffic Manager (GTM) instance.
        
        @param request: SwitchDnsGtmInstanceStrategyModeRequest
        @return: SwitchDnsGtmInstanceStrategyModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dns_gtm_instance_strategy_mode_with_options(request, runtime)

    async def switch_dns_gtm_instance_strategy_mode_async(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        """
        @summary Changes the access policy type for a Global Traffic Manager (GTM) instance.
        
        @param request: SwitchDnsGtmInstanceStrategyModeRequest
        @return: SwitchDnsGtmInstanceStrategyModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_dns_gtm_instance_strategy_mode_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TagResourcesResponse:
        """
        @summary Adds and modifies a tag for a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TagResourcesResponse:
        """
        @summary Adds and modifies a tag for a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
    ) -> alidns_20150109_models.TagResourcesResponse:
        """
        @summary Adds and modifies a tag for a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
    ) -> alidns_20150109_models.TagResourcesResponse:
        """
        @summary Adds and modifies a tag for a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_domain_with_options(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TransferDomainResponse:
        """
        @summary Transfers multiple domain names from the current account to another account at a time.
        
        @param request: TransferDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TransferDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_domain_with_options_async(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TransferDomainResponse:
        """
        @summary Transfers multiple domain names from the current account to another account at a time.
        
        @param request: TransferDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TransferDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_domain(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
    ) -> alidns_20150109_models.TransferDomainResponse:
        """
        @summary Transfers multiple domain names from the current account to another account at a time.
        
        @param request: TransferDomainRequest
        @return: TransferDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_domain_with_options(request, runtime)

    async def transfer_domain_async(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
    ) -> alidns_20150109_models.TransferDomainResponse:
        """
        @summary Transfers multiple domain names from the current account to another account at a time.
        
        @param request: TransferDomainRequest
        @return: TransferDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_domain_with_options_async(request, runtime)

    def unbind_instance_domains_with_options(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        """
        @summary Unbinds one or more domain names from a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call an API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call an API operation to bind only one domain name to the instance. However, if the instance that you want to bind to the desired domain name is already bound to a domain name, you can call this operation to unbind the original domain name from the instance and then bind the desired domain name to the instance.
        
        @param request: UnbindInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UnbindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        """
        @summary Unbinds one or more domain names from a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call an API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call an API operation to bind only one domain name to the instance. However, if the instance that you want to bind to the desired domain name is already bound to a domain name, you can call this operation to unbind the original domain name from the instance and then bind the desired domain name to the instance.
        
        @param request: UnbindInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UnbindInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_instance_domains(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        """
        @summary Unbinds one or more domain names from a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call an API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call an API operation to bind only one domain name to the instance. However, if the instance that you want to bind to the desired domain name is already bound to a domain name, you can call this operation to unbind the original domain name from the instance and then bind the desired domain name to the instance.
        
        @param request: UnbindInstanceDomainsRequest
        @return: UnbindInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_instance_domains_with_options(request, runtime)

    async def unbind_instance_domains_async(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        """
        @summary Unbinds one or more domain names from a paid Alibaba Cloud DNS instance based on the instance ID.
        
        @description A paid Alibaba Cloud DNS instance whose ID starts with dns is an instance of the new version. You can call an API operation to bind multiple domain names to the instance. If the upper limit is exceeded, an error message is returned.\\
        A paid Alibaba Cloud DNS instance whose ID does not start with dns is an instance of the old version. You can call an API operation to bind only one domain name to the instance. However, if the instance that you want to bind to the desired domain name is already bound to a domain name, you can call this operation to unbind the original domain name from the instance and then bind the desired domain name to the instance.
        
        @param request: UnbindInstanceDomainsRequest
        @return: UnbindInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_instance_domains_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_app_key_state_with_options(
        self,
        request: alidns_20150109_models.UpdateAppKeyStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateAppKeyStateResponse:
        """
        @summary 修改 AppKey 状态
        
        @param request: UpdateAppKeyStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppKeyStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppKeyState',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateAppKeyStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_key_state_with_options_async(
        self,
        request: alidns_20150109_models.UpdateAppKeyStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateAppKeyStateResponse:
        """
        @summary 修改 AppKey 状态
        
        @param request: UpdateAppKeyStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppKeyStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppKeyState',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateAppKeyStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_key_state(
        self,
        request: alidns_20150109_models.UpdateAppKeyStateRequest,
    ) -> alidns_20150109_models.UpdateAppKeyStateResponse:
        """
        @summary 修改 AppKey 状态
        
        @param request: UpdateAppKeyStateRequest
        @return: UpdateAppKeyStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_key_state_with_options(request, runtime)

    async def update_app_key_state_async(
        self,
        request: alidns_20150109_models.UpdateAppKeyStateRequest,
    ) -> alidns_20150109_models.UpdateAppKeyStateResponse:
        """
        @summary 修改 AppKey 状态
        
        @param request: UpdateAppKeyStateRequest
        @return: UpdateAppKeyStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_app_key_state_with_options_async(request, runtime)

    def update_cloud_gtm_address_with_options(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressResponse:
        """
        @param tmp_req: UpdateCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.health_tasks):
            request.health_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_with_options_async(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressResponse:
        """
        @param tmp_req: UpdateCloudGtmAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmAddressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.health_tasks):
            request.health_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.health_tasks, 'HealthTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.attribute_info):
            query['AttributeInfo'] = request.attribute_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        if not UtilClient.is_unset(request.health_tasks_shrink):
            query['HealthTasks'] = request.health_tasks_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddress',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressResponse:
        """
        @param request: UpdateCloudGtmAddressRequest
        @return: UpdateCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_with_options(request, runtime)

    async def update_cloud_gtm_address_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressResponse:
        """
        @param request: UpdateCloudGtmAddressRequest
        @return: UpdateCloudGtmAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_with_options_async(request, runtime)

    def update_cloud_gtm_address_enable_status_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_enable_status_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_enable_status(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressEnableStatusRequest
        @return: UpdateCloudGtmAddressEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_address_enable_status_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressEnableStatusRequest
        @return: UpdateCloudGtmAddressEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_manual_available_status_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressManualAvailableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressManualAvailableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressManualAvailableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_manual_available_status_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressManualAvailableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressManualAvailableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.available_mode):
            query['AvailableMode'] = request.available_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.manual_available_status):
            query['ManualAvailableStatus'] = request.manual_available_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressManualAvailableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_manual_available_status(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressManualAvailableStatusRequest
        @return: UpdateCloudGtmAddressManualAvailableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_manual_available_status_with_options(request, runtime)

    async def update_cloud_gtm_address_manual_available_status_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressManualAvailableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressManualAvailableStatusRequest
        @return: UpdateCloudGtmAddressManualAvailableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_manual_available_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_basic_config_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        """
        @param request: UpdateCloudGtmAddressPoolBasicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolBasicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolBasicConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_basic_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        """
        @param request: UpdateCloudGtmAddressPoolBasicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolBasicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.address_pool_name):
            query['AddressPoolName'] = request.address_pool_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.health_judgement):
            query['HealthJudgement'] = request.health_judgement
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolBasicConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_basic_config(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        """
        @param request: UpdateCloudGtmAddressPoolBasicConfigRequest
        @return: UpdateCloudGtmAddressPoolBasicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_pool_basic_config_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_basic_config_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolBasicConfigResponse:
        """
        @param request: UpdateCloudGtmAddressPoolBasicConfigRequest
        @return: UpdateCloudGtmAddressPoolBasicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_basic_config_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_enable_status_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressPoolEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_enable_status_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressPoolEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_enable_status(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressPoolEnableStatusRequest
        @return: UpdateCloudGtmAddressPoolEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_pool_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_enable_status_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolEnableStatusResponse:
        """
        @param request: UpdateCloudGtmAddressPoolEnableStatusRequest
        @return: UpdateCloudGtmAddressPoolEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_lb_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        """
        @param request: UpdateCloudGtmAddressPoolLbStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolLbStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_lb_strategy):
            query['AddressLbStrategy'] = request.address_lb_strategy
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolLbStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_lb_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        """
        @param request: UpdateCloudGtmAddressPoolLbStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolLbStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_lb_strategy):
            query['AddressLbStrategy'] = request.address_lb_strategy
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolLbStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_lb_strategy(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        """
        @param request: UpdateCloudGtmAddressPoolLbStrategyRequest
        @return: UpdateCloudGtmAddressPoolLbStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_pool_lb_strategy_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_lb_strategy_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolLbStrategyResponse:
        """
        @param request: UpdateCloudGtmAddressPoolLbStrategyRequest
        @return: UpdateCloudGtmAddressPoolLbStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_lb_strategy_with_options_async(request, runtime)

    def update_cloud_gtm_address_pool_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressPoolRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_pool_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressPoolRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressPoolRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressPoolRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_pool_remark(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressPoolRemarkRequest
        @return: UpdateCloudGtmAddressPoolRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_pool_remark_with_options(request, runtime)

    async def update_cloud_gtm_address_pool_remark_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressPoolRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressPoolRemarkRequest
        @return: UpdateCloudGtmAddressPoolRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_pool_remark_with_options_async(request, runtime)

    def update_cloud_gtm_address_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_address_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmAddressRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmAddressRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_address_remark(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressRemarkRequest
        @return: UpdateCloudGtmAddressRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_address_remark_with_options(request, runtime)

    async def update_cloud_gtm_address_remark_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmAddressRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmAddressRemarkResponse:
        """
        @param request: UpdateCloudGtmAddressRemarkRequest
        @return: UpdateCloudGtmAddressRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_address_remark_with_options_async(request, runtime)

    def update_cloud_gtm_global_alert_with_options(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmGlobalAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse:
        """
        @param tmp_req: UpdateCloudGtmGlobalAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmGlobalAlertResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmGlobalAlertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_config):
            request.alert_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not UtilClient.is_unset(tmp_req.alert_group):
            request.alert_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not UtilClient.is_unset(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmGlobalAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_global_alert_with_options_async(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmGlobalAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse:
        """
        @param tmp_req: UpdateCloudGtmGlobalAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmGlobalAlertResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmGlobalAlertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_config):
            request.alert_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not UtilClient.is_unset(tmp_req.alert_group):
            request.alert_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not UtilClient.is_unset(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmGlobalAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_global_alert(
        self,
        request: alidns_20150109_models.UpdateCloudGtmGlobalAlertRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse:
        """
        @param request: UpdateCloudGtmGlobalAlertRequest
        @return: UpdateCloudGtmGlobalAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_global_alert_with_options(request, runtime)

    async def update_cloud_gtm_global_alert_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmGlobalAlertRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmGlobalAlertResponse:
        """
        @param request: UpdateCloudGtmGlobalAlertRequest
        @return: UpdateCloudGtmGlobalAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_global_alert_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_alert_with_options(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse:
        """
        @param tmp_req: UpdateCloudGtmInstanceConfigAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigAlertResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_config):
            request.alert_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not UtilClient.is_unset(tmp_req.alert_group):
            request.alert_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not UtilClient.is_unset(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not UtilClient.is_unset(request.alert_mode):
            query['AlertMode'] = request.alert_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_alert_with_options_async(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse:
        """
        @param tmp_req: UpdateCloudGtmInstanceConfigAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigAlertResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_config):
            request.alert_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_config, 'AlertConfig', 'json')
        if not UtilClient.is_unset(tmp_req.alert_group):
            request.alert_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_group, 'AlertGroup', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.alert_config_shrink):
            query['AlertConfig'] = request.alert_config_shrink
        if not UtilClient.is_unset(request.alert_group_shrink):
            query['AlertGroup'] = request.alert_group_shrink
        if not UtilClient.is_unset(request.alert_mode):
            query['AlertMode'] = request.alert_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigAlert',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_alert(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigAlertRequest
        @return: UpdateCloudGtmInstanceConfigAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_config_alert_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_alert_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigAlertResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigAlertRequest
        @return: UpdateCloudGtmInstanceConfigAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_alert_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_basic_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigBasicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigBasicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigBasic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_basic_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigBasicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigBasicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.schedule_hostname):
            query['ScheduleHostname'] = request.schedule_hostname
        if not UtilClient.is_unset(request.schedule_zone_name):
            query['ScheduleZoneName'] = request.schedule_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigBasic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_basic(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigBasicRequest
        @return: UpdateCloudGtmInstanceConfigBasicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_config_basic_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_basic_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigBasicResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigBasicRequest
        @return: UpdateCloudGtmInstanceConfigBasicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_basic_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_enable_status_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_enable_status_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigEnableStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigEnableStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigEnableStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_enable_status(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigEnableStatusRequest
        @return: UpdateCloudGtmInstanceConfigEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_config_enable_status_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_enable_status_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigEnableStatusResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigEnableStatusRequest
        @return: UpdateCloudGtmInstanceConfigEnableStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_enable_status_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_lb_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigLbStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigLbStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_lb_strategy):
            query['AddressPoolLbStrategy'] = request.address_pool_lb_strategy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigLbStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_lb_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigLbStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigLbStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address_pool_lb_strategy):
            query['AddressPoolLbStrategy'] = request.address_pool_lb_strategy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sequence_lb_strategy_mode):
            query['SequenceLbStrategyMode'] = request.sequence_lb_strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigLbStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_lb_strategy(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigLbStrategyRequest
        @return: UpdateCloudGtmInstanceConfigLbStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_config_lb_strategy_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_lb_strategy_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigLbStrategyResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigLbStrategyRequest
        @return: UpdateCloudGtmInstanceConfigLbStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_lb_strategy_with_options_async(request, runtime)

    def update_cloud_gtm_instance_config_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_config_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceConfigRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceConfigRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_config_remark(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigRemarkRequest
        @return: UpdateCloudGtmInstanceConfigRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_config_remark_with_options(request, runtime)

    async def update_cloud_gtm_instance_config_remark_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceConfigRemarkResponse:
        """
        @param request: UpdateCloudGtmInstanceConfigRemarkRequest
        @return: UpdateCloudGtmInstanceConfigRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_config_remark_with_options_async(request, runtime)

    def update_cloud_gtm_instance_name_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceNameResponse:
        """
        @param request: UpdateCloudGtmInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_instance_name_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceNameResponse:
        """
        @param request: UpdateCloudGtmInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmInstanceName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_instance_name(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceNameRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceNameResponse:
        """
        @param request: UpdateCloudGtmInstanceNameRequest
        @return: UpdateCloudGtmInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_instance_name_with_options(request, runtime)

    async def update_cloud_gtm_instance_name_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmInstanceNameRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmInstanceNameResponse:
        """
        @param request: UpdateCloudGtmInstanceNameRequest
        @return: UpdateCloudGtmInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_instance_name_with_options_async(request, runtime)

    def update_cloud_gtm_monitor_template_with_options(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse:
        """
        @param tmp_req: UpdateCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmMonitorTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_monitor_template_with_options_async(
        self,
        tmp_req: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse:
        """
        @param tmp_req: UpdateCloudGtmMonitorTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmMonitorTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alidns_20150109_models.UpdateCloudGtmMonitorTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.isp_city_nodes):
            request.isp_city_nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.isp_city_nodes, 'IspCityNodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.failure_rate):
            query['FailureRate'] = request.failure_rate
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_nodes_shrink):
            query['IspCityNodes'] = request.isp_city_nodes_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmMonitorTemplate',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_monitor_template(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRequest
        @return: UpdateCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_monitor_template_with_options(request, runtime)

    async def update_cloud_gtm_monitor_template_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRequest
        @return: UpdateCloudGtmMonitorTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_monitor_template_with_options_async(request, runtime)

    def update_cloud_gtm_monitor_template_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmMonitorTemplateRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmMonitorTemplateRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_gtm_monitor_template_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudGtmMonitorTemplateRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudGtmMonitorTemplateRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_gtm_monitor_template_remark(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRemarkRequest
        @return: UpdateCloudGtmMonitorTemplateRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_gtm_monitor_template_remark_with_options(request, runtime)

    async def update_cloud_gtm_monitor_template_remark_async(
        self,
        request: alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkRequest,
    ) -> alidns_20150109_models.UpdateCloudGtmMonitorTemplateRemarkResponse:
        """
        @param request: UpdateCloudGtmMonitorTemplateRemarkRequest
        @return: UpdateCloudGtmMonitorTemplateRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_gtm_monitor_template_remark_with_options_async(request, runtime)

    def update_custom_line_with_options(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        """
        @summary Modifies a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: UpdateCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        """
        @summary Modifies a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: UpdateCustomLineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_line(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        """
        @summary Modifies a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: UpdateCustomLineRequest
        @return: UpdateCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    async def update_custom_line_async(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        """
        @summary Modifies a custom line.
        
        @description In each CIDR block, the end IP address must be greater than or equal to the start IP address.\\
        The CIDR blocks that are specified for all custom lines of a domain name cannot be overlapped.
        
        @param request: UpdateCustomLineRequest
        @return: UpdateCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_line_with_options_async(request, runtime)

    def update_dnsslbweight_with_options(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        """
        @summary Modifies the weight of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDNSSLBWeightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDNSSLBWeightResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSSLBWeight',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDNSSLBWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dnsslbweight_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        """
        @summary Modifies the weight of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDNSSLBWeightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDNSSLBWeightResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSSLBWeight',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDNSSLBWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dnsslbweight(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        """
        @summary Modifies the weight of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDNSSLBWeightRequest
        @return: UpdateDNSSLBWeightResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dnsslbweight_with_options(request, runtime)

    async def update_dnsslbweight_async(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        """
        @summary Modifies the weight of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDNSSLBWeightRequest
        @return: UpdateDNSSLBWeightResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dnsslbweight_with_options_async(request, runtime)

    def update_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        """
        @param request: UpdateDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_cache_domain_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        """
        @param request: UpdateDnsCacheDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsCacheDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_cache_domain(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        """
        @param request: UpdateDnsCacheDomainRequest
        @return: UpdateDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_with_options(request, runtime)

    async def update_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        """
        @param request: UpdateDnsCacheDomainRequest
        @return: UpdateDnsCacheDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_cache_domain_with_options_async(request, runtime)

    def update_dns_cache_domain_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        """
        @param request: UpdateDnsCacheDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsCacheDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_cache_domain_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        """
        @param request: UpdateDnsCacheDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsCacheDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_cache_domain_remark(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        """
        @param request: UpdateDnsCacheDomainRemarkRequest
        @return: UpdateDnsCacheDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_remark_with_options(request, runtime)

    async def update_dns_cache_domain_remark_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        """
        @param request: UpdateDnsCacheDomainRemarkRequest
        @return: UpdateDnsCacheDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_cache_domain_remark_with_options_async(request, runtime)

    def update_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        """
        @summary Modifies an access policy.
        
        @param request: UpdateDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        """
        @summary Modifies an access policy.
        
        @param request: UpdateDnsGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_access_strategy(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        """
        @summary Modifies an access policy.
        
        @param request: UpdateDnsGtmAccessStrategyRequest
        @return: UpdateDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_access_strategy_with_options(request, runtime)

    async def update_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        """
        @summary Modifies an access policy.
        
        @param request: UpdateDnsGtmAccessStrategyRequest
        @return: UpdateDnsGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_access_strategy_with_options_async(request, runtime)

    def update_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        """
        @summary Modifies the configurations of address pools for a GTM instance.
        
        @param request: UpdateDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        """
        @summary Modifies the configurations of address pools for a GTM instance.
        
        @param request: UpdateDnsGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_address_pool(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        """
        @summary Modifies the configurations of address pools for a GTM instance.
        
        @param request: UpdateDnsGtmAddressPoolRequest
        @return: UpdateDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_address_pool_with_options(request, runtime)

    async def update_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        """
        @summary Modifies the configurations of address pools for a GTM instance.
        
        @param request: UpdateDnsGtmAddressPoolRequest
        @return: UpdateDnsGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_address_pool_with_options_async(request, runtime)

    def update_dns_gtm_instance_global_config_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateDnsGtmInstanceGlobalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmInstanceGlobalConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.force_update):
            query['ForceUpdate'] = request.force_update
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.public_cname_mode):
            query['PublicCnameMode'] = request.public_cname_mode
        if not UtilClient.is_unset(request.public_rr):
            query['PublicRr'] = request.public_rr
        if not UtilClient.is_unset(request.public_user_domain_name):
            query['PublicUserDomainName'] = request.public_user_domain_name
        if not UtilClient.is_unset(request.public_zone_name):
            query['PublicZoneName'] = request.public_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_instance_global_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateDnsGtmInstanceGlobalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmInstanceGlobalConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.force_update):
            query['ForceUpdate'] = request.force_update
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.public_cname_mode):
            query['PublicCnameMode'] = request.public_cname_mode
        if not UtilClient.is_unset(request.public_rr):
            query['PublicRr'] = request.public_rr
        if not UtilClient.is_unset(request.public_user_domain_name):
            query['PublicUserDomainName'] = request.public_user_domain_name
        if not UtilClient.is_unset(request.public_zone_name):
            query['PublicZoneName'] = request.public_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_instance_global_config(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateDnsGtmInstanceGlobalConfigRequest
        @return: UpdateDnsGtmInstanceGlobalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_instance_global_config_with_options(request, runtime)

    async def update_dns_gtm_instance_global_config_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateDnsGtmInstanceGlobalConfigRequest
        @return: UpdateDnsGtmInstanceGlobalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_instance_global_config_with_options_async(request, runtime)

    def update_dns_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        """
        @summary Modifies a health check task.
        
        @param request: UpdateDnsGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dns_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        """
        @summary Modifies a health check task.
        
        @param request: UpdateDnsGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDnsGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dns_gtm_monitor(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        """
        @summary Modifies a health check task.
        
        @param request: UpdateDnsGtmMonitorRequest
        @return: UpdateDnsGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_monitor_with_options(request, runtime)

    async def update_dns_gtm_monitor_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        """
        @summary Modifies a health check task.
        
        @param request: UpdateDnsGtmMonitorRequest
        @return: UpdateDnsGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_monitor_with_options_async(request, runtime)

    def update_domain_group_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        """
        @summary Modifies the name of a domain name group based on the specified parameters.
        
        @param request: UpdateDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        """
        @summary Modifies the name of a domain name group based on the specified parameters.
        
        @param request: UpdateDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_group(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        """
        @summary Modifies the name of a domain name group based on the specified parameters.
        
        @param request: UpdateDomainGroupRequest
        @return: UpdateDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_group_with_options(request, runtime)

    async def update_domain_group_async(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        """
        @summary Modifies the name of a domain name group based on the specified parameters.
        
        @param request: UpdateDomainGroupRequest
        @return: UpdateDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_group_with_options_async(request, runtime)

    def update_domain_record_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_record(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRequest
        @return: UpdateDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_with_options(request, runtime)

    async def update_domain_record_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        """
        @summary Modifies a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRequest
        @return: UpdateDomainRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_record_with_options_async(request, runtime)

    def update_domain_record_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRecordRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecordRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_record_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRecordRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecordRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_record_remark(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRemarkRequest
        @return: UpdateDomainRecordRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_remark_with_options(request, runtime)

    async def update_domain_record_remark_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        """
        @summary Modifies the description of a Domain Name System (DNS) record based on the specified parameters.
        
        @param request: UpdateDomainRecordRemarkRequest
        @return: UpdateDomainRecordRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_record_remark_with_options_async(request, runtime)

    def update_domain_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        """
        @summary Modifies the description of a domain name based on the specified parameters.
        
        @param request: UpdateDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        """
        @summary Modifies the description of a domain name based on the specified parameters.
        
        @param request: UpdateDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_remark(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        """
        @summary Modifies the description of a domain name based on the specified parameters.
        
        @param request: UpdateDomainRemarkRequest
        @return: UpdateDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_remark_with_options(request, runtime)

    async def update_domain_remark_async(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        """
        @summary Modifies the description of a domain name based on the specified parameters.
        
        @param request: UpdateDomainRemarkRequest
        @return: UpdateDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_remark_with_options_async(request, runtime)

    def update_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        """
        @param request: UpdateGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        """
        @param request: UpdateGtmAccessStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmAccessStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAccessStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_access_strategy(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        """
        @param request: UpdateGtmAccessStrategyRequest
        @return: UpdateGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_access_strategy_with_options(request, runtime)

    async def update_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        """
        @param request: UpdateGtmAccessStrategyRequest
        @return: UpdateGtmAccessStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_access_strategy_with_options_async(request, runtime)

    def update_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        """
        @param request: UpdateGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        """
        @param request: UpdateGtmAddressPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmAddressPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_address_pool(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        """
        @param request: UpdateGtmAddressPoolRequest
        @return: UpdateGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_address_pool_with_options(request, runtime)

    async def update_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        """
        @param request: UpdateGtmAddressPoolRequest
        @return: UpdateGtmAddressPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_address_pool_with_options_async(request, runtime)

    def update_gtm_instance_global_config_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance based on the specified parameters.
        
        @param request: UpdateGtmInstanceGlobalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmInstanceGlobalConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_custom_domain_name):
            query['CnameCustomDomainName'] = request.cname_custom_domain_name
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.user_domain_name):
            query['UserDomainName'] = request.user_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_instance_global_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance based on the specified parameters.
        
        @param request: UpdateGtmInstanceGlobalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmInstanceGlobalConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_custom_domain_name):
            query['CnameCustomDomainName'] = request.cname_custom_domain_name
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.user_domain_name):
            query['UserDomainName'] = request.user_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_instance_global_config(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance based on the specified parameters.
        
        @param request: UpdateGtmInstanceGlobalConfigRequest
        @return: UpdateGtmInstanceGlobalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_instance_global_config_with_options(request, runtime)

    async def update_gtm_instance_global_config_async(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        """
        @summary Modifies the configurations of a Global Traffic Manager (GTM) instance based on the specified parameters.
        
        @param request: UpdateGtmInstanceGlobalConfigRequest
        @return: UpdateGtmInstanceGlobalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_instance_global_config_with_options_async(request, runtime)

    def update_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        """
        @summary Modifies the health check configuration for an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        """
        @summary Modifies the health check configuration for an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_monitor(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        """
        @summary Modifies the health check configuration for an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmMonitorRequest
        @return: UpdateGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_monitor_with_options(request, runtime)

    async def update_gtm_monitor_async(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        """
        @summary Modifies the health check configuration for an address pool of a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmMonitorRequest
        @return: UpdateGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_monitor_with_options_async(request, runtime)

    def update_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        """
        @summary Modifies a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        """
        @summary Modifies a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmRecoveryPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGtmRecoveryPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gtm_recovery_plan(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        """
        @summary Modifies a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmRecoveryPlanRequest
        @return: UpdateGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_recovery_plan_with_options(request, runtime)

    async def update_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        """
        @summary Modifies a disaster recovery plan for a Global Traffic Manager (GTM) instance.
        
        @param request: UpdateGtmRecoveryPlanRequest
        @return: UpdateGtmRecoveryPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_recovery_plan_with_options_async(request, runtime)

    def update_isp_flush_cache_instance_config_with_options(
        self,
        request: alidns_20150109_models.UpdateIspFlushCacheInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse:
        """
        @summary 修改缓存刷新套餐包配置
        
        @param request: UpdateIspFlushCacheInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIspFlushCacheInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIspFlushCacheInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_isp_flush_cache_instance_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateIspFlushCacheInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse:
        """
        @summary 修改缓存刷新套餐包配置
        
        @param request: UpdateIspFlushCacheInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIspFlushCacheInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIspFlushCacheInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_isp_flush_cache_instance_config(
        self,
        request: alidns_20150109_models.UpdateIspFlushCacheInstanceConfigRequest,
    ) -> alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse:
        """
        @summary 修改缓存刷新套餐包配置
        
        @param request: UpdateIspFlushCacheInstanceConfigRequest
        @return: UpdateIspFlushCacheInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_isp_flush_cache_instance_config_with_options(request, runtime)

    async def update_isp_flush_cache_instance_config_async(
        self,
        request: alidns_20150109_models.UpdateIspFlushCacheInstanceConfigRequest,
    ) -> alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse:
        """
        @summary 修改缓存刷新套餐包配置
        
        @param request: UpdateIspFlushCacheInstanceConfigRequest
        @return: UpdateIspFlushCacheInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_isp_flush_cache_instance_config_with_options_async(request, runtime)

    def validate_dns_gtm_cname_rr_can_use_with_options(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        """
        @summary 检查实例主机名是否可添加
        
        @param request: ValidateDnsGtmCnameRrCanUseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateDnsGtmCnameRrCanUseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.cname_rr):
            query['CnameRr'] = request.cname_rr
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.cname_zone):
            query['CnameZone'] = request.cname_zone
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmCnameRrCanUse',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_dns_gtm_cname_rr_can_use_with_options_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        """
        @summary 检查实例主机名是否可添加
        
        @param request: ValidateDnsGtmCnameRrCanUseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateDnsGtmCnameRrCanUseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.cname_rr):
            query['CnameRr'] = request.cname_rr
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.cname_zone):
            query['CnameZone'] = request.cname_zone
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmCnameRrCanUse',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_dns_gtm_cname_rr_can_use(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        """
        @summary 检查实例主机名是否可添加
        
        @param request: ValidateDnsGtmCnameRrCanUseRequest
        @return: ValidateDnsGtmCnameRrCanUseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_dns_gtm_cname_rr_can_use_with_options(request, runtime)

    async def validate_dns_gtm_cname_rr_can_use_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        """
        @summary 检查实例主机名是否可添加
        
        @param request: ValidateDnsGtmCnameRrCanUseRequest
        @return: ValidateDnsGtmCnameRrCanUseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_dns_gtm_cname_rr_can_use_with_options_async(request, runtime)

    def validate_pdns_udp_ip_segment_with_options(
        self,
        request: alidns_20150109_models.ValidatePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse:
        """
        @summary 验证公共DNS Udp Ip地址段
        
        @param request: ValidatePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_pdns_udp_ip_segment_with_options_async(
        self,
        request: alidns_20150109_models.ValidatePdnsUdpIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse:
        """
        @summary 验证公共DNS Udp Ip地址段
        
        @param request: ValidatePdnsUdpIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatePdnsUdpIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_pdns_udp_ip_segment(
        self,
        request: alidns_20150109_models.ValidatePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse:
        """
        @summary 验证公共DNS Udp Ip地址段
        
        @param request: ValidatePdnsUdpIpSegmentRequest
        @return: ValidatePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_pdns_udp_ip_segment_with_options(request, runtime)

    async def validate_pdns_udp_ip_segment_async(
        self,
        request: alidns_20150109_models.ValidatePdnsUdpIpSegmentRequest,
    ) -> alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse:
        """
        @summary 验证公共DNS Udp Ip地址段
        
        @param request: ValidatePdnsUdpIpSegmentRequest
        @return: ValidatePdnsUdpIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_pdns_udp_ip_segment_with_options_async(request, runtime)
