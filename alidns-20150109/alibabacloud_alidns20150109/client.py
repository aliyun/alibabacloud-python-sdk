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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['LineName'] = request.line_name
        query['IpSegment'] = request.ip_segment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['LineName'] = request.line_name
        query['IpSegment'] = request.ip_segment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    async def add_custom_line_async(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_line_with_options_async(request, runtime)

    def add_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['InstanceId'] = request.instance_id
        query['CacheTtlMin'] = request.cache_ttl_min
        query['CacheTtlMax'] = request.cache_ttl_max
        query['SourceProtocol'] = request.source_protocol
        query['SourceEdns'] = request.source_edns
        query['Remark'] = request.remark
        query['SourceDnsServer'] = request.source_dns_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['InstanceId'] = request.instance_id
        query['CacheTtlMin'] = request.cache_ttl_min
        query['CacheTtlMax'] = request.cache_ttl_max
        query['SourceProtocol'] = request.source_protocol
        query['SourceEdns'] = request.source_edns
        query['Remark'] = request.remark
        query['SourceDnsServer'] = request.source_dns_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_dns_cache_domain_with_options(request, runtime)

    async def add_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.AddDnsCacheDomainRequest,
    ) -> alidns_20150109_models.AddDnsCacheDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_cache_domain_with_options_async(request, runtime)

    def add_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyName'] = request.strategy_name
        query['Lines'] = request.lines
        query['DefaultAddrPoolType'] = request.default_addr_pool_type
        query['DefaultLbaStrategy'] = request.default_lba_strategy
        query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        query['DefaultLatencyOptimization'] = request.default_latency_optimization
        query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        query['FailoverLbaStrategy'] = request.failover_lba_strategy
        query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        query['StrategyMode'] = request.strategy_mode
        query['DefaultAddrPool'] = request.default_addr_pool
        query['FailoverAddrPool'] = request.failover_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyName'] = request.strategy_name
        query['Lines'] = request.lines
        query['DefaultAddrPoolType'] = request.default_addr_pool_type
        query['DefaultLbaStrategy'] = request.default_lba_strategy
        query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        query['DefaultLatencyOptimization'] = request.default_latency_optimization
        query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        query['FailoverLbaStrategy'] = request.failover_lba_strategy
        query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        query['StrategyMode'] = request.strategy_mode
        query['DefaultAddrPool'] = request.default_addr_pool
        query['FailoverAddrPool'] = request.failover_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_access_strategy_with_options(request, runtime)

    async def add_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_access_strategy_with_options_async(request, runtime)

    def add_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['LbaStrategy'] = request.lba_strategy
        query['MonitorStatus'] = request.monitor_status
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['Addr'] = request.addr
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['LbaStrategy'] = request.lba_strategy
        query['MonitorStatus'] = request.monitor_status
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['Addr'] = request.addr
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_address_pool_with_options(request, runtime)

    async def add_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_address_pool_with_options_async(request, runtime)

    def add_dns_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_monitor_with_options(request, runtime)

    async def add_dns_gtm_monitor_async(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dns_gtm_monitor_with_options_async(request, runtime)

    def add_domain_with_options(
        self,
        request: alidns_20150109_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: alidns_20150109_models.AddDomainRequest,
    ) -> alidns_20150109_models.AddDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def add_domain_backup_with_options(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['PeriodType'] = request.period_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainBackup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['PeriodType'] = request.period_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainBackup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_domain_backup_with_options(request, runtime)

    async def add_domain_backup_async(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_backup_with_options_async(request, runtime)

    def add_domain_group_with_options(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_domain_group_with_options(request, runtime)

    async def add_domain_group_async(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_group_with_options_async(request, runtime)

    def add_domain_record_with_options(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['RR'] = request.rr
        query['Type'] = request.type
        query['Value'] = request.value
        query['TTL'] = request.ttl
        query['Priority'] = request.priority
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['RR'] = request.rr
        query['Type'] = request.type
        query['Value'] = request.value
        query['TTL'] = request.ttl
        query['Priority'] = request.priority
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_domain_record_with_options(request, runtime)

    async def add_domain_record_async(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_record_with_options_async(request, runtime)

    def add_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyName'] = request.strategy_name
        query['DefaultAddrPoolId'] = request.default_addr_pool_id
        query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        query['AccessLines'] = request.access_lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyName'] = request.strategy_name
        query['DefaultAddrPoolId'] = request.default_addr_pool_id
        query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        query['AccessLines'] = request.access_lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_access_strategy_with_options(request, runtime)

    async def add_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_access_strategy_with_options_async(request, runtime)

    def add_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['MinAvailableAddrNum'] = request.min_available_addr_num
        query['MonitorStatus'] = request.monitor_status
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['Addr'] = request.addr
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['MinAvailableAddrNum'] = request.min_available_addr_num
        query['MonitorStatus'] = request.monitor_status
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['Addr'] = request.addr
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_address_pool_with_options(request, runtime)

    async def add_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_address_pool_with_options_async(request, runtime)

    def add_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_monitor_with_options(request, runtime)

    async def add_gtm_monitor_async(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_monitor_with_options_async(request, runtime)

    def add_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['Remark'] = request.remark
        query['FaultAddrPool'] = request.fault_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['Remark'] = request.remark
        query['FaultAddrPool'] = request.fault_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_recovery_plan_with_options(request, runtime)

    async def add_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_gtm_recovery_plan_with_options_async(request, runtime)

    def bind_instance_domains_with_options(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['DomainNames'] = request.domain_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['DomainNames'] = request.domain_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.bind_instance_domains_with_options(request, runtime)

    async def bind_instance_domains_async(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_instance_domains_with_options_async(request, runtime)

    def change_domain_group_with_options(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.change_domain_group_with_options(request, runtime)

    async def change_domain_group_async(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_domain_group_with_options_async(request, runtime)

    def change_domain_of_dns_product_with_options(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['InstanceId'] = request.instance_id
        query['NewDomain'] = request.new_domain
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeDomainOfDnsProduct',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['InstanceId'] = request.instance_id
        query['NewDomain'] = request.new_domain
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangeDomainOfDnsProduct',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.change_domain_of_dns_product_with_options(request, runtime)

    async def change_domain_of_dns_product_async(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_domain_of_dns_product_with_options_async(request, runtime)

    def copy_gtm_config_with_options(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['SourceId'] = request.source_id
        query['TargetId'] = request.target_id
        query['CopyType'] = request.copy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyGtmConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['SourceId'] = request.source_id
        query['TargetId'] = request.target_id
        query['CopyType'] = request.copy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyGtmConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.copy_gtm_config_with_options(request, runtime)

    async def copy_gtm_config_async(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_gtm_config_with_options_async(request, runtime)

    def delete_custom_lines_with_options(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineIds'] = request.line_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineIds'] = request.line_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_lines_with_options(request, runtime)

    async def delete_custom_lines_async(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_lines_with_options_async(request, runtime)

    def delete_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_cache_domain_with_options(request, runtime)

    async def delete_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.DeleteDnsCacheDomainRequest,
    ) -> alidns_20150109_models.DeleteDnsCacheDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_cache_domain_with_options_async(request, runtime)

    def delete_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_access_strategy_with_options(request, runtime)

    async def delete_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_gtm_access_strategy_with_options_async(request, runtime)

    def delete_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_address_pool_with_options(request, runtime)

    async def delete_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dns_gtm_address_pool_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_group_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_domain_record_with_options(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_record_with_options(request, runtime)

    async def delete_domain_record_async(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_record_with_options_async(request, runtime)

    def delete_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_access_strategy_with_options(request, runtime)

    async def delete_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_access_strategy_with_options_async(request, runtime)

    def delete_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_address_pool_with_options(request, runtime)

    async def delete_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_address_pool_with_options_async(request, runtime)

    def delete_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_recovery_plan_with_options(request, runtime)

    async def delete_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gtm_recovery_plan_with_options_async(request, runtime)

    def delete_sub_domain_records_with_options(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['RR'] = request.rr
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['RR'] = request.rr
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_domain_records_with_options(request, runtime)

    async def delete_sub_domain_records_async(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sub_domain_records_with_options_async(request, runtime)

    def describe_batch_result_count_with_options(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['TaskId'] = request.task_id
        query['BatchType'] = request.batch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultCount',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['TaskId'] = request.task_id
        query['BatchType'] = request.batch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultCount',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_count_with_options(request, runtime)

    async def describe_batch_result_count_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_result_count_with_options_async(request, runtime)

    def describe_batch_result_detail_with_options(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['TaskId'] = request.task_id
        query['BatchType'] = request.batch_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultDetail',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['TaskId'] = request.task_id
        query['BatchType'] = request.batch_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultDetail',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_detail_with_options(request, runtime)

    async def describe_batch_result_detail_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_result_detail_with_options_async(request, runtime)

    def describe_custom_line_with_options(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LineId'] = request.line_id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['LineId'] = request.line_id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_line_with_options(request, runtime)

    async def describe_custom_line_async(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_line_with_options_async(request, runtime)

    def describe_custom_lines_with_options(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    async def describe_custom_lines_async(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_lines_with_options_async(request, runtime)

    def describe_dns_cache_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsCacheDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsCacheDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_cache_domains_with_options(request, runtime)

    async def describe_dns_cache_domains_async(
        self,
        request: alidns_20150109_models.DescribeDnsCacheDomainsRequest,
    ) -> alidns_20150109_models.DescribeDnsCacheDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_cache_domains_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategies_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategies_with_options(request, runtime)

    async def describe_dns_gtm_access_strategies_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategies_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_with_options_async(request, runtime)

    def describe_dns_gtm_access_strategy_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_dns_gtm_access_strategy_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_addr_attribute_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Type'] = request.type
        query['Addrs'] = request.addrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddrAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Type'] = request.type
        query['Addrs'] = request.addrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddrAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_addr_attribute_info_with_options(request, runtime)

    async def describe_dns_gtm_addr_attribute_info_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_addr_attribute_info_with_options_async(request, runtime)

    def describe_dns_gtm_address_pool_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddressPoolAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddressPoolAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_address_pool_available_config_with_options(request, runtime)

    async def describe_dns_gtm_address_pool_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_address_pool_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_available_alert_group_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_available_alert_group_with_options(request, runtime)

    async def describe_dns_gtm_available_alert_group_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_dns_gtm_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_with_options(request, runtime)

    async def describe_dns_gtm_instance_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pool_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pool_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_dns_gtm_instance_address_pools_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_dns_gtm_instance_address_pools_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_dns_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instances_with_options(request, runtime)

    async def describe_dns_gtm_instances_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instances_with_options_async(request, runtime)

    def describe_dns_gtm_instance_status_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_status_with_options(request, runtime)

    async def describe_dns_gtm_instance_status_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_status_with_options_async(request, runtime)

    def describe_dns_gtm_instance_system_cname_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_dns_gtm_instance_system_cname_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_dns_gtm_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_logs_with_options(request, runtime)

    async def describe_dns_gtm_logs_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_logs_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_available_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_dns_gtm_monitor_config_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_config_with_options(request, runtime)

    async def describe_dns_gtm_monitor_config_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_gtm_monitor_config_with_options_async(request, runtime)

    def describe_dns_product_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instance_with_options(request, runtime)

    async def describe_dns_product_instance_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_product_instance_with_options_async(request, runtime)

    def describe_dns_product_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['VersionCode'] = request.version_code
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['VersionCode'] = request.version_code
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instances_with_options(request, runtime)

    async def describe_dns_product_instances_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dns_product_instances_with_options_async(request, runtime)

    def describe_dnsslbsub_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Rr'] = request.rr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDNSSLBSubDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Rr'] = request.rr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDNSSLBSubDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dnsslbsub_domains_with_options(request, runtime)

    async def describe_dnsslbsub_domains_async(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dnsslbsub_domains_with_options_async(request, runtime)

    def describe_doh_account_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohAccountStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohAccountStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_account_statistics_with_options(request, runtime)

    async def describe_doh_account_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_account_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_with_options(request, runtime)

    async def describe_doh_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_domain_statistics_with_options_async(request, runtime)

    def describe_doh_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['SubDomain'] = request.sub_domain
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['SubDomain'] = request.sub_domain
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_with_options_async(request, runtime)

    def describe_doh_sub_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['SubDomain'] = request.sub_domain
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['SubDomain'] = request.sub_domain
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_summary_with_options(request, runtime)

    async def describe_doh_sub_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_sub_domain_statistics_summary_with_options_async(request, runtime)

    def describe_doh_user_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDohUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_user_info_with_options(request, runtime)

    async def describe_doh_user_info_async(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_doh_user_info_with_options_async(request, runtime)

    def describe_domain_dnssec_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainDnssecInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainDnssecInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_dnssec_info_with_options(request, runtime)

    async def describe_domain_dnssec_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_dnssec_info_with_options_async(request, runtime)

    def describe_domain_groups_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_groups_with_options(request, runtime)

    async def describe_domain_groups_async(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_groups_with_options_async(request, runtime)

    def describe_domain_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_info_with_options(request, runtime)

    async def describe_domain_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_info_with_options_async(request, runtime)

    def describe_domain_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['endDate'] = request.end_date
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['endDate'] = request.end_date
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_logs_with_options(request, runtime)

    async def describe_domain_logs_async(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_logs_with_options_async(request, runtime)

    def describe_domain_ns_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainNs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainNs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ns_with_options(request, runtime)

    async def describe_domain_ns_async(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_ns_with_options_async(request, runtime)

    def describe_domain_record_info_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecordInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecordInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_record_info_with_options(request, runtime)

    async def describe_domain_record_info_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_record_info_with_options_async(request, runtime)

    def describe_domain_records_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['KeyWord'] = request.key_word
        query['RRKeyWord'] = request.rrkey_word
        query['TypeKeyWord'] = request.type_key_word
        query['ValueKeyWord'] = request.value_key_word
        query['OrderBy'] = request.order_by
        query['Direction'] = request.direction
        query['SearchMode'] = request.search_mode
        query['GroupId'] = request.group_id
        query['Type'] = request.type
        query['Line'] = request.line
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['KeyWord'] = request.key_word
        query['RRKeyWord'] = request.rrkey_word
        query['TypeKeyWord'] = request.type_key_word
        query['ValueKeyWord'] = request.value_key_word
        query['OrderBy'] = request.order_by
        query['Direction'] = request.direction
        query['SearchMode'] = request.search_mode
        query['GroupId'] = request.group_id
        query['Type'] = request.type
        query['Line'] = request.line
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_records_with_options(request, runtime)

    async def describe_domain_records_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_records_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchMode'] = request.search_mode
        query['ResourceGroupId'] = request.resource_group_id
        query['Starmark'] = request.starmark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['KeyWord'] = request.key_word
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SearchMode'] = request.search_mode
        query['ResourceGroupId'] = request.resource_group_id
        query['Starmark'] = request.starmark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_domain_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_with_options(request, runtime)

    async def describe_domain_statistics_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_statistics_with_options_async(request, runtime)

    def describe_domain_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['SearchMode'] = request.search_mode
        query['Keyword'] = request.keyword
        query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['SearchMode'] = request.search_mode
        query['Keyword'] = request.keyword
        query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_summary_with_options(request, runtime)

    async def describe_domain_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_statistics_summary_with_options_async(request, runtime)

    def describe_gtm_access_strategies_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategies_with_options(request, runtime)

    async def describe_gtm_access_strategies_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategies_with_options_async(request, runtime)

    def describe_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_with_options(request, runtime)

    async def describe_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategy_with_options_async(request, runtime)

    def describe_gtm_access_strategy_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_available_config_with_options(request, runtime)

    async def describe_gtm_access_strategy_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_access_strategy_available_config_with_options_async(request, runtime)

    def describe_gtm_available_alert_group_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_available_alert_group_with_options(request, runtime)

    async def describe_gtm_available_alert_group_async(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_available_alert_group_with_options_async(request, runtime)

    def describe_gtm_instance_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_with_options(request, runtime)

    async def describe_gtm_instance_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_with_options_async(request, runtime)

    def describe_gtm_instance_address_pool_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pool_with_options(request, runtime)

    async def describe_gtm_instance_address_pool_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_address_pool_with_options_async(request, runtime)

    def describe_gtm_instance_address_pools_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pools_with_options(request, runtime)

    async def describe_gtm_instance_address_pools_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_address_pools_with_options_async(request, runtime)

    def describe_gtm_instances_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['ResourceGroupId'] = request.resource_group_id
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['ResourceGroupId'] = request.resource_group_id
        query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instances_with_options(request, runtime)

    async def describe_gtm_instances_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instances_with_options_async(request, runtime)

    def describe_gtm_instance_status_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_status_with_options(request, runtime)

    async def describe_gtm_instance_status_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_status_with_options_async(request, runtime)

    def describe_gtm_instance_system_cname_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_system_cname_with_options(request, runtime)

    async def describe_gtm_instance_system_cname_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_instance_system_cname_with_options_async(request, runtime)

    def describe_gtm_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_logs_with_options(request, runtime)

    async def describe_gtm_logs_async(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_logs_with_options_async(request, runtime)

    def describe_gtm_monitor_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_available_config_with_options(request, runtime)

    async def describe_gtm_monitor_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_monitor_available_config_with_options_async(request, runtime)

    def describe_gtm_monitor_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_config_with_options(request, runtime)

    async def describe_gtm_monitor_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_monitor_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_with_options(request, runtime)

    async def describe_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plan_with_options_async(request, runtime)

    def describe_gtm_recovery_plan_available_config_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlanAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlanAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_available_config_with_options(request, runtime)

    async def describe_gtm_recovery_plan_available_config_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plan_available_config_with_options_async(request, runtime)

    def describe_gtm_recovery_plans_with_options(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlans',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlans',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plans_with_options(request, runtime)

    async def describe_gtm_recovery_plans_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gtm_recovery_plans_with_options_async(request, runtime)

    def describe_instance_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_domains_with_options(request, runtime)

    async def describe_instance_domains_async(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_domains_with_options_async(request, runtime)

    def describe_record_logs_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['KeyWord'] = request.key_word
        query['StartDate'] = request.start_date
        query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['KeyWord'] = request.key_word
        query['StartDate'] = request.start_date
        query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_record_logs_with_options(request, runtime)

    async def describe_record_logs_async(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_logs_with_options_async(request, runtime)

    def describe_record_statistics_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        query['Rr'] = request.rr
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        query['Rr'] = request.rr
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_with_options(request, runtime)

    async def describe_record_statistics_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_statistics_with_options_async(request, runtime)

    def describe_record_statistics_summary_with_options(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        query['SearchMode'] = request.search_mode
        query['Keyword'] = request.keyword
        query['Threshold'] = request.threshold
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        query['DomainName'] = request.domain_name
        query['SearchMode'] = request.search_mode
        query['Keyword'] = request.keyword
        query['Threshold'] = request.threshold
        query['DomainType'] = request.domain_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_summary_with_options(request, runtime)

    async def describe_record_statistics_summary_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_statistics_summary_with_options_async(request, runtime)

    def describe_sub_domain_records_with_options(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['SubDomain'] = request.sub_domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Type'] = request.type
        query['Line'] = request.line
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['SubDomain'] = request.sub_domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Type'] = request.type
        query['Line'] = request.line
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_domain_records_with_options(request, runtime)

    async def describe_sub_domain_records_async(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sub_domain_records_with_options_async(request, runtime)

    def describe_support_lines_with_options(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSupportLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSupportLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_support_lines_with_options(request, runtime)

    async def describe_support_lines_async(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_support_lines_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_transfer_domains_with_options(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['TransferType'] = request.transfer_type
        query['DomainName'] = request.domain_name
        query['FromUserId'] = request.from_user_id
        query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTransferDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['TransferType'] = request.transfer_type
        query['DomainName'] = request.domain_name
        query['FromUserId'] = request.from_user_id
        query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTransferDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_domains_with_options(request, runtime)

    async def describe_transfer_domains_async(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transfer_domains_with_options_async(request, runtime)

    def execute_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.execute_gtm_recovery_plan_with_options(request, runtime)

    async def execute_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_gtm_recovery_plan_with_options_async(request, runtime)

    def get_main_domain_name_with_options(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InputString'] = request.input_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMainDomainName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InputString'] = request.input_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMainDomainName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.get_main_domain_name_with_options(request, runtime)

    async def get_main_domain_name_async(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_main_domain_name_with_options_async(request, runtime)

    def get_txt_record_for_verify_with_options(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTxtRecordForVerify',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTxtRecordForVerify',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.get_txt_record_for_verify_with_options(request, runtime)

    async def get_txt_record_for_verify_async(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_txt_record_for_verify_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['Tag'] = request.tag
        query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['Tag'] = request.tag
        query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_hichina_domain_dnswith_options(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHichinaDomainDNS',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHichinaDomainDNS',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.modify_hichina_domain_dnswith_options(request, runtime)

    async def modify_hichina_domain_dns_async(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hichina_domain_dnswith_options_async(request, runtime)

    def move_domain_resource_group_with_options(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveDomainResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveDomainResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.move_domain_resource_group_with_options(request, runtime)

    async def move_domain_resource_group_async(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_domain_resource_group_with_options_async(request, runtime)

    def move_gtm_resource_group_with_options(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveGtmResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveGtmResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.move_gtm_resource_group_with_options(request, runtime)

    async def move_gtm_resource_group_async(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_gtm_resource_group_with_options_async(request, runtime)

    def operate_batch_domain_with_options(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Type'] = request.type
        query['DomainRecordInfo'] = request.domain_record_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateBatchDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Type'] = request.type
        query['DomainRecordInfo'] = request.domain_record_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateBatchDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.operate_batch_domain_with_options(request, runtime)

    async def operate_batch_domain_async(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_batch_domain_with_options_async(request, runtime)

    def preview_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PreviewGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PreviewGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.preview_gtm_recovery_plan_with_options(request, runtime)

    async def preview_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preview_gtm_recovery_plan_with_options_async(request, runtime)

    def retrieve_domain_with_options(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetrieveDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetrieveDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.retrieve_domain_with_options(request, runtime)

    async def retrieve_domain_async(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_domain_with_options_async(request, runtime)

    def rollback_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RollbackGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RollbackGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.rollback_gtm_recovery_plan_with_options(request, runtime)

    async def rollback_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_gtm_recovery_plan_with_options_async(request, runtime)

    def set_dns_gtm_access_mode_with_options(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDnsGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDnsGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_access_mode_with_options(request, runtime)

    async def set_dns_gtm_access_mode_async(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dns_gtm_access_mode_with_options_async(request, runtime)

    def set_dns_gtm_monitor_status_with_options(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDnsGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDnsGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_monitor_status_with_options(request, runtime)

    async def set_dns_gtm_monitor_status_async(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dns_gtm_monitor_status_with_options_async(request, runtime)

    def set_dnsslbstatus_with_options(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['SubDomain'] = request.sub_domain
        query['Open'] = request.open
        query['DomainName'] = request.domain_name
        query['Type'] = request.type
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDNSSLBStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['SubDomain'] = request.sub_domain
        query['Open'] = request.open
        query['DomainName'] = request.domain_name
        query['Type'] = request.type
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDNSSLBStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_dnsslbstatus_with_options(request, runtime)

    async def set_dnsslbstatus_async(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dnsslbstatus_with_options_async(request, runtime)

    def set_domain_dnssec_status_with_options(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainDnssecStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainDnssecStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_domain_dnssec_status_with_options(request, runtime)

    async def set_domain_dnssec_status_async(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_dnssec_status_with_options_async(request, runtime)

    def set_domain_record_status_with_options(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainRecordStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainRecordStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_domain_record_status_with_options(request, runtime)

    async def set_domain_record_status_async(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_record_status_with_options_async(request, runtime)

    def set_gtm_access_mode_with_options(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_access_mode_with_options(request, runtime)

    async def set_gtm_access_mode_async(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gtm_access_mode_with_options_async(request, runtime)

    def set_gtm_monitor_status_with_options(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_monitor_status_with_options(request, runtime)

    async def set_gtm_monitor_status_async(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gtm_monitor_status_with_options_async(request, runtime)

    def switch_dns_gtm_instance_strategy_mode_with_options(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDnsGtmInstanceStrategyMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDnsGtmInstanceStrategyMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.switch_dns_gtm_instance_strategy_mode_with_options(request, runtime)

    async def switch_dns_gtm_instance_strategy_mode_async(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dns_gtm_instance_strategy_mode_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
    ) -> alidns_20150109_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_domain_with_options(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TransferDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainNames'] = request.domain_names
        query['Remark'] = request.remark
        query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransferDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainNames'] = request.domain_names
        query['Remark'] = request.remark
        query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransferDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.transfer_domain_with_options(request, runtime)

    async def transfer_domain_async(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
    ) -> alidns_20150109_models.TransferDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_domain_with_options_async(request, runtime)

    def unbind_instance_domains_with_options(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainNames'] = request.domain_names
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainNames'] = request.domain_names
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.unbind_instance_domains_with_options(request, runtime)

    async def unbind_instance_domains_async(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_instance_domains_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_line_with_options(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineName'] = request.line_name
        query['LineId'] = request.line_id
        query['IpSegment'] = request.ip_segment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineName'] = request.line_name
        query['LineId'] = request.line_id
        query['IpSegment'] = request.ip_segment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    async def update_custom_line_async(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_line_with_options_async(request, runtime)

    def update_dns_cache_domain_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['InstanceId'] = request.instance_id
        query['CacheTtlMin'] = request.cache_ttl_min
        query['CacheTtlMax'] = request.cache_ttl_max
        query['SourceProtocol'] = request.source_protocol
        query['SourceEdns'] = request.source_edns
        query['SourceDnsServer'] = request.source_dns_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['InstanceId'] = request.instance_id
        query['CacheTtlMin'] = request.cache_ttl_min
        query['CacheTtlMax'] = request.cache_ttl_max
        query['SourceProtocol'] = request.source_protocol
        query['SourceEdns'] = request.source_edns
        query['SourceDnsServer'] = request.source_dns_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_with_options(request, runtime)

    async def update_dns_cache_domain_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_cache_domain_with_options_async(request, runtime)

    def update_dns_cache_domain_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_remark_with_options(request, runtime)

    async def update_dns_cache_domain_remark_async(
        self,
        request: alidns_20150109_models.UpdateDnsCacheDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_cache_domain_remark_with_options_async(request, runtime)

    def update_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['StrategyName'] = request.strategy_name
        query['Lines'] = request.lines
        query['DefaultAddrPoolType'] = request.default_addr_pool_type
        query['DefaultLbaStrategy'] = request.default_lba_strategy
        query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        query['DefaultLatencyOptimization'] = request.default_latency_optimization
        query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        query['FailoverLbaStrategy'] = request.failover_lba_strategy
        query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        query['DefaultAddrPool'] = request.default_addr_pool
        query['FailoverAddrPool'] = request.failover_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['StrategyName'] = request.strategy_name
        query['Lines'] = request.lines
        query['DefaultAddrPoolType'] = request.default_addr_pool_type
        query['DefaultLbaStrategy'] = request.default_lba_strategy
        query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        query['DefaultLatencyOptimization'] = request.default_latency_optimization
        query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        query['FailoverLbaStrategy'] = request.failover_lba_strategy
        query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        query['DefaultAddrPool'] = request.default_addr_pool
        query['FailoverAddrPool'] = request.failover_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_access_strategy_with_options(request, runtime)

    async def update_dns_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_access_strategy_with_options_async(request, runtime)

    def update_dns_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['Name'] = request.name
        query['LbaStrategy'] = request.lba_strategy
        query['Addr'] = request.addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['Name'] = request.name
        query['LbaStrategy'] = request.lba_strategy
        query['Addr'] = request.addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_address_pool_with_options(request, runtime)

    async def update_dns_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_address_pool_with_options_async(request, runtime)

    def update_dns_gtm_instance_global_config_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Ttl'] = request.ttl
        query['PublicCnameMode'] = request.public_cname_mode
        query['PublicUserDomainName'] = request.public_user_domain_name
        query['PublicZoneName'] = request.public_zone_name
        query['AlertGroup'] = request.alert_group
        query['CnameType'] = request.cname_type
        query['AlertConfig'] = request.alert_config
        query['PublicRr'] = request.public_rr
        query['ForceUpdate'] = request.force_update
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Ttl'] = request.ttl
        query['PublicCnameMode'] = request.public_cname_mode
        query['PublicUserDomainName'] = request.public_user_domain_name
        query['PublicZoneName'] = request.public_zone_name
        query['AlertGroup'] = request.alert_group
        query['CnameType'] = request.cname_type
        query['AlertConfig'] = request.alert_config
        query['PublicRr'] = request.public_rr
        query['ForceUpdate'] = request.force_update
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_instance_global_config_with_options(request, runtime)

    async def update_dns_gtm_instance_global_config_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_instance_global_config_with_options_async(request, runtime)

    def update_dns_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_monitor_with_options(request, runtime)

    async def update_dns_gtm_monitor_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dns_gtm_monitor_with_options_async(request, runtime)

    def update_dnsslbweight_with_options(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDNSSLBWeight',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDNSSLBWeight',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_dnsslbweight_with_options(request, runtime)

    async def update_dnsslbweight_async(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dnsslbweight_with_options_async(request, runtime)

    def update_domain_group_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_domain_group_with_options(request, runtime)

    async def update_domain_group_async(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_group_with_options_async(request, runtime)

    def update_domain_record_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['RR'] = request.rr
        query['Type'] = request.type
        query['Value'] = request.value
        query['TTL'] = request.ttl
        query['Priority'] = request.priority
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['RR'] = request.rr
        query['Type'] = request.type
        query['Value'] = request.value
        query['TTL'] = request.ttl
        query['Priority'] = request.priority
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_with_options(request, runtime)

    async def update_domain_record_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_record_with_options_async(request, runtime)

    def update_domain_record_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecordRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['RecordId'] = request.record_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecordRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_remark_with_options(request, runtime)

    async def update_domain_record_remark_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_record_remark_with_options_async(request, runtime)

    def update_domain_remark_with_options(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['DomainName'] = request.domain_name
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_domain_remark_with_options(request, runtime)

    async def update_domain_remark_async(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_remark_with_options_async(request, runtime)

    def update_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['StrategyName'] = request.strategy_name
        query['DefaultAddrPoolId'] = request.default_addr_pool_id
        query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        query['AccessLines'] = request.access_lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['StrategyId'] = request.strategy_id
        query['StrategyName'] = request.strategy_name
        query['DefaultAddrPoolId'] = request.default_addr_pool_id
        query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        query['AccessLines'] = request.access_lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_access_strategy_with_options(request, runtime)

    async def update_gtm_access_strategy_async(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_access_strategy_with_options_async(request, runtime)

    def update_gtm_address_pool_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['MinAvailableAddrNum'] = request.min_available_addr_num
        query['Addr'] = request.addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['AddrPoolId'] = request.addr_pool_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['MinAvailableAddrNum'] = request.min_available_addr_num
        query['Addr'] = request.addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_address_pool_with_options(request, runtime)

    async def update_gtm_address_pool_async(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_address_pool_with_options_async(request, runtime)

    def update_gtm_instance_global_config_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Ttl'] = request.ttl
        query['UserDomainName'] = request.user_domain_name
        query['LbaStrategy'] = request.lba_strategy
        query['AlertGroup'] = request.alert_group
        query['CnameMode'] = request.cname_mode
        query['CnameCustomDomainName'] = request.cname_custom_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Ttl'] = request.ttl
        query['UserDomainName'] = request.user_domain_name
        query['LbaStrategy'] = request.lba_strategy
        query['AlertGroup'] = request.alert_group
        query['CnameMode'] = request.cname_mode
        query['CnameCustomDomainName'] = request.cname_custom_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_instance_global_config_with_options(request, runtime)

    async def update_gtm_instance_global_config_async(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_instance_global_config_with_options_async(request, runtime)

    def update_gtm_monitor_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['MonitorConfigId'] = request.monitor_config_id
        query['ProtocolType'] = request.protocol_type
        query['Interval'] = request.interval
        query['EvaluationCount'] = request.evaluation_count
        query['Timeout'] = request.timeout
        query['MonitorExtendInfo'] = request.monitor_extend_info
        query['IspCityNode'] = request.isp_city_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_monitor_with_options(request, runtime)

    async def update_gtm_monitor_async(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_monitor_with_options_async(request, runtime)

    def update_gtm_recovery_plan_with_options(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        query['Name'] = request.name
        query['Remark'] = request.remark
        query['FaultAddrPool'] = request.fault_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecoveryPlanId'] = request.recovery_plan_id
        query['Name'] = request.name
        query['Remark'] = request.remark
        query['FaultAddrPool'] = request.fault_addr_pool
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_recovery_plan_with_options(request, runtime)

    async def update_gtm_recovery_plan_async(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gtm_recovery_plan_with_options_async(request, runtime)

    def validate_dns_gtm_attribute_info_with_options(
        self,
        request: alidns_20150109_models.ValidateDnsGtmAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineCode'] = request.line_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_dns_gtm_attribute_info_with_options_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['LineCode'] = request.line_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_dns_gtm_attribute_info(
        self,
        request: alidns_20150109_models.ValidateDnsGtmAttributeInfoRequest,
    ) -> alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_dns_gtm_attribute_info_with_options(request, runtime)

    async def validate_dns_gtm_attribute_info_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmAttributeInfoRequest,
    ) -> alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_dns_gtm_attribute_info_with_options_async(request, runtime)

    def validate_dns_gtm_cname_rr_can_use_with_options(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['CnameRr'] = request.cname_rr
        query['CnameType'] = request.cname_type
        query['CnameMode'] = request.cname_mode
        query['CnameZone'] = request.cname_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmCnameRrCanUse',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['InstanceId'] = request.instance_id
        query['CnameRr'] = request.cname_rr
        query['CnameType'] = request.cname_type
        query['CnameMode'] = request.cname_mode
        query['CnameZone'] = request.cname_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmCnameRrCanUse',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        runtime = util_models.RuntimeOptions()
        return self.validate_dns_gtm_cname_rr_can_use_with_options(request, runtime)

    async def validate_dns_gtm_cname_rr_can_use_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmCnameRrCanUseRequest,
    ) -> alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_dns_gtm_cname_rr_can_use_with_options_async(request, runtime)
