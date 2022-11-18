# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_smartag20180313 import models as smartag_20180313_models
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ActivateSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.ActivateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActivateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ActivateSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ActiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ActiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.AddACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddACLRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddDnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dnat_entry_with_options_async(
        self,
        request: smartag_20180313_models.AddDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddDnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddDnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def add_smart_access_gateway_dns_forward_with_options(
        self,
        request: smartag_20180313_models.AddSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not UtilClient.is_unset(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not UtilClient.is_unset(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: smartag_20180313_models.AddSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not UtilClient.is_unset(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not UtilClient.is_unset(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_smart_access_gateway_dns_forward(
        self,
        request: smartag_20180313_models.AddSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def add_smart_access_gateway_dns_forward_async(
        self,
        request: smartag_20180313_models.AddSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.AddSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def add_snat_entry_with_options(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_snat_entry_with_options_async(
        self,
        request: smartag_20180313_models.AddSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AddSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AddSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_aclwith_options_async(
        self,
        request: smartag_20180313_models.AssociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateACLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.AssociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_qos_with_options_async(
        self,
        request: smartag_20180313_models.AssociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateQosResponse(),
            await self.call_api_async(params, req, runtime)
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

    def associate_smart_agwith_application_bandwidth_package_with_options(
        self,
        request: smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not UtilClient.is_unset(request.associate_configs):
            query['AssociateConfigs'] = request.associate_configs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateSmartAGWithApplicationBandwidthPackage',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_smart_agwith_application_bandwidth_package_with_options_async(
        self,
        request: smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not UtilClient.is_unset(request.associate_configs):
            query['AssociateConfigs'] = request.associate_configs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateSmartAGWithApplicationBandwidthPackage',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_smart_agwith_application_bandwidth_package(
        self,
        request: smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
    ) -> smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_smart_agwith_application_bandwidth_package_with_options(request, runtime)

    async def associate_smart_agwith_application_bandwidth_package_async(
        self,
        request: smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
    ) -> smartag_20180313_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_smart_agwith_application_bandwidth_package_with_options_async(request, runtime)

    def bind_serial_number_with_options(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSerialNumber',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_serial_number_with_options_async(
        self,
        request: smartag_20180313_models.BindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSerialNumber',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.BindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_vbr_with_options_async(
        self,
        request: smartag_20180313_models.BindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.BindVbrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.BindVbrResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn_number):
            query['SnNumber'] = request.sn_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearSagCipher',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ClearSagCipherResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_sag_cipher_with_options_async(
        self,
        request: smartag_20180313_models.ClearSagCipherRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagCipherResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn_number):
            query['SnNumber'] = request.sn_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearSagCipher',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ClearSagCipherResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearSagRouteableAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ClearSagRouteableAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_sag_routeable_address_with_options_async(
        self,
        request: smartag_20180313_models.ClearSagRouteableAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ClearSagRouteableAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearSagRouteableAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ClearSagRouteableAddressResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aclwith_options_async(
        self,
        request: smartag_20180313_models.CreateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateACLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snat_cidr_block):
            query['SnatCidrBlock'] = request.snat_cidr_block
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.CreateCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snat_cidr_block):
            query['SnatCidrBlock'] = request.snat_cidr_block
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.CreateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not UtilClient.is_unset(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not UtilClient.is_unset(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not UtilClient.is_unset(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.CreateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not UtilClient.is_unset(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not UtilClient.is_unset(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not UtilClient.is_unset(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not UtilClient.is_unset(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not UtilClient.is_unset(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not UtilClient.is_unset(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_health_check_with_options_async(
        self,
        request: smartag_20180313_models.CreateHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not UtilClient.is_unset(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not UtilClient.is_unset(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not UtilClient.is_unset(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_probe_task_with_options(
        self,
        request: smartag_20180313_models.CreateProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_probe_task_with_options_async(
        self,
        request: smartag_20180313_models.CreateProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_probe_task(
        self,
        request: smartag_20180313_models.CreateProbeTaskRequest,
    ) -> smartag_20180313_models.CreateProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_probe_task_with_options(request, runtime)

    async def create_probe_task_async(
        self,
        request: smartag_20180313_models.CreateProbeTaskRequest,
    ) -> smartag_20180313_models.CreateProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_probe_task_with_options_async(request, runtime)

    def create_qos_with_options(
        self,
        request: smartag_20180313_models.CreateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.limit_type):
            query['LimitType'] = request.limit_type
        if not UtilClient.is_unset(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not UtilClient.is_unset(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not UtilClient.is_unset(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not UtilClient.is_unset(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosCarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.limit_type):
            query['LimitType'] = request.limit_type
        if not UtilClient.is_unset(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not UtilClient.is_unset(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not UtilClient.is_unset(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not UtilClient.is_unset(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosCarResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.CreateQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.CreateSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.CreateSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSagStaticRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_service_address_with_options(
        self,
        request: smartag_20180313_models.CreateServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_address_with_options_async(
        self,
        request: smartag_20180313_models.CreateServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_address(
        self,
        request: smartag_20180313_models.CreateServiceAddressRequest,
    ) -> smartag_20180313_models.CreateServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_address_with_options(request, runtime)

    async def create_service_address_async(
        self,
        request: smartag_20180313_models.CreateServiceAddressRequest,
    ) -> smartag_20180313_models.CreateServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_address_with_options_async(request, runtime)

    def create_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.already_have_sag):
            query['AlreadyHaveSag'] = request.already_have_sag
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.buyer_message):
            query['BuyerMessage'] = request.buyer_message
        if not UtilClient.is_unset(request.cpeversion):
            query['CPEVersion'] = request.cpeversion
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ha_type):
            query['HaType'] = request.ha_type
        if not UtilClient.is_unset(request.hard_ware_spec):
            query['HardWareSpec'] = request.hard_ware_spec
        if not UtilClient.is_unset(request.max_band_width):
            query['MaxBandWidth'] = request.max_band_width
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.receiver_address):
            query['ReceiverAddress'] = request.receiver_address
        if not UtilClient.is_unset(request.receiver_city):
            query['ReceiverCity'] = request.receiver_city
        if not UtilClient.is_unset(request.receiver_country):
            query['ReceiverCountry'] = request.receiver_country
        if not UtilClient.is_unset(request.receiver_district):
            query['ReceiverDistrict'] = request.receiver_district
        if not UtilClient.is_unset(request.receiver_email):
            query['ReceiverEmail'] = request.receiver_email
        if not UtilClient.is_unset(request.receiver_mobile):
            query['ReceiverMobile'] = request.receiver_mobile
        if not UtilClient.is_unset(request.receiver_name):
            query['ReceiverName'] = request.receiver_name
        if not UtilClient.is_unset(request.receiver_phone):
            query['ReceiverPhone'] = request.receiver_phone
        if not UtilClient.is_unset(request.receiver_state):
            query['ReceiverState'] = request.receiver_state
        if not UtilClient.is_unset(request.receiver_town):
            query['ReceiverTown'] = request.receiver_town
        if not UtilClient.is_unset(request.receiver_zip):
            query['ReceiverZip'] = request.receiver_zip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.already_have_sag):
            query['AlreadyHaveSag'] = request.already_have_sag
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.buyer_message):
            query['BuyerMessage'] = request.buyer_message
        if not UtilClient.is_unset(request.cpeversion):
            query['CPEVersion'] = request.cpeversion
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ha_type):
            query['HaType'] = request.ha_type
        if not UtilClient.is_unset(request.hard_ware_spec):
            query['HardWareSpec'] = request.hard_ware_spec
        if not UtilClient.is_unset(request.max_band_width):
            query['MaxBandWidth'] = request.max_band_width
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.receiver_address):
            query['ReceiverAddress'] = request.receiver_address
        if not UtilClient.is_unset(request.receiver_city):
            query['ReceiverCity'] = request.receiver_city
        if not UtilClient.is_unset(request.receiver_country):
            query['ReceiverCountry'] = request.receiver_country
        if not UtilClient.is_unset(request.receiver_district):
            query['ReceiverDistrict'] = request.receiver_district
        if not UtilClient.is_unset(request.receiver_email):
            query['ReceiverEmail'] = request.receiver_email
        if not UtilClient.is_unset(request.receiver_mobile):
            query['ReceiverMobile'] = request.receiver_mobile
        if not UtilClient.is_unset(request.receiver_name):
            query['ReceiverName'] = request.receiver_name
        if not UtilClient.is_unset(request.receiver_phone):
            query['ReceiverPhone'] = request.receiver_phone
        if not UtilClient.is_unset(request.receiver_state):
            query['ReceiverState'] = request.receiver_state
        if not UtilClient.is_unset(request.receiver_town):
            query['ReceiverTown'] = request.receiver_town
        if not UtilClient.is_unset(request.receiver_zip):
            query['ReceiverZip'] = request.receiver_zip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_mail):
            query['UserMail'] = request.user_mail
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_mail):
            query['UserMail'] = request.user_mail
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.CreateSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.CreateSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeactiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeactiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aclwith_options_async(
        self,
        request: smartag_20180313_models.DeleteACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteACLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acr_id):
            query['AcrId'] = request.acr_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.DeleteACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteACLRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acr_id):
            query['AcrId'] = request.acr_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.DeleteCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dnat_entry_id):
            query['DnatEntryId'] = request.dnat_entry_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteDnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dnat_entry_with_options_async(
        self,
        request: smartag_20180313_models.DeleteDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteDnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dnat_entry_id):
            query['DnatEntryId'] = request.dnat_entry_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteDnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.DeleteEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DeleteFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_health_check_with_options_async(
        self,
        request: smartag_20180313_models.DeleteHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_probe_task_with_options(
        self,
        request: smartag_20180313_models.DeleteProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_probe_task_with_options_async(
        self,
        request: smartag_20180313_models.DeleteProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_probe_task(
        self,
        request: smartag_20180313_models.DeleteProbeTaskRequest,
    ) -> smartag_20180313_models.DeleteProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_probe_task_with_options(request, runtime)

    async def delete_probe_task_async(
        self,
        request: smartag_20180313_models.DeleteProbeTaskRequest,
    ) -> smartag_20180313_models.DeleteProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_probe_task_with_options_async(request, runtime)

    def delete_qos_with_options(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosCarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosCarResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.DeleteQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_source):
            query['RouteSource'] = request.route_source
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteDistributionStrategy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteRouteDistributionStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_distribution_strategy_with_options_async(
        self,
        request: smartag_20180313_models.DeleteRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_source):
            query['RouteSource'] = request.route_source
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteDistributionStrategy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteRouteDistributionStrategyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_sag_express_connect_interface_with_options(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSagStaticRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_service_address_with_options(
        self,
        request: smartag_20180313_models.DeleteServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_address_with_options_async(
        self,
        request: smartag_20180313_models.DeleteServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_address(
        self,
        request: smartag_20180313_models.DeleteServiceAddressRequest,
    ) -> smartag_20180313_models.DeleteServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_address_with_options(request, runtime)

    async def delete_service_address_async(
        self,
        request: smartag_20180313_models.DeleteServiceAddressRequest,
    ) -> smartag_20180313_models.DeleteServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_address_with_options_async(request, runtime)

    def delete_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_smart_access_gateway_dns_forward_with_options(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smart_access_gateway_dns_forward(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def delete_smart_access_gateway_dns_forward_async(
        self,
        request: smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.DeleteSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def delete_snat_entry_with_options(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snat_entry_with_options_async(
        self,
        request: smartag_20180313_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatEntry',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DeleteSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeACLAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aclattribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeACLAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeACLAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeACLsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: smartag_20180313_models.DescribeACLsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeACLsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeACLsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBindableSmartAccessGateways',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bindable_smart_access_gateways_with_options_async(
        self,
        request: smartag_20180313_models.DescribeBindableSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBindableSmartAccessGateways',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeBindableSmartAccessGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientUserDNS',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeClientUserDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_user_dnswith_options_async(
        self,
        request: smartag_20180313_models.DescribeClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeClientUserDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientUserDNS',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeClientUserDNSResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudConnectNetworks',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeCloudConnectNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_connect_networks_with_options_async(
        self,
        request: smartag_20180313_models.DescribeCloudConnectNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeCloudConnectNetworksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudConnectNetworks',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeCloudConnectNetworksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceAutoUpgradePolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_auto_upgrade_policy_with_options_async(
        self,
        request: smartag_20180313_models.DescribeDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceAutoUpgradePolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeDeviceAutoUpgradePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnatEntries',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeDnatEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dnat_entries_with_options_async(
        self,
        request: smartag_20180313_models.DescribeDnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeDnatEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnatEntries',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeDnatEntriesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_log_sags_with_options(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowLogSags',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeFlowLogSagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_log_sags_with_options_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogSagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowLogSags',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeFlowLogSagsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_logs_with_options(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowLogs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeFlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_logs_with_options_async(
        self,
        request: smartag_20180313_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowLogs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeFlowLogsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_grant_rules_with_options(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantSagRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantSagRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_sag_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantSagRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantSagRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantSagVbrRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantSagVbrRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_sag_vbr_rules_with_options_async(
        self,
        request: smartag_20180313_models.DescribeGrantSagVbrRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeGrantSagVbrRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantSagVbrRules',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeGrantSagVbrRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeHealthCheckAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_attribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeHealthCheckAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthCheckAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeHealthCheckAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthChecks',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeHealthChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_checks_with_options_async(
        self,
        request: smartag_20180313_models.DescribeHealthChecksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeHealthChecksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthChecks',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeHealthChecksResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_qos_cars_with_options(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQosCars',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosCarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qos_cars_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosCarsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQosCars',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosCarsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_qos_policies_with_options(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQosPolicies',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qos_policies_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQosPolicies',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_qoses_with_options(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qos_ids):
            query['QosIds'] = request.qos_ids
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoses',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qoses_with_options_async(
        self,
        request: smartag_20180313_models.DescribeQosesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeQosesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qos_ids):
            query['QosIds'] = request.qos_ids
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoses',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeQosesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_regions_with_options(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: smartag_20180313_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteDistributionStrategies',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeRouteDistributionStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_distribution_strategies_with_options_async(
        self,
        request: smartag_20180313_models.DescribeRouteDistributionStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeRouteDistributionStrategiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteDistributionStrategies',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeRouteDistributionStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sagdevice_info_with_options(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSAGDeviceInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSAGDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sagdevice_info_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSAGDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSAGDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSAGDeviceInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSAGDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sag_current_dns_with_options(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagCurrentDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagCurrentDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_current_dns_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagCurrentDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagCurrentDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagCurrentDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagCurrentDnsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sag_drop_top_nwith_options(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagDropTopN',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagDropTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_drop_top_nwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagDropTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagDropTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagDropTopN',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagDropTopNResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sag_express_connect_interface_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagExpressConnectInterfaceList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_express_connect_interface_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagExpressConnectInterfaceList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagExpressConnectInterfaceListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_ha_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagHaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagHaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagLanList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagLanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_lan_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagLanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagLanListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagLanList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagLanListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagManagementPort',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagManagementPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_management_port_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagManagementPortResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagManagementPort',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagManagementPortResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagOnlineClientStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_online_client_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagOnlineClientStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagOnlineClientStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagPortList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagPortListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_port_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagPortListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagPortList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagPortListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagPortRouteProtocolList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagPortRouteProtocolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_port_route_protocol_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagPortRouteProtocolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagPortRouteProtocolListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagPortRouteProtocolList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagPortRouteProtocolListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRemoteAccess',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRemoteAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_remote_access_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRemoteAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRemoteAccess',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRemoteAccessResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sag_route_list_with_options(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteProtocolBgp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteProtocolBgpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_protocol_bgp_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteProtocolBgp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteProtocolBgpResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteProtocolOspf',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteProtocolOspfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_protocol_ospf_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagRouteProtocolOspf',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagRouteProtocolOspfResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagStaticRouteList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagStaticRouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_static_route_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagStaticRouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagStaticRouteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagStaticRouteList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagStaticRouteListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagTrafficTopN',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagTrafficTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_traffic_top_nwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagTrafficTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagTrafficTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagTrafficTopN',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagTrafficTopNResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagUserDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagUserDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_user_dns_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagUserDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagUserDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagUserDnsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_ids):
            query['VbrInstanceIds'] = request.vbr_instance_ids
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagVbrRelations',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagVbrRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_vbr_relations_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagVbrRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagVbrRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_ids):
            query['VbrInstanceIds'] = request.vbr_instance_ids
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagVbrRelations',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagVbrRelationsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWan4G',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWan4GResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_4gwith_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWan4GRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWan4GResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWan4G',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWan4GResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWanList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_list_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWanList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWanListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWifi',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWifiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wifi_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSagWifiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSagWifi',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSagWifiResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_attribute_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_mail):
            query['UserMail'] = request.user_mail
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayClientUsers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_client_users_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_mail):
            query['UserMail'] = request.user_mail
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayClientUsers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayClientUsersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_ha_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayHaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayHaResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_smart_access_gateway_versions_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayVersions',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_versions_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGatewayVersions',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewayVersionsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_smart_access_gateways_with_options(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not UtilClient.is_unset(request.associated_ccn_name):
            query['AssociatedCcnName'] = request.associated_ccn_name
        if not UtilClient.is_unset(request.business_state):
            query['BusinessState'] = request.business_state
        if not UtilClient.is_unset(request.can_associate_qos):
            query['CanAssociateQos'] = request.can_associate_qos
        if not UtilClient.is_unset(request.hardware_type):
            query['HardwareType'] = request.hardware_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        if not UtilClient.is_unset(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unbound_acl_ids):
            query['UnboundAclIds'] = request.unbound_acl_ids
        if not UtilClient.is_unset(request.version_comparator):
            query['VersionComparator'] = request.version_comparator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGateways',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateways_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSmartAccessGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSmartAccessGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not UtilClient.is_unset(request.associated_ccn_name):
            query['AssociatedCcnName'] = request.associated_ccn_name
        if not UtilClient.is_unset(request.business_state):
            query['BusinessState'] = request.business_state
        if not UtilClient.is_unset(request.can_associate_qos):
            query['CanAssociateQos'] = request.can_associate_qos
        if not UtilClient.is_unset(request.hardware_type):
            query['HardwareType'] = request.hardware_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        if not UtilClient.is_unset(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unbound_acl_ids):
            query['UnboundAclIds'] = request.unbound_acl_ids
        if not UtilClient.is_unset(request.version_comparator):
            query['VersionComparator'] = request.version_comparator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartAccessGateways',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSmartAccessGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_snat_entries_with_options(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatEntries',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSnatEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snat_entries_with_options_async(
        self,
        request: smartag_20180313_models.DescribeSnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeSnatEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatEntries',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeSnatEntriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnbindFlowLogSags',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUnbindFlowLogSagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unbind_flow_log_sags_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUnbindFlowLogSagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUnbindFlowLogSagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnbindFlowLogSags',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUnbindFlowLogSagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.statistics_date):
            query['StatisticsDate'] = request.statistics_date
        if not UtilClient.is_unset(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserFlowStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserFlowStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_flow_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserFlowStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserFlowStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.statistics_date):
            query['StatisticsDate'] = request.statistics_date
        if not UtilClient.is_unset(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserFlowStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserFlowStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_user_online_client_statistics_with_options(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserOnlineClientStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_online_client_statistics_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserOnlineClientStatistics',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserOnlineClientStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_user_online_clients_with_options(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserOnlineClients',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserOnlineClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_online_clients_with_options_async(
        self,
        request: smartag_20180313_models.DescribeUserOnlineClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DescribeUserOnlineClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserOnlineClients',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DescribeUserOnlineClientsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def diagnose_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiagnoseSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DiagnoseSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def diagnose_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DiagnoseSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiagnoseSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiagnoseSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DiagnoseSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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

    def disable_smart_agdpi_monitor_with_options(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmartAGDpiMonitor',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisableSmartAGDpiMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smart_agdpi_monitor_with_options_async(
        self,
        request: smartag_20180313_models.DisableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmartAGDpiMonitor',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisableSmartAGDpiMonitorResponse(),
            await self.call_api_async(params, req, runtime)
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

    def disable_smart_access_gateway_user_with_options(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmartAccessGatewayUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisableSmartAccessGatewayUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smart_access_gateway_user_with_options_async(
        self,
        request: smartag_20180313_models.DisableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmartAccessGatewayUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisableSmartAccessGatewayUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def disassociate_aclwith_options(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_aclwith_options_async(
        self,
        request: smartag_20180313_models.DisassociateACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateACLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_flow_log_with_options_async(
        self,
        request: smartag_20180313_models.DisassociateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateFlowLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_qos_with_options_async(
        self,
        request: smartag_20180313_models.DisassociateQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DisassociateQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DisassociateQosResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiscribeSmartAccessGatewayDiagnosisReport',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def discribe_smart_access_gateway_diagnosis_report_with_options_async(
        self,
        request: smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DiscribeSmartAccessGatewayDiagnosisReport',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DiscribeSmartAccessGatewayDiagnosisReportResponse(),
            await self.call_api_async(params, req, runtime)
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

    def dissociate_smart_agfrom_application_bandwidth_package_with_options(
        self,
        request: smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agid_list):
            query['SmartAGIdList'] = request.smart_agid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateSmartAGFromApplicationBandwidthPackage',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_smart_agfrom_application_bandwidth_package_with_options_async(
        self,
        request: smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agid_list):
            query['SmartAGIdList'] = request.smart_agid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateSmartAGFromApplicationBandwidthPackage',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_smart_agfrom_application_bandwidth_package(
        self,
        request: smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
    ) -> smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_smart_agfrom_application_bandwidth_package_with_options(request, runtime)

    async def dissociate_smart_agfrom_application_bandwidth_package_async(
        self,
        request: smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
    ) -> smartag_20180313_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_smart_agfrom_application_bandwidth_package_with_options_async(request, runtime)

    def downgrade_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DowngradeSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DowngradeSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.DowngradeSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
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

    def enable_smart_agdpi_monitor_with_options(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmartAGDpiMonitor',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.EnableSmartAGDpiMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smart_agdpi_monitor_with_options_async(
        self,
        request: smartag_20180313_models.EnableSmartAGDpiMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAGDpiMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmartAGDpiMonitor',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.EnableSmartAGDpiMonitorResponse(),
            await self.call_api_async(params, req, runtime)
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

    def enable_smart_access_gateway_user_with_options(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmartAccessGatewayUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.EnableSmartAccessGatewayUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smart_access_gateway_user_with_options_async(
        self,
        request: smartag_20180313_models.EnableSmartAccessGatewayUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.EnableSmartAccessGatewayUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmartAccessGatewayUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.EnableSmartAccessGatewayUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_acl_attribute_with_options(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAclAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acl_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAclAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAclAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetAclAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_advanced_monitor_state_with_options(
        self,
        request: smartag_20180313_models.GetAdvancedMonitorStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAdvancedMonitorStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvancedMonitorState',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetAdvancedMonitorStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_monitor_state_with_options_async(
        self,
        request: smartag_20180313_models.GetAdvancedMonitorStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetAdvancedMonitorStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvancedMonitorState',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetAdvancedMonitorStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_monitor_state(
        self,
        request: smartag_20180313_models.GetAdvancedMonitorStateRequest,
    ) -> smartag_20180313_models.GetAdvancedMonitorStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_advanced_monitor_state_with_options(request, runtime)

    async def get_advanced_monitor_state_async(
        self,
        request: smartag_20180313_models.GetAdvancedMonitorStateRequest,
    ) -> smartag_20180313_models.GetAdvancedMonitorStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_advanced_monitor_state_with_options_async(request, runtime)

    def get_cloud_connect_network_use_limit_with_options(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudConnectNetworkUseLimit',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_connect_network_use_limit_with_options_async(
        self,
        request: smartag_20180313_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudConnectNetworkUseLimit',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetCloudConnectNetworkUseLimitResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetQosAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qos_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetQosAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetQosAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetQosAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_smart_agdpi_attribute_with_options(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartAGDpiAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetSmartAGDpiAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_agdpi_attribute_with_options_async(
        self,
        request: smartag_20180313_models.GetSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartAGDpiAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetSmartAGDpiAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_smart_access_gateway_use_limit_with_options(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartAccessGatewayUseLimit',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_access_gateway_use_limit_with_options_async(
        self,
        request: smartag_20180313_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartAccessGatewayUseLimit',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GetSmartAccessGatewayUseLimitResponse(),
            await self.call_api_async(params, req, runtime)
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

    def grant_instance_to_cbn_with_options(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not UtilClient.is_unset(request.cen_uid):
            query['CenUid'] = request.cen_uid
        if not UtilClient.is_unset(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantInstanceToCbn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantInstanceToCbnResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_instance_to_cbn_with_options_async(
        self,
        request: smartag_20180313_models.GrantInstanceToCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantInstanceToCbnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not UtilClient.is_unset(request.cen_uid):
            query['CenUid'] = request.cen_uid
        if not UtilClient.is_unset(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantInstanceToCbn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantInstanceToCbnResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.ccn_uid):
            query['CcnUid'] = request.ccn_uid
        if not UtilClient.is_unset(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantSagInstanceToCcn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantSagInstanceToCcnResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_sag_instance_to_ccn_with_options_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToCcnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.ccn_uid):
            query['CcnUid'] = request.ccn_uid
        if not UtilClient.is_unset(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantSagInstanceToCcn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantSagInstanceToCcnResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        if not UtilClient.is_unset(request.vbr_uid):
            query['VbrUid'] = request.vbr_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantSagInstanceToVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantSagInstanceToVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_sag_instance_to_vbr_with_options_async(
        self,
        request: smartag_20180313_models.GrantSagInstanceToVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.GrantSagInstanceToVbrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        if not UtilClient.is_unset(request.vbr_uid):
            query['VbrUid'] = request.vbr_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantSagInstanceToVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.GrantSagInstanceToVbrResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickOutClients',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.KickOutClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_out_clients_with_options_async(
        self,
        request: smartag_20180313_models.KickOutClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.KickOutClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickOutClients',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.KickOutClientsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_access_point_network_qualities_with_options(
        self,
        request: smartag_20180313_models.ListAccessPointNetworkQualitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointNetworkQualitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessPointNetworkQualities',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAccessPointNetworkQualitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_point_network_qualities_with_options_async(
        self,
        request: smartag_20180313_models.ListAccessPointNetworkQualitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointNetworkQualitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessPointNetworkQualities',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAccessPointNetworkQualitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_point_network_qualities(
        self,
        request: smartag_20180313_models.ListAccessPointNetworkQualitiesRequest,
    ) -> smartag_20180313_models.ListAccessPointNetworkQualitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_point_network_qualities_with_options(request, runtime)

    async def list_access_point_network_qualities_async(
        self,
        request: smartag_20180313_models.ListAccessPointNetworkQualitiesRequest,
    ) -> smartag_20180313_models.ListAccessPointNetworkQualitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_point_network_qualities_with_options_async(request, runtime)

    def list_access_points_with_options(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessPoints',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_points_with_options_async(
        self,
        request: smartag_20180313_models.ListAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAccessPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessPoints',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_available_service_address_with_options(
        self,
        request: smartag_20180313_models.ListAvailableServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAvailableServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAvailableServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_service_address_with_options_async(
        self,
        request: smartag_20180313_models.ListAvailableServiceAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListAvailableServiceAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableServiceAddress',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListAvailableServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_service_address(
        self,
        request: smartag_20180313_models.ListAvailableServiceAddressRequest,
    ) -> smartag_20180313_models.ListAvailableServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_available_service_address_with_options(request, runtime)

    async def list_available_service_address_async(
        self,
        request: smartag_20180313_models.ListAvailableServiceAddressRequest,
    ) -> smartag_20180313_models.ListAvailableServiceAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_available_service_address_with_options_async(request, runtime)

    def list_dpi_config_error_with_options(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dpi_config_type):
            query['DpiConfigType'] = request.dpi_config_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_instance_id):
            query['RuleInstanceId'] = request.rule_instance_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiConfigError',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiConfigErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_config_error_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiConfigErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiConfigErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dpi_config_type):
            query['DpiConfigType'] = request.dpi_config_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_instance_id):
            query['RuleInstanceId'] = request.rule_instance_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiConfigError',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiConfigErrorResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_group_names):
            query['DpiGroupNames'] = request.dpi_group_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiGroups',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_groups_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_group_names):
            query['DpiGroupNames'] = request.dpi_group_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiGroups',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dpi_group_id):
            query['DpiGroupId'] = request.dpi_group_id
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.dpi_signature_names):
            query['DpiSignatureNames'] = request.dpi_signature_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiSignatures',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_signatures_with_options_async(
        self,
        request: smartag_20180313_models.ListDpiSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListDpiSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dpi_group_id):
            query['DpiGroupId'] = request.dpi_group_id
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.dpi_signature_names):
            query['DpiSignatureNames'] = request.dpi_signature_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDpiSignatures',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListDpiSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.ListEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_probe_task_with_options(
        self,
        request: smartag_20180313_models.ListProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sag_name):
            query['SagName'] = request.sag_name
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_probe_task_with_options_async(
        self,
        request: smartag_20180313_models.ListProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sag_name):
            query['SagName'] = request.sag_name
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_probe_task(
        self,
        request: smartag_20180313_models.ListProbeTaskRequest,
    ) -> smartag_20180313_models.ListProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_probe_task_with_options(request, runtime)

    async def list_probe_task_async(
        self,
        request: smartag_20180313_models.ListProbeTaskRequest,
    ) -> smartag_20180313_models.ListProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_probe_task_with_options_async(request, runtime)

    def list_smart_agapi_unsupported_feature_with_options(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_api_name):
            query['OpenApiName'] = request.open_api_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartAGApiUnsupportedFeature',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_smart_agapi_unsupported_feature_with_options_async(
        self,
        request: smartag_20180313_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_api_name):
            query['OpenApiName'] = request.open_api_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartAGApiUnsupportedFeature',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListSmartAGApiUnsupportedFeatureResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agstatus):
            query['SmartAGStatus'] = request.smart_agstatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartAGByAccessPoint',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListSmartAGByAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_smart_agby_access_point_with_options_async(
        self,
        request: smartag_20180313_models.ListSmartAGByAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ListSmartAGByAccessPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agstatus):
            query['SmartAGStatus'] = request.smart_agstatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartAGByAccessPoint',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ListSmartAGByAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aclwith_options_async(
        self,
        request: smartag_20180313_models.ModifyACLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyACL',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyACLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acr_id):
            query['AcrId'] = request.acr_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aclrule_with_options_async(
        self,
        request: smartag_20180313_models.ModifyACLRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyACLRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acr_id):
            query['AcrId'] = request.acr_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyACLRule',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.app_dns):
            query['AppDNS'] = request.app_dns
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recovered_dns):
            query['RecoveredDNS'] = request.recovered_dns
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClientUserDNS',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyClientUserDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_client_user_dnswith_options_async(
        self,
        request: smartag_20180313_models.ModifyClientUserDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyClientUserDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_dns):
            query['AppDNS'] = request.app_dns
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recovered_dns):
            query['RecoveredDNS'] = request.recovered_dns
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClientUserDNS',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyClientUserDNSResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.interworking_status):
            query['InterworkingStatus'] = request.interworking_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_connect_network_with_options_async(
        self,
        request: smartag_20180313_models.ModifyCloudConnectNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyCloudConnectNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.interworking_status):
            query['InterworkingStatus'] = request.interworking_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudConnectNetwork',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceAutoUpgradePolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_auto_upgrade_policy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyDeviceAutoUpgradePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceAutoUpgradePolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyDeviceAutoUpgradePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not UtilClient.is_unset(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not UtilClient.is_unset(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not UtilClient.is_unset(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowLogAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: smartag_20180313_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not UtilClient.is_unset(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not UtilClient.is_unset(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not UtilClient.is_unset(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowLogAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyFlowLogAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not UtilClient.is_unset(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not UtilClient.is_unset(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not UtilClient.is_unset(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_health_check_with_options_async(
        self,
        request: smartag_20180313_models.ModifyHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not UtilClient.is_unset(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not UtilClient.is_unset(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not UtilClient.is_unset(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheck',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_qos_with_options(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_name):
            query['QosName'] = request.qos_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQos',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.limit_type):
            query['LimitType'] = request.limit_type
        if not UtilClient.is_unset(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not UtilClient.is_unset(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not UtilClient.is_unset(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not UtilClient.is_unset(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_car_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosCarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosCarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.limit_type):
            query['LimitType'] = request.limit_type
        if not UtilClient.is_unset(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not UtilClient.is_unset(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not UtilClient.is_unset(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not UtilClient.is_unset(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQosCar',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosCarResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_policy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not UtilClient.is_unset(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not UtilClient.is_unset(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not UtilClient.is_unset(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.qos_id):
            query['QosId'] = request.qos_id
        if not UtilClient.is_unset(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQosPolicy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_distribution):
            query['RouteDistribution'] = request.route_distribution
        if not UtilClient.is_unset(request.route_source):
            query['RouteSource'] = request.route_source
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRouteDistributionStrategy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyRouteDistributionStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_route_distribution_strategy_with_options_async(
        self,
        request: smartag_20180313_models.ModifyRouteDistributionStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifyRouteDistributionStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not UtilClient.is_unset(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_distribution):
            query['RouteDistribution'] = request.route_distribution
        if not UtilClient.is_unset(request.route_source):
            query['RouteSource'] = request.route_source
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRouteDistributionStrategy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifyRouteDistributionStrategyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_sagadmin_password_with_options(
        self,
        request: smartag_20180313_models.ModifySAGAdminPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySAGAdminPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySAGAdminPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySAGAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sagadmin_password_with_options_async(
        self,
        request: smartag_20180313_models.ModifySAGAdminPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySAGAdminPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySAGAdminPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySAGAdminPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sagadmin_password(
        self,
        request: smartag_20180313_models.ModifySAGAdminPasswordRequest,
    ) -> smartag_20180313_models.ModifySAGAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sagadmin_password_with_options(request, runtime)

    async def modify_sagadmin_password_async(
        self,
        request: smartag_20180313_models.ModifySAGAdminPasswordRequest,
    ) -> smartag_20180313_models.ModifySAGAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sagadmin_password_with_options_async(request, runtime)

    def modify_sag_express_connect_interface_with_options(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_express_connect_interface_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagExpressConnectInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagExpressConnectInterfaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagExpressConnectInterface',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.virtual_ip):
            query['VirtualIp'] = request.virtual_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_ha_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagHaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.virtual_ip):
            query['VirtualIp'] = request.virtual_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagHa',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagHaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.end_ip):
            query['EndIp'] = request.end_ip
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.lease):
            query['Lease'] = request.lease
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.start_ip):
            query['StartIp'] = request.start_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagLan',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagLanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_lan_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagLanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagLanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ip):
            query['EndIp'] = request.end_ip
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.lease):
            query['Lease'] = request.lease
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.start_ip):
            query['StartIp'] = request.start_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagLan',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagLanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagManagementPort',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagManagementPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_management_port_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagManagementPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagManagementPortResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagManagementPort',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagManagementPortResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagPortRole',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagPortRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_port_role_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagPortRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagPortRole',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagPortRoleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_port_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remote_access_ip):
            query['RemoteAccessIp'] = request.remote_access_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRemoteAccess',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRemoteAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_remote_access_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRemoteAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRemoteAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remote_access_ip):
            query['RemoteAccessIp'] = request.remote_access_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRemoteAccess',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRemoteAccessResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.local_as):
            query['LocalAs'] = request.local_as
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRouteProtocolBgp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRouteProtocolBgpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_route_protocol_bgp_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolBgpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolBgpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.local_as):
            query['LocalAs'] = request.local_as
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRouteProtocolBgp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRouteProtocolBgpResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.area_id):
            query['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not UtilClient.is_unset(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not UtilClient.is_unset(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not UtilClient.is_unset(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRouteProtocolOspf',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRouteProtocolOspfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_route_protocol_ospf_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagRouteProtocolOspfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagRouteProtocolOspfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area_id):
            query['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not UtilClient.is_unset(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not UtilClient.is_unset(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not UtilClient.is_unset(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagRouteProtocolOspf',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagRouteProtocolOspfResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_static_route_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagStaticRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagStaticRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagStaticRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagUserDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagUserDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_user_dns_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagUserDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagUserDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagUserDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagUserDnsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWan',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wan_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.mask):
            query['Mask'] = request.mask
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWan',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.snat):
            query['Snat'] = request.snat
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not UtilClient.is_unset(request.snat):
            query['Snat'] = request.snat
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.is_auth):
            query['IsAuth'] = request.is_auth
        if not UtilClient.is_unset(request.is_broadcast):
            query['IsBroadcast'] = request.is_broadcast
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ssid):
            query['SSID'] = request.ssid
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWifi',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWifiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wifi_with_options_async(
        self,
        request: smartag_20180313_models.ModifySagWifiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySagWifiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.is_auth):
            query['IsAuth'] = request.is_auth
        if not UtilClient.is_unset(request.is_broadcast):
            query['IsBroadcast'] = request.is_broadcast
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ssid):
            query['SSID'] = request.ssid
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySagWifi',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySagWifiResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_software_connection_audit):
            query['EnableSoftwareConnectionAudit'] = request.enable_software_connection_audit
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.position):
            query['Position'] = request.position
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.routing_strategy):
            query['RoutingStrategy'] = request.routing_strategy
        if not UtilClient.is_unset(request.security_lock_threshold):
            query['SecurityLockThreshold'] = request.security_lock_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_software_connection_audit):
            query['EnableSoftwareConnectionAudit'] = request.enable_software_connection_audit
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.position):
            query['Position'] = request.position
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.routing_strategy):
            query['RoutingStrategy'] = request.routing_strategy
        if not UtilClient.is_unset(request.security_lock_threshold):
            query['SecurityLockThreshold'] = request.security_lock_threshold
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_client_user_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGatewayClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.up_bandwidth_4g):
            query['UpBandwidth4G'] = request.up_bandwidth_4g
        if not UtilClient.is_unset(request.up_bandwidth_wan):
            query['UpBandwidthWan'] = request.up_bandwidth_wan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGatewayUpBandwidth',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_up_bandwidth_with_options_async(
        self,
        request: smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.up_bandwidth_4g):
            query['UpBandwidth4G'] = request.up_bandwidth_4g
        if not UtilClient.is_unset(request.up_bandwidth_wan):
            query['UpBandwidthWan'] = request.up_bandwidth_wan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmartAccessGatewayUpBandwidth',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ModifySmartAccessGatewayUpBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: smartag_20180313_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def probe_access_point_network_quality_with_options(
        self,
        request: smartag_20180313_models.ProbeAccessPointNetworkQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ProbeAccessPointNetworkQualityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_ids):
            query['AccessPointIds'] = request.access_point_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProbeAccessPointNetworkQuality',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ProbeAccessPointNetworkQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def probe_access_point_network_quality_with_options_async(
        self,
        request: smartag_20180313_models.ProbeAccessPointNetworkQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ProbeAccessPointNetworkQualityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_ids):
            query['AccessPointIds'] = request.access_point_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProbeAccessPointNetworkQuality',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ProbeAccessPointNetworkQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def probe_access_point_network_quality(
        self,
        request: smartag_20180313_models.ProbeAccessPointNetworkQualityRequest,
    ) -> smartag_20180313_models.ProbeAccessPointNetworkQualityResponse:
        runtime = util_models.RuntimeOptions()
        return self.probe_access_point_network_quality_with_options(request, runtime)

    async def probe_access_point_network_quality_async(
        self,
        request: smartag_20180313_models.ProbeAccessPointNetworkQualityRequest,
    ) -> smartag_20180313_models.ProbeAccessPointNetworkQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.probe_access_point_network_quality_with_options_async(request, runtime)

    def reboot_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RebootSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.RebootSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RebootSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RebootSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSmartAccessGatewayClientUserPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_smart_access_gateway_client_user_password_with_options_async(
        self,
        request: smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSmartAccessGatewayClientUserPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ResetSmartAccessGatewayClientUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromCbn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeInstanceFromCbnResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_cbn_with_options_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromCbnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromCbnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromCbn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeInstanceFromCbnResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeInstanceFromVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_vbr_with_options_async(
        self,
        request: smartag_20180313_models.RevokeInstanceFromVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeInstanceFromVbrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeInstanceFromVbrResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSagInstanceFromCcn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeSagInstanceFromCcnResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_sag_instance_from_ccn_with_options_async(
        self,
        request: smartag_20180313_models.RevokeSagInstanceFromCcnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RevokeSagInstanceFromCcnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSagInstanceFromCcn',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RevokeSagInstanceFromCcnResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.origin_region_id):
            query['OriginRegionId'] = request.origin_region_id
        if not UtilClient.is_unset(request.origin_smart_agid):
            query['OriginSmartAGId'] = request.origin_smart_agid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_smart_agid):
            query['TargetSmartAGId'] = request.target_smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoamClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RoamClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def roam_client_user_with_options_async(
        self,
        request: smartag_20180313_models.RoamClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.RoamClientUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.origin_region_id):
            query['OriginRegionId'] = request.origin_region_id
        if not UtilClient.is_unset(request.origin_smart_agid):
            query['OriginSmartAGId'] = request.origin_smart_agid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_smart_agid):
            query['TargetSmartAGId'] = request.target_smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoamClientUser',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.RoamClientUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_advanced_monitor_state_with_options(
        self,
        request: smartag_20180313_models.SetAdvancedMonitorStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SetAdvancedMonitorStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAdvancedMonitorState',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.SetAdvancedMonitorStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_advanced_monitor_state_with_options_async(
        self,
        request: smartag_20180313_models.SetAdvancedMonitorStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SetAdvancedMonitorStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAdvancedMonitorState',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.SetAdvancedMonitorStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_advanced_monitor_state(
        self,
        request: smartag_20180313_models.SetAdvancedMonitorStateRequest,
    ) -> smartag_20180313_models.SetAdvancedMonitorStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_advanced_monitor_state_with_options(request, runtime)

    async def set_advanced_monitor_state_async(
        self,
        request: smartag_20180313_models.SetAdvancedMonitorStateRequest,
    ) -> smartag_20180313_models.SetAdvancedMonitorStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_advanced_monitor_state_with_options_async(request, runtime)

    def synchronize_smart_agweb_config_with_options(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeSmartAGWebConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.SynchronizeSmartAGWebConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_smart_agweb_config_with_options_async(
        self,
        request: smartag_20180313_models.SynchronizeSmartAGWebConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.SynchronizeSmartAGWebConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeSmartAGWebConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.SynchronizeSmartAGWebConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSerialNumber',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_serial_number_with_options_async(
        self,
        request: smartag_20180313_models.UnbindSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSerialNumber',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UnbindSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_vbr_with_options_async(
        self,
        request: smartag_20180313_models.UnbindVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnbindVbrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindVbr',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnbindVbrResponse(),
            await self.call_api_async(params, req, runtime)
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

    def unlock_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnlockSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UnlockSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UnlockSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UnlockSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.UpdateEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_probe_task_with_options(
        self,
        request: smartag_20180313_models.UpdateProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_probe_task_with_options_async(
        self,
        request: smartag_20180313_models.UpdateProbeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateProbeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not UtilClient.is_unset(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_id):
            query['SagId'] = request.sag_id
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProbeTask',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_probe_task(
        self,
        request: smartag_20180313_models.UpdateProbeTaskRequest,
    ) -> smartag_20180313_models.UpdateProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_probe_task_with_options(request, runtime)

    async def update_probe_task_async(
        self,
        request: smartag_20180313_models.UpdateProbeTaskRequest,
    ) -> smartag_20180313_models.UpdateProbeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_probe_task_with_options_async(request, runtime)

    def update_smart_agaccess_point_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGAccessPoint',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agaccess_point_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGAccessPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGAccessPoint',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dpi_enabled):
            query['DpiEnabled'] = request.dpi_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGDpiAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGDpiAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agdpi_attribute_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGDpiAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGDpiAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dpi_enabled):
            query['DpiEnabled'] = request.dpi_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGDpiAttribute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGDpiAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agenterprise_code_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGEnterpriseCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGEnterpriseCode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_smart_aguser_accelerate_config_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAGUserAccelerateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGUserAccelerateConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_aguser_accelerate_config_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGUserAccelerateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAGUserAccelerateConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_aguser_accelerate_config(
        self,
        request: smartag_20180313_models.UpdateSmartAGUserAccelerateConfigRequest,
    ) -> smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_aguser_accelerate_config_with_options(request, runtime)

    async def update_smart_aguser_accelerate_config_async(
        self,
        request: smartag_20180313_models.UpdateSmartAGUserAccelerateConfigRequest,
    ) -> smartag_20180313_models.UpdateSmartAGUserAccelerateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_aguser_accelerate_config_with_options_async(request, runtime)

    def update_smart_access_gateway_admin_password_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayAdminPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_admin_password_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayAdminPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_admin_password(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_admin_password_with_options(request, runtime)

    async def update_smart_access_gateway_admin_password_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_admin_password_with_options_async(request, runtime)

    def update_smart_access_gateway_bgp_route_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.local_as):
            query['LocalAs'] = request.local_as
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayBgpRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_bgp_route_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.local_as):
            query['LocalAs'] = request.local_as
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayBgpRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_bgp_route(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_bgp_route_with_options(request, runtime)

    async def update_smart_access_gateway_bgp_route_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayBgpRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_bgp_route_with_options_async(request, runtime)

    def update_smart_access_gateway_dns_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_dns_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_dns(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_dns_with_options(request, runtime)

    async def update_smart_access_gateway_dns_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_dns_with_options_async(request, runtime)

    def update_smart_access_gateway_dns_forward_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not UtilClient.is_unset(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not UtilClient.is_unset(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not UtilClient.is_unset(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not UtilClient.is_unset(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayDnsForward',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_dns_forward(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def update_smart_access_gateway_dns_forward_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayDnsForwardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def update_smart_access_gateway_global_route_protocol_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_global_route_protocol(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_global_route_protocol_with_options(request, runtime)

    async def update_smart_access_gateway_global_route_protocol_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_global_route_protocol_with_options_async(request, runtime)

    def update_smart_access_gateway_ospf_route_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area_id):
            query['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not UtilClient.is_unset(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not UtilClient.is_unset(request.interface_name):
            query['InterfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not UtilClient.is_unset(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not UtilClient.is_unset(request.networks):
            query['Networks'] = request.networks
        if not UtilClient.is_unset(request.ospf_cost):
            query['OspfCost'] = request.ospf_cost
        if not UtilClient.is_unset(request.ospf_network_type):
            query['OspfNetworkType'] = request.ospf_network_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.redistribute_protocol):
            query['RedistributeProtocol'] = request.redistribute_protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayOspfRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_ospf_route_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area_id):
            query['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not UtilClient.is_unset(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not UtilClient.is_unset(request.interface_name):
            query['InterfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not UtilClient.is_unset(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not UtilClient.is_unset(request.networks):
            query['Networks'] = request.networks
        if not UtilClient.is_unset(request.ospf_cost):
            query['OspfCost'] = request.ospf_cost
        if not UtilClient.is_unset(request.ospf_network_type):
            query['OspfNetworkType'] = request.ospf_network_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.redistribute_protocol):
            query['RedistributeProtocol'] = request.redistribute_protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayOspfRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_ospf_route(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_ospf_route_with_options(request, runtime)

    async def update_smart_access_gateway_ospf_route_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayOspfRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_ospf_route_with_options_async(request, runtime)

    def update_smart_access_gateway_port_route_protocol_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_port_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.port_name):
            query['PortName'] = request.port_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_port_route_protocol(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_port_route_protocol_with_options(request, runtime)

    async def update_smart_access_gateway_port_route_protocol_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_port_route_protocol_with_options_async(request, runtime)

    def update_smart_access_gateway_version_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayVersion',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_version_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayVersion',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayVersionResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_smart_access_gateway_wan_snat_with_options(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.snat):
            query['Snat'] = request.snat
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not UtilClient.is_unset(request.snat):
            query['Snat'] = request.snat
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartAccessGatewayWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_wan_snat(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayWanSnatRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_access_gateway_wan_snat_with_options(request, runtime)

    async def update_smart_access_gateway_wan_snat_async(
        self,
        request: smartag_20180313_models.UpdateSmartAccessGatewayWanSnatRequest,
    ) -> smartag_20180313_models.UpdateSmartAccessGatewayWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_access_gateway_wan_snat_with_options_async(request, runtime)

    def upgrade_smart_access_gateway_with_options(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpgradeSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_smart_access_gateway_with_options_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSmartAccessGateway',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpgradeSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_smart_access_gateway_software_with_options_async(
        self,
        request: smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not UtilClient.is_unset(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSmartAccessGatewaySoftware',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.UpgradeSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
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

    def view_smart_access_gateway_bgp_route_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayBgpRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayBgpRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_bgp_route_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayBgpRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayBgpRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_bgp_route(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayBgpRouteRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_bgp_route_with_options(request, runtime)

    async def view_smart_access_gateway_bgp_route_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayBgpRouteRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayBgpRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_bgp_route_with_options_async(request, runtime)

    def view_smart_access_gateway_dns_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_dns_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayDns',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_dns(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_dns_with_options(request, runtime)

    async def view_smart_access_gateway_dns_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_dns_with_options_async(request, runtime)

    def view_smart_access_gateway_dns_forwards_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayDnsForwards',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_dns_forwards_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayDnsForwards',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_dns_forwards(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_dns_forwards_with_options(request, runtime)

    async def view_smart_access_gateway_dns_forwards_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayDnsForwardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_dns_forwards_with_options_async(request, runtime)

    def view_smart_access_gateway_global_route_protocol_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_global_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayGlobalRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_global_route_protocol(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_global_route_protocol_with_options(request, runtime)

    async def view_smart_access_gateway_global_route_protocol_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_global_route_protocol_with_options_async(request, runtime)

    def view_smart_access_gateway_ospf_route_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayOspfRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayOspfRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_ospf_route_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayOspfRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayOspfRoute',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_ospf_route(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayOspfRouteRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_ospf_route_with_options(request, runtime)

    async def view_smart_access_gateway_ospf_route_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayOspfRouteRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayOspfRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_ospf_route_with_options_async(request, runtime)

    def view_smart_access_gateway_port_route_protocol_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_port_route_protocol_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayPortRouteProtocol',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_port_route_protocol(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_port_route_protocol_with_options(request, runtime)

    async def view_smart_access_gateway_port_route_protocol_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_port_route_protocol_with_options_async(request, runtime)

    def view_smart_access_gateway_routes_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayRoutes',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_routes_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayRoutes',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_routes(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayRoutesRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_routes_with_options(request, runtime)

    async def view_smart_access_gateway_routes_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayRoutesRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_routes_with_options_async(request, runtime)

    def view_smart_access_gateway_wan_snat_with_options(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_wan_snat_with_options_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayWanSnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not UtilClient.is_unset(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ViewSmartAccessGatewayWanSnat',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_wan_snat(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayWanSnatRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return self.view_smart_access_gateway_wan_snat_with_options(request, runtime)

    async def view_smart_access_gateway_wan_snat_async(
        self,
        request: smartag_20180313_models.ViewSmartAccessGatewayWanSnatRequest,
    ) -> smartag_20180313_models.ViewSmartAccessGatewayWanSnatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.view_smart_access_gateway_wan_snat_with_options_async(request, runtime)
