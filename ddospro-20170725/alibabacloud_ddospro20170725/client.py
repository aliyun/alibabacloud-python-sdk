# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddospro20170725 import models as ddo_spro_20170725_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddospro', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_switch_priority_with_options(
        self,
        request: ddo_spro_20170725_models.ConfigSwitchPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ConfigSwitchPriorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ConfigSwitchPriorityResponse().from_map(
            self.do_rpcrequest('ConfigSwitchPriority', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_switch_priority_with_options_async(
        self,
        request: ddo_spro_20170725_models.ConfigSwitchPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ConfigSwitchPriorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ConfigSwitchPriorityResponse().from_map(
            await self.do_rpcrequest_async('ConfigSwitchPriority', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_switch_priority(
        self,
        request: ddo_spro_20170725_models.ConfigSwitchPriorityRequest,
    ) -> ddo_spro_20170725_models.ConfigSwitchPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_switch_priority_with_options(request, runtime)

    async def config_switch_priority_async(
        self,
        request: ddo_spro_20170725_models.ConfigSwitchPriorityRequest,
    ) -> ddo_spro_20170725_models.ConfigSwitchPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_switch_priority_with_options_async(request, runtime)

    def create_cc_customed_rule_with_options(
        self,
        request: ddo_spro_20170725_models.CreateCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateCcCustomedRuleResponse().from_map(
            self.do_rpcrequest('CreateCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cc_customed_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.CreateCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateCcCustomedRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cc_customed_rule(
        self,
        request: ddo_spro_20170725_models.CreateCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.CreateCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cc_customed_rule_with_options(request, runtime)

    async def create_cc_customed_rule_async(
        self,
        request: ddo_spro_20170725_models.CreateCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.CreateCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cc_customed_rule_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: ddo_spro_20170725_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateDomainResponse().from_map(
            self.do_rpcrequest('CreateDomain', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: ddo_spro_20170725_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateDomainResponse().from_map(
            await self.do_rpcrequest_async('CreateDomain', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain(
        self,
        request: ddo_spro_20170725_models.CreateDomainRequest,
    ) -> ddo_spro_20170725_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: ddo_spro_20170725_models.CreateDomainRequest,
    ) -> ddo_spro_20170725_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_port_rule_with_options(
        self,
        request: ddo_spro_20170725_models.CreatePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreatePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreatePortRuleResponse().from_map(
            self.do_rpcrequest('CreatePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_port_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.CreatePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreatePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreatePortRuleResponse().from_map(
            await self.do_rpcrequest_async('CreatePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_port_rule(
        self,
        request: ddo_spro_20170725_models.CreatePortRuleRequest,
    ) -> ddo_spro_20170725_models.CreatePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_port_rule_with_options(request, runtime)

    async def create_port_rule_async(
        self,
        request: ddo_spro_20170725_models.CreatePortRuleRequest,
    ) -> ddo_spro_20170725_models.CreatePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_port_rule_with_options_async(request, runtime)

    def create_transmit_line_with_options(
        self,
        request: ddo_spro_20170725_models.CreateTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateTransmitLineResponse().from_map(
            self.do_rpcrequest('CreateTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_transmit_line_with_options_async(
        self,
        request: ddo_spro_20170725_models.CreateTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.CreateTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.CreateTransmitLineResponse().from_map(
            await self.do_rpcrequest_async('CreateTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_transmit_line(
        self,
        request: ddo_spro_20170725_models.CreateTransmitLineRequest,
    ) -> ddo_spro_20170725_models.CreateTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transmit_line_with_options(request, runtime)

    async def create_transmit_line_async(
        self,
        request: ddo_spro_20170725_models.CreateTransmitLineRequest,
    ) -> ddo_spro_20170725_models.CreateTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transmit_line_with_options_async(request, runtime)

    def delete_cc_customed_rule_with_options(
        self,
        request: ddo_spro_20170725_models.DeleteCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteCcCustomedRuleResponse().from_map(
            self.do_rpcrequest('DeleteCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cc_customed_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.DeleteCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteCcCustomedRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cc_customed_rule(
        self,
        request: ddo_spro_20170725_models.DeleteCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.DeleteCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cc_customed_rule_with_options(request, runtime)

    async def delete_cc_customed_rule_async(
        self,
        request: ddo_spro_20170725_models.DeleteCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.DeleteCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cc_customed_rule_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: ddo_spro_20170725_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteDomainResponse().from_map(
            self.do_rpcrequest('DeleteDomain', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: ddo_spro_20170725_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomain', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain(
        self,
        request: ddo_spro_20170725_models.DeleteDomainRequest,
    ) -> ddo_spro_20170725_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: ddo_spro_20170725_models.DeleteDomainRequest,
    ) -> ddo_spro_20170725_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_port_rule_with_options(
        self,
        request: ddo_spro_20170725_models.DeletePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeletePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeletePortRuleResponse().from_map(
            self.do_rpcrequest('DeletePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_port_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.DeletePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeletePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeletePortRuleResponse().from_map(
            await self.do_rpcrequest_async('DeletePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_port_rule(
        self,
        request: ddo_spro_20170725_models.DeletePortRuleRequest,
    ) -> ddo_spro_20170725_models.DeletePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_port_rule_with_options(request, runtime)

    async def delete_port_rule_async(
        self,
        request: ddo_spro_20170725_models.DeletePortRuleRequest,
    ) -> ddo_spro_20170725_models.DeletePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_port_rule_with_options_async(request, runtime)

    def delete_transmit_line_with_options(
        self,
        request: ddo_spro_20170725_models.DeleteTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteTransmitLineResponse().from_map(
            self.do_rpcrequest('DeleteTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_transmit_line_with_options_async(
        self,
        request: ddo_spro_20170725_models.DeleteTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DeleteTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DeleteTransmitLineResponse().from_map(
            await self.do_rpcrequest_async('DeleteTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_transmit_line(
        self,
        request: ddo_spro_20170725_models.DeleteTransmitLineRequest,
    ) -> ddo_spro_20170725_models.DeleteTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transmit_line_with_options(request, runtime)

    async def delete_transmit_line_async(
        self,
        request: ddo_spro_20170725_models.DeleteTransmitLineRequest,
    ) -> ddo_spro_20170725_models.DeleteTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transmit_line_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeBackSourceCidrResponse().from_map(
            self.do_rpcrequest('DescribeBackSourceCidr', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeBackSourceCidrResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackSourceCidr', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_source_cidr(
        self,
        request: ddo_spro_20170725_models.DescribeBackSourceCidrRequest,
    ) -> ddo_spro_20170725_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddo_spro_20170725_models.DescribeBackSourceCidrRequest,
    ) -> ddo_spro_20170725_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_biz_flow_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeBizFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeBizFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeBizFlowResponse().from_map(
            self.do_rpcrequest('DescribeBizFlow', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_flow_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeBizFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeBizFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeBizFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeBizFlow', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_flow(
        self,
        request: ddo_spro_20170725_models.DescribeBizFlowRequest,
    ) -> ddo_spro_20170725_models.DescribeBizFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_flow_with_options(request, runtime)

    async def describe_biz_flow_async(
        self,
        request: ddo_spro_20170725_models.DescribeBizFlowRequest,
    ) -> ddo_spro_20170725_models.DescribeBizFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_flow_with_options_async(request, runtime)

    def describe_cc_events_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeCcEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeCcEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeCcEventsResponse().from_map(
            self.do_rpcrequest('DescribeCcEvents', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_events_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeCcEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeCcEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeCcEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcEvents', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_events(
        self,
        request: ddo_spro_20170725_models.DescribeCcEventsRequest,
    ) -> ddo_spro_20170725_models.DescribeCcEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_events_with_options(request, runtime)

    async def describe_cc_events_async(
        self,
        request: ddo_spro_20170725_models.DescribeCcEventsRequest,
    ) -> ddo_spro_20170725_models.DescribeCcEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_events_with_options_async(request, runtime)

    def describe_cname_auto_status_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeCnameAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeCnameAutoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeCnameAutoStatusResponse().from_map(
            self.do_rpcrequest('DescribeCnameAutoStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cname_auto_status_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeCnameAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeCnameAutoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeCnameAutoStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeCnameAutoStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cname_auto_status(
        self,
        request: ddo_spro_20170725_models.DescribeCnameAutoStatusRequest,
    ) -> ddo_spro_20170725_models.DescribeCnameAutoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cname_auto_status_with_options(request, runtime)

    async def describe_cname_auto_status_async(
        self,
        request: ddo_spro_20170725_models.DescribeCnameAutoStatusRequest,
    ) -> ddo_spro_20170725_models.DescribeCnameAutoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cname_auto_status_with_options_async(request, runtime)

    def describe_ddos_attack_events_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackEventsResponse().from_map(
            self.do_rpcrequest('DescribeDdosAttackEvents', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_attack_events_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosAttackEvents', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_attack_events(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventsRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_attack_events_with_options(request, runtime)

    async def describe_ddos_attack_events_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventsRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_attack_events_with_options_async(request, runtime)

    def describe_ddos_attack_event_source_ips_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse().from_map(
            self.do_rpcrequest('DescribeDdosAttackEventSourceIps', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_attack_event_source_ips_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosAttackEventSourceIps', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_attack_event_source_ips(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_attack_event_source_ips_with_options(request, runtime)

    async def describe_ddos_attack_event_source_ips_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackEventSourceIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_attack_event_source_ips_with_options_async(request, runtime)

    def describe_ddos_attack_type_chart_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackTypeChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse().from_map(
            self.do_rpcrequest('DescribeDdosAttackTypeChart', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_attack_type_chart_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackTypeChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosAttackTypeChart', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_attack_type_chart(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackTypeChartRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_attack_type_chart_with_options(request, runtime)

    async def describe_ddos_attack_type_chart_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosAttackTypeChartRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosAttackTypeChartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_attack_type_chart_with_options_async(request, runtime)

    def describe_ddos_flow_proportion_diagram_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse().from_map(
            self.do_rpcrequest('DescribeDdosFlowProportionDiagram', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_flow_proportion_diagram_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosFlowProportionDiagram', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_flow_proportion_diagram(
        self,
        request: ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_flow_proportion_diagram_with_options(request, runtime)

    async def describe_ddos_flow_proportion_diagram_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosFlowProportionDiagramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_flow_proportion_diagram_with_options_async(request, runtime)

    def describe_ddos_ip_config_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosIpConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosIpConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosIpConfigResponse().from_map(
            self.do_rpcrequest('DescribeDdosIpConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_ip_config_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosIpConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosIpConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosIpConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosIpConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_ip_config(
        self,
        request: ddo_spro_20170725_models.DescribeDdosIpConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosIpConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_ip_config_with_options(request, runtime)

    async def describe_ddos_ip_config_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosIpConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosIpConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_ip_config_with_options_async(request, runtime)

    def describe_ddos_peak_flow_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDdosPeakFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosPeakFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosPeakFlowResponse().from_map(
            self.do_rpcrequest('DescribeDdosPeakFlow', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_peak_flow_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosPeakFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDdosPeakFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDdosPeakFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosPeakFlow', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_peak_flow(
        self,
        request: ddo_spro_20170725_models.DescribeDdosPeakFlowRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosPeakFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_peak_flow_with_options(request, runtime)

    async def describe_ddos_peak_flow_async(
        self,
        request: ddo_spro_20170725_models.DescribeDdosPeakFlowRequest,
    ) -> ddo_spro_20170725_models.DescribeDdosPeakFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_peak_flow_with_options_async(request, runtime)

    def describe_domain_config_page_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDomainConfigPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDomainConfigPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDomainConfigPageResponse().from_map(
            self.do_rpcrequest('DescribeDomainConfigPage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_config_page_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDomainConfigPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDomainConfigPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDomainConfigPageResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainConfigPage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_config_page(
        self,
        request: ddo_spro_20170725_models.DescribeDomainConfigPageRequest,
    ) -> ddo_spro_20170725_models.DescribeDomainConfigPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_config_page_with_options(request, runtime)

    async def describe_domain_config_page_async(
        self,
        request: ddo_spro_20170725_models.DescribeDomainConfigPageRequest,
    ) -> ddo_spro_20170725_models.DescribeDomainConfigPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_config_page_with_options_async(request, runtime)

    def describe_domain_security_config_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeDomainSecurityConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse().from_map(
            self.do_rpcrequest('DescribeDomainSecurityConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_security_config_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeDomainSecurityConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSecurityConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_security_config(
        self,
        request: ddo_spro_20170725_models.DescribeDomainSecurityConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_security_config_with_options(request, runtime)

    async def describe_domain_security_config_async(
        self,
        request: ddo_spro_20170725_models.DescribeDomainSecurityConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeDomainSecurityConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_security_config_with_options_async(request, runtime)

    def describe_health_check_config_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeHealthCheckConfigResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_config_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeHealthCheckConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_config(
        self,
        request: ddo_spro_20170725_models.DescribeHealthCheckConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_config_with_options(request, runtime)

    async def describe_health_check_config_async(
        self,
        request: ddo_spro_20170725_models.DescribeHealthCheckConfigRequest,
    ) -> ddo_spro_20170725_models.DescribeHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_config_with_options_async(request, runtime)

    def describe_instance_page_with_options(
        self,
        request: ddo_spro_20170725_models.DescribeInstancePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeInstancePageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeInstancePageResponse().from_map(
            self.do_rpcrequest('DescribeInstancePage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_page_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribeInstancePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribeInstancePageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribeInstancePageResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstancePage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_page(
        self,
        request: ddo_spro_20170725_models.DescribeInstancePageRequest,
    ) -> ddo_spro_20170725_models.DescribeInstancePageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_page_with_options(request, runtime)

    async def describe_instance_page_async(
        self,
        request: ddo_spro_20170725_models.DescribeInstancePageRequest,
    ) -> ddo_spro_20170725_models.DescribeInstancePageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_page_with_options_async(request, runtime)

    def describe_port_rule_page_with_options(
        self,
        request: ddo_spro_20170725_models.DescribePortRulePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribePortRulePageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribePortRulePageResponse().from_map(
            self.do_rpcrequest('DescribePortRulePage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_rule_page_with_options_async(
        self,
        request: ddo_spro_20170725_models.DescribePortRulePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.DescribePortRulePageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.DescribePortRulePageResponse().from_map(
            await self.do_rpcrequest_async('DescribePortRulePage', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_rule_page(
        self,
        request: ddo_spro_20170725_models.DescribePortRulePageRequest,
    ) -> ddo_spro_20170725_models.DescribePortRulePageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_rule_page_with_options(request, runtime)

    async def describe_port_rule_page_async(
        self,
        request: ddo_spro_20170725_models.DescribePortRulePageRequest,
    ) -> ddo_spro_20170725_models.DescribePortRulePageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_rule_page_with_options_async(request, runtime)

    def list_cc_customed_rule_with_options(
        self,
        request: ddo_spro_20170725_models.ListCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ListCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ListCcCustomedRuleResponse().from_map(
            self.do_rpcrequest('ListCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cc_customed_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.ListCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ListCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ListCcCustomedRuleResponse().from_map(
            await self.do_rpcrequest_async('ListCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cc_customed_rule(
        self,
        request: ddo_spro_20170725_models.ListCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.ListCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cc_customed_rule_with_options(request, runtime)

    async def list_cc_customed_rule_async(
        self,
        request: ddo_spro_20170725_models.ListCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.ListCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cc_customed_rule_with_options_async(request, runtime)

    def modify_cc_custom_status_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyCcCustomStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcCustomStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcCustomStatusResponse().from_map(
            self.do_rpcrequest('ModifyCcCustomStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cc_custom_status_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcCustomStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcCustomStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcCustomStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyCcCustomStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cc_custom_status(
        self,
        request: ddo_spro_20170725_models.ModifyCcCustomStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyCcCustomStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cc_custom_status_with_options(request, runtime)

    async def modify_cc_custom_status_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcCustomStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyCcCustomStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cc_custom_status_with_options_async(request, runtime)

    def modify_cc_status_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcStatusResponse().from_map(
            self.do_rpcrequest('ModifyCcStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cc_status_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyCcStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cc_status(
        self,
        request: ddo_spro_20170725_models.ModifyCcStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cc_status_with_options(request, runtime)

    async def modify_cc_status_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cc_status_with_options_async(request, runtime)

    def modify_cc_template_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyCcTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcTemplateResponse().from_map(
            self.do_rpcrequest('ModifyCcTemplate', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cc_template_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyCcTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyCcTemplateResponse().from_map(
            await self.do_rpcrequest_async('ModifyCcTemplate', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cc_template(
        self,
        request: ddo_spro_20170725_models.ModifyCcTemplateRequest,
    ) -> ddo_spro_20170725_models.ModifyCcTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cc_template_with_options(request, runtime)

    async def modify_cc_template_async(
        self,
        request: ddo_spro_20170725_models.ModifyCcTemplateRequest,
    ) -> ddo_spro_20170725_models.ModifyCcTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cc_template_with_options_async(request, runtime)

    def modify_ddo_sprotect_config_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyDDoSProtectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse().from_map(
            self.do_rpcrequest('ModifyDDoSProtectConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ddo_sprotect_config_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyDDoSProtectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyDDoSProtectConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ddo_sprotect_config(
        self,
        request: ddo_spro_20170725_models.ModifyDDoSProtectConfigRequest,
    ) -> ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ddo_sprotect_config_with_options(request, runtime)

    async def modify_ddo_sprotect_config_async(
        self,
        request: ddo_spro_20170725_models.ModifyDDoSProtectConfigRequest,
    ) -> ddo_spro_20170725_models.ModifyDDoSProtectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ddo_sprotect_config_with_options_async(request, runtime)

    def modify_domain_black_white_list_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyDomainBlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse().from_map(
            self.do_rpcrequest('ModifyDomainBlackWhiteList', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_domain_black_white_list_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyDomainBlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainBlackWhiteList', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_black_white_list(
        self,
        request: ddo_spro_20170725_models.ModifyDomainBlackWhiteListRequest,
    ) -> ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_black_white_list_with_options(request, runtime)

    async def modify_domain_black_white_list_async(
        self,
        request: ddo_spro_20170725_models.ModifyDomainBlackWhiteListRequest,
    ) -> ddo_spro_20170725_models.ModifyDomainBlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_black_white_list_with_options_async(request, runtime)

    def modify_domain_proxy_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyDomainProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDomainProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDomainProxyResponse().from_map(
            self.do_rpcrequest('ModifyDomainProxy', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_domain_proxy_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyDomainProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyDomainProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyDomainProxyResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainProxy', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_proxy(
        self,
        request: ddo_spro_20170725_models.ModifyDomainProxyRequest,
    ) -> ddo_spro_20170725_models.ModifyDomainProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_proxy_with_options(request, runtime)

    async def modify_domain_proxy_async(
        self,
        request: ddo_spro_20170725_models.ModifyDomainProxyRequest,
    ) -> ddo_spro_20170725_models.ModifyDomainProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_proxy_with_options_async(request, runtime)

    def modify_elastic_bandwidth_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyElasticBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyElasticBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyElasticBandwidthResponse().from_map(
            self.do_rpcrequest('ModifyElasticBandwidth', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_elastic_bandwidth_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyElasticBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyElasticBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyElasticBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyElasticBandwidth', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elastic_bandwidth(
        self,
        request: ddo_spro_20170725_models.ModifyElasticBandwidthRequest,
    ) -> ddo_spro_20170725_models.ModifyElasticBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_bandwidth_with_options(request, runtime)

    async def modify_elastic_bandwidth_async(
        self,
        request: ddo_spro_20170725_models.ModifyElasticBandwidthRequest,
    ) -> ddo_spro_20170725_models.ModifyElasticBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_bandwidth_with_options_async(request, runtime)

    def modify_health_check_config_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyHealthCheckConfigResponse().from_map(
            self.do_rpcrequest('ModifyHealthCheckConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_health_check_config_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyHealthCheckConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyHealthCheckConfig', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_health_check_config(
        self,
        request: ddo_spro_20170725_models.ModifyHealthCheckConfigRequest,
    ) -> ddo_spro_20170725_models.ModifyHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    async def modify_health_check_config_async(
        self,
        request: ddo_spro_20170725_models.ModifyHealthCheckConfigRequest,
    ) -> ddo_spro_20170725_models.ModifyHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_health_check_config_with_options_async(request, runtime)

    def modify_ip_cname_status_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyIpCnameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyIpCnameStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyIpCnameStatusResponse().from_map(
            self.do_rpcrequest('ModifyIpCnameStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ip_cname_status_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyIpCnameStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyIpCnameStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyIpCnameStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpCnameStatus', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_cname_status(
        self,
        request: ddo_spro_20170725_models.ModifyIpCnameStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyIpCnameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_cname_status_with_options(request, runtime)

    async def modify_ip_cname_status_async(
        self,
        request: ddo_spro_20170725_models.ModifyIpCnameStatusRequest,
    ) -> ddo_spro_20170725_models.ModifyIpCnameStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_cname_status_with_options_async(request, runtime)

    def modify_persistence_time_out_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyPersistenceTimeOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse().from_map(
            self.do_rpcrequest('ModifyPersistenceTimeOut', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_persistence_time_out_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyPersistenceTimeOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse().from_map(
            await self.do_rpcrequest_async('ModifyPersistenceTimeOut', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_persistence_time_out(
        self,
        request: ddo_spro_20170725_models.ModifyPersistenceTimeOutRequest,
    ) -> ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_persistence_time_out_with_options(request, runtime)

    async def modify_persistence_time_out_async(
        self,
        request: ddo_spro_20170725_models.ModifyPersistenceTimeOutRequest,
    ) -> ddo_spro_20170725_models.ModifyPersistenceTimeOutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_persistence_time_out_with_options_async(request, runtime)

    def modify_real_servers_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyRealServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyRealServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyRealServersResponse().from_map(
            self.do_rpcrequest('ModifyRealServers', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_real_servers_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyRealServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyRealServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyRealServersResponse().from_map(
            await self.do_rpcrequest_async('ModifyRealServers', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_real_servers(
        self,
        request: ddo_spro_20170725_models.ModifyRealServersRequest,
    ) -> ddo_spro_20170725_models.ModifyRealServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_real_servers_with_options(request, runtime)

    async def modify_real_servers_async(
        self,
        request: ddo_spro_20170725_models.ModifyRealServersRequest,
    ) -> ddo_spro_20170725_models.ModifyRealServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_real_servers_with_options_async(request, runtime)

    def modify_transmit_line_with_options(
        self,
        request: ddo_spro_20170725_models.ModifyTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyTransmitLineResponse().from_map(
            self.do_rpcrequest('ModifyTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_transmit_line_with_options_async(
        self,
        request: ddo_spro_20170725_models.ModifyTransmitLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.ModifyTransmitLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.ModifyTransmitLineResponse().from_map(
            await self.do_rpcrequest_async('ModifyTransmitLine', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_transmit_line(
        self,
        request: ddo_spro_20170725_models.ModifyTransmitLineRequest,
    ) -> ddo_spro_20170725_models.ModifyTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_transmit_line_with_options(request, runtime)

    async def modify_transmit_line_async(
        self,
        request: ddo_spro_20170725_models.ModifyTransmitLineRequest,
    ) -> ddo_spro_20170725_models.ModifyTransmitLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_transmit_line_with_options_async(request, runtime)

    def update_cc_customed_rule_with_options(
        self,
        request: ddo_spro_20170725_models.UpdateCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.UpdateCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.UpdateCcCustomedRuleResponse().from_map(
            self.do_rpcrequest('UpdateCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_customed_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.UpdateCcCustomedRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.UpdateCcCustomedRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.UpdateCcCustomedRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcCustomedRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_customed_rule(
        self,
        request: ddo_spro_20170725_models.UpdateCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.UpdateCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_customed_rule_with_options(request, runtime)

    async def update_cc_customed_rule_async(
        self,
        request: ddo_spro_20170725_models.UpdateCcCustomedRuleRequest,
    ) -> ddo_spro_20170725_models.UpdateCcCustomedRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_customed_rule_with_options_async(request, runtime)

    def update_port_rule_with_options(
        self,
        request: ddo_spro_20170725_models.UpdatePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.UpdatePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.UpdatePortRuleResponse().from_map(
            self.do_rpcrequest('UpdatePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_port_rule_with_options_async(
        self,
        request: ddo_spro_20170725_models.UpdatePortRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddo_spro_20170725_models.UpdatePortRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddo_spro_20170725_models.UpdatePortRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdatePortRule', '2017-07-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_port_rule(
        self,
        request: ddo_spro_20170725_models.UpdatePortRuleRequest,
    ) -> ddo_spro_20170725_models.UpdatePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_port_rule_with_options(request, runtime)

    async def update_port_rule_async(
        self,
        request: ddo_spro_20170725_models.UpdatePortRuleRequest,
    ) -> ddo_spro_20170725_models.UpdatePortRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_port_rule_with_options_async(request, runtime)
