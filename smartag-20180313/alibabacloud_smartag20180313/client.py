# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_smartag20180313 import models as smartag_20180313_models
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
        self._endpoint = self.get_endpoint('smartag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.ActivateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActivateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ActivateSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('ActivateSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.ActivateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActivateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ActivateSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('ActivateSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_smart_access_gateway(
        self,
        request: smartag_20180313_models.ActivateSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.ActivateSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_smart_access_gateway_with_options(request, runtime)

    async def activate_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.ActivateSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.ActivateSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_smart_access_gateway_with_options_async(request, runtime)

    def active_flow_log_with_options(
        self,
        request: smartag_20180313_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ActiveFlowLogResponse().from_map(
            self.do_rpcrequest('ActiveFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ActiveFlowLogResponse().from_map(
            await self.do_rpcrequest_async('ActiveFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def active_flow_log(
        self,
        request: smartag_20180313_models.ActiveFlowLogRequest,
    ) -> smartag_20180313_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: smartag_20180313_models.ActiveFlowLogRequest,
    ) -> smartag_20180313_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def add_aclrule_with_options(
        self,
        request: smartag_20180313_models.AddACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddACLRuleResponse().from_map(
            self.do_rpcrequest('AddACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.AddACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddACLRuleResponse().from_map(
            await self.do_rpcrequest_async('AddACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_aclrule(
        self,
        request: smartag_20180313_models.AddACLRuleRequest,
    ) -> smartag_20180313_models.AddACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_aclrule_with_options(request, runtime)

    async def add_aclrule_async(
        self,
        request: smartag_20180313_models.AddACLRuleRequest,
    ) -> smartag_20180313_models.AddACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_aclrule_with_options_async(request, runtime)

    def add_dnat_entry_with_options(
        self,
        request: smartag_20180313_models.AddDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddDnatEntryResponse().from_map(
            self.do_rpcrequest('AddDnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dnat_entry_with_options_async(
        self,
        request: smartag_20180313_models.AddDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddDnatEntryResponse().from_map(
            await self.do_rpcrequest_async('AddDnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dnat_entry(
        self,
        request: smartag_20180313_models.AddDnatEntryRequest,
    ) -> smartag_20180313_models.AddDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_dnat_entry_with_options(request, runtime)

    async def add_dnat_entry_async(
        self,
        request: smartag_20180313_models.AddDnatEntryRequest,
    ) -> smartag_20180313_models.AddDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dnat_entry_with_options_async(request, runtime)

    def add_network_optimization_setting_with_options(
        self,
        request: smartag_20180313_models.AddNetworkOptimizationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddNetworkOptimizationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddNetworkOptimizationSettingResponse().from_map(
            self.do_rpcrequest('AddNetworkOptimizationSetting', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_network_optimization_setting_with_options_async(
        self,
        request: smartag_20180313_models.AddNetworkOptimizationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddNetworkOptimizationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddNetworkOptimizationSettingResponse().from_map(
            await self.do_rpcrequest_async('AddNetworkOptimizationSetting', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_network_optimization_setting(
        self,
        request: smartag_20180313_models.AddNetworkOptimizationSettingRequest,
    ) -> smartag_20180313_models.AddNetworkOptimizationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_network_optimization_setting_with_options(request, runtime)

    async def add_network_optimization_setting_async(
        self,
        request: smartag_20180313_models.AddNetworkOptimizationSettingRequest,
    ) -> smartag_20180313_models.AddNetworkOptimizationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_network_optimization_setting_with_options_async(request, runtime)

    def add_sag_cidr_with_options(
        self,
        request: smartag_20180313_models.AddSagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddSagCidrResponse().from_map(
            self.do_rpcrequest('AddSagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sag_cidr_with_options_async(
        self,
        request: smartag_20180313_models.AddSagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddSagCidrResponse().from_map(
            await self.do_rpcrequest_async('AddSagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sag_cidr(
        self,
        request: smartag_20180313_models.AddSagCidrRequest,
    ) -> smartag_20180313_models.AddSagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sag_cidr_with_options(request, runtime)

    async def add_sag_cidr_async(
        self,
        request: smartag_20180313_models.AddSagCidrRequest,
    ) -> smartag_20180313_models.AddSagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sag_cidr_with_options_async(request, runtime)

    def add_snat_entry_with_options(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddSnatEntryResponse().from_map(
            self.do_rpcrequest('AddSnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_snat_entry_with_options_async(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AddSnatEntryResponse().from_map(
            await self.do_rpcrequest_async('AddSnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_snat_entry(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_snat_entry_with_options(request, runtime)

    async def add_snat_entry_async(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_snat_entry_with_options_async(request, runtime)

    def associate_aclwith_options(
        self,
        request: smartag_20180313_models.AssociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateACLResponse().from_map(
            self.do_rpcrequest('AssociateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_aclwith_options_async(
        self,
        request: smartag_20180313_models.AssociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateACLResponse().from_map(
            await self.do_rpcrequest_async('AssociateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_acl(
        self,
        request: smartag_20180313_models.AssociateACLRequest,
    ) -> smartag_20180313_models.AssociateACLResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_aclwith_options(request, runtime)

    async def associate_acl_async(
        self,
        request: smartag_20180313_models.AssociateACLRequest,
    ) -> smartag_20180313_models.AssociateACLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_aclwith_options_async(request, runtime)

    def associate_flow_log_with_options(
        self,
        request: smartag_20180313_models.AssociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateFlowLogResponse().from_map(
            self.do_rpcrequest('AssociateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.AssociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateFlowLogResponse().from_map(
            await self.do_rpcrequest_async('AssociateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_flow_log(
        self,
        request: smartag_20180313_models.AssociateFlowLogRequest,
    ) -> smartag_20180313_models.AssociateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_flow_log_with_options(request, runtime)

    async def associate_flow_log_async(
        self,
        request: smartag_20180313_models.AssociateFlowLogRequest,
    ) -> smartag_20180313_models.AssociateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_flow_log_with_options_async(request, runtime)

    def associate_qos_with_options(
        self,
        request: smartag_20180313_models.AssociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateQosResponse().from_map(
            self.do_rpcrequest('AssociateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_qos_with_options_async(
        self,
        request: smartag_20180313_models.AssociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AssociateQosResponse().from_map(
            await self.do_rpcrequest_async('AssociateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_qos(
        self,
        request: smartag_20180313_models.AssociateQosRequest,
    ) -> smartag_20180313_models.AssociateQosResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_qos_with_options(request, runtime)

    async def associate_qos_async(
        self,
        request: smartag_20180313_models.AssociateQosRequest,
    ) -> smartag_20180313_models.AssociateQosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_qos_with_options_async(request, runtime)

    def attach_network_optimization_sags_with_options(
        self,
        request: smartag_20180313_models.AttachNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AttachNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AttachNetworkOptimizationSagsResponse().from_map(
            self.do_rpcrequest('AttachNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_network_optimization_sags_with_options_async(
        self,
        request: smartag_20180313_models.AttachNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AttachNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.AttachNetworkOptimizationSagsResponse().from_map(
            await self.do_rpcrequest_async('AttachNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_network_optimization_sags(
        self,
        request: smartag_20180313_models.AttachNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.AttachNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_network_optimization_sags_with_options(request, runtime)

    async def attach_network_optimization_sags_async(
        self,
        request: smartag_20180313_models.AttachNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.AttachNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_network_optimization_sags_with_options_async(request, runtime)

    def bind_serial_number_with_options(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindSerialNumberResponse().from_map(
            self.do_rpcrequest('BindSerialNumber', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_serial_number_with_options_async(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindSerialNumberResponse().from_map(
            await self.do_rpcrequest_async('BindSerialNumber', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_serial_number(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_serial_number_with_options(request, runtime)

    async def bind_serial_number_async(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_serial_number_with_options_async(request, runtime)

    def bind_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.BindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('BindSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.BindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('BindSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_smart_access_gateway(
        self,
        request: smartag_20180313_models.BindSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.BindSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_smart_access_gateway_with_options(request, runtime)

    async def bind_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.BindSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.BindSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_smart_access_gateway_with_options_async(request, runtime)

    def bind_vbr_with_options(
        self,
        request: smartag_20180313_models.BindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindVbrResponse().from_map(
            self.do_rpcrequest('BindVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_vbr_with_options_async(
        self,
        request: smartag_20180313_models.BindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.BindVbrResponse().from_map(
            await self.do_rpcrequest_async('BindVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_vbr(
        self,
        request: smartag_20180313_models.BindVbrRequest,
    ) -> smartag_20180313_models.BindVbrResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_vbr_with_options(request, runtime)

    async def bind_vbr_async(
        self,
        request: smartag_20180313_models.BindVbrRequest,
    ) -> smartag_20180313_models.BindVbrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_vbr_with_options_async(request, runtime)

    def clear_sag_cipher_with_options(
        self,
        request: smartag_20180313_models.ClearSagCipherRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagCipherResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ClearSagCipherResponse().from_map(
            self.do_rpcrequest('ClearSagCipher', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_sag_cipher_with_options_async(
        self,
        request: smartag_20180313_models.ClearSagCipherRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagCipherResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ClearSagCipherResponse().from_map(
            await self.do_rpcrequest_async('ClearSagCipher', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_sag_cipher(
        self,
        request: smartag_20180313_models.ClearSagCipherRequest,
    ) -> smartag_20180313_models.ClearSagCipherResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_sag_cipher_with_options(request, runtime)

    async def clear_sag_cipher_async(
        self,
        request: smartag_20180313_models.ClearSagCipherRequest,
    ) -> smartag_20180313_models.ClearSagCipherResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_sag_cipher_with_options_async(request, runtime)

    def clear_sag_routeable_address_with_options(
        self,
        request: smartag_20180313_models.ClearSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ClearSagRouteableAddressResponse().from_map(
            self.do_rpcrequest('ClearSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_sag_routeable_address_with_options_async(
        self,
        request: smartag_20180313_models.ClearSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ClearSagRouteableAddressResponse().from_map(
            await self.do_rpcrequest_async('ClearSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_sag_routeable_address(
        self,
        request: smartag_20180313_models.ClearSagRouteableAddressRequest,
    ) -> smartag_20180313_models.ClearSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_sag_routeable_address_with_options(request, runtime)

    async def clear_sag_routeable_address_async(
        self,
        request: smartag_20180313_models.ClearSagRouteableAddressRequest,
    ) -> smartag_20180313_models.ClearSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_sag_routeable_address_with_options_async(request, runtime)

    def create_aclwith_options(
        self,
        request: smartag_20180313_models.CreateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateACLResponse().from_map(
            self.do_rpcrequest('CreateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_aclwith_options_async(
        self,
        request: smartag_20180313_models.CreateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateACLResponse().from_map(
            await self.do_rpcrequest_async('CreateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl(
        self,
        request: smartag_20180313_models.CreateACLRequest,
    ) -> smartag_20180313_models.CreateACLResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aclwith_options(request, runtime)

    async def create_acl_async(
        self,
        request: smartag_20180313_models.CreateACLRequest,
    ) -> smartag_20180313_models.CreateACLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aclwith_options_async(request, runtime)

    def create_cloud_connect_network_with_options(
        self,
        request: smartag_20180313_models.CreateCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateCloudConnectNetworkResponse().from_map(
            self.do_rpcrequest('CreateCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.CreateCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateCloudConnectNetworkResponse().from_map(
            await self.do_rpcrequest_async('CreateCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cloud_connect_network(
        self,
        request: smartag_20180313_models.CreateCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.CreateCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_connect_network_with_options(request, runtime)

    async def create_cloud_connect_network_async(
        self,
        request: smartag_20180313_models.CreateCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.CreateCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_connect_network_with_options_async(request, runtime)

    def create_enterprise_code_with_options(
        self,
        request: smartag_20180313_models.CreateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateEnterpriseCodeResponse().from_map(
            self.do_rpcrequest('CreateEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.CreateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateEnterpriseCodeResponse().from_map(
            await self.do_rpcrequest_async('CreateEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_enterprise_code(
        self,
        request: smartag_20180313_models.CreateEnterpriseCodeRequest,
    ) -> smartag_20180313_models.CreateEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_enterprise_code_with_options(request, runtime)

    async def create_enterprise_code_async(
        self,
        request: smartag_20180313_models.CreateEnterpriseCodeRequest,
    ) -> smartag_20180313_models.CreateEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_enterprise_code_with_options_async(request, runtime)

    def create_flow_log_with_options(
        self,
        request: smartag_20180313_models.CreateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateFlowLogResponse().from_map(
            self.do_rpcrequest('CreateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.CreateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateFlowLogResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_log(
        self,
        request: smartag_20180313_models.CreateFlowLogRequest,
    ) -> smartag_20180313_models.CreateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_log_with_options(request, runtime)

    async def create_flow_log_async(
        self,
        request: smartag_20180313_models.CreateFlowLogRequest,
    ) -> smartag_20180313_models.CreateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_log_with_options_async(request, runtime)

    def create_health_check_with_options(
        self,
        request: smartag_20180313_models.CreateHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateHealthCheckResponse().from_map(
            self.do_rpcrequest('CreateHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_health_check_with_options_async(
        self,
        request: smartag_20180313_models.CreateHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateHealthCheckResponse().from_map(
            await self.do_rpcrequest_async('CreateHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_health_check(
        self,
        request: smartag_20180313_models.CreateHealthCheckRequest,
    ) -> smartag_20180313_models.CreateHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_health_check_with_options(request, runtime)

    async def create_health_check_async(
        self,
        request: smartag_20180313_models.CreateHealthCheckRequest,
    ) -> smartag_20180313_models.CreateHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_health_check_with_options_async(request, runtime)

    def create_network_optimization_with_options(
        self,
        request: smartag_20180313_models.CreateNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateNetworkOptimizationResponse().from_map(
            self.do_rpcrequest('CreateNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_optimization_with_options_async(
        self,
        request: smartag_20180313_models.CreateNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateNetworkOptimizationResponse().from_map(
            await self.do_rpcrequest_async('CreateNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_optimization(
        self,
        request: smartag_20180313_models.CreateNetworkOptimizationRequest,
    ) -> smartag_20180313_models.CreateNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_optimization_with_options(request, runtime)

    async def create_network_optimization_async(
        self,
        request: smartag_20180313_models.CreateNetworkOptimizationRequest,
    ) -> smartag_20180313_models.CreateNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_optimization_with_options_async(request, runtime)

    def create_qos_with_options(
        self,
        request: smartag_20180313_models.CreateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosResponse().from_map(
            self.do_rpcrequest('CreateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_qos_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosResponse().from_map(
            await self.do_rpcrequest_async('CreateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_qos(
        self,
        request: smartag_20180313_models.CreateQosRequest,
    ) -> smartag_20180313_models.CreateQosResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_qos_with_options(request, runtime)

    async def create_qos_async(
        self,
        request: smartag_20180313_models.CreateQosRequest,
    ) -> smartag_20180313_models.CreateQosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_qos_with_options_async(request, runtime)

    def create_qos_car_with_options(
        self,
        request: smartag_20180313_models.CreateQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosCarResponse().from_map(
            self.do_rpcrequest('CreateQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosCarResponse().from_map(
            await self.do_rpcrequest_async('CreateQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_qos_car(
        self,
        request: smartag_20180313_models.CreateQosCarRequest,
    ) -> smartag_20180313_models.CreateQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_qos_car_with_options(request, runtime)

    async def create_qos_car_async(
        self,
        request: smartag_20180313_models.CreateQosCarRequest,
    ) -> smartag_20180313_models.CreateQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_qos_car_with_options_async(request, runtime)

    def create_qos_policy_with_options(
        self,
        request: smartag_20180313_models.CreateQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosPolicyResponse().from_map(
            self.do_rpcrequest('CreateQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateQosPolicyResponse().from_map(
            await self.do_rpcrequest_async('CreateQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_qos_policy(
        self,
        request: smartag_20180313_models.CreateQosPolicyRequest,
    ) -> smartag_20180313_models.CreateQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_qos_policy_with_options(request, runtime)

    async def create_qos_policy_async(
        self,
        request: smartag_20180313_models.CreateQosPolicyRequest,
    ) -> smartag_20180313_models.CreateQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_qos_policy_with_options_async(request, runtime)

    def create_sag_express_connect_interface_with_options(
        self,
        request: smartag_20180313_models.CreateSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSagExpressConnectInterfaceResponse().from_map(
            self.do_rpcrequest('CreateSagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.CreateSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSagExpressConnectInterfaceResponse().from_map(
            await self.do_rpcrequest_async('CreateSagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sag_express_connect_interface(
        self,
        request: smartag_20180313_models.CreateSagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.CreateSagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sag_express_connect_interface_with_options(request, runtime)

    async def create_sag_express_connect_interface_async(
        self,
        request: smartag_20180313_models.CreateSagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.CreateSagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sag_express_connect_interface_with_options_async(request, runtime)

    def create_sag_static_route_with_options(
        self,
        request: smartag_20180313_models.CreateSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSagStaticRouteResponse().from_map(
            self.do_rpcrequest('CreateSagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.CreateSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSagStaticRouteResponse().from_map(
            await self.do_rpcrequest_async('CreateSagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sag_static_route(
        self,
        request: smartag_20180313_models.CreateSagStaticRouteRequest,
    ) -> smartag_20180313_models.CreateSagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sag_static_route_with_options(request, runtime)

    async def create_sag_static_route_async(
        self,
        request: smartag_20180313_models.CreateSagStaticRouteRequest,
    ) -> smartag_20180313_models.CreateSagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sag_static_route_with_options_async(request, runtime)

    def create_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('CreateSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_smart_access_gateway(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_smart_access_gateway_with_options(request, runtime)

    async def create_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_access_gateway_with_options_async(request, runtime)

    def create_smart_access_gateway_client_user_with_options(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse().from_map(
            self.do_rpcrequest('CreateSmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse().from_map(
            await self.do_rpcrequest_async('CreateSmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_smart_access_gateway_client_user(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_smart_access_gateway_client_user_with_options(request, runtime)

    async def create_smart_access_gateway_client_user_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_access_gateway_client_user_with_options_async(request, runtime)

    def create_smart_access_gateway_software_with_options(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse().from_map(
            self.do_rpcrequest('CreateSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse().from_map(
            await self.do_rpcrequest_async('CreateSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_smart_access_gateway_software(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_smart_access_gateway_software_with_options(request, runtime)

    async def create_smart_access_gateway_software_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_access_gateway_software_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: smartag_20180313_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeactiveFlowLogResponse().from_map(
            self.do_rpcrequest('DeactiveFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeactiveFlowLogResponse().from_map(
            await self.do_rpcrequest_async('DeactiveFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactive_flow_log(
        self,
        request: smartag_20180313_models.DeactiveFlowLogRequest,
    ) -> smartag_20180313_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: smartag_20180313_models.DeactiveFlowLogRequest,
    ) -> smartag_20180313_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_aclwith_options(
        self,
        request: smartag_20180313_models.DeleteACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteACLResponse().from_map(
            self.do_rpcrequest('DeleteACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aclwith_options_async(
        self,
        request: smartag_20180313_models.DeleteACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteACLResponse().from_map(
            await self.do_rpcrequest_async('DeleteACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl(
        self,
        request: smartag_20180313_models.DeleteACLRequest,
    ) -> smartag_20180313_models.DeleteACLResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aclwith_options(request, runtime)

    async def delete_acl_async(
        self,
        request: smartag_20180313_models.DeleteACLRequest,
    ) -> smartag_20180313_models.DeleteACLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aclwith_options_async(request, runtime)

    def delete_aclrule_with_options(
        self,
        request: smartag_20180313_models.DeleteACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteACLRuleResponse().from_map(
            self.do_rpcrequest('DeleteACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.DeleteACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteACLRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aclrule(
        self,
        request: smartag_20180313_models.DeleteACLRuleRequest,
    ) -> smartag_20180313_models.DeleteACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aclrule_with_options(request, runtime)

    async def delete_aclrule_async(
        self,
        request: smartag_20180313_models.DeleteACLRuleRequest,
    ) -> smartag_20180313_models.DeleteACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aclrule_with_options_async(request, runtime)

    def delete_cloud_connect_network_with_options(
        self,
        request: smartag_20180313_models.DeleteCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteCloudConnectNetworkResponse().from_map(
            self.do_rpcrequest('DeleteCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.DeleteCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteCloudConnectNetworkResponse().from_map(
            await self.do_rpcrequest_async('DeleteCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cloud_connect_network(
        self,
        request: smartag_20180313_models.DeleteCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.DeleteCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_connect_network_with_options(request, runtime)

    async def delete_cloud_connect_network_async(
        self,
        request: smartag_20180313_models.DeleteCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.DeleteCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_connect_network_with_options_async(request, runtime)

    def delete_dnat_entry_with_options(
        self,
        request: smartag_20180313_models.DeleteDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteDnatEntryResponse().from_map(
            self.do_rpcrequest('DeleteDnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dnat_entry_with_options_async(
        self,
        request: smartag_20180313_models.DeleteDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteDnatEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteDnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dnat_entry(
        self,
        request: smartag_20180313_models.DeleteDnatEntryRequest,
    ) -> smartag_20180313_models.DeleteDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dnat_entry_with_options(request, runtime)

    async def delete_dnat_entry_async(
        self,
        request: smartag_20180313_models.DeleteDnatEntryRequest,
    ) -> smartag_20180313_models.DeleteDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dnat_entry_with_options_async(request, runtime)

    def delete_enterprise_code_with_options(
        self,
        request: smartag_20180313_models.DeleteEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteEnterpriseCodeResponse().from_map(
            self.do_rpcrequest('DeleteEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.DeleteEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteEnterpriseCodeResponse().from_map(
            await self.do_rpcrequest_async('DeleteEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_enterprise_code(
        self,
        request: smartag_20180313_models.DeleteEnterpriseCodeRequest,
    ) -> smartag_20180313_models.DeleteEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_code_with_options(request, runtime)

    async def delete_enterprise_code_async(
        self,
        request: smartag_20180313_models.DeleteEnterpriseCodeRequest,
    ) -> smartag_20180313_models.DeleteEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_enterprise_code_with_options_async(request, runtime)

    def delete_flow_log_with_options(
        self,
        request: smartag_20180313_models.DeleteFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteFlowLogResponse().from_map(
            self.do_rpcrequest('DeleteFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DeleteFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteFlowLogResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_log(
        self,
        request: smartag_20180313_models.DeleteFlowLogRequest,
    ) -> smartag_20180313_models.DeleteFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_log_with_options(request, runtime)

    async def delete_flow_log_async(
        self,
        request: smartag_20180313_models.DeleteFlowLogRequest,
    ) -> smartag_20180313_models.DeleteFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_log_with_options_async(request, runtime)

    def delete_health_check_with_options(
        self,
        request: smartag_20180313_models.DeleteHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteHealthCheckResponse().from_map(
            self.do_rpcrequest('DeleteHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_health_check_with_options_async(
        self,
        request: smartag_20180313_models.DeleteHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteHealthCheckResponse().from_map(
            await self.do_rpcrequest_async('DeleteHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_health_check(
        self,
        request: smartag_20180313_models.DeleteHealthCheckRequest,
    ) -> smartag_20180313_models.DeleteHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_health_check_with_options(request, runtime)

    async def delete_health_check_async(
        self,
        request: smartag_20180313_models.DeleteHealthCheckRequest,
    ) -> smartag_20180313_models.DeleteHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_health_check_with_options_async(request, runtime)

    def delete_network_optimization_with_options(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteNetworkOptimizationResponse().from_map(
            self.do_rpcrequest('DeleteNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_optimization_with_options_async(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteNetworkOptimizationResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_optimization(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationRequest,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_optimization_with_options(request, runtime)

    async def delete_network_optimization_async(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationRequest,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_optimization_with_options_async(request, runtime)

    def delete_network_optimization_setting_with_options(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteNetworkOptimizationSettingResponse().from_map(
            self.do_rpcrequest('DeleteNetworkOptimizationSetting', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_optimization_setting_with_options_async(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteNetworkOptimizationSettingResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkOptimizationSetting', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_optimization_setting(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationSettingRequest,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_optimization_setting_with_options(request, runtime)

    async def delete_network_optimization_setting_async(
        self,
        request: smartag_20180313_models.DeleteNetworkOptimizationSettingRequest,
    ) -> smartag_20180313_models.DeleteNetworkOptimizationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_optimization_setting_with_options_async(request, runtime)

    def delete_qos_with_options(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosResponse().from_map(
            self.do_rpcrequest('DeleteQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_qos_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosResponse().from_map(
            await self.do_rpcrequest_async('DeleteQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_qos(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
    ) -> smartag_20180313_models.DeleteQosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_qos_with_options(request, runtime)

    async def delete_qos_async(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
    ) -> smartag_20180313_models.DeleteQosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_qos_with_options_async(request, runtime)

    def delete_qos_car_with_options(
        self,
        request: smartag_20180313_models.DeleteQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosCarResponse().from_map(
            self.do_rpcrequest('DeleteQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosCarResponse().from_map(
            await self.do_rpcrequest_async('DeleteQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_qos_car(
        self,
        request: smartag_20180313_models.DeleteQosCarRequest,
    ) -> smartag_20180313_models.DeleteQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_qos_car_with_options(request, runtime)

    async def delete_qos_car_async(
        self,
        request: smartag_20180313_models.DeleteQosCarRequest,
    ) -> smartag_20180313_models.DeleteQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_qos_car_with_options_async(request, runtime)

    def delete_qos_policy_with_options(
        self,
        request: smartag_20180313_models.DeleteQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosPolicyResponse().from_map(
            self.do_rpcrequest('DeleteQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteQosPolicyResponse().from_map(
            await self.do_rpcrequest_async('DeleteQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_qos_policy(
        self,
        request: smartag_20180313_models.DeleteQosPolicyRequest,
    ) -> smartag_20180313_models.DeleteQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_qos_policy_with_options(request, runtime)

    async def delete_qos_policy_async(
        self,
        request: smartag_20180313_models.DeleteQosPolicyRequest,
    ) -> smartag_20180313_models.DeleteQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_qos_policy_with_options_async(request, runtime)

    def delete_route_distribution_strategy_with_options(
        self,
        request: smartag_20180313_models.DeleteRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteRouteDistributionStrategyResponse().from_map(
            self.do_rpcrequest('DeleteRouteDistributionStrategy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_route_distribution_strategy_with_options_async(
        self,
        request: smartag_20180313_models.DeleteRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteRouteDistributionStrategyResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouteDistributionStrategy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_distribution_strategy(
        self,
        request: smartag_20180313_models.DeleteRouteDistributionStrategyRequest,
    ) -> smartag_20180313_models.DeleteRouteDistributionStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_distribution_strategy_with_options(request, runtime)

    async def delete_route_distribution_strategy_async(
        self,
        request: smartag_20180313_models.DeleteRouteDistributionStrategyRequest,
    ) -> smartag_20180313_models.DeleteRouteDistributionStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_distribution_strategy_with_options_async(request, runtime)

    def delete_sag_cidr_with_options(
        self,
        request: smartag_20180313_models.DeleteSagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagCidrResponse().from_map(
            self.do_rpcrequest('DeleteSagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sag_cidr_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagCidrResponse().from_map(
            await self.do_rpcrequest_async('DeleteSagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sag_cidr(
        self,
        request: smartag_20180313_models.DeleteSagCidrRequest,
    ) -> smartag_20180313_models.DeleteSagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sag_cidr_with_options(request, runtime)

    async def delete_sag_cidr_async(
        self,
        request: smartag_20180313_models.DeleteSagCidrRequest,
    ) -> smartag_20180313_models.DeleteSagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sag_cidr_with_options_async(request, runtime)

    def delete_sag_express_connect_interface_with_options(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse().from_map(
            self.do_rpcrequest('DeleteSagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteSagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sag_express_connect_interface(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sag_express_connect_interface_with_options(request, runtime)

    async def delete_sag_express_connect_interface_async(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sag_express_connect_interface_with_options_async(request, runtime)

    def delete_sag_static_route_with_options(
        self,
        request: smartag_20180313_models.DeleteSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagStaticRouteResponse().from_map(
            self.do_rpcrequest('DeleteSagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSagStaticRouteResponse().from_map(
            await self.do_rpcrequest_async('DeleteSagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sag_static_route(
        self,
        request: smartag_20180313_models.DeleteSagStaticRouteRequest,
    ) -> smartag_20180313_models.DeleteSagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sag_static_route_with_options(request, runtime)

    async def delete_sag_static_route_async(
        self,
        request: smartag_20180313_models.DeleteSagStaticRouteRequest,
    ) -> smartag_20180313_models.DeleteSagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sag_static_route_with_options_async(request, runtime)

    def delete_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('DeleteSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_smart_access_gateway(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_access_gateway_with_options(request, runtime)

    async def delete_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smart_access_gateway_with_options_async(request, runtime)

    def delete_smart_access_gateway_client_user_with_options(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse().from_map(
            self.do_rpcrequest('DeleteSmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteSmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_smart_access_gateway_client_user(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_access_gateway_client_user_with_options(request, runtime)

    async def delete_smart_access_gateway_client_user_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smart_access_gateway_client_user_with_options_async(request, runtime)

    def delete_snat_entry_with_options(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSnatEntryResponse().from_map(
            self.do_rpcrequest('DeleteSnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snat_entry_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DeleteSnatEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteSnatEntry', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snat_entry(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snat_entry_with_options(request, runtime)

    async def delete_snat_entry_async(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snat_entry_with_options_async(request, runtime)

    def describe_aclattribute_with_options(
        self,
        request: smartag_20180313_models.DescribeACLAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeACLAttributeResponse().from_map(
            self.do_rpcrequest('DescribeACLAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_aclattribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeACLAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeACLAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeACLAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_aclattribute(
        self,
        request: smartag_20180313_models.DescribeACLAttributeRequest,
    ) -> smartag_20180313_models.DescribeACLAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_aclattribute_with_options(request, runtime)

    async def describe_aclattribute_async(
        self,
        request: smartag_20180313_models.DescribeACLAttributeRequest,
    ) -> smartag_20180313_models.DescribeACLAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_aclattribute_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: smartag_20180313_models.DescribeACLsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeACLsResponse().from_map(
            self.do_rpcrequest('DescribeACLs', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: smartag_20180313_models.DescribeACLsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeACLsResponse().from_map(
            await self.do_rpcrequest_async('DescribeACLs', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acls(
        self,
        request: smartag_20180313_models.DescribeACLsRequest,
    ) -> smartag_20180313_models.DescribeACLsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: smartag_20180313_models.DescribeACLsRequest,
    ) -> smartag_20180313_models.DescribeACLsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_bindable_smart_access_gateways_with_options(
        self,
        request: smartag_20180313_models.DescribeBindableSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeBindableSmartAccessGateways', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bindable_smart_access_gateways_with_options_async(
        self,
        request: smartag_20180313_models.DescribeBindableSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeBindableSmartAccessGateways', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bindable_smart_access_gateways(
        self,
        request: smartag_20180313_models.DescribeBindableSmartAccessGatewaysRequest,
    ) -> smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bindable_smart_access_gateways_with_options(request, runtime)

    async def describe_bindable_smart_access_gateways_async(
        self,
        request: smartag_20180313_models.DescribeBindableSmartAccessGatewaysRequest,
    ) -> smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bindable_smart_access_gateways_with_options_async(request, runtime)

    def describe_client_user_dnswith_options(
        self,
        request: smartag_20180313_models.DescribeClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeClientUserDNSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeClientUserDNSResponse().from_map(
            self.do_rpcrequest('DescribeClientUserDNS', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_client_user_dnswith_options_async(
        self,
        request: smartag_20180313_models.DescribeClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeClientUserDNSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeClientUserDNSResponse().from_map(
            await self.do_rpcrequest_async('DescribeClientUserDNS', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_client_user_dns(
        self,
        request: smartag_20180313_models.DescribeClientUserDNSRequest,
    ) -> smartag_20180313_models.DescribeClientUserDNSResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_user_dnswith_options(request, runtime)

    async def describe_client_user_dns_async(
        self,
        request: smartag_20180313_models.DescribeClientUserDNSRequest,
    ) -> smartag_20180313_models.DescribeClientUserDNSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_user_dnswith_options_async(request, runtime)

    def describe_cloud_connect_networks_with_options(
        self,
        request: smartag_20180313_models.DescribeCloudConnectNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeCloudConnectNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeCloudConnectNetworksResponse().from_map(
            self.do_rpcrequest('DescribeCloudConnectNetworks', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_connect_networks_with_options_async(
        self,
        request: smartag_20180313_models.DescribeCloudConnectNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeCloudConnectNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeCloudConnectNetworksResponse().from_map(
            await self.do_rpcrequest_async('DescribeCloudConnectNetworks', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_connect_networks(
        self,
        request: smartag_20180313_models.DescribeCloudConnectNetworksRequest,
    ) -> smartag_20180313_models.DescribeCloudConnectNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_connect_networks_with_options(request, runtime)

    async def describe_cloud_connect_networks_async(
        self,
        request: smartag_20180313_models.DescribeCloudConnectNetworksRequest,
    ) -> smartag_20180313_models.DescribeCloudConnectNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_connect_networks_with_options_async(request, runtime)

    def describe_device_auto_upgrade_policy_with_options(
        self,
        request: smartag_20180313_models.DescribeDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse().from_map(
            self.do_rpcrequest('DescribeDeviceAutoUpgradePolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_auto_upgrade_policy_with_options_async(
        self,
        request: smartag_20180313_models.DescribeDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceAutoUpgradePolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_auto_upgrade_policy(
        self,
        request: smartag_20180313_models.DescribeDeviceAutoUpgradePolicyRequest,
    ) -> smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_auto_upgrade_policy_with_options(request, runtime)

    async def describe_device_auto_upgrade_policy_async(
        self,
        request: smartag_20180313_models.DescribeDeviceAutoUpgradePolicyRequest,
    ) -> smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_auto_upgrade_policy_with_options_async(request, runtime)

    def describe_dnat_entries_with_options(
        self,
        request: smartag_20180313_models.DescribeDnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeDnatEntriesResponse().from_map(
            self.do_rpcrequest('DescribeDnatEntries', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dnat_entries_with_options_async(
        self,
        request: smartag_20180313_models.DescribeDnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeDnatEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnatEntries', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dnat_entries(
        self,
        request: smartag_20180313_models.DescribeDnatEntriesRequest,
    ) -> smartag_20180313_models.DescribeDnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dnat_entries_with_options(request, runtime)

    async def describe_dnat_entries_async(
        self,
        request: smartag_20180313_models.DescribeDnatEntriesRequest,
    ) -> smartag_20180313_models.DescribeDnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dnat_entries_with_options_async(request, runtime)

    def describe_flow_logs_with_options(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeFlowLogsResponse().from_map(
            self.do_rpcrequest('DescribeFlowLogs', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_logs_with_options_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeFlowLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowLogs', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_logs(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_logs_with_options(request, runtime)

    async def describe_flow_logs_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_logs_with_options_async(request, runtime)

    def describe_flow_log_sags_with_options(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeFlowLogSagsResponse().from_map(
            self.do_rpcrequest('DescribeFlowLogSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_log_sags_with_options_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeFlowLogSagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowLogSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_log_sags(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_log_sags_with_options(request, runtime)

    async def describe_flow_log_sags_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_log_sags_with_options_async(request, runtime)

    def describe_grant_rules_with_options(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantRulesResponse().from_map(
            self.do_rpcrequest('DescribeGrantRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grant_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGrantRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grant_rules(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_with_options(request, runtime)

    async def describe_grant_rules_async(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_rules_with_options_async(request, runtime)

    def describe_grant_sag_rules_with_options(
        self,
        request: smartag_20180313_models.DescribeGrantSagRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantSagRulesResponse().from_map(
            self.do_rpcrequest('DescribeGrantSagRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grant_sag_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantSagRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGrantSagRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grant_sag_rules(
        self,
        request: smartag_20180313_models.DescribeGrantSagRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantSagRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_sag_rules_with_options(request, runtime)

    async def describe_grant_sag_rules_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantSagRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_sag_rules_with_options_async(request, runtime)

    def describe_grant_sag_vbr_rules_with_options(
        self,
        request: smartag_20180313_models.DescribeGrantSagVbrRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagVbrRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantSagVbrRulesResponse().from_map(
            self.do_rpcrequest('DescribeGrantSagVbrRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grant_sag_vbr_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagVbrRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagVbrRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeGrantSagVbrRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGrantSagVbrRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grant_sag_vbr_rules(
        self,
        request: smartag_20180313_models.DescribeGrantSagVbrRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantSagVbrRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_sag_vbr_rules_with_options(request, runtime)

    async def describe_grant_sag_vbr_rules_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagVbrRulesRequest,
    ) -> smartag_20180313_models.DescribeGrantSagVbrRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_sag_vbr_rules_with_options_async(request, runtime)

    def describe_health_check_attribute_with_options(
        self,
        request: smartag_20180313_models.DescribeHealthCheckAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthCheckAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeHealthCheckAttributeResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_attribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeHealthCheckAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthCheckAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeHealthCheckAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_attribute(
        self,
        request: smartag_20180313_models.DescribeHealthCheckAttributeRequest,
    ) -> smartag_20180313_models.DescribeHealthCheckAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_attribute_with_options(request, runtime)

    async def describe_health_check_attribute_async(
        self,
        request: smartag_20180313_models.DescribeHealthCheckAttributeRequest,
    ) -> smartag_20180313_models.DescribeHealthCheckAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_attribute_with_options_async(request, runtime)

    def describe_health_checks_with_options(
        self,
        request: smartag_20180313_models.DescribeHealthChecksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthChecksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeHealthChecksResponse().from_map(
            self.do_rpcrequest('DescribeHealthChecks', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_checks_with_options_async(
        self,
        request: smartag_20180313_models.DescribeHealthChecksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthChecksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeHealthChecksResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthChecks', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_checks(
        self,
        request: smartag_20180313_models.DescribeHealthChecksRequest,
    ) -> smartag_20180313_models.DescribeHealthChecksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_checks_with_options(request, runtime)

    async def describe_health_checks_async(
        self,
        request: smartag_20180313_models.DescribeHealthChecksRequest,
    ) -> smartag_20180313_models.DescribeHealthChecksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_checks_with_options_async(request, runtime)

    def describe_network_optimizations_with_options(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationsResponse().from_map(
            self.do_rpcrequest('DescribeNetworkOptimizations', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_optimizations_with_options_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkOptimizations', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_optimizations(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_optimizations_with_options(request, runtime)

    async def describe_network_optimizations_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_optimizations_with_options_async(request, runtime)

    def describe_network_optimization_sags_with_options(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationSagsResponse().from_map(
            self.do_rpcrequest('DescribeNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_optimization_sags_with_options_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationSagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_optimization_sags(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_optimization_sags_with_options(request, runtime)

    async def describe_network_optimization_sags_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_optimization_sags_with_options_async(request, runtime)

    def describe_network_optimization_settings_with_options(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse().from_map(
            self.do_rpcrequest('DescribeNetworkOptimizationSettings', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_optimization_settings_with_options_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkOptimizationSettings', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_optimization_settings(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSettingsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_optimization_settings_with_options(request, runtime)

    async def describe_network_optimization_settings_async(
        self,
        request: smartag_20180313_models.DescribeNetworkOptimizationSettingsRequest,
    ) -> smartag_20180313_models.DescribeNetworkOptimizationSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_optimization_settings_with_options_async(request, runtime)

    def describe_pbr_interfaces_with_options(
        self,
        request: smartag_20180313_models.DescribePbrInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePbrInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePbrInterfacesResponse().from_map(
            self.do_rpcrequest('DescribePbrInterfaces', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pbr_interfaces_with_options_async(
        self,
        request: smartag_20180313_models.DescribePbrInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePbrInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePbrInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribePbrInterfaces', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pbr_interfaces(
        self,
        request: smartag_20180313_models.DescribePbrInterfacesRequest,
    ) -> smartag_20180313_models.DescribePbrInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pbr_interfaces_with_options(request, runtime)

    async def describe_pbr_interfaces_async(
        self,
        request: smartag_20180313_models.DescribePbrInterfacesRequest,
    ) -> smartag_20180313_models.DescribePbrInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pbr_interfaces_with_options_async(request, runtime)

    def describe_pbr_rules_with_options(
        self,
        request: smartag_20180313_models.DescribePbrRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePbrRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePbrRulesResponse().from_map(
            self.do_rpcrequest('DescribePbrRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pbr_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribePbrRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePbrRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePbrRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribePbrRules', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pbr_rules(
        self,
        request: smartag_20180313_models.DescribePbrRulesRequest,
    ) -> smartag_20180313_models.DescribePbrRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pbr_rules_with_options(request, runtime)

    async def describe_pbr_rules_async(
        self,
        request: smartag_20180313_models.DescribePbrRulesRequest,
    ) -> smartag_20180313_models.DescribePbrRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pbr_rules_with_options_async(request, runtime)

    def describe_policy_based_routings_with_options(
        self,
        request: smartag_20180313_models.DescribePolicyBasedRoutingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePolicyBasedRoutingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePolicyBasedRoutingsResponse().from_map(
            self.do_rpcrequest('DescribePolicyBasedRoutings', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_policy_based_routings_with_options_async(
        self,
        request: smartag_20180313_models.DescribePolicyBasedRoutingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribePolicyBasedRoutingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribePolicyBasedRoutingsResponse().from_map(
            await self.do_rpcrequest_async('DescribePolicyBasedRoutings', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_based_routings(
        self,
        request: smartag_20180313_models.DescribePolicyBasedRoutingsRequest,
    ) -> smartag_20180313_models.DescribePolicyBasedRoutingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_based_routings_with_options(request, runtime)

    async def describe_policy_based_routings_async(
        self,
        request: smartag_20180313_models.DescribePolicyBasedRoutingsRequest,
    ) -> smartag_20180313_models.DescribePolicyBasedRoutingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_based_routings_with_options_async(request, runtime)

    def describe_qos_cars_with_options(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosCarsResponse().from_map(
            self.do_rpcrequest('DescribeQosCars', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_qos_cars_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosCarsResponse().from_map(
            await self.do_rpcrequest_async('DescribeQosCars', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_qos_cars(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qos_cars_with_options(request, runtime)

    async def describe_qos_cars_async(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qos_cars_with_options_async(request, runtime)

    def describe_qoses_with_options(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosesResponse().from_map(
            self.do_rpcrequest('DescribeQoses', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_qoses_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosesResponse().from_map(
            await self.do_rpcrequest_async('DescribeQoses', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_qoses(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qoses_with_options(request, runtime)

    async def describe_qoses_async(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qoses_with_options_async(request, runtime)

    def describe_qos_policies_with_options(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosPoliciesResponse().from_map(
            self.do_rpcrequest('DescribeQosPolicies', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_qos_policies_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeQosPoliciesResponse().from_map(
            await self.do_rpcrequest_async('DescribeQosPolicies', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_qos_policies(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qos_policies_with_options(request, runtime)

    async def describe_qos_policies_async(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qos_policies_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_route_distribution_strategies_with_options(
        self,
        request: smartag_20180313_models.DescribeRouteDistributionStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRouteDistributionStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeRouteDistributionStrategiesResponse().from_map(
            self.do_rpcrequest('DescribeRouteDistributionStrategies', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_distribution_strategies_with_options_async(
        self,
        request: smartag_20180313_models.DescribeRouteDistributionStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRouteDistributionStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeRouteDistributionStrategiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouteDistributionStrategies', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_distribution_strategies(
        self,
        request: smartag_20180313_models.DescribeRouteDistributionStrategiesRequest,
    ) -> smartag_20180313_models.DescribeRouteDistributionStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_distribution_strategies_with_options(request, runtime)

    async def describe_route_distribution_strategies_async(
        self,
        request: smartag_20180313_models.DescribeRouteDistributionStrategiesRequest,
    ) -> smartag_20180313_models.DescribeRouteDistributionStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_distribution_strategies_with_options_async(request, runtime)

    def describe_sag_current_dns_with_options(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagCurrentDnsResponse().from_map(
            self.do_rpcrequest('DescribeSagCurrentDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_current_dns_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagCurrentDnsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagCurrentDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_current_dns(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_current_dns_with_options(request, runtime)

    async def describe_sag_current_dns_async(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_current_dns_with_options_async(request, runtime)

    def describe_sagdevice_info_with_options(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSAGDeviceInfoResponse().from_map(
            self.do_rpcrequest('DescribeSAGDeviceInfo', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sagdevice_info_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSAGDeviceInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeSAGDeviceInfo', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sagdevice_info(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sagdevice_info_with_options(request, runtime)

    async def describe_sagdevice_info_async(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sagdevice_info_with_options_async(request, runtime)

    def describe_sag_drop_top_nwith_options(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagDropTopNResponse().from_map(
            self.do_rpcrequest('DescribeSagDropTopN', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_drop_top_nwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagDropTopNResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagDropTopN', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_drop_top_n(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_drop_top_nwith_options(request, runtime)

    async def describe_sag_drop_top_n_async(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_drop_top_nwith_options_async(request, runtime)

    def describe_sag_ecroute_backup_attribute_with_options(
        self,
        request: smartag_20180313_models.DescribeSagECRouteBackupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeSagECRouteBackupAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_ecroute_backup_attribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagECRouteBackupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagECRouteBackupAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_ecroute_backup_attribute(
        self,
        request: smartag_20180313_models.DescribeSagECRouteBackupAttributeRequest,
    ) -> smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_ecroute_backup_attribute_with_options(request, runtime)

    async def describe_sag_ecroute_backup_attribute_async(
        self,
        request: smartag_20180313_models.DescribeSagECRouteBackupAttributeRequest,
    ) -> smartag_20180313_models.DescribeSagECRouteBackupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_ecroute_backup_attribute_with_options_async(request, runtime)

    def describe_sag_express_connect_interface_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse().from_map(
            self.do_rpcrequest('DescribeSagExpressConnectInterfaceList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_express_connect_interface_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagExpressConnectInterfaceList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_express_connect_interface_list(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_express_connect_interface_list_with_options(request, runtime)

    async def describe_sag_express_connect_interface_list_async(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_express_connect_interface_list_with_options_async(request, runtime)

    def describe_sag_global_route_protocol_with_options(
        self,
        request: smartag_20180313_models.DescribeSagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse().from_map(
            self.do_rpcrequest('DescribeSagGlobalRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagGlobalRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_global_route_protocol(
        self,
        request: smartag_20180313_models.DescribeSagGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_global_route_protocol_with_options(request, runtime)

    async def describe_sag_global_route_protocol_async(
        self,
        request: smartag_20180313_models.DescribeSagGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_global_route_protocol_with_options_async(request, runtime)

    def describe_sag_ha_with_options(
        self,
        request: smartag_20180313_models.DescribeSagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagHaResponse().from_map(
            self.do_rpcrequest('DescribeSagHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_ha_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagHaResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_ha(
        self,
        request: smartag_20180313_models.DescribeSagHaRequest,
    ) -> smartag_20180313_models.DescribeSagHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_ha_with_options(request, runtime)

    async def describe_sag_ha_async(
        self,
        request: smartag_20180313_models.DescribeSagHaRequest,
    ) -> smartag_20180313_models.DescribeSagHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_ha_with_options_async(request, runtime)

    def describe_sag_lan_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagLanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagLanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagLanListResponse().from_map(
            self.do_rpcrequest('DescribeSagLanList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_lan_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagLanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagLanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagLanListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagLanList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_lan_list(
        self,
        request: smartag_20180313_models.DescribeSagLanListRequest,
    ) -> smartag_20180313_models.DescribeSagLanListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_lan_list_with_options(request, runtime)

    async def describe_sag_lan_list_async(
        self,
        request: smartag_20180313_models.DescribeSagLanListRequest,
    ) -> smartag_20180313_models.DescribeSagLanListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_lan_list_with_options_async(request, runtime)

    def describe_sag_management_port_with_options(
        self,
        request: smartag_20180313_models.DescribeSagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagManagementPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagManagementPortResponse().from_map(
            self.do_rpcrequest('DescribeSagManagementPort', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_management_port_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagManagementPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagManagementPortResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagManagementPort', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_management_port(
        self,
        request: smartag_20180313_models.DescribeSagManagementPortRequest,
    ) -> smartag_20180313_models.DescribeSagManagementPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_management_port_with_options(request, runtime)

    async def describe_sag_management_port_async(
        self,
        request: smartag_20180313_models.DescribeSagManagementPortRequest,
    ) -> smartag_20180313_models.DescribeSagManagementPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_management_port_with_options_async(request, runtime)

    def describe_sag_online_client_statistics_with_options(
        self,
        request: smartag_20180313_models.DescribeSagOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeSagOnlineClientStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_online_client_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagOnlineClientStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_online_client_statistics(
        self,
        request: smartag_20180313_models.DescribeSagOnlineClientStatisticsRequest,
    ) -> smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_online_client_statistics_with_options(request, runtime)

    async def describe_sag_online_client_statistics_async(
        self,
        request: smartag_20180313_models.DescribeSagOnlineClientStatisticsRequest,
    ) -> smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_online_client_statistics_with_options_async(request, runtime)

    def describe_sag_port_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagPortListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagPortListResponse().from_map(
            self.do_rpcrequest('DescribeSagPortList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_port_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagPortListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagPortListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagPortList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_port_list(
        self,
        request: smartag_20180313_models.DescribeSagPortListRequest,
    ) -> smartag_20180313_models.DescribeSagPortListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_port_list_with_options(request, runtime)

    async def describe_sag_port_list_async(
        self,
        request: smartag_20180313_models.DescribeSagPortListRequest,
    ) -> smartag_20180313_models.DescribeSagPortListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_port_list_with_options_async(request, runtime)

    def describe_sag_port_route_protocol_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagPortRouteProtocolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortRouteProtocolListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagPortRouteProtocolListResponse().from_map(
            self.do_rpcrequest('DescribeSagPortRouteProtocolList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_port_route_protocol_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagPortRouteProtocolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortRouteProtocolListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagPortRouteProtocolListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagPortRouteProtocolList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_port_route_protocol_list(
        self,
        request: smartag_20180313_models.DescribeSagPortRouteProtocolListRequest,
    ) -> smartag_20180313_models.DescribeSagPortRouteProtocolListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_port_route_protocol_list_with_options(request, runtime)

    async def describe_sag_port_route_protocol_list_async(
        self,
        request: smartag_20180313_models.DescribeSagPortRouteProtocolListRequest,
    ) -> smartag_20180313_models.DescribeSagPortRouteProtocolListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_port_route_protocol_list_with_options_async(request, runtime)

    def describe_sag_remote_access_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRemoteAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRemoteAccessResponse().from_map(
            self.do_rpcrequest('DescribeSagRemoteAccess', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_remote_access_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRemoteAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRemoteAccessResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagRemoteAccess', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_remote_access(
        self,
        request: smartag_20180313_models.DescribeSagRemoteAccessRequest,
    ) -> smartag_20180313_models.DescribeSagRemoteAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_remote_access_with_options(request, runtime)

    async def describe_sag_remote_access_async(
        self,
        request: smartag_20180313_models.DescribeSagRemoteAccessRequest,
    ) -> smartag_20180313_models.DescribeSagRemoteAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_remote_access_with_options_async(request, runtime)

    def describe_sag_routeable_address_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteableAddressResponse().from_map(
            self.do_rpcrequest('DescribeSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_routeable_address_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteableAddressResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_routeable_address(
        self,
        request: smartag_20180313_models.DescribeSagRouteableAddressRequest,
    ) -> smartag_20180313_models.DescribeSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_routeable_address_with_options(request, runtime)

    async def describe_sag_routeable_address_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteableAddressRequest,
    ) -> smartag_20180313_models.DescribeSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_routeable_address_with_options_async(request, runtime)

    def describe_sag_route_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteListResponse().from_map(
            self.do_rpcrequest('DescribeSagRouteList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_route_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagRouteList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_route_list(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_route_list_with_options(request, runtime)

    async def describe_sag_route_list_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_route_list_with_options_async(request, runtime)

    def describe_sag_route_protocol_bgp_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteProtocolBgpResponse().from_map(
            self.do_rpcrequest('DescribeSagRouteProtocolBgp', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_route_protocol_bgp_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteProtocolBgpResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagRouteProtocolBgp', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_route_protocol_bgp(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolBgpRequest,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolBgpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_route_protocol_bgp_with_options(request, runtime)

    async def describe_sag_route_protocol_bgp_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolBgpRequest,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolBgpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_route_protocol_bgp_with_options_async(request, runtime)

    def describe_sag_route_protocol_ospf_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteProtocolOspfResponse().from_map(
            self.do_rpcrequest('DescribeSagRouteProtocolOspf', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_route_protocol_ospf_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagRouteProtocolOspfResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagRouteProtocolOspf', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_route_protocol_ospf(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolOspfRequest,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolOspfResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_route_protocol_ospf_with_options(request, runtime)

    async def describe_sag_route_protocol_ospf_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolOspfRequest,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolOspfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_route_protocol_ospf_with_options_async(request, runtime)

    def describe_sag_static_route_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagStaticRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagStaticRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagStaticRouteListResponse().from_map(
            self.do_rpcrequest('DescribeSagStaticRouteList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_static_route_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagStaticRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagStaticRouteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagStaticRouteListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagStaticRouteList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_static_route_list(
        self,
        request: smartag_20180313_models.DescribeSagStaticRouteListRequest,
    ) -> smartag_20180313_models.DescribeSagStaticRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_static_route_list_with_options(request, runtime)

    async def describe_sag_static_route_list_async(
        self,
        request: smartag_20180313_models.DescribeSagStaticRouteListRequest,
    ) -> smartag_20180313_models.DescribeSagStaticRouteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_static_route_list_with_options_async(request, runtime)

    def describe_sag_traffic_top_nwith_options(
        self,
        request: smartag_20180313_models.DescribeSagTrafficTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagTrafficTopNResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagTrafficTopNResponse().from_map(
            self.do_rpcrequest('DescribeSagTrafficTopN', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_traffic_top_nwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagTrafficTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagTrafficTopNResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagTrafficTopNResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagTrafficTopN', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_traffic_top_n(
        self,
        request: smartag_20180313_models.DescribeSagTrafficTopNRequest,
    ) -> smartag_20180313_models.DescribeSagTrafficTopNResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_traffic_top_nwith_options(request, runtime)

    async def describe_sag_traffic_top_n_async(
        self,
        request: smartag_20180313_models.DescribeSagTrafficTopNRequest,
    ) -> smartag_20180313_models.DescribeSagTrafficTopNResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_traffic_top_nwith_options_async(request, runtime)

    def describe_sag_user_dns_with_options(
        self,
        request: smartag_20180313_models.DescribeSagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagUserDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagUserDnsResponse().from_map(
            self.do_rpcrequest('DescribeSagUserDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_user_dns_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagUserDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagUserDnsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagUserDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_user_dns(
        self,
        request: smartag_20180313_models.DescribeSagUserDnsRequest,
    ) -> smartag_20180313_models.DescribeSagUserDnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_user_dns_with_options(request, runtime)

    async def describe_sag_user_dns_async(
        self,
        request: smartag_20180313_models.DescribeSagUserDnsRequest,
    ) -> smartag_20180313_models.DescribeSagUserDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_user_dns_with_options_async(request, runtime)

    def describe_sag_vbr_relations_with_options(
        self,
        request: smartag_20180313_models.DescribeSagVbrRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagVbrRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagVbrRelationsResponse().from_map(
            self.do_rpcrequest('DescribeSagVbrRelations', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_vbr_relations_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagVbrRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagVbrRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagVbrRelationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagVbrRelations', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_vbr_relations(
        self,
        request: smartag_20180313_models.DescribeSagVbrRelationsRequest,
    ) -> smartag_20180313_models.DescribeSagVbrRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_vbr_relations_with_options(request, runtime)

    async def describe_sag_vbr_relations_async(
        self,
        request: smartag_20180313_models.DescribeSagVbrRelationsRequest,
    ) -> smartag_20180313_models.DescribeSagVbrRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_vbr_relations_with_options_async(request, runtime)

    def describe_sag_wan_4gwith_options(
        self,
        request: smartag_20180313_models.DescribeSagWan4GRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWan4GResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWan4GResponse().from_map(
            self.do_rpcrequest('DescribeSagWan4G', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_wan_4gwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWan4GRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWan4GResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWan4GResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagWan4G', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_wan_4g(
        self,
        request: smartag_20180313_models.DescribeSagWan4GRequest,
    ) -> smartag_20180313_models.DescribeSagWan4GResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_wan_4gwith_options(request, runtime)

    async def describe_sag_wan_4g_async(
        self,
        request: smartag_20180313_models.DescribeSagWan4GRequest,
    ) -> smartag_20180313_models.DescribeSagWan4GResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_wan_4gwith_options_async(request, runtime)

    def describe_sag_wan_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagWanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWanListResponse().from_map(
            self.do_rpcrequest('DescribeSagWanList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_wan_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWanListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagWanList', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_wan_list(
        self,
        request: smartag_20180313_models.DescribeSagWanListRequest,
    ) -> smartag_20180313_models.DescribeSagWanListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_wan_list_with_options(request, runtime)

    async def describe_sag_wan_list_async(
        self,
        request: smartag_20180313_models.DescribeSagWanListRequest,
    ) -> smartag_20180313_models.DescribeSagWanListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_wan_list_with_options_async(request, runtime)

    def describe_sag_wan_snat_with_options(
        self,
        request: smartag_20180313_models.DescribeSagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanSnatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWanSnatResponse().from_map(
            self.do_rpcrequest('DescribeSagWanSnat', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanSnatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWanSnatResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagWanSnat', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_wan_snat(
        self,
        request: smartag_20180313_models.DescribeSagWanSnatRequest,
    ) -> smartag_20180313_models.DescribeSagWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_wan_snat_with_options(request, runtime)

    async def describe_sag_wan_snat_async(
        self,
        request: smartag_20180313_models.DescribeSagWanSnatRequest,
    ) -> smartag_20180313_models.DescribeSagWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_wan_snat_with_options_async(request, runtime)

    def describe_sag_wifi_with_options(
        self,
        request: smartag_20180313_models.DescribeSagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWifiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWifiResponse().from_map(
            self.do_rpcrequest('DescribeSagWifi', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sag_wifi_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWifiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSagWifiResponse().from_map(
            await self.do_rpcrequest_async('DescribeSagWifi', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sag_wifi(
        self,
        request: smartag_20180313_models.DescribeSagWifiRequest,
    ) -> smartag_20180313_models.DescribeSagWifiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sag_wifi_with_options(request, runtime)

    async def describe_sag_wifi_async(
        self,
        request: smartag_20180313_models.DescribeSagWifiRequest,
    ) -> smartag_20180313_models.DescribeSagWifiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sag_wifi_with_options_async(request, runtime)

    def describe_smart_access_gateway_attribute_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse().from_map(
            self.do_rpcrequest('DescribeSmartAccessGatewayAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_smart_access_gateway_attribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeSmartAccessGatewayAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_smart_access_gateway_attribute(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayAttributeRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_access_gateway_attribute_with_options(request, runtime)

    async def describe_smart_access_gateway_attribute_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayAttributeRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_access_gateway_attribute_with_options_async(request, runtime)

    def describe_smart_access_gateway_client_users_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse().from_map(
            self.do_rpcrequest('DescribeSmartAccessGatewayClientUsers', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_smart_access_gateway_client_users_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse().from_map(
            await self.do_rpcrequest_async('DescribeSmartAccessGatewayClientUsers', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_smart_access_gateway_client_users(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayClientUsersRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_access_gateway_client_users_with_options(request, runtime)

    async def describe_smart_access_gateway_client_users_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayClientUsersRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_access_gateway_client_users_with_options_async(request, runtime)

    def describe_smart_access_gateway_ha_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayHaResponse().from_map(
            self.do_rpcrequest('DescribeSmartAccessGatewayHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_smart_access_gateway_ha_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayHaResponse().from_map(
            await self.do_rpcrequest_async('DescribeSmartAccessGatewayHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_smart_access_gateway_ha(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayHaRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_access_gateway_ha_with_options(request, runtime)

    async def describe_smart_access_gateway_ha_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayHaRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_access_gateway_ha_with_options_async(request, runtime)

    def describe_smart_access_gateways_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeSmartAccessGateways', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_smart_access_gateways_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeSmartAccessGateways', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_smart_access_gateways(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_access_gateways_with_options(request, runtime)

    async def describe_smart_access_gateways_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_access_gateways_with_options_async(request, runtime)

    def describe_smart_access_gateway_versions_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse().from_map(
            self.do_rpcrequest('DescribeSmartAccessGatewayVersions', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_smart_access_gateway_versions_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSmartAccessGatewayVersions', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_smart_access_gateway_versions(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_access_gateway_versions_with_options(request, runtime)

    async def describe_smart_access_gateway_versions_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_access_gateway_versions_with_options_async(request, runtime)

    def describe_snat_entries_with_options(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSnatEntriesResponse().from_map(
            self.do_rpcrequest('DescribeSnatEntries', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snat_entries_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeSnatEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnatEntries', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snat_entries(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snat_entries_with_options(request, runtime)

    async def describe_snat_entries_async(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snat_entries_with_options_async(request, runtime)

    def describe_unbind_flow_log_sags_with_options(
        self,
        request: smartag_20180313_models.DescribeUnbindFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUnbindFlowLogSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUnbindFlowLogSagsResponse().from_map(
            self.do_rpcrequest('DescribeUnbindFlowLogSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_unbind_flow_log_sags_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUnbindFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUnbindFlowLogSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUnbindFlowLogSagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUnbindFlowLogSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_unbind_flow_log_sags(
        self,
        request: smartag_20180313_models.DescribeUnbindFlowLogSagsRequest,
    ) -> smartag_20180313_models.DescribeUnbindFlowLogSagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_unbind_flow_log_sags_with_options(request, runtime)

    async def describe_unbind_flow_log_sags_async(
        self,
        request: smartag_20180313_models.DescribeUnbindFlowLogSagsRequest,
    ) -> smartag_20180313_models.DescribeUnbindFlowLogSagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_unbind_flow_log_sags_with_options_async(request, runtime)

    def describe_user_flow_statistics_with_options(
        self,
        request: smartag_20180313_models.DescribeUserFlowStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserFlowStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserFlowStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeUserFlowStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_flow_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserFlowStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserFlowStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserFlowStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserFlowStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_flow_statistics(
        self,
        request: smartag_20180313_models.DescribeUserFlowStatisticsRequest,
    ) -> smartag_20180313_models.DescribeUserFlowStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_flow_statistics_with_options(request, runtime)

    async def describe_user_flow_statistics_async(
        self,
        request: smartag_20180313_models.DescribeUserFlowStatisticsRequest,
    ) -> smartag_20180313_models.DescribeUserFlowStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_flow_statistics_with_options_async(request, runtime)

    def describe_user_online_clients_with_options(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserOnlineClientsResponse().from_map(
            self.do_rpcrequest('DescribeUserOnlineClients', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_online_clients_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserOnlineClientsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserOnlineClients', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_online_clients(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_online_clients_with_options(request, runtime)

    async def describe_user_online_clients_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_online_clients_with_options_async(request, runtime)

    def describe_user_online_client_statistics_with_options(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeUserOnlineClientStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_online_client_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserOnlineClientStatistics', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_online_client_statistics(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_online_client_statistics_with_options(request, runtime)

    async def describe_user_online_client_statistics_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_online_client_statistics_with_options_async(request, runtime)

    def detach_network_optimization_sags_with_options(
        self,
        request: smartag_20180313_models.DetachNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DetachNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DetachNetworkOptimizationSagsResponse().from_map(
            self.do_rpcrequest('DetachNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_network_optimization_sags_with_options_async(
        self,
        request: smartag_20180313_models.DetachNetworkOptimizationSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DetachNetworkOptimizationSagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DetachNetworkOptimizationSagsResponse().from_map(
            await self.do_rpcrequest_async('DetachNetworkOptimizationSags', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_network_optimization_sags(
        self,
        request: smartag_20180313_models.DetachNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.DetachNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_network_optimization_sags_with_options(request, runtime)

    async def detach_network_optimization_sags_async(
        self,
        request: smartag_20180313_models.DetachNetworkOptimizationSagsRequest,
    ) -> smartag_20180313_models.DetachNetworkOptimizationSagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_network_optimization_sags_with_options_async(request, runtime)

    def diagnose_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DiagnoseSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('DiagnoseSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def diagnose_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DiagnoseSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('DiagnoseSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def diagnose_smart_access_gateway(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.diagnose_smart_access_gateway_with_options(request, runtime)

    async def diagnose_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.diagnose_smart_access_gateway_with_options_async(request, runtime)

    def disable_smart_access_gateway_user_with_options(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisableSmartAccessGatewayUserResponse().from_map(
            self.do_rpcrequest('DisableSmartAccessGatewayUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_smart_access_gateway_user_with_options_async(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisableSmartAccessGatewayUserResponse().from_map(
            await self.do_rpcrequest_async('DisableSmartAccessGatewayUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_smart_access_gateway_user(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_smart_access_gateway_user_with_options(request, runtime)

    async def disable_smart_access_gateway_user_async(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_smart_access_gateway_user_with_options_async(request, runtime)

    def disable_smart_agdpi_monitor_with_options(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisableSmartAGDpiMonitorResponse().from_map(
            self.do_rpcrequest('DisableSmartAGDpiMonitor', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_smart_agdpi_monitor_with_options_async(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisableSmartAGDpiMonitorResponse().from_map(
            await self.do_rpcrequest_async('DisableSmartAGDpiMonitor', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_smart_agdpi_monitor(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_smart_agdpi_monitor_with_options(request, runtime)

    async def disable_smart_agdpi_monitor_async(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_smart_agdpi_monitor_with_options_async(request, runtime)

    def disassociate_aclwith_options(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateACLResponse().from_map(
            self.do_rpcrequest('DisassociateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disassociate_aclwith_options_async(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateACLResponse().from_map(
            await self.do_rpcrequest_async('DisassociateACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disassociate_acl(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_aclwith_options(request, runtime)

    async def disassociate_acl_async(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_aclwith_options_async(request, runtime)

    def disassociate_flow_log_with_options(
        self,
        request: smartag_20180313_models.DisassociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateFlowLogResponse().from_map(
            self.do_rpcrequest('DisassociateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disassociate_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DisassociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateFlowLogResponse().from_map(
            await self.do_rpcrequest_async('DisassociateFlowLog', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disassociate_flow_log(
        self,
        request: smartag_20180313_models.DisassociateFlowLogRequest,
    ) -> smartag_20180313_models.DisassociateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_flow_log_with_options(request, runtime)

    async def disassociate_flow_log_async(
        self,
        request: smartag_20180313_models.DisassociateFlowLogRequest,
    ) -> smartag_20180313_models.DisassociateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_flow_log_with_options_async(request, runtime)

    def disassociate_qos_with_options(
        self,
        request: smartag_20180313_models.DisassociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateQosResponse().from_map(
            self.do_rpcrequest('DisassociateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disassociate_qos_with_options_async(
        self,
        request: smartag_20180313_models.DisassociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DisassociateQosResponse().from_map(
            await self.do_rpcrequest_async('DisassociateQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disassociate_qos(
        self,
        request: smartag_20180313_models.DisassociateQosRequest,
    ) -> smartag_20180313_models.DisassociateQosResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_qos_with_options(request, runtime)

    async def disassociate_qos_async(
        self,
        request: smartag_20180313_models.DisassociateQosRequest,
    ) -> smartag_20180313_models.DisassociateQosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_qos_with_options_async(request, runtime)

    def discribe_smart_access_gateway_diagnosis_report_with_options(
        self,
        request: smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse().from_map(
            self.do_rpcrequest('DiscribeSmartAccessGatewayDiagnosisReport', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def discribe_smart_access_gateway_diagnosis_report_with_options_async(
        self,
        request: smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse().from_map(
            await self.do_rpcrequest_async('DiscribeSmartAccessGatewayDiagnosisReport', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def discribe_smart_access_gateway_diagnosis_report(
        self,
        request: smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
    ) -> smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.discribe_smart_access_gateway_diagnosis_report_with_options(request, runtime)

    async def discribe_smart_access_gateway_diagnosis_report_async(
        self,
        request: smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
    ) -> smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.discribe_smart_access_gateway_diagnosis_report_with_options_async(request, runtime)

    def downgrade_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DowngradeSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('DowngradeSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def downgrade_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DowngradeSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('DowngradeSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def downgrade_smart_access_gateway(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.downgrade_smart_access_gateway_with_options(request, runtime)

    async def downgrade_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.downgrade_smart_access_gateway_with_options_async(request, runtime)

    def downgrade_smart_access_gateway_software_with_options(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse().from_map(
            self.do_rpcrequest('DowngradeSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def downgrade_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse().from_map(
            await self.do_rpcrequest_async('DowngradeSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def downgrade_smart_access_gateway_software(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.downgrade_smart_access_gateway_software_with_options(request, runtime)

    async def downgrade_smart_access_gateway_software_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.downgrade_smart_access_gateway_software_with_options_async(request, runtime)

    def enable_smart_access_gateway_user_with_options(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.EnableSmartAccessGatewayUserResponse().from_map(
            self.do_rpcrequest('EnableSmartAccessGatewayUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_smart_access_gateway_user_with_options_async(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.EnableSmartAccessGatewayUserResponse().from_map(
            await self.do_rpcrequest_async('EnableSmartAccessGatewayUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_smart_access_gateway_user(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_smart_access_gateway_user_with_options(request, runtime)

    async def enable_smart_access_gateway_user_async(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_smart_access_gateway_user_with_options_async(request, runtime)

    def enable_smart_agdpi_monitor_with_options(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.EnableSmartAGDpiMonitorResponse().from_map(
            self.do_rpcrequest('EnableSmartAGDpiMonitor', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_smart_agdpi_monitor_with_options_async(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.EnableSmartAGDpiMonitorResponse().from_map(
            await self.do_rpcrequest_async('EnableSmartAGDpiMonitor', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_smart_agdpi_monitor(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_smart_agdpi_monitor_with_options(request, runtime)

    async def enable_smart_agdpi_monitor_async(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_smart_agdpi_monitor_with_options_async(request, runtime)

    def get_acl_attribute_with_options(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetAclAttributeResponse().from_map(
            self.do_rpcrequest('GetAclAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_acl_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetAclAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetAclAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_acl_attribute(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_acl_attribute_with_options(request, runtime)

    async def get_acl_attribute_async(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_acl_attribute_with_options_async(request, runtime)

    def get_cloud_connect_network_use_limit_with_options(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse().from_map(
            self.do_rpcrequest('GetCloudConnectNetworkUseLimit', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cloud_connect_network_use_limit_with_options_async(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse().from_map(
            await self.do_rpcrequest_async('GetCloudConnectNetworkUseLimit', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cloud_connect_network_use_limit(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_connect_network_use_limit_with_options(request, runtime)

    async def get_cloud_connect_network_use_limit_async(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_connect_network_use_limit_with_options_async(request, runtime)

    def get_qos_attribute_with_options(
        self,
        request: smartag_20180313_models.GetQosAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetQosAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetQosAttributeResponse().from_map(
            self.do_rpcrequest('GetQosAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_qos_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetQosAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetQosAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetQosAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetQosAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_qos_attribute(
        self,
        request: smartag_20180313_models.GetQosAttributeRequest,
    ) -> smartag_20180313_models.GetQosAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qos_attribute_with_options(request, runtime)

    async def get_qos_attribute_async(
        self,
        request: smartag_20180313_models.GetQosAttributeRequest,
    ) -> smartag_20180313_models.GetQosAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qos_attribute_with_options_async(request, runtime)

    def get_smart_access_gateway_use_limit_with_options(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse().from_map(
            self.do_rpcrequest('GetSmartAccessGatewayUseLimit', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_smart_access_gateway_use_limit_with_options_async(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse().from_map(
            await self.do_rpcrequest_async('GetSmartAccessGatewayUseLimit', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_smart_access_gateway_use_limit(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_smart_access_gateway_use_limit_with_options(request, runtime)

    async def get_smart_access_gateway_use_limit_async(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_smart_access_gateway_use_limit_with_options_async(request, runtime)

    def get_smart_agdpi_attribute_with_options(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetSmartAGDpiAttributeResponse().from_map(
            self.do_rpcrequest('GetSmartAGDpiAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_smart_agdpi_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GetSmartAGDpiAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetSmartAGDpiAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_smart_agdpi_attribute(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_smart_agdpi_attribute_with_options(request, runtime)

    async def get_smart_agdpi_attribute_async(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_smart_agdpi_attribute_with_options_async(request, runtime)

    def grant_instance_to_cbn_with_options(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantInstanceToCbnResponse().from_map(
            self.do_rpcrequest('GrantInstanceToCbn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_instance_to_cbn_with_options_async(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantInstanceToCbnResponse().from_map(
            await self.do_rpcrequest_async('GrantInstanceToCbn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_instance_to_cbn(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_cbn_with_options(request, runtime)

    async def grant_instance_to_cbn_async(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_instance_to_cbn_with_options_async(request, runtime)

    def grant_sag_instance_to_ccn_with_options(
        self,
        request: smartag_20180313_models.GrantSagInstanceToCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToCcnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantSagInstanceToCcnResponse().from_map(
            self.do_rpcrequest('GrantSagInstanceToCcn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_sag_instance_to_ccn_with_options_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToCcnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantSagInstanceToCcnResponse().from_map(
            await self.do_rpcrequest_async('GrantSagInstanceToCcn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_sag_instance_to_ccn(
        self,
        request: smartag_20180313_models.GrantSagInstanceToCcnRequest,
    ) -> smartag_20180313_models.GrantSagInstanceToCcnResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_sag_instance_to_ccn_with_options(request, runtime)

    async def grant_sag_instance_to_ccn_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToCcnRequest,
    ) -> smartag_20180313_models.GrantSagInstanceToCcnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_sag_instance_to_ccn_with_options_async(request, runtime)

    def grant_sag_instance_to_vbr_with_options(
        self,
        request: smartag_20180313_models.GrantSagInstanceToVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantSagInstanceToVbrResponse().from_map(
            self.do_rpcrequest('GrantSagInstanceToVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_sag_instance_to_vbr_with_options_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.GrantSagInstanceToVbrResponse().from_map(
            await self.do_rpcrequest_async('GrantSagInstanceToVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_sag_instance_to_vbr(
        self,
        request: smartag_20180313_models.GrantSagInstanceToVbrRequest,
    ) -> smartag_20180313_models.GrantSagInstanceToVbrResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_sag_instance_to_vbr_with_options(request, runtime)

    async def grant_sag_instance_to_vbr_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToVbrRequest,
    ) -> smartag_20180313_models.GrantSagInstanceToVbrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_sag_instance_to_vbr_with_options_async(request, runtime)

    def kick_out_clients_with_options(
        self,
        request: smartag_20180313_models.KickOutClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.KickOutClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.KickOutClientsResponse().from_map(
            self.do_rpcrequest('KickOutClients', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kick_out_clients_with_options_async(
        self,
        request: smartag_20180313_models.KickOutClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.KickOutClientsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.KickOutClientsResponse().from_map(
            await self.do_rpcrequest_async('KickOutClients', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kick_out_clients(
        self,
        request: smartag_20180313_models.KickOutClientsRequest,
    ) -> smartag_20180313_models.KickOutClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.kick_out_clients_with_options(request, runtime)

    async def kick_out_clients_async(
        self,
        request: smartag_20180313_models.KickOutClientsRequest,
    ) -> smartag_20180313_models.KickOutClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kick_out_clients_with_options_async(request, runtime)

    def list_access_points_with_options(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListAccessPointsResponse().from_map(
            self.do_rpcrequest('ListAccessPoints', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_access_points_with_options_async(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListAccessPointsResponse().from_map(
            await self.do_rpcrequest_async('ListAccessPoints', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_access_points(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_points_with_options(request, runtime)

    async def list_access_points_async(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_points_with_options_async(request, runtime)

    def list_dpi_config_error_with_options(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiConfigErrorResponse().from_map(
            self.do_rpcrequest('ListDpiConfigError', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dpi_config_error_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiConfigErrorResponse().from_map(
            await self.do_rpcrequest_async('ListDpiConfigError', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dpi_config_error(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dpi_config_error_with_options(request, runtime)

    async def list_dpi_config_error_async(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dpi_config_error_with_options_async(request, runtime)

    def list_dpi_groups_with_options(
        self,
        request: smartag_20180313_models.ListDpiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiGroupsResponse().from_map(
            self.do_rpcrequest('ListDpiGroups', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dpi_groups_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListDpiGroups', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dpi_groups(
        self,
        request: smartag_20180313_models.ListDpiGroupsRequest,
    ) -> smartag_20180313_models.ListDpiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dpi_groups_with_options(request, runtime)

    async def list_dpi_groups_async(
        self,
        request: smartag_20180313_models.ListDpiGroupsRequest,
    ) -> smartag_20180313_models.ListDpiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dpi_groups_with_options_async(request, runtime)

    def list_dpi_signatures_with_options(
        self,
        request: smartag_20180313_models.ListDpiSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiSignaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiSignaturesResponse().from_map(
            self.do_rpcrequest('ListDpiSignatures', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dpi_signatures_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiSignaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListDpiSignaturesResponse().from_map(
            await self.do_rpcrequest_async('ListDpiSignatures', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dpi_signatures(
        self,
        request: smartag_20180313_models.ListDpiSignaturesRequest,
    ) -> smartag_20180313_models.ListDpiSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dpi_signatures_with_options(request, runtime)

    async def list_dpi_signatures_async(
        self,
        request: smartag_20180313_models.ListDpiSignaturesRequest,
    ) -> smartag_20180313_models.ListDpiSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dpi_signatures_with_options_async(request, runtime)

    def list_enterprise_code_with_options(
        self,
        request: smartag_20180313_models.ListEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListEnterpriseCodeResponse().from_map(
            self.do_rpcrequest('ListEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.ListEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListEnterpriseCodeResponse().from_map(
            await self.do_rpcrequest_async('ListEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_enterprise_code(
        self,
        request: smartag_20180313_models.ListEnterpriseCodeRequest,
    ) -> smartag_20180313_models.ListEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_code_with_options(request, runtime)

    async def list_enterprise_code_async(
        self,
        request: smartag_20180313_models.ListEnterpriseCodeRequest,
    ) -> smartag_20180313_models.ListEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_enterprise_code_with_options_async(request, runtime)

    def list_smart_agapi_unsupported_feature_with_options(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse().from_map(
            self.do_rpcrequest('ListSmartAGApiUnsupportedFeature', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_smart_agapi_unsupported_feature_with_options_async(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse().from_map(
            await self.do_rpcrequest_async('ListSmartAGApiUnsupportedFeature', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_smart_agapi_unsupported_feature(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_smart_agapi_unsupported_feature_with_options(request, runtime)

    async def list_smart_agapi_unsupported_feature_async(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_smart_agapi_unsupported_feature_with_options_async(request, runtime)

    def list_smart_agby_access_point_with_options(
        self,
        request: smartag_20180313_models.ListSmartAGByAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGByAccessPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListSmartAGByAccessPointResponse().from_map(
            self.do_rpcrequest('ListSmartAGByAccessPoint', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_smart_agby_access_point_with_options_async(
        self,
        request: smartag_20180313_models.ListSmartAGByAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGByAccessPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ListSmartAGByAccessPointResponse().from_map(
            await self.do_rpcrequest_async('ListSmartAGByAccessPoint', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_smart_agby_access_point(
        self,
        request: smartag_20180313_models.ListSmartAGByAccessPointRequest,
    ) -> smartag_20180313_models.ListSmartAGByAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_smart_agby_access_point_with_options(request, runtime)

    async def list_smart_agby_access_point_async(
        self,
        request: smartag_20180313_models.ListSmartAGByAccessPointRequest,
    ) -> smartag_20180313_models.ListSmartAGByAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_smart_agby_access_point_with_options_async(request, runtime)

    def modify_aclwith_options(
        self,
        request: smartag_20180313_models.ModifyACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyACLResponse().from_map(
            self.do_rpcrequest('ModifyACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_aclwith_options_async(
        self,
        request: smartag_20180313_models.ModifyACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyACLResponse().from_map(
            await self.do_rpcrequest_async('ModifyACL', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_acl(
        self,
        request: smartag_20180313_models.ModifyACLRequest,
    ) -> smartag_20180313_models.ModifyACLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_aclwith_options(request, runtime)

    async def modify_acl_async(
        self,
        request: smartag_20180313_models.ModifyACLRequest,
    ) -> smartag_20180313_models.ModifyACLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_aclwith_options_async(request, runtime)

    def modify_aclrule_with_options(
        self,
        request: smartag_20180313_models.ModifyACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyACLRuleResponse().from_map(
            self.do_rpcrequest('ModifyACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.ModifyACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyACLRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyACLRule', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_aclrule(
        self,
        request: smartag_20180313_models.ModifyACLRuleRequest,
    ) -> smartag_20180313_models.ModifyACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_aclrule_with_options(request, runtime)

    async def modify_aclrule_async(
        self,
        request: smartag_20180313_models.ModifyACLRuleRequest,
    ) -> smartag_20180313_models.ModifyACLRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_aclrule_with_options_async(request, runtime)

    def modify_client_user_dnswith_options(
        self,
        request: smartag_20180313_models.ModifyClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyClientUserDNSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyClientUserDNSResponse().from_map(
            self.do_rpcrequest('ModifyClientUserDNS', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_client_user_dnswith_options_async(
        self,
        request: smartag_20180313_models.ModifyClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyClientUserDNSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyClientUserDNSResponse().from_map(
            await self.do_rpcrequest_async('ModifyClientUserDNS', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_client_user_dns(
        self,
        request: smartag_20180313_models.ModifyClientUserDNSRequest,
    ) -> smartag_20180313_models.ModifyClientUserDNSResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_client_user_dnswith_options(request, runtime)

    async def modify_client_user_dns_async(
        self,
        request: smartag_20180313_models.ModifyClientUserDNSRequest,
    ) -> smartag_20180313_models.ModifyClientUserDNSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_client_user_dnswith_options_async(request, runtime)

    def modify_cloud_connect_network_with_options(
        self,
        request: smartag_20180313_models.ModifyCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyCloudConnectNetworkResponse().from_map(
            self.do_rpcrequest('ModifyCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.ModifyCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyCloudConnectNetworkResponse().from_map(
            await self.do_rpcrequest_async('ModifyCloudConnectNetwork', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cloud_connect_network(
        self,
        request: smartag_20180313_models.ModifyCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.ModifyCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_connect_network_with_options(request, runtime)

    async def modify_cloud_connect_network_async(
        self,
        request: smartag_20180313_models.ModifyCloudConnectNetworkRequest,
    ) -> smartag_20180313_models.ModifyCloudConnectNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cloud_connect_network_with_options_async(request, runtime)

    def modify_device_auto_upgrade_policy_with_options(
        self,
        request: smartag_20180313_models.ModifyDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse().from_map(
            self.do_rpcrequest('ModifyDeviceAutoUpgradePolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_device_auto_upgrade_policy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyDeviceAutoUpgradePolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_auto_upgrade_policy(
        self,
        request: smartag_20180313_models.ModifyDeviceAutoUpgradePolicyRequest,
    ) -> smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_device_auto_upgrade_policy_with_options(request, runtime)

    async def modify_device_auto_upgrade_policy_async(
        self,
        request: smartag_20180313_models.ModifyDeviceAutoUpgradePolicyRequest,
    ) -> smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_auto_upgrade_policy_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: smartag_20180313_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyFlowLogAttributeResponse().from_map(
            self.do_rpcrequest('ModifyFlowLogAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: smartag_20180313_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyFlowLogAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowLogAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: smartag_20180313_models.ModifyFlowLogAttributeRequest,
    ) -> smartag_20180313_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: smartag_20180313_models.ModifyFlowLogAttributeRequest,
    ) -> smartag_20180313_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def modify_health_check_with_options(
        self,
        request: smartag_20180313_models.ModifyHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyHealthCheckResponse().from_map(
            self.do_rpcrequest('ModifyHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_health_check_with_options_async(
        self,
        request: smartag_20180313_models.ModifyHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyHealthCheckResponse().from_map(
            await self.do_rpcrequest_async('ModifyHealthCheck', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_health_check(
        self,
        request: smartag_20180313_models.ModifyHealthCheckRequest,
    ) -> smartag_20180313_models.ModifyHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_with_options(request, runtime)

    async def modify_health_check_async(
        self,
        request: smartag_20180313_models.ModifyHealthCheckRequest,
    ) -> smartag_20180313_models.ModifyHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_health_check_with_options_async(request, runtime)

    def modify_network_optimization_with_options(
        self,
        request: smartag_20180313_models.ModifyNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyNetworkOptimizationResponse().from_map(
            self.do_rpcrequest('ModifyNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_optimization_with_options_async(
        self,
        request: smartag_20180313_models.ModifyNetworkOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyNetworkOptimizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyNetworkOptimizationResponse().from_map(
            await self.do_rpcrequest_async('ModifyNetworkOptimization', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_optimization(
        self,
        request: smartag_20180313_models.ModifyNetworkOptimizationRequest,
    ) -> smartag_20180313_models.ModifyNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_optimization_with_options(request, runtime)

    async def modify_network_optimization_async(
        self,
        request: smartag_20180313_models.ModifyNetworkOptimizationRequest,
    ) -> smartag_20180313_models.ModifyNetworkOptimizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_optimization_with_options_async(request, runtime)

    def modify_qos_with_options(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosResponse().from_map(
            self.do_rpcrequest('ModifyQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_qos_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosResponse().from_map(
            await self.do_rpcrequest_async('ModifyQos', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_qos(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
    ) -> smartag_20180313_models.ModifyQosResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_qos_with_options(request, runtime)

    async def modify_qos_async(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
    ) -> smartag_20180313_models.ModifyQosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_qos_with_options_async(request, runtime)

    def modify_qos_car_with_options(
        self,
        request: smartag_20180313_models.ModifyQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosCarResponse().from_map(
            self.do_rpcrequest('ModifyQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosCarResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosCarResponse().from_map(
            await self.do_rpcrequest_async('ModifyQosCar', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_qos_car(
        self,
        request: smartag_20180313_models.ModifyQosCarRequest,
    ) -> smartag_20180313_models.ModifyQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_qos_car_with_options(request, runtime)

    async def modify_qos_car_async(
        self,
        request: smartag_20180313_models.ModifyQosCarRequest,
    ) -> smartag_20180313_models.ModifyQosCarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_qos_car_with_options_async(request, runtime)

    def modify_qos_policy_with_options(
        self,
        request: smartag_20180313_models.ModifyQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosPolicyResponse().from_map(
            self.do_rpcrequest('ModifyQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyQosPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyQosPolicy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_qos_policy(
        self,
        request: smartag_20180313_models.ModifyQosPolicyRequest,
    ) -> smartag_20180313_models.ModifyQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_qos_policy_with_options(request, runtime)

    async def modify_qos_policy_async(
        self,
        request: smartag_20180313_models.ModifyQosPolicyRequest,
    ) -> smartag_20180313_models.ModifyQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_qos_policy_with_options_async(request, runtime)

    def modify_route_distribution_strategy_with_options(
        self,
        request: smartag_20180313_models.ModifyRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyRouteDistributionStrategyResponse().from_map(
            self.do_rpcrequest('ModifyRouteDistributionStrategy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_route_distribution_strategy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifyRouteDistributionStrategyResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouteDistributionStrategy', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_route_distribution_strategy(
        self,
        request: smartag_20180313_models.ModifyRouteDistributionStrategyRequest,
    ) -> smartag_20180313_models.ModifyRouteDistributionStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_route_distribution_strategy_with_options(request, runtime)

    async def modify_route_distribution_strategy_async(
        self,
        request: smartag_20180313_models.ModifyRouteDistributionStrategyRequest,
    ) -> smartag_20180313_models.ModifyRouteDistributionStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_route_distribution_strategy_with_options_async(request, runtime)

    def modify_sag_cidr_with_options(
        self,
        request: smartag_20180313_models.ModifySagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagCidrResponse().from_map(
            self.do_rpcrequest('ModifySagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_cidr_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagCidrResponse().from_map(
            await self.do_rpcrequest_async('ModifySagCidr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_cidr(
        self,
        request: smartag_20180313_models.ModifySagCidrRequest,
    ) -> smartag_20180313_models.ModifySagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_cidr_with_options(request, runtime)

    async def modify_sag_cidr_async(
        self,
        request: smartag_20180313_models.ModifySagCidrRequest,
    ) -> smartag_20180313_models.ModifySagCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_cidr_with_options_async(request, runtime)

    def modify_sag_ecroute_backup_with_options(
        self,
        request: smartag_20180313_models.ModifySagECRouteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagECRouteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagECRouteBackupResponse().from_map(
            self.do_rpcrequest('ModifySagECRouteBackup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_ecroute_backup_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagECRouteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagECRouteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagECRouteBackupResponse().from_map(
            await self.do_rpcrequest_async('ModifySagECRouteBackup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_ecroute_backup(
        self,
        request: smartag_20180313_models.ModifySagECRouteBackupRequest,
    ) -> smartag_20180313_models.ModifySagECRouteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_ecroute_backup_with_options(request, runtime)

    async def modify_sag_ecroute_backup_async(
        self,
        request: smartag_20180313_models.ModifySagECRouteBackupRequest,
    ) -> smartag_20180313_models.ModifySagECRouteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_ecroute_backup_with_options_async(request, runtime)

    def modify_sag_express_connect_interface_with_options(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagExpressConnectInterfaceResponse().from_map(
            self.do_rpcrequest('ModifySagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagExpressConnectInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ModifySagExpressConnectInterface', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_express_connect_interface(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_express_connect_interface_with_options(request, runtime)

    async def modify_sag_express_connect_interface_async(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_express_connect_interface_with_options_async(request, runtime)

    def modify_sag_global_route_protocol_with_options(
        self,
        request: smartag_20180313_models.ModifySagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagGlobalRouteProtocolResponse().from_map(
            self.do_rpcrequest('ModifySagGlobalRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagGlobalRouteProtocolResponse().from_map(
            await self.do_rpcrequest_async('ModifySagGlobalRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_global_route_protocol(
        self,
        request: smartag_20180313_models.ModifySagGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.ModifySagGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_global_route_protocol_with_options(request, runtime)

    async def modify_sag_global_route_protocol_async(
        self,
        request: smartag_20180313_models.ModifySagGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.ModifySagGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_global_route_protocol_with_options_async(request, runtime)

    def modify_sag_ha_with_options(
        self,
        request: smartag_20180313_models.ModifySagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagHaResponse().from_map(
            self.do_rpcrequest('ModifySagHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_ha_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagHaResponse().from_map(
            await self.do_rpcrequest_async('ModifySagHa', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_ha(
        self,
        request: smartag_20180313_models.ModifySagHaRequest,
    ) -> smartag_20180313_models.ModifySagHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_ha_with_options(request, runtime)

    async def modify_sag_ha_async(
        self,
        request: smartag_20180313_models.ModifySagHaRequest,
    ) -> smartag_20180313_models.ModifySagHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_ha_with_options_async(request, runtime)

    def modify_sag_lan_with_options(
        self,
        request: smartag_20180313_models.ModifySagLanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagLanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagLanResponse().from_map(
            self.do_rpcrequest('ModifySagLan', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_lan_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagLanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagLanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagLanResponse().from_map(
            await self.do_rpcrequest_async('ModifySagLan', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_lan(
        self,
        request: smartag_20180313_models.ModifySagLanRequest,
    ) -> smartag_20180313_models.ModifySagLanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_lan_with_options(request, runtime)

    async def modify_sag_lan_async(
        self,
        request: smartag_20180313_models.ModifySagLanRequest,
    ) -> smartag_20180313_models.ModifySagLanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_lan_with_options_async(request, runtime)

    def modify_sag_management_port_with_options(
        self,
        request: smartag_20180313_models.ModifySagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagManagementPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagManagementPortResponse().from_map(
            self.do_rpcrequest('ModifySagManagementPort', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_management_port_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagManagementPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagManagementPortResponse().from_map(
            await self.do_rpcrequest_async('ModifySagManagementPort', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_management_port(
        self,
        request: smartag_20180313_models.ModifySagManagementPortRequest,
    ) -> smartag_20180313_models.ModifySagManagementPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_management_port_with_options(request, runtime)

    async def modify_sag_management_port_async(
        self,
        request: smartag_20180313_models.ModifySagManagementPortRequest,
    ) -> smartag_20180313_models.ModifySagManagementPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_management_port_with_options_async(request, runtime)

    def modify_sag_port_role_with_options(
        self,
        request: smartag_20180313_models.ModifySagPortRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagPortRoleResponse().from_map(
            self.do_rpcrequest('ModifySagPortRole', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_port_role_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagPortRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagPortRoleResponse().from_map(
            await self.do_rpcrequest_async('ModifySagPortRole', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_port_role(
        self,
        request: smartag_20180313_models.ModifySagPortRoleRequest,
    ) -> smartag_20180313_models.ModifySagPortRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_port_role_with_options(request, runtime)

    async def modify_sag_port_role_async(
        self,
        request: smartag_20180313_models.ModifySagPortRoleRequest,
    ) -> smartag_20180313_models.ModifySagPortRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_port_role_with_options_async(request, runtime)

    def modify_sag_port_route_protocol_with_options(
        self,
        request: smartag_20180313_models.ModifySagPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagPortRouteProtocolResponse().from_map(
            self.do_rpcrequest('ModifySagPortRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_port_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagPortRouteProtocolResponse().from_map(
            await self.do_rpcrequest_async('ModifySagPortRouteProtocol', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_port_route_protocol(
        self,
        request: smartag_20180313_models.ModifySagPortRouteProtocolRequest,
    ) -> smartag_20180313_models.ModifySagPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_port_route_protocol_with_options(request, runtime)

    async def modify_sag_port_route_protocol_async(
        self,
        request: smartag_20180313_models.ModifySagPortRouteProtocolRequest,
    ) -> smartag_20180313_models.ModifySagPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_port_route_protocol_with_options_async(request, runtime)

    def modify_sag_remote_access_with_options(
        self,
        request: smartag_20180313_models.ModifySagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRemoteAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRemoteAccessResponse().from_map(
            self.do_rpcrequest('ModifySagRemoteAccess', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_remote_access_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRemoteAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRemoteAccessResponse().from_map(
            await self.do_rpcrequest_async('ModifySagRemoteAccess', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_remote_access(
        self,
        request: smartag_20180313_models.ModifySagRemoteAccessRequest,
    ) -> smartag_20180313_models.ModifySagRemoteAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_remote_access_with_options(request, runtime)

    async def modify_sag_remote_access_async(
        self,
        request: smartag_20180313_models.ModifySagRemoteAccessRequest,
    ) -> smartag_20180313_models.ModifySagRemoteAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_remote_access_with_options_async(request, runtime)

    def modify_sag_route_protocol_bgp_with_options(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRouteProtocolBgpResponse().from_map(
            self.do_rpcrequest('ModifySagRouteProtocolBgp', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_route_protocol_bgp_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRouteProtocolBgpResponse().from_map(
            await self.do_rpcrequest_async('ModifySagRouteProtocolBgp', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_route_protocol_bgp(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolBgpRequest,
    ) -> smartag_20180313_models.ModifySagRouteProtocolBgpResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_route_protocol_bgp_with_options(request, runtime)

    async def modify_sag_route_protocol_bgp_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolBgpRequest,
    ) -> smartag_20180313_models.ModifySagRouteProtocolBgpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_route_protocol_bgp_with_options_async(request, runtime)

    def modify_sag_route_protocol_ospf_with_options(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRouteProtocolOspfResponse().from_map(
            self.do_rpcrequest('ModifySagRouteProtocolOspf', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_route_protocol_ospf_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagRouteProtocolOspfResponse().from_map(
            await self.do_rpcrequest_async('ModifySagRouteProtocolOspf', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_route_protocol_ospf(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolOspfRequest,
    ) -> smartag_20180313_models.ModifySagRouteProtocolOspfResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_route_protocol_ospf_with_options(request, runtime)

    async def modify_sag_route_protocol_ospf_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolOspfRequest,
    ) -> smartag_20180313_models.ModifySagRouteProtocolOspfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_route_protocol_ospf_with_options_async(request, runtime)

    def modify_sag_static_route_with_options(
        self,
        request: smartag_20180313_models.ModifySagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagStaticRouteResponse().from_map(
            self.do_rpcrequest('ModifySagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagStaticRouteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagStaticRouteResponse().from_map(
            await self.do_rpcrequest_async('ModifySagStaticRoute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_static_route(
        self,
        request: smartag_20180313_models.ModifySagStaticRouteRequest,
    ) -> smartag_20180313_models.ModifySagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_static_route_with_options(request, runtime)

    async def modify_sag_static_route_async(
        self,
        request: smartag_20180313_models.ModifySagStaticRouteRequest,
    ) -> smartag_20180313_models.ModifySagStaticRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_static_route_with_options_async(request, runtime)

    def modify_sag_user_dns_with_options(
        self,
        request: smartag_20180313_models.ModifySagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagUserDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagUserDnsResponse().from_map(
            self.do_rpcrequest('ModifySagUserDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_user_dns_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagUserDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagUserDnsResponse().from_map(
            await self.do_rpcrequest_async('ModifySagUserDns', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_user_dns(
        self,
        request: smartag_20180313_models.ModifySagUserDnsRequest,
    ) -> smartag_20180313_models.ModifySagUserDnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_user_dns_with_options(request, runtime)

    async def modify_sag_user_dns_async(
        self,
        request: smartag_20180313_models.ModifySagUserDnsRequest,
    ) -> smartag_20180313_models.ModifySagUserDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_user_dns_with_options_async(request, runtime)

    def modify_sag_wan_with_options(
        self,
        request: smartag_20180313_models.ModifySagWanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWanResponse().from_map(
            self.do_rpcrequest('ModifySagWan', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_wan_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWanResponse().from_map(
            await self.do_rpcrequest_async('ModifySagWan', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_wan(
        self,
        request: smartag_20180313_models.ModifySagWanRequest,
    ) -> smartag_20180313_models.ModifySagWanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_wan_with_options(request, runtime)

    async def modify_sag_wan_async(
        self,
        request: smartag_20180313_models.ModifySagWanRequest,
    ) -> smartag_20180313_models.ModifySagWanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_wan_with_options_async(request, runtime)

    def modify_sag_wan_snat_with_options(
        self,
        request: smartag_20180313_models.ModifySagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanSnatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWanSnatResponse().from_map(
            self.do_rpcrequest('ModifySagWanSnat', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanSnatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWanSnatResponse().from_map(
            await self.do_rpcrequest_async('ModifySagWanSnat', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_wan_snat(
        self,
        request: smartag_20180313_models.ModifySagWanSnatRequest,
    ) -> smartag_20180313_models.ModifySagWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_wan_snat_with_options(request, runtime)

    async def modify_sag_wan_snat_async(
        self,
        request: smartag_20180313_models.ModifySagWanSnatRequest,
    ) -> smartag_20180313_models.ModifySagWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_wan_snat_with_options_async(request, runtime)

    def modify_sag_wifi_with_options(
        self,
        request: smartag_20180313_models.ModifySagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWifiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWifiResponse().from_map(
            self.do_rpcrequest('ModifySagWifi', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sag_wifi_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWifiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySagWifiResponse().from_map(
            await self.do_rpcrequest_async('ModifySagWifi', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sag_wifi(
        self,
        request: smartag_20180313_models.ModifySagWifiRequest,
    ) -> smartag_20180313_models.ModifySagWifiResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sag_wifi_with_options(request, runtime)

    async def modify_sag_wifi_async(
        self,
        request: smartag_20180313_models.ModifySagWifiRequest,
    ) -> smartag_20180313_models.ModifySagWifiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sag_wifi_with_options_async(request, runtime)

    def modify_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('ModifySmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('ModifySmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_smart_access_gateway(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_smart_access_gateway_with_options(request, runtime)

    async def modify_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_smart_access_gateway_with_options_async(request, runtime)

    def modify_smart_access_gateway_client_user_with_options(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse().from_map(
            self.do_rpcrequest('ModifySmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse().from_map(
            await self.do_rpcrequest_async('ModifySmartAccessGatewayClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_smart_access_gateway_client_user(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_smart_access_gateway_client_user_with_options(request, runtime)

    async def modify_smart_access_gateway_client_user_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayClientUserRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_smart_access_gateway_client_user_with_options_async(request, runtime)

    def modify_smart_access_gateway_up_bandwidth_with_options(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse().from_map(
            self.do_rpcrequest('ModifySmartAccessGatewayUpBandwidth', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_smart_access_gateway_up_bandwidth_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifySmartAccessGatewayUpBandwidth', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_smart_access_gateway_up_bandwidth(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_smart_access_gateway_up_bandwidth_with_options(request, runtime)

    async def modify_smart_access_gateway_up_bandwidth_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthRequest,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_smart_access_gateway_up_bandwidth_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: smartag_20180313_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: smartag_20180313_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: smartag_20180313_models.MoveResourceGroupRequest,
    ) -> smartag_20180313_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: smartag_20180313_models.MoveResourceGroupRequest,
    ) -> smartag_20180313_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def orchestrate_sag_ecroute_backup_with_options(
        self,
        request: smartag_20180313_models.OrchestrateSagECRouteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.OrchestrateSagECRouteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.OrchestrateSagECRouteBackupResponse().from_map(
            self.do_rpcrequest('OrchestrateSagECRouteBackup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def orchestrate_sag_ecroute_backup_with_options_async(
        self,
        request: smartag_20180313_models.OrchestrateSagECRouteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.OrchestrateSagECRouteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.OrchestrateSagECRouteBackupResponse().from_map(
            await self.do_rpcrequest_async('OrchestrateSagECRouteBackup', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def orchestrate_sag_ecroute_backup(
        self,
        request: smartag_20180313_models.OrchestrateSagECRouteBackupRequest,
    ) -> smartag_20180313_models.OrchestrateSagECRouteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.orchestrate_sag_ecroute_backup_with_options(request, runtime)

    async def orchestrate_sag_ecroute_backup_async(
        self,
        request: smartag_20180313_models.OrchestrateSagECRouteBackupRequest,
    ) -> smartag_20180313_models.OrchestrateSagECRouteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.orchestrate_sag_ecroute_backup_with_options_async(request, runtime)

    def reboot_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RebootSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('RebootSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RebootSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('RebootSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_smart_access_gateway(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_smart_access_gateway_with_options(request, runtime)

    async def reboot_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_smart_access_gateway_with_options_async(request, runtime)

    def reset_smart_access_gateway_client_user_password_with_options(
        self,
        request: smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse().from_map(
            self.do_rpcrequest('ResetSmartAccessGatewayClientUserPassword', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_smart_access_gateway_client_user_password_with_options_async(
        self,
        request: smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetSmartAccessGatewayClientUserPassword', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_smart_access_gateway_client_user_password(
        self,
        request: smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordRequest,
    ) -> smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_smart_access_gateway_client_user_password_with_options(request, runtime)

    async def reset_smart_access_gateway_client_user_password_async(
        self,
        request: smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordRequest,
    ) -> smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_smart_access_gateway_client_user_password_with_options_async(request, runtime)

    def revoke_instance_from_cbn_with_options(
        self,
        request: smartag_20180313_models.RevokeInstanceFromCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromCbnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeInstanceFromCbnResponse().from_map(
            self.do_rpcrequest('RevokeInstanceFromCbn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_instance_from_cbn_with_options_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromCbnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeInstanceFromCbnResponse().from_map(
            await self.do_rpcrequest_async('RevokeInstanceFromCbn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_instance_from_cbn(
        self,
        request: smartag_20180313_models.RevokeInstanceFromCbnRequest,
    ) -> smartag_20180313_models.RevokeInstanceFromCbnResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_cbn_with_options(request, runtime)

    async def revoke_instance_from_cbn_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromCbnRequest,
    ) -> smartag_20180313_models.RevokeInstanceFromCbnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_instance_from_cbn_with_options_async(request, runtime)

    def revoke_instance_from_vbr_with_options(
        self,
        request: smartag_20180313_models.RevokeInstanceFromVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeInstanceFromVbrResponse().from_map(
            self.do_rpcrequest('RevokeInstanceFromVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_instance_from_vbr_with_options_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeInstanceFromVbrResponse().from_map(
            await self.do_rpcrequest_async('RevokeInstanceFromVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_instance_from_vbr(
        self,
        request: smartag_20180313_models.RevokeInstanceFromVbrRequest,
    ) -> smartag_20180313_models.RevokeInstanceFromVbrResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_vbr_with_options(request, runtime)

    async def revoke_instance_from_vbr_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromVbrRequest,
    ) -> smartag_20180313_models.RevokeInstanceFromVbrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_instance_from_vbr_with_options_async(request, runtime)

    def revoke_sag_instance_from_ccn_with_options(
        self,
        request: smartag_20180313_models.RevokeSagInstanceFromCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeSagInstanceFromCcnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeSagInstanceFromCcnResponse().from_map(
            self.do_rpcrequest('RevokeSagInstanceFromCcn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_sag_instance_from_ccn_with_options_async(
        self,
        request: smartag_20180313_models.RevokeSagInstanceFromCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeSagInstanceFromCcnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RevokeSagInstanceFromCcnResponse().from_map(
            await self.do_rpcrequest_async('RevokeSagInstanceFromCcn', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_sag_instance_from_ccn(
        self,
        request: smartag_20180313_models.RevokeSagInstanceFromCcnRequest,
    ) -> smartag_20180313_models.RevokeSagInstanceFromCcnResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_sag_instance_from_ccn_with_options(request, runtime)

    async def revoke_sag_instance_from_ccn_async(
        self,
        request: smartag_20180313_models.RevokeSagInstanceFromCcnRequest,
    ) -> smartag_20180313_models.RevokeSagInstanceFromCcnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_sag_instance_from_ccn_with_options_async(request, runtime)

    def roam_client_user_with_options(
        self,
        request: smartag_20180313_models.RoamClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RoamClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RoamClientUserResponse().from_map(
            self.do_rpcrequest('RoamClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def roam_client_user_with_options_async(
        self,
        request: smartag_20180313_models.RoamClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RoamClientUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.RoamClientUserResponse().from_map(
            await self.do_rpcrequest_async('RoamClientUser', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def roam_client_user(
        self,
        request: smartag_20180313_models.RoamClientUserRequest,
    ) -> smartag_20180313_models.RoamClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.roam_client_user_with_options(request, runtime)

    async def roam_client_user_async(
        self,
        request: smartag_20180313_models.RoamClientUserRequest,
    ) -> smartag_20180313_models.RoamClientUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.roam_client_user_with_options_async(request, runtime)

    def set_sag_routeable_address_with_options(
        self,
        request: smartag_20180313_models.SetSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SetSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.SetSagRouteableAddressResponse().from_map(
            self.do_rpcrequest('SetSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_sag_routeable_address_with_options_async(
        self,
        request: smartag_20180313_models.SetSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SetSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.SetSagRouteableAddressResponse().from_map(
            await self.do_rpcrequest_async('SetSagRouteableAddress', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_sag_routeable_address(
        self,
        request: smartag_20180313_models.SetSagRouteableAddressRequest,
    ) -> smartag_20180313_models.SetSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_sag_routeable_address_with_options(request, runtime)

    async def set_sag_routeable_address_async(
        self,
        request: smartag_20180313_models.SetSagRouteableAddressRequest,
    ) -> smartag_20180313_models.SetSagRouteableAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_sag_routeable_address_with_options_async(request, runtime)

    def synchronize_smart_agweb_config_with_options(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.SynchronizeSmartAGWebConfigResponse().from_map(
            self.do_rpcrequest('SynchronizeSmartAGWebConfig', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def synchronize_smart_agweb_config_with_options_async(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.SynchronizeSmartAGWebConfigResponse().from_map(
            await self.do_rpcrequest_async('SynchronizeSmartAGWebConfig', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def synchronize_smart_agweb_config(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.synchronize_smart_agweb_config_with_options(request, runtime)

    async def synchronize_smart_agweb_config_async(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.synchronize_smart_agweb_config_with_options_async(request, runtime)

    def unbind_serial_number_with_options(
        self,
        request: smartag_20180313_models.UnbindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSerialNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindSerialNumberResponse().from_map(
            self.do_rpcrequest('UnbindSerialNumber', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_serial_number_with_options_async(
        self,
        request: smartag_20180313_models.UnbindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSerialNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindSerialNumberResponse().from_map(
            await self.do_rpcrequest_async('UnbindSerialNumber', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_serial_number(
        self,
        request: smartag_20180313_models.UnbindSerialNumberRequest,
    ) -> smartag_20180313_models.UnbindSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_serial_number_with_options(request, runtime)

    async def unbind_serial_number_async(
        self,
        request: smartag_20180313_models.UnbindSerialNumberRequest,
    ) -> smartag_20180313_models.UnbindSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_serial_number_with_options_async(request, runtime)

    def unbind_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.UnbindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('UnbindSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UnbindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('UnbindSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_smart_access_gateway(
        self,
        request: smartag_20180313_models.UnbindSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UnbindSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_smart_access_gateway_with_options(request, runtime)

    async def unbind_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.UnbindSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UnbindSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_smart_access_gateway_with_options_async(request, runtime)

    def unbind_vbr_with_options(
        self,
        request: smartag_20180313_models.UnbindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindVbrResponse().from_map(
            self.do_rpcrequest('UnbindVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_vbr_with_options_async(
        self,
        request: smartag_20180313_models.UnbindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnbindVbrResponse().from_map(
            await self.do_rpcrequest_async('UnbindVbr', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_vbr(
        self,
        request: smartag_20180313_models.UnbindVbrRequest,
    ) -> smartag_20180313_models.UnbindVbrResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_vbr_with_options(request, runtime)

    async def unbind_vbr_async(
        self,
        request: smartag_20180313_models.UnbindVbrRequest,
    ) -> smartag_20180313_models.UnbindVbrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_vbr_with_options_async(request, runtime)

    def unicom_order_confirm_with_options(
        self,
        request: smartag_20180313_models.UnicomOrderConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnicomOrderConfirmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnicomOrderConfirmResponse().from_map(
            self.do_rpcrequest('UnicomOrderConfirm', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unicom_order_confirm_with_options_async(
        self,
        request: smartag_20180313_models.UnicomOrderConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnicomOrderConfirmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnicomOrderConfirmResponse().from_map(
            await self.do_rpcrequest_async('UnicomOrderConfirm', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unicom_order_confirm(
        self,
        request: smartag_20180313_models.UnicomOrderConfirmRequest,
    ) -> smartag_20180313_models.UnicomOrderConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return self.unicom_order_confirm_with_options(request, runtime)

    async def unicom_order_confirm_async(
        self,
        request: smartag_20180313_models.UnicomOrderConfirmRequest,
    ) -> smartag_20180313_models.UnicomOrderConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unicom_order_confirm_with_options_async(request, runtime)

    def unicom_sign_confirm_with_options(
        self,
        request: smartag_20180313_models.UnicomSignConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnicomSignConfirmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnicomSignConfirmResponse().from_map(
            self.do_rpcrequest('UnicomSignConfirm', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unicom_sign_confirm_with_options_async(
        self,
        request: smartag_20180313_models.UnicomSignConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnicomSignConfirmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnicomSignConfirmResponse().from_map(
            await self.do_rpcrequest_async('UnicomSignConfirm', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unicom_sign_confirm(
        self,
        request: smartag_20180313_models.UnicomSignConfirmRequest,
    ) -> smartag_20180313_models.UnicomSignConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return self.unicom_sign_confirm_with_options(request, runtime)

    async def unicom_sign_confirm_async(
        self,
        request: smartag_20180313_models.UnicomSignConfirmRequest,
    ) -> smartag_20180313_models.UnicomSignConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unicom_sign_confirm_with_options_async(request, runtime)

    def unlock_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnlockSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('UnlockSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unlock_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UnlockSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('UnlockSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_smart_access_gateway(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_smart_access_gateway_with_options(request, runtime)

    async def unlock_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_smart_access_gateway_with_options_async(request, runtime)

    def update_enterprise_code_with_options(
        self,
        request: smartag_20180313_models.UpdateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateEnterpriseCodeResponse().from_map(
            self.do_rpcrequest('UpdateEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.UpdateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateEnterpriseCodeResponse().from_map(
            await self.do_rpcrequest_async('UpdateEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_enterprise_code(
        self,
        request: smartag_20180313_models.UpdateEnterpriseCodeRequest,
    ) -> smartag_20180313_models.UpdateEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_code_with_options(request, runtime)

    async def update_enterprise_code_async(
        self,
        request: smartag_20180313_models.UpdateEnterpriseCodeRequest,
    ) -> smartag_20180313_models.UpdateEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_enterprise_code_with_options_async(request, runtime)

    def update_smart_access_gateway_version_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse().from_map(
            self.do_rpcrequest('UpdateSmartAccessGatewayVersion', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smart_access_gateway_version_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse().from_map(
            await self.do_rpcrequest_async('UpdateSmartAccessGatewayVersion', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_access_gateway_version(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_version_with_options(request, runtime)

    async def update_smart_access_gateway_version_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_version_with_options_async(request, runtime)

    def update_smart_agaccess_point_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGAccessPointResponse().from_map(
            self.do_rpcrequest('UpdateSmartAGAccessPoint', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smart_agaccess_point_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGAccessPointResponse().from_map(
            await self.do_rpcrequest_async('UpdateSmartAGAccessPoint', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_agaccess_point(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_agaccess_point_with_options(request, runtime)

    async def update_smart_agaccess_point_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_agaccess_point_with_options_async(request, runtime)

    def update_smart_agdpi_attribute_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGDpiAttributeResponse().from_map(
            self.do_rpcrequest('UpdateSmartAGDpiAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smart_agdpi_attribute_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGDpiAttributeResponse().from_map(
            await self.do_rpcrequest_async('UpdateSmartAGDpiAttribute', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_agdpi_attribute(
        self,
        request: smartag_20180313_models.UpdateSmartAGDpiAttributeRequest,
    ) -> smartag_20180313_models.UpdateSmartAGDpiAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_agdpi_attribute_with_options(request, runtime)

    async def update_smart_agdpi_attribute_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGDpiAttributeRequest,
    ) -> smartag_20180313_models.UpdateSmartAGDpiAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_agdpi_attribute_with_options_async(request, runtime)

    def update_smart_agenterprise_code_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAGEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse().from_map(
            self.do_rpcrequest('UpdateSmartAGEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smart_agenterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse().from_map(
            await self.do_rpcrequest_async('UpdateSmartAGEnterpriseCode', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_agenterprise_code(
        self,
        request: smartag_20180313_models.UpdateSmartAGEnterpriseCodeRequest,
    ) -> smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_agenterprise_code_with_options(request, runtime)

    async def update_smart_agenterprise_code_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGEnterpriseCodeRequest,
    ) -> smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_agenterprise_code_with_options_async(request, runtime)

    def upgrade_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpgradeSmartAccessGatewayResponse().from_map(
            self.do_rpcrequest('UpgradeSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpgradeSmartAccessGatewayResponse().from_map(
            await self.do_rpcrequest_async('UpgradeSmartAccessGateway', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_smart_access_gateway(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_smart_access_gateway_with_options(request, runtime)

    async def upgrade_smart_access_gateway_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_smart_access_gateway_with_options_async(request, runtime)

    def upgrade_smart_access_gateway_software_with_options(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse().from_map(
            self.do_rpcrequest('UpgradeSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse().from_map(
            await self.do_rpcrequest_async('UpgradeSmartAccessGatewaySoftware', '2018-03-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_smart_access_gateway_software(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_smart_access_gateway_software_with_options(request, runtime)

    async def upgrade_smart_access_gateway_software_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareRequest,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_smart_access_gateway_software_with_options_async(request, runtime)
