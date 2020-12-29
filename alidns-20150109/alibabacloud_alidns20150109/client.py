# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alidns20150109 import models as alidns_20150109_models
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddCustomLineResponse().from_map(
            self.do_rpcrequest('AddCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.AddCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddCustomLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddCustomLineResponse().from_map(
            await self.do_rpcrequest_async('AddCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('AddDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('AddDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('AddDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('AddDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmMonitorResponse().from_map(
            self.do_rpcrequest('AddDnsGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dns_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.AddDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDnsGtmMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDnsGtmMonitorResponse().from_map(
            await self.do_rpcrequest_async('AddDnsGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainResponse().from_map(
            self.do_rpcrequest('AddDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainResponse().from_map(
            await self.do_rpcrequest_async('AddDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainBackupResponse().from_map(
            self.do_rpcrequest('AddDomainBackup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_domain_backup_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainBackupResponse().from_map(
            await self.do_rpcrequest_async('AddDomainBackup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainGroupResponse().from_map(
            self.do_rpcrequest('AddDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('AddDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainRecordResponse().from_map(
            self.do_rpcrequest('AddDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.AddDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddDomainRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddDomainRecordResponse().from_map(
            await self.do_rpcrequest_async('AddDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('AddGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('AddGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('AddGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('AddGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmMonitorResponse().from_map(
            self.do_rpcrequest('AddGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmMonitorResponse().from_map(
            await self.do_rpcrequest_async('AddGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('AddGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.AddGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.AddGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.AddGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('AddGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.BindInstanceDomainsResponse().from_map(
            self.do_rpcrequest('BindInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.BindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.BindInstanceDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.BindInstanceDomainsResponse().from_map(
            await self.do_rpcrequest_async('BindInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ChangeDomainGroupResponse().from_map(
            self.do_rpcrequest('ChangeDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.ChangeDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ChangeDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('ChangeDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ChangeDomainOfDnsProductResponse().from_map(
            self.do_rpcrequest('ChangeDomainOfDnsProduct', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_domain_of_dns_product_with_options_async(
        self,
        request: alidns_20150109_models.ChangeDomainOfDnsProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ChangeDomainOfDnsProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ChangeDomainOfDnsProductResponse().from_map(
            await self.do_rpcrequest_async('ChangeDomainOfDnsProduct', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.CopyGtmConfigResponse().from_map(
            self.do_rpcrequest('CopyGtmConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_gtm_config_with_options_async(
        self,
        request: alidns_20150109_models.CopyGtmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.CopyGtmConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.CopyGtmConfigResponse().from_map(
            await self.do_rpcrequest_async('CopyGtmConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteCustomLinesResponse().from_map(
            self.do_rpcrequest('DeleteCustomLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_custom_lines_with_options_async(
        self,
        request: alidns_20150109_models.DeleteCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteCustomLinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteCustomLinesResponse().from_map(
            await self.do_rpcrequest_async('DeleteCustomLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('DeleteDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('DeleteDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDnsGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('DeleteDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDnsGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('DeleteDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainResponse().from_map(
            self.do_rpcrequest('DeleteDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainGroupResponse().from_map(
            self.do_rpcrequest('DeleteDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainRecordResponse().from_map(
            self.do_rpcrequest('DeleteDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.DeleteDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteDomainRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteDomainRecordResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('DeleteGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('DeleteGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('DeleteGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('DeleteGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('DeleteGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.DeleteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('DeleteGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteSubDomainRecordsResponse().from_map(
            self.do_rpcrequest('DeleteSubDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sub_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DeleteSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DeleteSubDomainRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DeleteSubDomainRecordsResponse().from_map(
            await self.do_rpcrequest_async('DeleteSubDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeBatchResultCountResponse().from_map(
            self.do_rpcrequest('DescribeBatchResultCount', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_batch_result_count_with_options_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeBatchResultCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeBatchResultCount', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeBatchResultDetailResponse().from_map(
            self.do_rpcrequest('DescribeBatchResultDetail', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_batch_result_detail_with_options_async(
        self,
        request: alidns_20150109_models.DescribeBatchResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeBatchResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeBatchResultDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeBatchResultDetail', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeCustomLineResponse().from_map(
            self.do_rpcrequest('DescribeCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeCustomLineResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeCustomLinesResponse().from_map(
            self.do_rpcrequest('DescribeCustomLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_lines_with_options_async(
        self,
        request: alidns_20150109_models.DescribeCustomLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeCustomLinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeCustomLinesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dns_gtm_access_strategies_with_options(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAccessStrategies', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_access_strategies_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAccessStrategies', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAccessStrategyAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_access_strategy_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAccessStrategyAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAddrAttributeInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_addr_attribute_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAddrAttributeInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAddressPoolAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_address_pool_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAddressPoolAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmAvailableAlertGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_available_alert_group_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmAvailableAlertGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstanceAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instance_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstanceAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstanceAddressPools', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instance_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstanceAddressPools', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstancesResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstanceStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instance_status_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstanceStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmInstanceSystemCname', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_instance_system_cname_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmInstanceSystemCname', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmLogsResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmMonitorAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_monitor_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmMonitorAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse().from_map(
            self.do_rpcrequest('DescribeDnsGtmMonitorConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_gtm_monitor_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsGtmMonitorConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsProductInstanceResponse().from_map(
            self.do_rpcrequest('DescribeDnsProductInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_product_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsProductInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsProductInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsProductInstancesResponse().from_map(
            self.do_rpcrequest('DescribeDnsProductInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dns_product_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDnsProductInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDnsProductInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDnsProductInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnsProductInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDNSSLBSubDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDNSSLBSubDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dnsslbsub_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDNSSLBSubDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDNSSLBSubDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDNSSLBSubDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDNSSLBSubDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohAccountStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDohAccountStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_account_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohAccountStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohAccountStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohAccountStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohDomainStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDohDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohDomainStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse().from_map(
            self.do_rpcrequest('DescribeDohDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohSubDomainStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDohSubDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_sub_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohSubDomainStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohSubDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse().from_map(
            self.do_rpcrequest('DescribeDohSubDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_sub_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohSubDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohUserInfoResponse().from_map(
            self.do_rpcrequest('DescribeDohUserInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_doh_user_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDohUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDohUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDohUserInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDohUserInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainDnssecInfoResponse().from_map(
            self.do_rpcrequest('DescribeDomainDnssecInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_dnssec_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainDnssecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainDnssecInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainDnssecInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainDnssecInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainGroupsResponse().from_map(
            self.do_rpcrequest('DescribeDomainGroups', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_groups_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainGroups', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainInfoResponse().from_map(
            self.do_rpcrequest('DescribeDomainInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainLogsResponse().from_map(
            self.do_rpcrequest('DescribeDomainLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainNsResponse().from_map(
            self.do_rpcrequest('DescribeDomainNs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_ns_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainNsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainNsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainNs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainRecordInfoResponse().from_map(
            self.do_rpcrequest('DescribeDomainRecordInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_record_info_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainRecordInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRecordInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainRecordsResponse().from_map(
            self.do_rpcrequest('DescribeDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainStatisticsSummaryResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeDomainStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeDomainStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeDomainStatisticsSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategiesResponse().from_map(
            self.do_rpcrequest('DescribeGtmAccessStrategies', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_access_strategies_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmAccessStrategies', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('DescribeGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeGtmAccessStrategyAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_access_strategy_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmAccessStrategyAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse().from_map(
            self.do_rpcrequest('DescribeGtmAvailableAlertGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_available_alert_group_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmAvailableAlertGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmAvailableAlertGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instance_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstance', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstanceAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instance_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstanceAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstanceAddressPools', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instance_address_pools_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceAddressPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstanceAddressPools', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstancesResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instances_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstances', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstanceStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instance_status_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstanceStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse().from_map(
            self.do_rpcrequest('DescribeGtmInstanceSystemCname', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_instance_system_cname_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmInstanceSystemCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmInstanceSystemCname', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmLogsResponse().from_map(
            self.do_rpcrequest('DescribeGtmLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeGtmMonitorAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_monitor_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmMonitorAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmMonitorConfigResponse().from_map(
            self.do_rpcrequest('DescribeGtmMonitorConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_monitor_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmMonitorConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmMonitorConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmMonitorConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmMonitorConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('DescribeGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse().from_map(
            self.do_rpcrequest('DescribeGtmRecoveryPlanAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_recovery_plan_available_config_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmRecoveryPlanAvailableConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlansResponse().from_map(
            self.do_rpcrequest('DescribeGtmRecoveryPlans', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gtm_recovery_plans_with_options_async(
        self,
        request: alidns_20150109_models.DescribeGtmRecoveryPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeGtmRecoveryPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeGtmRecoveryPlansResponse().from_map(
            await self.do_rpcrequest_async('DescribeGtmRecoveryPlans', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeInstanceDomainsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeInstanceDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeInstanceDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordLogsResponse().from_map(
            self.do_rpcrequest('DescribeRecordLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_logs_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordLogs', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeRecordStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_statistics_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordStatistics', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordStatisticsSummaryResponse().from_map(
            self.do_rpcrequest('DescribeRecordStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_statistics_summary_with_options_async(
        self,
        request: alidns_20150109_models.DescribeRecordStatisticsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeRecordStatisticsSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeRecordStatisticsSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordStatisticsSummary', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeSubDomainRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSubDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sub_domain_records_with_options_async(
        self,
        request: alidns_20150109_models.DescribeSubDomainRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSubDomainRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeSubDomainRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubDomainRecords', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeSupportLinesResponse().from_map(
            self.do_rpcrequest('DescribeSupportLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_support_lines_with_options_async(
        self,
        request: alidns_20150109_models.DescribeSupportLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeSupportLinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeSupportLinesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSupportLines', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeTagsResponse().from_map(
            self.do_rpcrequest('DescribeTags', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: alidns_20150109_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTags', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeTransferDomainsResponse().from_map(
            self.do_rpcrequest('DescribeTransferDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_transfer_domains_with_options_async(
        self,
        request: alidns_20150109_models.DescribeTransferDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.DescribeTransferDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.DescribeTransferDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTransferDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ExecuteGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('ExecuteGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.ExecuteGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ExecuteGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ExecuteGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('ExecuteGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.GetMainDomainNameResponse().from_map(
            self.do_rpcrequest('GetMainDomainName', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_main_domain_name_with_options_async(
        self,
        request: alidns_20150109_models.GetMainDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetMainDomainNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.GetMainDomainNameResponse().from_map(
            await self.do_rpcrequest_async('GetMainDomainName', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.GetTxtRecordForVerifyResponse().from_map(
            self.do_rpcrequest('GetTxtRecordForVerify', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_txt_record_for_verify_with_options_async(
        self,
        request: alidns_20150109_models.GetTxtRecordForVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.GetTxtRecordForVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.GetTxtRecordForVerifyResponse().from_map(
            await self.do_rpcrequest_async('GetTxtRecordForVerify', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alidns_20150109_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ModifyHichinaDomainDNSResponse().from_map(
            self.do_rpcrequest('ModifyHichinaDomainDNS', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hichina_domain_dnswith_options_async(
        self,
        request: alidns_20150109_models.ModifyHichinaDomainDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ModifyHichinaDomainDNSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ModifyHichinaDomainDNSResponse().from_map(
            await self.do_rpcrequest_async('ModifyHichinaDomainDNS', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.MoveDomainResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveDomainResourceGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_domain_resource_group_with_options_async(
        self,
        request: alidns_20150109_models.MoveDomainResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveDomainResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.MoveDomainResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveDomainResourceGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.MoveGtmResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveGtmResourceGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_gtm_resource_group_with_options_async(
        self,
        request: alidns_20150109_models.MoveGtmResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.MoveGtmResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.MoveGtmResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveGtmResourceGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.OperateBatchDomainResponse().from_map(
            self.do_rpcrequest('OperateBatchDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_batch_domain_with_options_async(
        self,
        request: alidns_20150109_models.OperateBatchDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.OperateBatchDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.OperateBatchDomainResponse().from_map(
            await self.do_rpcrequest_async('OperateBatchDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.PreviewGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('PreviewGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preview_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.PreviewGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.PreviewGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.PreviewGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('PreviewGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.RetrieveDomainResponse().from_map(
            self.do_rpcrequest('RetrieveDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retrieve_domain_with_options_async(
        self,
        request: alidns_20150109_models.RetrieveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RetrieveDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.RetrieveDomainResponse().from_map(
            await self.do_rpcrequest_async('RetrieveDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.RollbackGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('RollbackGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.RollbackGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.RollbackGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.RollbackGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('RollbackGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDnsGtmAccessModeResponse().from_map(
            self.do_rpcrequest('SetDnsGtmAccessMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dns_gtm_access_mode_with_options_async(
        self,
        request: alidns_20150109_models.SetDnsGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDnsGtmAccessModeResponse().from_map(
            await self.do_rpcrequest_async('SetDnsGtmAccessMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDnsGtmMonitorStatusResponse().from_map(
            self.do_rpcrequest('SetDnsGtmMonitorStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dns_gtm_monitor_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDnsGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDnsGtmMonitorStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDnsGtmMonitorStatusResponse().from_map(
            await self.do_rpcrequest_async('SetDnsGtmMonitorStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDNSSLBStatusResponse().from_map(
            self.do_rpcrequest('SetDNSSLBStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dnsslbstatus_with_options_async(
        self,
        request: alidns_20150109_models.SetDNSSLBStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDNSSLBStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDNSSLBStatusResponse().from_map(
            await self.do_rpcrequest_async('SetDNSSLBStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDomainDnssecStatusResponse().from_map(
            self.do_rpcrequest('SetDomainDnssecStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_dnssec_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDomainDnssecStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainDnssecStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDomainDnssecStatusResponse().from_map(
            await self.do_rpcrequest_async('SetDomainDnssecStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDomainRecordStatusResponse().from_map(
            self.do_rpcrequest('SetDomainRecordStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_record_status_with_options_async(
        self,
        request: alidns_20150109_models.SetDomainRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetDomainRecordStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetDomainRecordStatusResponse().from_map(
            await self.do_rpcrequest_async('SetDomainRecordStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetGtmAccessModeResponse().from_map(
            self.do_rpcrequest('SetGtmAccessMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_gtm_access_mode_with_options_async(
        self,
        request: alidns_20150109_models.SetGtmAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetGtmAccessModeResponse().from_map(
            await self.do_rpcrequest_async('SetGtmAccessMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetGtmMonitorStatusResponse().from_map(
            self.do_rpcrequest('SetGtmMonitorStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_gtm_monitor_status_with_options_async(
        self,
        request: alidns_20150109_models.SetGtmMonitorStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SetGtmMonitorStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SetGtmMonitorStatusResponse().from_map(
            await self.do_rpcrequest_async('SetGtmMonitorStatus', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse().from_map(
            self.do_rpcrequest('SwitchDnsGtmInstanceStrategyMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dns_gtm_instance_strategy_mode_with_options_async(
        self,
        request: alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse().from_map(
            await self.do_rpcrequest_async('SwitchDnsGtmInstanceStrategyMode', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alidns_20150109_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.TransferDomainResponse().from_map(
            self.do_rpcrequest('TransferDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_domain_with_options_async(
        self,
        request: alidns_20150109_models.TransferDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.TransferDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.TransferDomainResponse().from_map(
            await self.do_rpcrequest_async('TransferDomain', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UnbindInstanceDomainsResponse().from_map(
            self.do_rpcrequest('UnbindInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_instance_domains_with_options_async(
        self,
        request: alidns_20150109_models.UnbindInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UnbindInstanceDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UnbindInstanceDomainsResponse().from_map(
            await self.do_rpcrequest_async('UnbindInstanceDomains', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: alidns_20150109_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateCustomLineResponse().from_map(
            self.do_rpcrequest('UpdateCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_custom_line_with_options_async(
        self,
        request: alidns_20150109_models.UpdateCustomLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateCustomLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateCustomLineResponse().from_map(
            await self.do_rpcrequest_async('UpdateCustomLine', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_dns_gtm_access_strategy_with_options(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('UpdateDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dns_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('UpdateDnsGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('UpdateDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dns_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('UpdateDnsGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse().from_map(
            self.do_rpcrequest('UpdateDnsGtmInstanceGlobalConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dns_gtm_instance_global_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateDnsGtmInstanceGlobalConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmMonitorResponse().from_map(
            self.do_rpcrequest('UpdateDnsGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dns_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDnsGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDnsGtmMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDnsGtmMonitorResponse().from_map(
            await self.do_rpcrequest_async('UpdateDnsGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDNSSLBWeightResponse().from_map(
            self.do_rpcrequest('UpdateDNSSLBWeight', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dnsslbweight_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDNSSLBWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDNSSLBWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDNSSLBWeightResponse().from_map(
            await self.do_rpcrequest_async('UpdateDNSSLBWeight', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainGroupResponse().from_map(
            self.do_rpcrequest('UpdateDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_group_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainGroup', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRecordResponse().from_map(
            self.do_rpcrequest('UpdateDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_record_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRecordResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainRecord', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRecordRemarkResponse().from_map(
            self.do_rpcrequest('UpdateDomainRecordRemark', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_record_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRecordRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRecordRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainRecordRemark', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRemarkResponse().from_map(
            self.do_rpcrequest('UpdateDomainRemark', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_remark_with_options_async(
        self,
        request: alidns_20150109_models.UpdateDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateDomainRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateDomainRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainRemark', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmAccessStrategyResponse().from_map(
            self.do_rpcrequest('UpdateGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gtm_access_strategy_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmAccessStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAccessStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmAccessStrategyResponse().from_map(
            await self.do_rpcrequest_async('UpdateGtmAccessStrategy', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmAddressPoolResponse().from_map(
            self.do_rpcrequest('UpdateGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gtm_address_pool_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmAddressPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmAddressPoolResponse().from_map(
            await self.do_rpcrequest_async('UpdateGtmAddressPool', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse().from_map(
            self.do_rpcrequest('UpdateGtmInstanceGlobalConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gtm_instance_global_config_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmInstanceGlobalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateGtmInstanceGlobalConfig', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmMonitorResponse().from_map(
            self.do_rpcrequest('UpdateGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gtm_monitor_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmMonitorResponse().from_map(
            await self.do_rpcrequest_async('UpdateGtmMonitor', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmRecoveryPlanResponse().from_map(
            self.do_rpcrequest('UpdateGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gtm_recovery_plan_with_options_async(
        self,
        request: alidns_20150109_models.UpdateGtmRecoveryPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.UpdateGtmRecoveryPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.UpdateGtmRecoveryPlanResponse().from_map(
            await self.do_rpcrequest_async('UpdateGtmRecoveryPlan', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse().from_map(
            self.do_rpcrequest('ValidateDnsGtmAttributeInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_dns_gtm_attribute_info_with_options_async(
        self,
        request: alidns_20150109_models.ValidateDnsGtmAttributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alidns_20150109_models.ValidateDnsGtmAttributeInfoResponse().from_map(
            await self.do_rpcrequest_async('ValidateDnsGtmAttributeInfo', '2015-01-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
