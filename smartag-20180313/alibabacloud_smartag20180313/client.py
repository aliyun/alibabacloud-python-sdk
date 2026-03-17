# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_smartag20180313 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_smart_access_gateway_with_options(
        self,
        request: main_models.ActivateSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_smart_access_gateway_with_options_async(
        self,
        request: main_models.ActivateSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_smart_access_gateway(
        self,
        request: main_models.ActivateSmartAccessGatewayRequest,
    ) -> main_models.ActivateSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.activate_smart_access_gateway_with_options(request, runtime)

    async def activate_smart_access_gateway_async(
        self,
        request: main_models.ActivateSmartAccessGatewayRequest,
    ) -> main_models.ActivateSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.activate_smart_access_gateway_with_options_async(request, runtime)

    def active_flow_log_with_options(
        self,
        request: main_models.ActiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: main_models.ActiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_flow_log(
        self,
        request: main_models.ActiveFlowLogRequest,
    ) -> main_models.ActiveFlowLogResponse:
        runtime = RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: main_models.ActiveFlowLogRequest,
    ) -> main_models.ActiveFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def add_aclrule_with_options(
        self,
        request: main_models.AddACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_aclrule_with_options_async(
        self,
        request: main_models.AddACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_aclrule(
        self,
        request: main_models.AddACLRuleRequest,
    ) -> main_models.AddACLRuleResponse:
        runtime = RuntimeOptions()
        return self.add_aclrule_with_options(request, runtime)

    async def add_aclrule_async(
        self,
        request: main_models.AddACLRuleRequest,
    ) -> main_models.AddACLRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_aclrule_with_options_async(request, runtime)

    def add_dnat_entry_with_options(
        self,
        request: main_models.AddDnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not DaraCore.is_null(request.external_port):
            query['ExternalPort'] = request.external_port
        if not DaraCore.is_null(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not DaraCore.is_null(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dnat_entry_with_options_async(
        self,
        request: main_models.AddDnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not DaraCore.is_null(request.external_port):
            query['ExternalPort'] = request.external_port
        if not DaraCore.is_null(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not DaraCore.is_null(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dnat_entry(
        self,
        request: main_models.AddDnatEntryRequest,
    ) -> main_models.AddDnatEntryResponse:
        runtime = RuntimeOptions()
        return self.add_dnat_entry_with_options(request, runtime)

    async def add_dnat_entry_async(
        self,
        request: main_models.AddDnatEntryRequest,
    ) -> main_models.AddDnatEntryResponse:
        runtime = RuntimeOptions()
        return await self.add_dnat_entry_with_options_async(request, runtime)

    def add_smart_access_gateway_dns_forward_with_options(
        self,
        request: main_models.AddSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not DaraCore.is_null(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not DaraCore.is_null(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: main_models.AddSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not DaraCore.is_null(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not DaraCore.is_null(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_smart_access_gateway_dns_forward(
        self,
        request: main_models.AddSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.AddSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return self.add_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def add_smart_access_gateway_dns_forward_async(
        self,
        request: main_models.AddSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.AddSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return await self.add_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def add_snat_entry_with_options(
        self,
        request: main_models.AddSnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_snat_entry_with_options_async(
        self,
        request: main_models.AddSnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_snat_entry(
        self,
        request: main_models.AddSnatEntryRequest,
    ) -> main_models.AddSnatEntryResponse:
        runtime = RuntimeOptions()
        return self.add_snat_entry_with_options(request, runtime)

    async def add_snat_entry_async(
        self,
        request: main_models.AddSnatEntryRequest,
    ) -> main_models.AddSnatEntryResponse:
        runtime = RuntimeOptions()
        return await self.add_snat_entry_with_options_async(request, runtime)

    def associate_aclwith_options(
        self,
        request: main_models.AssociateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_aclwith_options_async(
        self,
        request: main_models.AssociateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_acl(
        self,
        request: main_models.AssociateACLRequest,
    ) -> main_models.AssociateACLResponse:
        runtime = RuntimeOptions()
        return self.associate_aclwith_options(request, runtime)

    async def associate_acl_async(
        self,
        request: main_models.AssociateACLRequest,
    ) -> main_models.AssociateACLResponse:
        runtime = RuntimeOptions()
        return await self.associate_aclwith_options_async(request, runtime)

    def associate_flow_log_with_options(
        self,
        request: main_models.AssociateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_flow_log_with_options_async(
        self,
        request: main_models.AssociateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_flow_log(
        self,
        request: main_models.AssociateFlowLogRequest,
    ) -> main_models.AssociateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.associate_flow_log_with_options(request, runtime)

    async def associate_flow_log_async(
        self,
        request: main_models.AssociateFlowLogRequest,
    ) -> main_models.AssociateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.associate_flow_log_with_options_async(request, runtime)

    def associate_qos_with_options(
        self,
        request: main_models.AssociateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_qos_with_options_async(
        self,
        request: main_models.AssociateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateQosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_qos(
        self,
        request: main_models.AssociateQosRequest,
    ) -> main_models.AssociateQosResponse:
        runtime = RuntimeOptions()
        return self.associate_qos_with_options(request, runtime)

    async def associate_qos_async(
        self,
        request: main_models.AssociateQosRequest,
    ) -> main_models.AssociateQosResponse:
        runtime = RuntimeOptions()
        return await self.associate_qos_with_options_async(request, runtime)

    def associate_smart_agwith_application_bandwidth_package_with_options(
        self,
        request: main_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not DaraCore.is_null(request.associate_configs):
            query['AssociateConfigs'] = request.associate_configs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateSmartAGWithApplicationBandwidthPackage',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_smart_agwith_application_bandwidth_package_with_options_async(
        self,
        request: main_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not DaraCore.is_null(request.associate_configs):
            query['AssociateConfigs'] = request.associate_configs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateSmartAGWithApplicationBandwidthPackage',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_smart_agwith_application_bandwidth_package(
        self,
        request: main_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
    ) -> main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.associate_smart_agwith_application_bandwidth_package_with_options(request, runtime)

    async def associate_smart_agwith_application_bandwidth_package_async(
        self,
        request: main_models.AssociateSmartAGWithApplicationBandwidthPackageRequest,
    ) -> main_models.AssociateSmartAGWithApplicationBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.associate_smart_agwith_application_bandwidth_package_with_options_async(request, runtime)

    def bind_serial_number_with_options(
        self,
        request: main_models.BindSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSerialNumber',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_serial_number_with_options_async(
        self,
        request: main_models.BindSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSerialNumber',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_serial_number(
        self,
        request: main_models.BindSerialNumberRequest,
    ) -> main_models.BindSerialNumberResponse:
        runtime = RuntimeOptions()
        return self.bind_serial_number_with_options(request, runtime)

    async def bind_serial_number_async(
        self,
        request: main_models.BindSerialNumberRequest,
    ) -> main_models.BindSerialNumberResponse:
        runtime = RuntimeOptions()
        return await self.bind_serial_number_with_options_async(request, runtime)

    def bind_smart_access_gateway_with_options(
        self,
        request: main_models.BindSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_smart_access_gateway_with_options_async(
        self,
        request: main_models.BindSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_smart_access_gateway(
        self,
        request: main_models.BindSmartAccessGatewayRequest,
    ) -> main_models.BindSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.bind_smart_access_gateway_with_options(request, runtime)

    async def bind_smart_access_gateway_async(
        self,
        request: main_models.BindSmartAccessGatewayRequest,
    ) -> main_models.BindSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.bind_smart_access_gateway_with_options_async(request, runtime)

    def bind_vbr_with_options(
        self,
        request: main_models.BindVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_vbr_with_options_async(
        self,
        request: main_models.BindVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVbrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_vbr(
        self,
        request: main_models.BindVbrRequest,
    ) -> main_models.BindVbrResponse:
        runtime = RuntimeOptions()
        return self.bind_vbr_with_options(request, runtime)

    async def bind_vbr_async(
        self,
        request: main_models.BindVbrRequest,
    ) -> main_models.BindVbrResponse:
        runtime = RuntimeOptions()
        return await self.bind_vbr_with_options_async(request, runtime)

    def clear_sag_cipher_with_options(
        self,
        request: main_models.ClearSagCipherRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearSagCipherResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn_number):
            query['SnNumber'] = request.sn_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearSagCipher',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearSagCipherResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_sag_cipher_with_options_async(
        self,
        request: main_models.ClearSagCipherRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearSagCipherResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn_number):
            query['SnNumber'] = request.sn_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearSagCipher',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearSagCipherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_sag_cipher(
        self,
        request: main_models.ClearSagCipherRequest,
    ) -> main_models.ClearSagCipherResponse:
        runtime = RuntimeOptions()
        return self.clear_sag_cipher_with_options(request, runtime)

    async def clear_sag_cipher_async(
        self,
        request: main_models.ClearSagCipherRequest,
    ) -> main_models.ClearSagCipherResponse:
        runtime = RuntimeOptions()
        return await self.clear_sag_cipher_with_options_async(request, runtime)

    def clear_sag_routeable_address_with_options(
        self,
        request: main_models.ClearSagRouteableAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearSagRouteableAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearSagRouteableAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearSagRouteableAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_sag_routeable_address_with_options_async(
        self,
        request: main_models.ClearSagRouteableAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearSagRouteableAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearSagRouteableAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearSagRouteableAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_sag_routeable_address(
        self,
        request: main_models.ClearSagRouteableAddressRequest,
    ) -> main_models.ClearSagRouteableAddressResponse:
        runtime = RuntimeOptions()
        return self.clear_sag_routeable_address_with_options(request, runtime)

    async def clear_sag_routeable_address_async(
        self,
        request: main_models.ClearSagRouteableAddressRequest,
    ) -> main_models.ClearSagRouteableAddressResponse:
        runtime = RuntimeOptions()
        return await self.clear_sag_routeable_address_with_options_async(request, runtime)

    def create_aclwith_options(
        self,
        request: main_models.CreateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aclwith_options_async(
        self,
        request: main_models.CreateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: main_models.CreateACLRequest,
    ) -> main_models.CreateACLResponse:
        runtime = RuntimeOptions()
        return self.create_aclwith_options(request, runtime)

    async def create_acl_async(
        self,
        request: main_models.CreateACLRequest,
    ) -> main_models.CreateACLResponse:
        runtime = RuntimeOptions()
        return await self.create_aclwith_options_async(request, runtime)

    def create_cloud_connect_network_with_options(
        self,
        request: main_models.CreateCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snat_cidr_block):
            query['SnatCidrBlock'] = request.snat_cidr_block
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_connect_network_with_options_async(
        self,
        request: main_models.CreateCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snat_cidr_block):
            query['SnatCidrBlock'] = request.snat_cidr_block
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_connect_network(
        self,
        request: main_models.CreateCloudConnectNetworkRequest,
    ) -> main_models.CreateCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_connect_network_with_options(request, runtime)

    async def create_cloud_connect_network_async(
        self,
        request: main_models.CreateCloudConnectNetworkRequest,
    ) -> main_models.CreateCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_connect_network_with_options_async(request, runtime)

    def create_enterprise_code_with_options(
        self,
        request: main_models.CreateEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_code_with_options_async(
        self,
        request: main_models.CreateEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise_code(
        self,
        request: main_models.CreateEnterpriseCodeRequest,
    ) -> main_models.CreateEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return self.create_enterprise_code_with_options(request, runtime)

    async def create_enterprise_code_async(
        self,
        request: main_models.CreateEnterpriseCodeRequest,
    ) -> main_models.CreateEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return await self.create_enterprise_code_with_options_async(request, runtime)

    def create_flow_log_with_options(
        self,
        request: main_models.CreateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not DaraCore.is_null(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not DaraCore.is_null(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not DaraCore.is_null(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_log_with_options_async(
        self,
        request: main_models.CreateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not DaraCore.is_null(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not DaraCore.is_null(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not DaraCore.is_null(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_log(
        self,
        request: main_models.CreateFlowLogRequest,
    ) -> main_models.CreateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.create_flow_log_with_options(request, runtime)

    async def create_flow_log_async(
        self,
        request: main_models.CreateFlowLogRequest,
    ) -> main_models.CreateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_log_with_options_async(request, runtime)

    def create_health_check_with_options(
        self,
        request: main_models.CreateHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not DaraCore.is_null(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not DaraCore.is_null(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not DaraCore.is_null(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_health_check_with_options_async(
        self,
        request: main_models.CreateHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not DaraCore.is_null(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not DaraCore.is_null(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not DaraCore.is_null(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_health_check(
        self,
        request: main_models.CreateHealthCheckRequest,
    ) -> main_models.CreateHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.create_health_check_with_options(request, runtime)

    async def create_health_check_async(
        self,
        request: main_models.CreateHealthCheckRequest,
    ) -> main_models.CreateHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_health_check_with_options_async(request, runtime)

    def create_probe_task_with_options(
        self,
        request: main_models.CreateProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_probe_task_with_options_async(
        self,
        request: main_models.CreateProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_probe_task(
        self,
        request: main_models.CreateProbeTaskRequest,
    ) -> main_models.CreateProbeTaskResponse:
        runtime = RuntimeOptions()
        return self.create_probe_task_with_options(request, runtime)

    async def create_probe_task_async(
        self,
        request: main_models.CreateProbeTaskRequest,
    ) -> main_models.CreateProbeTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_probe_task_with_options_async(request, runtime)

    def create_qos_with_options(
        self,
        request: main_models.CreateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_with_options_async(
        self,
        request: main_models.CreateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_qos(
        self,
        request: main_models.CreateQosRequest,
    ) -> main_models.CreateQosResponse:
        runtime = RuntimeOptions()
        return self.create_qos_with_options(request, runtime)

    async def create_qos_async(
        self,
        request: main_models.CreateQosRequest,
    ) -> main_models.CreateQosResponse:
        runtime = RuntimeOptions()
        return await self.create_qos_with_options_async(request, runtime)

    def create_qos_car_with_options(
        self,
        request: main_models.CreateQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not DaraCore.is_null(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not DaraCore.is_null(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not DaraCore.is_null(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_car_with_options_async(
        self,
        request: main_models.CreateQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not DaraCore.is_null(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not DaraCore.is_null(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not DaraCore.is_null(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosCarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_qos_car(
        self,
        request: main_models.CreateQosCarRequest,
    ) -> main_models.CreateQosCarResponse:
        runtime = RuntimeOptions()
        return self.create_qos_car_with_options(request, runtime)

    async def create_qos_car_async(
        self,
        request: main_models.CreateQosCarRequest,
    ) -> main_models.CreateQosCarResponse:
        runtime = RuntimeOptions()
        return await self.create_qos_car_with_options_async(request, runtime)

    def create_qos_policy_with_options(
        self,
        request: main_models.CreateQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_policy_with_options_async(
        self,
        request: main_models.CreateQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_qos_policy(
        self,
        request: main_models.CreateQosPolicyRequest,
    ) -> main_models.CreateQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_qos_policy_with_options(request, runtime)

    async def create_qos_policy_async(
        self,
        request: main_models.CreateQosPolicyRequest,
    ) -> main_models.CreateQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_qos_policy_with_options_async(request, runtime)

    def create_sag_express_connect_interface_with_options(
        self,
        request: main_models.CreateSagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sag_express_connect_interface_with_options_async(
        self,
        request: main_models.CreateSagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sag_express_connect_interface(
        self,
        request: main_models.CreateSagExpressConnectInterfaceRequest,
    ) -> main_models.CreateSagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return self.create_sag_express_connect_interface_with_options(request, runtime)

    async def create_sag_express_connect_interface_async(
        self,
        request: main_models.CreateSagExpressConnectInterfaceRequest,
    ) -> main_models.CreateSagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.create_sag_express_connect_interface_with_options_async(request, runtime)

    def create_sag_static_route_with_options(
        self,
        request: main_models.CreateSagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sag_static_route_with_options_async(
        self,
        request: main_models.CreateSagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sag_static_route(
        self,
        request: main_models.CreateSagStaticRouteRequest,
    ) -> main_models.CreateSagStaticRouteResponse:
        runtime = RuntimeOptions()
        return self.create_sag_static_route_with_options(request, runtime)

    async def create_sag_static_route_async(
        self,
        request: main_models.CreateSagStaticRouteRequest,
    ) -> main_models.CreateSagStaticRouteResponse:
        runtime = RuntimeOptions()
        return await self.create_sag_static_route_with_options_async(request, runtime)

    def create_service_address_with_options(
        self,
        request: main_models.CreateServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_address_with_options_async(
        self,
        request: main_models.CreateServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_address(
        self,
        request: main_models.CreateServiceAddressRequest,
    ) -> main_models.CreateServiceAddressResponse:
        runtime = RuntimeOptions()
        return self.create_service_address_with_options(request, runtime)

    async def create_service_address_async(
        self,
        request: main_models.CreateServiceAddressRequest,
    ) -> main_models.CreateServiceAddressResponse:
        runtime = RuntimeOptions()
        return await self.create_service_address_with_options_async(request, runtime)

    def create_smart_access_gateway_with_options(
        self,
        request: main_models.CreateSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_have_sag):
            query['AlreadyHaveSag'] = request.already_have_sag
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.buyer_message):
            query['BuyerMessage'] = request.buyer_message
        if not DaraCore.is_null(request.cpeversion):
            query['CPEVersion'] = request.cpeversion
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ha_type):
            query['HaType'] = request.ha_type
        if not DaraCore.is_null(request.hard_ware_spec):
            query['HardWareSpec'] = request.hard_ware_spec
        if not DaraCore.is_null(request.max_band_width):
            query['MaxBandWidth'] = request.max_band_width
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.receiver_address):
            query['ReceiverAddress'] = request.receiver_address
        if not DaraCore.is_null(request.receiver_city):
            query['ReceiverCity'] = request.receiver_city
        if not DaraCore.is_null(request.receiver_country):
            query['ReceiverCountry'] = request.receiver_country
        if not DaraCore.is_null(request.receiver_district):
            query['ReceiverDistrict'] = request.receiver_district
        if not DaraCore.is_null(request.receiver_email):
            query['ReceiverEmail'] = request.receiver_email
        if not DaraCore.is_null(request.receiver_mobile):
            query['ReceiverMobile'] = request.receiver_mobile
        if not DaraCore.is_null(request.receiver_name):
            query['ReceiverName'] = request.receiver_name
        if not DaraCore.is_null(request.receiver_phone):
            query['ReceiverPhone'] = request.receiver_phone
        if not DaraCore.is_null(request.receiver_state):
            query['ReceiverState'] = request.receiver_state
        if not DaraCore.is_null(request.receiver_town):
            query['ReceiverTown'] = request.receiver_town
        if not DaraCore.is_null(request.receiver_zip):
            query['ReceiverZip'] = request.receiver_zip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_with_options_async(
        self,
        request: main_models.CreateSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_have_sag):
            query['AlreadyHaveSag'] = request.already_have_sag
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.buyer_message):
            query['BuyerMessage'] = request.buyer_message
        if not DaraCore.is_null(request.cpeversion):
            query['CPEVersion'] = request.cpeversion
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ha_type):
            query['HaType'] = request.ha_type
        if not DaraCore.is_null(request.hard_ware_spec):
            query['HardWareSpec'] = request.hard_ware_spec
        if not DaraCore.is_null(request.max_band_width):
            query['MaxBandWidth'] = request.max_band_width
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.receiver_address):
            query['ReceiverAddress'] = request.receiver_address
        if not DaraCore.is_null(request.receiver_city):
            query['ReceiverCity'] = request.receiver_city
        if not DaraCore.is_null(request.receiver_country):
            query['ReceiverCountry'] = request.receiver_country
        if not DaraCore.is_null(request.receiver_district):
            query['ReceiverDistrict'] = request.receiver_district
        if not DaraCore.is_null(request.receiver_email):
            query['ReceiverEmail'] = request.receiver_email
        if not DaraCore.is_null(request.receiver_mobile):
            query['ReceiverMobile'] = request.receiver_mobile
        if not DaraCore.is_null(request.receiver_name):
            query['ReceiverName'] = request.receiver_name
        if not DaraCore.is_null(request.receiver_phone):
            query['ReceiverPhone'] = request.receiver_phone
        if not DaraCore.is_null(request.receiver_state):
            query['ReceiverState'] = request.receiver_state
        if not DaraCore.is_null(request.receiver_town):
            query['ReceiverTown'] = request.receiver_town
        if not DaraCore.is_null(request.receiver_zip):
            query['ReceiverZip'] = request.receiver_zip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_access_gateway(
        self,
        request: main_models.CreateSmartAccessGatewayRequest,
    ) -> main_models.CreateSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.create_smart_access_gateway_with_options(request, runtime)

    async def create_smart_access_gateway_async(
        self,
        request: main_models.CreateSmartAccessGatewayRequest,
    ) -> main_models.CreateSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.create_smart_access_gateway_with_options_async(request, runtime)

    def create_smart_access_gateway_client_user_with_options(
        self,
        request: main_models.CreateSmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_mail):
            query['UserMail'] = request.user_mail
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_client_user_with_options_async(
        self,
        request: main_models.CreateSmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_mail):
            query['UserMail'] = request.user_mail
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_access_gateway_client_user(
        self,
        request: main_models.CreateSmartAccessGatewayClientUserRequest,
    ) -> main_models.CreateSmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return self.create_smart_access_gateway_client_user_with_options(request, runtime)

    async def create_smart_access_gateway_client_user_async(
        self,
        request: main_models.CreateSmartAccessGatewayClientUserRequest,
    ) -> main_models.CreateSmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return await self.create_smart_access_gateway_client_user_with_options_async(request, runtime)

    def create_smart_access_gateway_software_with_options(
        self,
        request: main_models.CreateSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_access_gateway_software_with_options_async(
        self,
        request: main_models.CreateSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_access_gateway_software(
        self,
        request: main_models.CreateSmartAccessGatewaySoftwareRequest,
    ) -> main_models.CreateSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return self.create_smart_access_gateway_software_with_options(request, runtime)

    async def create_smart_access_gateway_software_async(
        self,
        request: main_models.CreateSmartAccessGatewaySoftwareRequest,
    ) -> main_models.CreateSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return await self.create_smart_access_gateway_software_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: main_models.DeactiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: main_models.DeactiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_flow_log(
        self,
        request: main_models.DeactiveFlowLogRequest,
    ) -> main_models.DeactiveFlowLogResponse:
        runtime = RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: main_models.DeactiveFlowLogRequest,
    ) -> main_models.DeactiveFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_aclwith_options(
        self,
        request: main_models.DeleteACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aclwith_options_async(
        self,
        request: main_models.DeleteACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: main_models.DeleteACLRequest,
    ) -> main_models.DeleteACLResponse:
        runtime = RuntimeOptions()
        return self.delete_aclwith_options(request, runtime)

    async def delete_acl_async(
        self,
        request: main_models.DeleteACLRequest,
    ) -> main_models.DeleteACLResponse:
        runtime = RuntimeOptions()
        return await self.delete_aclwith_options_async(request, runtime)

    def delete_aclrule_with_options(
        self,
        request: main_models.DeleteACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acr_id):
            query['AcrId'] = request.acr_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aclrule_with_options_async(
        self,
        request: main_models.DeleteACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acr_id):
            query['AcrId'] = request.acr_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aclrule(
        self,
        request: main_models.DeleteACLRuleRequest,
    ) -> main_models.DeleteACLRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_aclrule_with_options(request, runtime)

    async def delete_aclrule_async(
        self,
        request: main_models.DeleteACLRuleRequest,
    ) -> main_models.DeleteACLRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_aclrule_with_options_async(request, runtime)

    def delete_cloud_connect_network_with_options(
        self,
        request: main_models.DeleteCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_connect_network_with_options_async(
        self,
        request: main_models.DeleteCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_connect_network(
        self,
        request: main_models.DeleteCloudConnectNetworkRequest,
    ) -> main_models.DeleteCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_connect_network_with_options(request, runtime)

    async def delete_cloud_connect_network_async(
        self,
        request: main_models.DeleteCloudConnectNetworkRequest,
    ) -> main_models.DeleteCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_connect_network_with_options_async(request, runtime)

    def delete_dnat_entry_with_options(
        self,
        request: main_models.DeleteDnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dnat_entry_id):
            query['DnatEntryId'] = request.dnat_entry_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dnat_entry_with_options_async(
        self,
        request: main_models.DeleteDnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dnat_entry_id):
            query['DnatEntryId'] = request.dnat_entry_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dnat_entry(
        self,
        request: main_models.DeleteDnatEntryRequest,
    ) -> main_models.DeleteDnatEntryResponse:
        runtime = RuntimeOptions()
        return self.delete_dnat_entry_with_options(request, runtime)

    async def delete_dnat_entry_async(
        self,
        request: main_models.DeleteDnatEntryRequest,
    ) -> main_models.DeleteDnatEntryResponse:
        runtime = RuntimeOptions()
        return await self.delete_dnat_entry_with_options_async(request, runtime)

    def delete_enterprise_code_with_options(
        self,
        request: main_models.DeleteEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_code_with_options_async(
        self,
        request: main_models.DeleteEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_code(
        self,
        request: main_models.DeleteEnterpriseCodeRequest,
    ) -> main_models.DeleteEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return self.delete_enterprise_code_with_options(request, runtime)

    async def delete_enterprise_code_async(
        self,
        request: main_models.DeleteEnterpriseCodeRequest,
    ) -> main_models.DeleteEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_enterprise_code_with_options_async(request, runtime)

    def delete_flow_log_with_options(
        self,
        request: main_models.DeleteFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_log_with_options_async(
        self,
        request: main_models.DeleteFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_log(
        self,
        request: main_models.DeleteFlowLogRequest,
    ) -> main_models.DeleteFlowLogResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_log_with_options(request, runtime)

    async def delete_flow_log_async(
        self,
        request: main_models.DeleteFlowLogRequest,
    ) -> main_models.DeleteFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_log_with_options_async(request, runtime)

    def delete_health_check_with_options(
        self,
        request: main_models.DeleteHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_health_check_with_options_async(
        self,
        request: main_models.DeleteHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_health_check(
        self,
        request: main_models.DeleteHealthCheckRequest,
    ) -> main_models.DeleteHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.delete_health_check_with_options(request, runtime)

    async def delete_health_check_async(
        self,
        request: main_models.DeleteHealthCheckRequest,
    ) -> main_models.DeleteHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.delete_health_check_with_options_async(request, runtime)

    def delete_probe_task_with_options(
        self,
        request: main_models.DeleteProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_probe_task_with_options_async(
        self,
        request: main_models.DeleteProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_probe_task(
        self,
        request: main_models.DeleteProbeTaskRequest,
    ) -> main_models.DeleteProbeTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_probe_task_with_options(request, runtime)

    async def delete_probe_task_async(
        self,
        request: main_models.DeleteProbeTaskRequest,
    ) -> main_models.DeleteProbeTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_probe_task_with_options_async(request, runtime)

    def delete_qos_with_options(
        self,
        request: main_models.DeleteQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_with_options_async(
        self,
        request: main_models.DeleteQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qos(
        self,
        request: main_models.DeleteQosRequest,
    ) -> main_models.DeleteQosResponse:
        runtime = RuntimeOptions()
        return self.delete_qos_with_options(request, runtime)

    async def delete_qos_async(
        self,
        request: main_models.DeleteQosRequest,
    ) -> main_models.DeleteQosResponse:
        runtime = RuntimeOptions()
        return await self.delete_qos_with_options_async(request, runtime)

    def delete_qos_car_with_options(
        self,
        request: main_models.DeleteQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_car_with_options_async(
        self,
        request: main_models.DeleteQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosCarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qos_car(
        self,
        request: main_models.DeleteQosCarRequest,
    ) -> main_models.DeleteQosCarResponse:
        runtime = RuntimeOptions()
        return self.delete_qos_car_with_options(request, runtime)

    async def delete_qos_car_async(
        self,
        request: main_models.DeleteQosCarRequest,
    ) -> main_models.DeleteQosCarResponse:
        runtime = RuntimeOptions()
        return await self.delete_qos_car_with_options_async(request, runtime)

    def delete_qos_policy_with_options(
        self,
        request: main_models.DeleteQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_policy_with_options_async(
        self,
        request: main_models.DeleteQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qos_policy(
        self,
        request: main_models.DeleteQosPolicyRequest,
    ) -> main_models.DeleteQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_qos_policy_with_options(request, runtime)

    async def delete_qos_policy_async(
        self,
        request: main_models.DeleteQosPolicyRequest,
    ) -> main_models.DeleteQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_qos_policy_with_options_async(request, runtime)

    def delete_route_distribution_strategy_with_options(
        self,
        request: main_models.DeleteRouteDistributionStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteDistributionStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_source):
            query['RouteSource'] = request.route_source
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteDistributionStrategy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteDistributionStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_distribution_strategy_with_options_async(
        self,
        request: main_models.DeleteRouteDistributionStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteDistributionStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_source):
            query['RouteSource'] = request.route_source
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteDistributionStrategy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteDistributionStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_distribution_strategy(
        self,
        request: main_models.DeleteRouteDistributionStrategyRequest,
    ) -> main_models.DeleteRouteDistributionStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_route_distribution_strategy_with_options(request, runtime)

    async def delete_route_distribution_strategy_async(
        self,
        request: main_models.DeleteRouteDistributionStrategyRequest,
    ) -> main_models.DeleteRouteDistributionStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_route_distribution_strategy_with_options_async(request, runtime)

    def delete_sag_express_connect_interface_with_options(
        self,
        request: main_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sag_express_connect_interface_with_options_async(
        self,
        request: main_models.DeleteSagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sag_express_connect_interface(
        self,
        request: main_models.DeleteSagExpressConnectInterfaceRequest,
    ) -> main_models.DeleteSagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return self.delete_sag_express_connect_interface_with_options(request, runtime)

    async def delete_sag_express_connect_interface_async(
        self,
        request: main_models.DeleteSagExpressConnectInterfaceRequest,
    ) -> main_models.DeleteSagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_sag_express_connect_interface_with_options_async(request, runtime)

    def delete_sag_static_route_with_options(
        self,
        request: main_models.DeleteSagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sag_static_route_with_options_async(
        self,
        request: main_models.DeleteSagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sag_static_route(
        self,
        request: main_models.DeleteSagStaticRouteRequest,
    ) -> main_models.DeleteSagStaticRouteResponse:
        runtime = RuntimeOptions()
        return self.delete_sag_static_route_with_options(request, runtime)

    async def delete_sag_static_route_async(
        self,
        request: main_models.DeleteSagStaticRouteRequest,
    ) -> main_models.DeleteSagStaticRouteResponse:
        runtime = RuntimeOptions()
        return await self.delete_sag_static_route_with_options_async(request, runtime)

    def delete_service_address_with_options(
        self,
        request: main_models.DeleteServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_address_with_options_async(
        self,
        request: main_models.DeleteServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_address(
        self,
        request: main_models.DeleteServiceAddressRequest,
    ) -> main_models.DeleteServiceAddressResponse:
        runtime = RuntimeOptions()
        return self.delete_service_address_with_options(request, runtime)

    async def delete_service_address_async(
        self,
        request: main_models.DeleteServiceAddressRequest,
    ) -> main_models.DeleteServiceAddressResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_address_with_options_async(request, runtime)

    def delete_smart_access_gateway_with_options(
        self,
        request: main_models.DeleteSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_with_options_async(
        self,
        request: main_models.DeleteSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smart_access_gateway(
        self,
        request: main_models.DeleteSmartAccessGatewayRequest,
    ) -> main_models.DeleteSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.delete_smart_access_gateway_with_options(request, runtime)

    async def delete_smart_access_gateway_async(
        self,
        request: main_models.DeleteSmartAccessGatewayRequest,
    ) -> main_models.DeleteSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.delete_smart_access_gateway_with_options_async(request, runtime)

    def delete_smart_access_gateway_client_user_with_options(
        self,
        request: main_models.DeleteSmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_client_user_with_options_async(
        self,
        request: main_models.DeleteSmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smart_access_gateway_client_user(
        self,
        request: main_models.DeleteSmartAccessGatewayClientUserRequest,
    ) -> main_models.DeleteSmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return self.delete_smart_access_gateway_client_user_with_options(request, runtime)

    async def delete_smart_access_gateway_client_user_async(
        self,
        request: main_models.DeleteSmartAccessGatewayClientUserRequest,
    ) -> main_models.DeleteSmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_smart_access_gateway_client_user_with_options_async(request, runtime)

    def delete_smart_access_gateway_dns_forward_with_options(
        self,
        request: main_models.DeleteSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: main_models.DeleteSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smart_access_gateway_dns_forward(
        self,
        request: main_models.DeleteSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.DeleteSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return self.delete_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def delete_smart_access_gateway_dns_forward_async(
        self,
        request: main_models.DeleteSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.DeleteSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return await self.delete_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def delete_snat_entry_with_options(
        self,
        request: main_models.DeleteSnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snat_entry_with_options_async(
        self,
        request: main_models.DeleteSnatEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnatEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnatEntry',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snat_entry(
        self,
        request: main_models.DeleteSnatEntryRequest,
    ) -> main_models.DeleteSnatEntryResponse:
        runtime = RuntimeOptions()
        return self.delete_snat_entry_with_options(request, runtime)

    async def delete_snat_entry_async(
        self,
        request: main_models.DeleteSnatEntryRequest,
    ) -> main_models.DeleteSnatEntryResponse:
        runtime = RuntimeOptions()
        return await self.delete_snat_entry_with_options_async(request, runtime)

    def describe_aclattribute_with_options(
        self,
        request: main_models.DescribeACLAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aclattribute_with_options_async(
        self,
        request: main_models.DescribeACLAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aclattribute(
        self,
        request: main_models.DescribeACLAttributeRequest,
    ) -> main_models.DescribeACLAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_aclattribute_with_options(request, runtime)

    async def describe_aclattribute_async(
        self,
        request: main_models.DescribeACLAttributeRequest,
    ) -> main_models.DescribeACLAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_aclattribute_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: main_models.DescribeACLsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLs',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: main_models.DescribeACLsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLs',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acls(
        self,
        request: main_models.DescribeACLsRequest,
    ) -> main_models.DescribeACLsResponse:
        runtime = RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: main_models.DescribeACLsRequest,
    ) -> main_models.DescribeACLsResponse:
        runtime = RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_bindable_smart_access_gateways_with_options(
        self,
        request: main_models.DescribeBindableSmartAccessGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBindableSmartAccessGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBindableSmartAccessGateways',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBindableSmartAccessGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bindable_smart_access_gateways_with_options_async(
        self,
        request: main_models.DescribeBindableSmartAccessGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBindableSmartAccessGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBindableSmartAccessGateways',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBindableSmartAccessGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bindable_smart_access_gateways(
        self,
        request: main_models.DescribeBindableSmartAccessGatewaysRequest,
    ) -> main_models.DescribeBindableSmartAccessGatewaysResponse:
        runtime = RuntimeOptions()
        return self.describe_bindable_smart_access_gateways_with_options(request, runtime)

    async def describe_bindable_smart_access_gateways_async(
        self,
        request: main_models.DescribeBindableSmartAccessGatewaysRequest,
    ) -> main_models.DescribeBindableSmartAccessGatewaysResponse:
        runtime = RuntimeOptions()
        return await self.describe_bindable_smart_access_gateways_with_options_async(request, runtime)

    def describe_client_user_dnswith_options(
        self,
        request: main_models.DescribeClientUserDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientUserDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientUserDNS',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientUserDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_user_dnswith_options_async(
        self,
        request: main_models.DescribeClientUserDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientUserDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientUserDNS',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientUserDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_user_dns(
        self,
        request: main_models.DescribeClientUserDNSRequest,
    ) -> main_models.DescribeClientUserDNSResponse:
        runtime = RuntimeOptions()
        return self.describe_client_user_dnswith_options(request, runtime)

    async def describe_client_user_dns_async(
        self,
        request: main_models.DescribeClientUserDNSRequest,
    ) -> main_models.DescribeClientUserDNSResponse:
        runtime = RuntimeOptions()
        return await self.describe_client_user_dnswith_options_async(request, runtime)

    def describe_cloud_connect_networks_with_options(
        self,
        request: main_models.DescribeCloudConnectNetworksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudConnectNetworksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudConnectNetworks',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudConnectNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_connect_networks_with_options_async(
        self,
        request: main_models.DescribeCloudConnectNetworksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudConnectNetworksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudConnectNetworks',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudConnectNetworksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_connect_networks(
        self,
        request: main_models.DescribeCloudConnectNetworksRequest,
    ) -> main_models.DescribeCloudConnectNetworksResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_connect_networks_with_options(request, runtime)

    async def describe_cloud_connect_networks_async(
        self,
        request: main_models.DescribeCloudConnectNetworksRequest,
    ) -> main_models.DescribeCloudConnectNetworksResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_connect_networks_with_options_async(request, runtime)

    def describe_device_auto_upgrade_policy_with_options(
        self,
        request: main_models.DescribeDeviceAutoUpgradePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceAutoUpgradePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceAutoUpgradePolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceAutoUpgradePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_auto_upgrade_policy_with_options_async(
        self,
        request: main_models.DescribeDeviceAutoUpgradePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceAutoUpgradePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceAutoUpgradePolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceAutoUpgradePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_auto_upgrade_policy(
        self,
        request: main_models.DescribeDeviceAutoUpgradePolicyRequest,
    ) -> main_models.DescribeDeviceAutoUpgradePolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_device_auto_upgrade_policy_with_options(request, runtime)

    async def describe_device_auto_upgrade_policy_async(
        self,
        request: main_models.DescribeDeviceAutoUpgradePolicyRequest,
    ) -> main_models.DescribeDeviceAutoUpgradePolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_auto_upgrade_policy_with_options_async(request, runtime)

    def describe_dnat_entries_with_options(
        self,
        request: main_models.DescribeDnatEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnatEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnatEntries',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnatEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dnat_entries_with_options_async(
        self,
        request: main_models.DescribeDnatEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnatEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnatEntries',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnatEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dnat_entries(
        self,
        request: main_models.DescribeDnatEntriesRequest,
    ) -> main_models.DescribeDnatEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_dnat_entries_with_options(request, runtime)

    async def describe_dnat_entries_async(
        self,
        request: main_models.DescribeDnatEntriesRequest,
    ) -> main_models.DescribeDnatEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dnat_entries_with_options_async(request, runtime)

    def describe_flow_log_sags_with_options(
        self,
        request: main_models.DescribeFlowLogSagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogSagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogSags',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogSagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_log_sags_with_options_async(
        self,
        request: main_models.DescribeFlowLogSagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogSagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogSags',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogSagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_log_sags(
        self,
        request: main_models.DescribeFlowLogSagsRequest,
    ) -> main_models.DescribeFlowLogSagsResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_log_sags_with_options(request, runtime)

    async def describe_flow_log_sags_async(
        self,
        request: main_models.DescribeFlowLogSagsRequest,
    ) -> main_models.DescribeFlowLogSagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_log_sags_with_options_async(request, runtime)

    def describe_flow_logs_with_options(
        self,
        request: main_models.DescribeFlowLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogs',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_logs_with_options_async(
        self,
        request: main_models.DescribeFlowLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogs',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_logs(
        self,
        request: main_models.DescribeFlowLogsRequest,
    ) -> main_models.DescribeFlowLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_logs_with_options(request, runtime)

    async def describe_flow_logs_async(
        self,
        request: main_models.DescribeFlowLogsRequest,
    ) -> main_models.DescribeFlowLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_logs_with_options_async(request, runtime)

    def describe_grant_rules_with_options(
        self,
        request: main_models.DescribeGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_with_options_async(
        self,
        request: main_models.DescribeGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_rules(
        self,
        request: main_models.DescribeGrantRulesRequest,
    ) -> main_models.DescribeGrantRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_grant_rules_with_options(request, runtime)

    async def describe_grant_rules_async(
        self,
        request: main_models.DescribeGrantRulesRequest,
    ) -> main_models.DescribeGrantRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_grant_rules_with_options_async(request, runtime)

    def describe_grant_sag_rules_with_options(
        self,
        request: main_models.DescribeGrantSagRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantSagRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantSagRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantSagRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_sag_rules_with_options_async(
        self,
        request: main_models.DescribeGrantSagRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantSagRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantSagRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantSagRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_sag_rules(
        self,
        request: main_models.DescribeGrantSagRulesRequest,
    ) -> main_models.DescribeGrantSagRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_grant_sag_rules_with_options(request, runtime)

    async def describe_grant_sag_rules_async(
        self,
        request: main_models.DescribeGrantSagRulesRequest,
    ) -> main_models.DescribeGrantSagRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_grant_sag_rules_with_options_async(request, runtime)

    def describe_grant_sag_vbr_rules_with_options(
        self,
        request: main_models.DescribeGrantSagVbrRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantSagVbrRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantSagVbrRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantSagVbrRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_sag_vbr_rules_with_options_async(
        self,
        request: main_models.DescribeGrantSagVbrRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantSagVbrRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantSagVbrRules',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantSagVbrRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_sag_vbr_rules(
        self,
        request: main_models.DescribeGrantSagVbrRulesRequest,
    ) -> main_models.DescribeGrantSagVbrRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_grant_sag_vbr_rules_with_options(request, runtime)

    async def describe_grant_sag_vbr_rules_async(
        self,
        request: main_models.DescribeGrantSagVbrRulesRequest,
    ) -> main_models.DescribeGrantSagVbrRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_grant_sag_vbr_rules_with_options_async(request, runtime)

    def describe_health_check_attribute_with_options(
        self,
        request: main_models.DescribeHealthCheckAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_attribute_with_options_async(
        self,
        request: main_models.DescribeHealthCheckAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_check_attribute(
        self,
        request: main_models.DescribeHealthCheckAttributeRequest,
    ) -> main_models.DescribeHealthCheckAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_health_check_attribute_with_options(request, runtime)

    async def describe_health_check_attribute_async(
        self,
        request: main_models.DescribeHealthCheckAttributeRequest,
    ) -> main_models.DescribeHealthCheckAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_check_attribute_with_options_async(request, runtime)

    def describe_health_checks_with_options(
        self,
        request: main_models.DescribeHealthChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthChecks',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_checks_with_options_async(
        self,
        request: main_models.DescribeHealthChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthChecks',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthChecksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_checks(
        self,
        request: main_models.DescribeHealthChecksRequest,
    ) -> main_models.DescribeHealthChecksResponse:
        runtime = RuntimeOptions()
        return self.describe_health_checks_with_options(request, runtime)

    async def describe_health_checks_async(
        self,
        request: main_models.DescribeHealthChecksRequest,
    ) -> main_models.DescribeHealthChecksResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_checks_with_options_async(request, runtime)

    def describe_qos_cars_with_options(
        self,
        request: main_models.DescribeQosCarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosCarsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQosCars',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosCarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qos_cars_with_options_async(
        self,
        request: main_models.DescribeQosCarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosCarsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQosCars',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosCarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qos_cars(
        self,
        request: main_models.DescribeQosCarsRequest,
    ) -> main_models.DescribeQosCarsResponse:
        runtime = RuntimeOptions()
        return self.describe_qos_cars_with_options(request, runtime)

    async def describe_qos_cars_async(
        self,
        request: main_models.DescribeQosCarsRequest,
    ) -> main_models.DescribeQosCarsResponse:
        runtime = RuntimeOptions()
        return await self.describe_qos_cars_with_options_async(request, runtime)

    def describe_qos_policies_with_options(
        self,
        request: main_models.DescribeQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQosPolicies',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qos_policies_with_options_async(
        self,
        request: main_models.DescribeQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQosPolicies',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qos_policies(
        self,
        request: main_models.DescribeQosPoliciesRequest,
    ) -> main_models.DescribeQosPoliciesResponse:
        runtime = RuntimeOptions()
        return self.describe_qos_policies_with_options(request, runtime)

    async def describe_qos_policies_async(
        self,
        request: main_models.DescribeQosPoliciesRequest,
    ) -> main_models.DescribeQosPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.describe_qos_policies_with_options_async(request, runtime)

    def describe_qoses_with_options(
        self,
        request: main_models.DescribeQosesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qos_ids):
            query['QosIds'] = request.qos_ids
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQoses',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qoses_with_options_async(
        self,
        request: main_models.DescribeQosesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQosesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qos_ids):
            query['QosIds'] = request.qos_ids
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQoses',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQosesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qoses(
        self,
        request: main_models.DescribeQosesRequest,
    ) -> main_models.DescribeQosesResponse:
        runtime = RuntimeOptions()
        return self.describe_qoses_with_options(request, runtime)

    async def describe_qoses_async(
        self,
        request: main_models.DescribeQosesRequest,
    ) -> main_models.DescribeQosesResponse:
        runtime = RuntimeOptions()
        return await self.describe_qoses_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_route_distribution_strategies_with_options(
        self,
        request: main_models.DescribeRouteDistributionStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteDistributionStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteDistributionStrategies',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteDistributionStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_distribution_strategies_with_options_async(
        self,
        request: main_models.DescribeRouteDistributionStrategiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteDistributionStrategiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteDistributionStrategies',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteDistributionStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_route_distribution_strategies(
        self,
        request: main_models.DescribeRouteDistributionStrategiesRequest,
    ) -> main_models.DescribeRouteDistributionStrategiesResponse:
        runtime = RuntimeOptions()
        return self.describe_route_distribution_strategies_with_options(request, runtime)

    async def describe_route_distribution_strategies_async(
        self,
        request: main_models.DescribeRouteDistributionStrategiesRequest,
    ) -> main_models.DescribeRouteDistributionStrategiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_route_distribution_strategies_with_options_async(request, runtime)

    def describe_sagdevice_info_with_options(
        self,
        request: main_models.DescribeSAGDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSAGDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSAGDeviceInfo',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSAGDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sagdevice_info_with_options_async(
        self,
        request: main_models.DescribeSAGDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSAGDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSAGDeviceInfo',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSAGDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sagdevice_info(
        self,
        request: main_models.DescribeSAGDeviceInfoRequest,
    ) -> main_models.DescribeSAGDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sagdevice_info_with_options(request, runtime)

    async def describe_sagdevice_info_async(
        self,
        request: main_models.DescribeSAGDeviceInfoRequest,
    ) -> main_models.DescribeSAGDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sagdevice_info_with_options_async(request, runtime)

    def describe_sag_current_dns_with_options(
        self,
        request: main_models.DescribeSagCurrentDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagCurrentDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagCurrentDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagCurrentDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_current_dns_with_options_async(
        self,
        request: main_models.DescribeSagCurrentDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagCurrentDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagCurrentDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagCurrentDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_current_dns(
        self,
        request: main_models.DescribeSagCurrentDnsRequest,
    ) -> main_models.DescribeSagCurrentDnsResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_current_dns_with_options(request, runtime)

    async def describe_sag_current_dns_async(
        self,
        request: main_models.DescribeSagCurrentDnsRequest,
    ) -> main_models.DescribeSagCurrentDnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_current_dns_with_options_async(request, runtime)

    def describe_sag_drop_top_nwith_options(
        self,
        request: main_models.DescribeSagDropTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagDropTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagDropTopN',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagDropTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_drop_top_nwith_options_async(
        self,
        request: main_models.DescribeSagDropTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagDropTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagDropTopN',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagDropTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_drop_top_n(
        self,
        request: main_models.DescribeSagDropTopNRequest,
    ) -> main_models.DescribeSagDropTopNResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_drop_top_nwith_options(request, runtime)

    async def describe_sag_drop_top_n_async(
        self,
        request: main_models.DescribeSagDropTopNRequest,
    ) -> main_models.DescribeSagDropTopNResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_drop_top_nwith_options_async(request, runtime)

    def describe_sag_express_connect_interface_list_with_options(
        self,
        request: main_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagExpressConnectInterfaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagExpressConnectInterfaceList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagExpressConnectInterfaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_express_connect_interface_list_with_options_async(
        self,
        request: main_models.DescribeSagExpressConnectInterfaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagExpressConnectInterfaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagExpressConnectInterfaceList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagExpressConnectInterfaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_express_connect_interface_list(
        self,
        request: main_models.DescribeSagExpressConnectInterfaceListRequest,
    ) -> main_models.DescribeSagExpressConnectInterfaceListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_express_connect_interface_list_with_options(request, runtime)

    async def describe_sag_express_connect_interface_list_async(
        self,
        request: main_models.DescribeSagExpressConnectInterfaceListRequest,
    ) -> main_models.DescribeSagExpressConnectInterfaceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_express_connect_interface_list_with_options_async(request, runtime)

    def describe_sag_global_route_protocol_with_options(
        self,
        request: main_models.DescribeSagGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_global_route_protocol_with_options_async(
        self,
        request: main_models.DescribeSagGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_global_route_protocol(
        self,
        request: main_models.DescribeSagGlobalRouteProtocolRequest,
    ) -> main_models.DescribeSagGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_global_route_protocol_with_options(request, runtime)

    async def describe_sag_global_route_protocol_async(
        self,
        request: main_models.DescribeSagGlobalRouteProtocolRequest,
    ) -> main_models.DescribeSagGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_global_route_protocol_with_options_async(request, runtime)

    def describe_sag_ha_with_options(
        self,
        request: main_models.DescribeSagHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_ha_with_options_async(
        self,
        request: main_models.DescribeSagHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_ha(
        self,
        request: main_models.DescribeSagHaRequest,
    ) -> main_models.DescribeSagHaResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_ha_with_options(request, runtime)

    async def describe_sag_ha_async(
        self,
        request: main_models.DescribeSagHaRequest,
    ) -> main_models.DescribeSagHaResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_ha_with_options_async(request, runtime)

    def describe_sag_lan_list_with_options(
        self,
        request: main_models.DescribeSagLanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagLanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagLanList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagLanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_lan_list_with_options_async(
        self,
        request: main_models.DescribeSagLanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagLanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagLanList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagLanListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_lan_list(
        self,
        request: main_models.DescribeSagLanListRequest,
    ) -> main_models.DescribeSagLanListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_lan_list_with_options(request, runtime)

    async def describe_sag_lan_list_async(
        self,
        request: main_models.DescribeSagLanListRequest,
    ) -> main_models.DescribeSagLanListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_lan_list_with_options_async(request, runtime)

    def describe_sag_management_port_with_options(
        self,
        request: main_models.DescribeSagManagementPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagManagementPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagManagementPort',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagManagementPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_management_port_with_options_async(
        self,
        request: main_models.DescribeSagManagementPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagManagementPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagManagementPort',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagManagementPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_management_port(
        self,
        request: main_models.DescribeSagManagementPortRequest,
    ) -> main_models.DescribeSagManagementPortResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_management_port_with_options(request, runtime)

    async def describe_sag_management_port_async(
        self,
        request: main_models.DescribeSagManagementPortRequest,
    ) -> main_models.DescribeSagManagementPortResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_management_port_with_options_async(request, runtime)

    def describe_sag_online_client_statistics_with_options(
        self,
        request: main_models.DescribeSagOnlineClientStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagOnlineClientStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagOnlineClientStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagOnlineClientStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_online_client_statistics_with_options_async(
        self,
        request: main_models.DescribeSagOnlineClientStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagOnlineClientStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagOnlineClientStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagOnlineClientStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_online_client_statistics(
        self,
        request: main_models.DescribeSagOnlineClientStatisticsRequest,
    ) -> main_models.DescribeSagOnlineClientStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_online_client_statistics_with_options(request, runtime)

    async def describe_sag_online_client_statistics_async(
        self,
        request: main_models.DescribeSagOnlineClientStatisticsRequest,
    ) -> main_models.DescribeSagOnlineClientStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_online_client_statistics_with_options_async(request, runtime)

    def describe_sag_port_list_with_options(
        self,
        request: main_models.DescribeSagPortListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagPortListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagPortList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagPortListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_port_list_with_options_async(
        self,
        request: main_models.DescribeSagPortListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagPortListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagPortList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagPortListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_port_list(
        self,
        request: main_models.DescribeSagPortListRequest,
    ) -> main_models.DescribeSagPortListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_port_list_with_options(request, runtime)

    async def describe_sag_port_list_async(
        self,
        request: main_models.DescribeSagPortListRequest,
    ) -> main_models.DescribeSagPortListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_port_list_with_options_async(request, runtime)

    def describe_sag_port_route_protocol_list_with_options(
        self,
        request: main_models.DescribeSagPortRouteProtocolListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagPortRouteProtocolListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagPortRouteProtocolList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagPortRouteProtocolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_port_route_protocol_list_with_options_async(
        self,
        request: main_models.DescribeSagPortRouteProtocolListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagPortRouteProtocolListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagPortRouteProtocolList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagPortRouteProtocolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_port_route_protocol_list(
        self,
        request: main_models.DescribeSagPortRouteProtocolListRequest,
    ) -> main_models.DescribeSagPortRouteProtocolListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_port_route_protocol_list_with_options(request, runtime)

    async def describe_sag_port_route_protocol_list_async(
        self,
        request: main_models.DescribeSagPortRouteProtocolListRequest,
    ) -> main_models.DescribeSagPortRouteProtocolListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_port_route_protocol_list_with_options_async(request, runtime)

    def describe_sag_remote_access_with_options(
        self,
        request: main_models.DescribeSagRemoteAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRemoteAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRemoteAccess',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRemoteAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_remote_access_with_options_async(
        self,
        request: main_models.DescribeSagRemoteAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRemoteAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRemoteAccess',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRemoteAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_remote_access(
        self,
        request: main_models.DescribeSagRemoteAccessRequest,
    ) -> main_models.DescribeSagRemoteAccessResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_remote_access_with_options(request, runtime)

    async def describe_sag_remote_access_async(
        self,
        request: main_models.DescribeSagRemoteAccessRequest,
    ) -> main_models.DescribeSagRemoteAccessResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_remote_access_with_options_async(request, runtime)

    def describe_sag_route_list_with_options(
        self,
        request: main_models.DescribeSagRouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_list_with_options_async(
        self,
        request: main_models.DescribeSagRouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_route_list(
        self,
        request: main_models.DescribeSagRouteListRequest,
    ) -> main_models.DescribeSagRouteListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_route_list_with_options(request, runtime)

    async def describe_sag_route_list_async(
        self,
        request: main_models.DescribeSagRouteListRequest,
    ) -> main_models.DescribeSagRouteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_route_list_with_options_async(request, runtime)

    def describe_sag_route_protocol_bgp_with_options(
        self,
        request: main_models.DescribeSagRouteProtocolBgpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteProtocolBgpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteProtocolBgp',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteProtocolBgpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_protocol_bgp_with_options_async(
        self,
        request: main_models.DescribeSagRouteProtocolBgpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteProtocolBgpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteProtocolBgp',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteProtocolBgpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_route_protocol_bgp(
        self,
        request: main_models.DescribeSagRouteProtocolBgpRequest,
    ) -> main_models.DescribeSagRouteProtocolBgpResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_route_protocol_bgp_with_options(request, runtime)

    async def describe_sag_route_protocol_bgp_async(
        self,
        request: main_models.DescribeSagRouteProtocolBgpRequest,
    ) -> main_models.DescribeSagRouteProtocolBgpResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_route_protocol_bgp_with_options_async(request, runtime)

    def describe_sag_route_protocol_ospf_with_options(
        self,
        request: main_models.DescribeSagRouteProtocolOspfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteProtocolOspfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteProtocolOspf',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteProtocolOspfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_route_protocol_ospf_with_options_async(
        self,
        request: main_models.DescribeSagRouteProtocolOspfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagRouteProtocolOspfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagRouteProtocolOspf',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagRouteProtocolOspfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_route_protocol_ospf(
        self,
        request: main_models.DescribeSagRouteProtocolOspfRequest,
    ) -> main_models.DescribeSagRouteProtocolOspfResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_route_protocol_ospf_with_options(request, runtime)

    async def describe_sag_route_protocol_ospf_async(
        self,
        request: main_models.DescribeSagRouteProtocolOspfRequest,
    ) -> main_models.DescribeSagRouteProtocolOspfResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_route_protocol_ospf_with_options_async(request, runtime)

    def describe_sag_static_route_list_with_options(
        self,
        request: main_models.DescribeSagStaticRouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagStaticRouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagStaticRouteList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagStaticRouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_static_route_list_with_options_async(
        self,
        request: main_models.DescribeSagStaticRouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagStaticRouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagStaticRouteList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagStaticRouteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_static_route_list(
        self,
        request: main_models.DescribeSagStaticRouteListRequest,
    ) -> main_models.DescribeSagStaticRouteListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_static_route_list_with_options(request, runtime)

    async def describe_sag_static_route_list_async(
        self,
        request: main_models.DescribeSagStaticRouteListRequest,
    ) -> main_models.DescribeSagStaticRouteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_static_route_list_with_options_async(request, runtime)

    def describe_sag_traffic_top_nwith_options(
        self,
        request: main_models.DescribeSagTrafficTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagTrafficTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagTrafficTopN',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagTrafficTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_traffic_top_nwith_options_async(
        self,
        request: main_models.DescribeSagTrafficTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagTrafficTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagTrafficTopN',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagTrafficTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_traffic_top_n(
        self,
        request: main_models.DescribeSagTrafficTopNRequest,
    ) -> main_models.DescribeSagTrafficTopNResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_traffic_top_nwith_options(request, runtime)

    async def describe_sag_traffic_top_n_async(
        self,
        request: main_models.DescribeSagTrafficTopNRequest,
    ) -> main_models.DescribeSagTrafficTopNResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_traffic_top_nwith_options_async(request, runtime)

    def describe_sag_user_dns_with_options(
        self,
        request: main_models.DescribeSagUserDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagUserDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagUserDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagUserDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_user_dns_with_options_async(
        self,
        request: main_models.DescribeSagUserDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagUserDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagUserDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagUserDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_user_dns(
        self,
        request: main_models.DescribeSagUserDnsRequest,
    ) -> main_models.DescribeSagUserDnsResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_user_dns_with_options(request, runtime)

    async def describe_sag_user_dns_async(
        self,
        request: main_models.DescribeSagUserDnsRequest,
    ) -> main_models.DescribeSagUserDnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_user_dns_with_options_async(request, runtime)

    def describe_sag_vbr_relations_with_options(
        self,
        request: main_models.DescribeSagVbrRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagVbrRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_ids):
            query['VbrInstanceIds'] = request.vbr_instance_ids
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagVbrRelations',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagVbrRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_vbr_relations_with_options_async(
        self,
        request: main_models.DescribeSagVbrRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagVbrRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_ids):
            query['VbrInstanceIds'] = request.vbr_instance_ids
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagVbrRelations',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagVbrRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_vbr_relations(
        self,
        request: main_models.DescribeSagVbrRelationsRequest,
    ) -> main_models.DescribeSagVbrRelationsResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_vbr_relations_with_options(request, runtime)

    async def describe_sag_vbr_relations_async(
        self,
        request: main_models.DescribeSagVbrRelationsRequest,
    ) -> main_models.DescribeSagVbrRelationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_vbr_relations_with_options_async(request, runtime)

    def describe_sag_wan_4gwith_options(
        self,
        request: main_models.DescribeSagWan4GRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWan4GResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWan4G',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWan4GResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_4gwith_options_async(
        self,
        request: main_models.DescribeSagWan4GRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWan4GResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWan4G',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWan4GResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_wan_4g(
        self,
        request: main_models.DescribeSagWan4GRequest,
    ) -> main_models.DescribeSagWan4GResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_wan_4gwith_options(request, runtime)

    async def describe_sag_wan_4g_async(
        self,
        request: main_models.DescribeSagWan4GRequest,
    ) -> main_models.DescribeSagWan4GResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_wan_4gwith_options_async(request, runtime)

    def describe_sag_wan_list_with_options(
        self,
        request: main_models.DescribeSagWanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWanList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_list_with_options_async(
        self,
        request: main_models.DescribeSagWanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWanList',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWanListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_wan_list(
        self,
        request: main_models.DescribeSagWanListRequest,
    ) -> main_models.DescribeSagWanListResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_wan_list_with_options(request, runtime)

    async def describe_sag_wan_list_async(
        self,
        request: main_models.DescribeSagWanListRequest,
    ) -> main_models.DescribeSagWanListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_wan_list_with_options_async(request, runtime)

    def describe_sag_wan_snat_with_options(
        self,
        request: main_models.DescribeSagWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wan_snat_with_options_async(
        self,
        request: main_models.DescribeSagWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_wan_snat(
        self,
        request: main_models.DescribeSagWanSnatRequest,
    ) -> main_models.DescribeSagWanSnatResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_wan_snat_with_options(request, runtime)

    async def describe_sag_wan_snat_async(
        self,
        request: main_models.DescribeSagWanSnatRequest,
    ) -> main_models.DescribeSagWanSnatResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_wan_snat_with_options_async(request, runtime)

    def describe_sag_wifi_with_options(
        self,
        request: main_models.DescribeSagWifiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWifiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWifi',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWifiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sag_wifi_with_options_async(
        self,
        request: main_models.DescribeSagWifiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSagWifiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSagWifi',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSagWifiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sag_wifi(
        self,
        request: main_models.DescribeSagWifiRequest,
    ) -> main_models.DescribeSagWifiResponse:
        runtime = RuntimeOptions()
        return self.describe_sag_wifi_with_options(request, runtime)

    async def describe_sag_wifi_async(
        self,
        request: main_models.DescribeSagWifiRequest,
    ) -> main_models.DescribeSagWifiResponse:
        runtime = RuntimeOptions()
        return await self.describe_sag_wifi_with_options_async(request, runtime)

    def describe_smart_access_gateway_attribute_with_options(
        self,
        request: main_models.DescribeSmartAccessGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_attribute_with_options_async(
        self,
        request: main_models.DescribeSmartAccessGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_access_gateway_attribute(
        self,
        request: main_models.DescribeSmartAccessGatewayAttributeRequest,
    ) -> main_models.DescribeSmartAccessGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_access_gateway_attribute_with_options(request, runtime)

    async def describe_smart_access_gateway_attribute_async(
        self,
        request: main_models.DescribeSmartAccessGatewayAttributeRequest,
    ) -> main_models.DescribeSmartAccessGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_access_gateway_attribute_with_options_async(request, runtime)

    def describe_smart_access_gateway_client_users_with_options(
        self,
        request: main_models.DescribeSmartAccessGatewayClientUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayClientUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_mail):
            query['UserMail'] = request.user_mail
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayClientUsers',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayClientUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_client_users_with_options_async(
        self,
        request: main_models.DescribeSmartAccessGatewayClientUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayClientUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_mail):
            query['UserMail'] = request.user_mail
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayClientUsers',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayClientUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_access_gateway_client_users(
        self,
        request: main_models.DescribeSmartAccessGatewayClientUsersRequest,
    ) -> main_models.DescribeSmartAccessGatewayClientUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_access_gateway_client_users_with_options(request, runtime)

    async def describe_smart_access_gateway_client_users_async(
        self,
        request: main_models.DescribeSmartAccessGatewayClientUsersRequest,
    ) -> main_models.DescribeSmartAccessGatewayClientUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_access_gateway_client_users_with_options_async(request, runtime)

    def describe_smart_access_gateway_ha_with_options(
        self,
        request: main_models.DescribeSmartAccessGatewayHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_ha_with_options_async(
        self,
        request: main_models.DescribeSmartAccessGatewayHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_access_gateway_ha(
        self,
        request: main_models.DescribeSmartAccessGatewayHaRequest,
    ) -> main_models.DescribeSmartAccessGatewayHaResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_access_gateway_ha_with_options(request, runtime)

    async def describe_smart_access_gateway_ha_async(
        self,
        request: main_models.DescribeSmartAccessGatewayHaRequest,
    ) -> main_models.DescribeSmartAccessGatewayHaResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_access_gateway_ha_with_options_async(request, runtime)

    def describe_smart_access_gateway_versions_with_options(
        self,
        request: main_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayVersions',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateway_versions_with_options_async(
        self,
        request: main_models.DescribeSmartAccessGatewayVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewayVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGatewayVersions',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewayVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_access_gateway_versions(
        self,
        request: main_models.DescribeSmartAccessGatewayVersionsRequest,
    ) -> main_models.DescribeSmartAccessGatewayVersionsResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_access_gateway_versions_with_options(request, runtime)

    async def describe_smart_access_gateway_versions_async(
        self,
        request: main_models.DescribeSmartAccessGatewayVersionsRequest,
    ) -> main_models.DescribeSmartAccessGatewayVersionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_access_gateway_versions_with_options_async(request, runtime)

    def describe_smart_access_gateways_with_options(
        self,
        request: main_models.DescribeSmartAccessGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not DaraCore.is_null(request.associated_ccn_name):
            query['AssociatedCcnName'] = request.associated_ccn_name
        if not DaraCore.is_null(request.business_state):
            query['BusinessState'] = request.business_state
        if not DaraCore.is_null(request.can_associate_qos):
            query['CanAssociateQos'] = request.can_associate_qos
        if not DaraCore.is_null(request.hardware_type):
            query['HardwareType'] = request.hardware_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        if not DaraCore.is_null(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unbound_acl_ids):
            query['UnboundAclIds'] = request.unbound_acl_ids
        if not DaraCore.is_null(request.version_comparator):
            query['VersionComparator'] = request.version_comparator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGateways',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_access_gateways_with_options_async(
        self,
        request: main_models.DescribeSmartAccessGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmartAccessGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.associated_ccn_id):
            query['AssociatedCcnId'] = request.associated_ccn_id
        if not DaraCore.is_null(request.associated_ccn_name):
            query['AssociatedCcnName'] = request.associated_ccn_name
        if not DaraCore.is_null(request.business_state):
            query['BusinessState'] = request.business_state
        if not DaraCore.is_null(request.can_associate_qos):
            query['CanAssociateQos'] = request.can_associate_qos
        if not DaraCore.is_null(request.hardware_type):
            query['HardwareType'] = request.hardware_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agids):
            query['SmartAGIds'] = request.smart_agids
        if not DaraCore.is_null(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unbound_acl_ids):
            query['UnboundAclIds'] = request.unbound_acl_ids
        if not DaraCore.is_null(request.version_comparator):
            query['VersionComparator'] = request.version_comparator
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmartAccessGateways',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmartAccessGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_access_gateways(
        self,
        request: main_models.DescribeSmartAccessGatewaysRequest,
    ) -> main_models.DescribeSmartAccessGatewaysResponse:
        runtime = RuntimeOptions()
        return self.describe_smart_access_gateways_with_options(request, runtime)

    async def describe_smart_access_gateways_async(
        self,
        request: main_models.DescribeSmartAccessGatewaysRequest,
    ) -> main_models.DescribeSmartAccessGatewaysResponse:
        runtime = RuntimeOptions()
        return await self.describe_smart_access_gateways_with_options_async(request, runtime)

    def describe_snat_entries_with_options(
        self,
        request: main_models.DescribeSnatEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnatEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnatEntries',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnatEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snat_entries_with_options_async(
        self,
        request: main_models.DescribeSnatEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnatEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnatEntries',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnatEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snat_entries(
        self,
        request: main_models.DescribeSnatEntriesRequest,
    ) -> main_models.DescribeSnatEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_snat_entries_with_options(request, runtime)

    async def describe_snat_entries_async(
        self,
        request: main_models.DescribeSnatEntriesRequest,
    ) -> main_models.DescribeSnatEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_snat_entries_with_options_async(request, runtime)

    def describe_unbind_flow_log_sags_with_options(
        self,
        request: main_models.DescribeUnbindFlowLogSagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnbindFlowLogSagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnbindFlowLogSags',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnbindFlowLogSagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unbind_flow_log_sags_with_options_async(
        self,
        request: main_models.DescribeUnbindFlowLogSagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnbindFlowLogSagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnbindFlowLogSags',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnbindFlowLogSagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_unbind_flow_log_sags(
        self,
        request: main_models.DescribeUnbindFlowLogSagsRequest,
    ) -> main_models.DescribeUnbindFlowLogSagsResponse:
        runtime = RuntimeOptions()
        return self.describe_unbind_flow_log_sags_with_options(request, runtime)

    async def describe_unbind_flow_log_sags_async(
        self,
        request: main_models.DescribeUnbindFlowLogSagsRequest,
    ) -> main_models.DescribeUnbindFlowLogSagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_unbind_flow_log_sags_with_options_async(request, runtime)

    def describe_user_flow_statistics_with_options(
        self,
        request: main_models.DescribeUserFlowStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserFlowStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.statistics_date):
            query['StatisticsDate'] = request.statistics_date
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserFlowStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserFlowStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_flow_statistics_with_options_async(
        self,
        request: main_models.DescribeUserFlowStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserFlowStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.statistics_date):
            query['StatisticsDate'] = request.statistics_date
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserFlowStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserFlowStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_flow_statistics(
        self,
        request: main_models.DescribeUserFlowStatisticsRequest,
    ) -> main_models.DescribeUserFlowStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_flow_statistics_with_options(request, runtime)

    async def describe_user_flow_statistics_async(
        self,
        request: main_models.DescribeUserFlowStatisticsRequest,
    ) -> main_models.DescribeUserFlowStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_flow_statistics_with_options_async(request, runtime)

    def describe_user_online_client_statistics_with_options(
        self,
        request: main_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserOnlineClientStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserOnlineClientStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserOnlineClientStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_online_client_statistics_with_options_async(
        self,
        request: main_models.DescribeUserOnlineClientStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserOnlineClientStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserOnlineClientStatistics',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserOnlineClientStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_online_client_statistics(
        self,
        request: main_models.DescribeUserOnlineClientStatisticsRequest,
    ) -> main_models.DescribeUserOnlineClientStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_online_client_statistics_with_options(request, runtime)

    async def describe_user_online_client_statistics_async(
        self,
        request: main_models.DescribeUserOnlineClientStatisticsRequest,
    ) -> main_models.DescribeUserOnlineClientStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_online_client_statistics_with_options_async(request, runtime)

    def describe_user_online_clients_with_options(
        self,
        request: main_models.DescribeUserOnlineClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserOnlineClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserOnlineClients',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserOnlineClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_online_clients_with_options_async(
        self,
        request: main_models.DescribeUserOnlineClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserOnlineClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserOnlineClients',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserOnlineClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_online_clients(
        self,
        request: main_models.DescribeUserOnlineClientsRequest,
    ) -> main_models.DescribeUserOnlineClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_online_clients_with_options(request, runtime)

    async def describe_user_online_clients_async(
        self,
        request: main_models.DescribeUserOnlineClientsRequest,
    ) -> main_models.DescribeUserOnlineClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_online_clients_with_options_async(request, runtime)

    def diagnose_smart_access_gateway_with_options(
        self,
        request: main_models.DiagnoseSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiagnoseSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiagnoseSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiagnoseSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def diagnose_smart_access_gateway_with_options_async(
        self,
        request: main_models.DiagnoseSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiagnoseSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiagnoseSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiagnoseSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def diagnose_smart_access_gateway(
        self,
        request: main_models.DiagnoseSmartAccessGatewayRequest,
    ) -> main_models.DiagnoseSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.diagnose_smart_access_gateway_with_options(request, runtime)

    async def diagnose_smart_access_gateway_async(
        self,
        request: main_models.DiagnoseSmartAccessGatewayRequest,
    ) -> main_models.DiagnoseSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.diagnose_smart_access_gateway_with_options_async(request, runtime)

    def disable_smart_agdpi_monitor_with_options(
        self,
        request: main_models.DisableSmartAGDpiMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmartAGDpiMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmartAGDpiMonitor',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmartAGDpiMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smart_agdpi_monitor_with_options_async(
        self,
        request: main_models.DisableSmartAGDpiMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmartAGDpiMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmartAGDpiMonitor',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmartAGDpiMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_smart_agdpi_monitor(
        self,
        request: main_models.DisableSmartAGDpiMonitorRequest,
    ) -> main_models.DisableSmartAGDpiMonitorResponse:
        runtime = RuntimeOptions()
        return self.disable_smart_agdpi_monitor_with_options(request, runtime)

    async def disable_smart_agdpi_monitor_async(
        self,
        request: main_models.DisableSmartAGDpiMonitorRequest,
    ) -> main_models.DisableSmartAGDpiMonitorResponse:
        runtime = RuntimeOptions()
        return await self.disable_smart_agdpi_monitor_with_options_async(request, runtime)

    def disable_smart_access_gateway_user_with_options(
        self,
        request: main_models.DisableSmartAccessGatewayUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmartAccessGatewayUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmartAccessGatewayUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmartAccessGatewayUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smart_access_gateway_user_with_options_async(
        self,
        request: main_models.DisableSmartAccessGatewayUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmartAccessGatewayUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmartAccessGatewayUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmartAccessGatewayUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_smart_access_gateway_user(
        self,
        request: main_models.DisableSmartAccessGatewayUserRequest,
    ) -> main_models.DisableSmartAccessGatewayUserResponse:
        runtime = RuntimeOptions()
        return self.disable_smart_access_gateway_user_with_options(request, runtime)

    async def disable_smart_access_gateway_user_async(
        self,
        request: main_models.DisableSmartAccessGatewayUserRequest,
    ) -> main_models.DisableSmartAccessGatewayUserResponse:
        runtime = RuntimeOptions()
        return await self.disable_smart_access_gateway_user_with_options_async(request, runtime)

    def disassociate_aclwith_options(
        self,
        request: main_models.DisassociateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_aclwith_options_async(
        self,
        request: main_models.DisassociateACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_acl(
        self,
        request: main_models.DisassociateACLRequest,
    ) -> main_models.DisassociateACLResponse:
        runtime = RuntimeOptions()
        return self.disassociate_aclwith_options(request, runtime)

    async def disassociate_acl_async(
        self,
        request: main_models.DisassociateACLRequest,
    ) -> main_models.DisassociateACLResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_aclwith_options_async(request, runtime)

    def disassociate_flow_log_with_options(
        self,
        request: main_models.DisassociateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_flow_log_with_options_async(
        self,
        request: main_models.DisassociateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateFlowLog',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_flow_log(
        self,
        request: main_models.DisassociateFlowLogRequest,
    ) -> main_models.DisassociateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.disassociate_flow_log_with_options(request, runtime)

    async def disassociate_flow_log_async(
        self,
        request: main_models.DisassociateFlowLogRequest,
    ) -> main_models.DisassociateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_flow_log_with_options_async(request, runtime)

    def disassociate_qos_with_options(
        self,
        request: main_models.DisassociateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_qos_with_options_async(
        self,
        request: main_models.DisassociateQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateQosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_qos(
        self,
        request: main_models.DisassociateQosRequest,
    ) -> main_models.DisassociateQosResponse:
        runtime = RuntimeOptions()
        return self.disassociate_qos_with_options(request, runtime)

    async def disassociate_qos_async(
        self,
        request: main_models.DisassociateQosRequest,
    ) -> main_models.DisassociateQosResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_qos_with_options_async(request, runtime)

    def discribe_smart_access_gateway_diagnosis_report_with_options(
        self,
        request: main_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiscribeSmartAccessGatewayDiagnosisReport',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def discribe_smart_access_gateway_diagnosis_report_with_options_async(
        self,
        request: main_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DiscribeSmartAccessGatewayDiagnosisReport',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def discribe_smart_access_gateway_diagnosis_report(
        self,
        request: main_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
    ) -> main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        runtime = RuntimeOptions()
        return self.discribe_smart_access_gateway_diagnosis_report_with_options(request, runtime)

    async def discribe_smart_access_gateway_diagnosis_report_async(
        self,
        request: main_models.DiscribeSmartAccessGatewayDiagnosisReportRequest,
    ) -> main_models.DiscribeSmartAccessGatewayDiagnosisReportResponse:
        runtime = RuntimeOptions()
        return await self.discribe_smart_access_gateway_diagnosis_report_with_options_async(request, runtime)

    def dissociate_smart_agfrom_application_bandwidth_package_with_options(
        self,
        request: main_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agid_list):
            query['SmartAGIdList'] = request.smart_agid_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateSmartAGFromApplicationBandwidthPackage',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_smart_agfrom_application_bandwidth_package_with_options_async(
        self,
        request: main_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_bandwidth_package_id):
            query['ApplicationBandwidthPackageId'] = request.application_bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agid_list):
            query['SmartAGIdList'] = request.smart_agid_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateSmartAGFromApplicationBandwidthPackage',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_smart_agfrom_application_bandwidth_package(
        self,
        request: main_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
    ) -> main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.dissociate_smart_agfrom_application_bandwidth_package_with_options(request, runtime)

    async def dissociate_smart_agfrom_application_bandwidth_package_async(
        self,
        request: main_models.DissociateSmartAGFromApplicationBandwidthPackageRequest,
    ) -> main_models.DissociateSmartAGFromApplicationBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_smart_agfrom_application_bandwidth_package_with_options_async(request, runtime)

    def downgrade_smart_access_gateway_with_options(
        self,
        request: main_models.DowngradeSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_smart_access_gateway_with_options_async(
        self,
        request: main_models.DowngradeSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_smart_access_gateway(
        self,
        request: main_models.DowngradeSmartAccessGatewayRequest,
    ) -> main_models.DowngradeSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.downgrade_smart_access_gateway_with_options(request, runtime)

    async def downgrade_smart_access_gateway_async(
        self,
        request: main_models.DowngradeSmartAccessGatewayRequest,
    ) -> main_models.DowngradeSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.downgrade_smart_access_gateway_with_options_async(request, runtime)

    def downgrade_smart_access_gateway_software_with_options(
        self,
        request: main_models.DowngradeSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_smart_access_gateway_software_with_options_async(
        self,
        request: main_models.DowngradeSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_smart_access_gateway_software(
        self,
        request: main_models.DowngradeSmartAccessGatewaySoftwareRequest,
    ) -> main_models.DowngradeSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return self.downgrade_smart_access_gateway_software_with_options(request, runtime)

    async def downgrade_smart_access_gateway_software_async(
        self,
        request: main_models.DowngradeSmartAccessGatewaySoftwareRequest,
    ) -> main_models.DowngradeSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return await self.downgrade_smart_access_gateway_software_with_options_async(request, runtime)

    def enable_smart_agdpi_monitor_with_options(
        self,
        request: main_models.EnableSmartAGDpiMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmartAGDpiMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmartAGDpiMonitor',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmartAGDpiMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smart_agdpi_monitor_with_options_async(
        self,
        request: main_models.EnableSmartAGDpiMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmartAGDpiMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmartAGDpiMonitor',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmartAGDpiMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_smart_agdpi_monitor(
        self,
        request: main_models.EnableSmartAGDpiMonitorRequest,
    ) -> main_models.EnableSmartAGDpiMonitorResponse:
        runtime = RuntimeOptions()
        return self.enable_smart_agdpi_monitor_with_options(request, runtime)

    async def enable_smart_agdpi_monitor_async(
        self,
        request: main_models.EnableSmartAGDpiMonitorRequest,
    ) -> main_models.EnableSmartAGDpiMonitorResponse:
        runtime = RuntimeOptions()
        return await self.enable_smart_agdpi_monitor_with_options_async(request, runtime)

    def enable_smart_access_gateway_user_with_options(
        self,
        request: main_models.EnableSmartAccessGatewayUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmartAccessGatewayUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmartAccessGatewayUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmartAccessGatewayUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smart_access_gateway_user_with_options_async(
        self,
        request: main_models.EnableSmartAccessGatewayUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmartAccessGatewayUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmartAccessGatewayUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmartAccessGatewayUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_smart_access_gateway_user(
        self,
        request: main_models.EnableSmartAccessGatewayUserRequest,
    ) -> main_models.EnableSmartAccessGatewayUserResponse:
        runtime = RuntimeOptions()
        return self.enable_smart_access_gateway_user_with_options(request, runtime)

    async def enable_smart_access_gateway_user_async(
        self,
        request: main_models.EnableSmartAccessGatewayUserRequest,
    ) -> main_models.EnableSmartAccessGatewayUserResponse:
        runtime = RuntimeOptions()
        return await self.enable_smart_access_gateway_user_with_options_async(request, runtime)

    def get_acl_attribute_with_options(
        self,
        request: main_models.GetAclAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAclAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAclAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acl_attribute_with_options_async(
        self,
        request: main_models.GetAclAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAclAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAclAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAclAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_acl_attribute(
        self,
        request: main_models.GetAclAttributeRequest,
    ) -> main_models.GetAclAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_acl_attribute_with_options(request, runtime)

    async def get_acl_attribute_async(
        self,
        request: main_models.GetAclAttributeRequest,
    ) -> main_models.GetAclAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_acl_attribute_with_options_async(request, runtime)

    def get_advanced_monitor_state_with_options(
        self,
        request: main_models.GetAdvancedMonitorStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedMonitorStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdvancedMonitorState',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedMonitorStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_monitor_state_with_options_async(
        self,
        request: main_models.GetAdvancedMonitorStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedMonitorStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdvancedMonitorState',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedMonitorStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_monitor_state(
        self,
        request: main_models.GetAdvancedMonitorStateRequest,
    ) -> main_models.GetAdvancedMonitorStateResponse:
        runtime = RuntimeOptions()
        return self.get_advanced_monitor_state_with_options(request, runtime)

    async def get_advanced_monitor_state_async(
        self,
        request: main_models.GetAdvancedMonitorStateRequest,
    ) -> main_models.GetAdvancedMonitorStateResponse:
        runtime = RuntimeOptions()
        return await self.get_advanced_monitor_state_with_options_async(request, runtime)

    def get_cloud_connect_network_use_limit_with_options(
        self,
        request: main_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudConnectNetworkUseLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudConnectNetworkUseLimit',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudConnectNetworkUseLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_connect_network_use_limit_with_options_async(
        self,
        request: main_models.GetCloudConnectNetworkUseLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudConnectNetworkUseLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudConnectNetworkUseLimit',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudConnectNetworkUseLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_connect_network_use_limit(
        self,
        request: main_models.GetCloudConnectNetworkUseLimitRequest,
    ) -> main_models.GetCloudConnectNetworkUseLimitResponse:
        runtime = RuntimeOptions()
        return self.get_cloud_connect_network_use_limit_with_options(request, runtime)

    async def get_cloud_connect_network_use_limit_async(
        self,
        request: main_models.GetCloudConnectNetworkUseLimitRequest,
    ) -> main_models.GetCloudConnectNetworkUseLimitResponse:
        runtime = RuntimeOptions()
        return await self.get_cloud_connect_network_use_limit_with_options_async(request, runtime)

    def get_qos_attribute_with_options(
        self,
        request: main_models.GetQosAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQosAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQosAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQosAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qos_attribute_with_options_async(
        self,
        request: main_models.GetQosAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQosAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQosAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQosAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qos_attribute(
        self,
        request: main_models.GetQosAttributeRequest,
    ) -> main_models.GetQosAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_qos_attribute_with_options(request, runtime)

    async def get_qos_attribute_async(
        self,
        request: main_models.GetQosAttributeRequest,
    ) -> main_models.GetQosAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_qos_attribute_with_options_async(request, runtime)

    def get_smart_agdpi_attribute_with_options(
        self,
        request: main_models.GetSmartAGDpiAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAGDpiAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAGDpiAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAGDpiAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_agdpi_attribute_with_options_async(
        self,
        request: main_models.GetSmartAGDpiAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAGDpiAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAGDpiAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAGDpiAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_agdpi_attribute(
        self,
        request: main_models.GetSmartAGDpiAttributeRequest,
    ) -> main_models.GetSmartAGDpiAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_smart_agdpi_attribute_with_options(request, runtime)

    async def get_smart_agdpi_attribute_async(
        self,
        request: main_models.GetSmartAGDpiAttributeRequest,
    ) -> main_models.GetSmartAGDpiAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_smart_agdpi_attribute_with_options_async(request, runtime)

    def get_smart_access_gateway_use_limit_with_options(
        self,
        request: main_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAccessGatewayUseLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAccessGatewayUseLimit',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAccessGatewayUseLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_access_gateway_use_limit_with_options_async(
        self,
        request: main_models.GetSmartAccessGatewayUseLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAccessGatewayUseLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAccessGatewayUseLimit',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAccessGatewayUseLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_access_gateway_use_limit(
        self,
        request: main_models.GetSmartAccessGatewayUseLimitRequest,
    ) -> main_models.GetSmartAccessGatewayUseLimitResponse:
        runtime = RuntimeOptions()
        return self.get_smart_access_gateway_use_limit_with_options(request, runtime)

    async def get_smart_access_gateway_use_limit_async(
        self,
        request: main_models.GetSmartAccessGatewayUseLimitRequest,
    ) -> main_models.GetSmartAccessGatewayUseLimitResponse:
        runtime = RuntimeOptions()
        return await self.get_smart_access_gateway_use_limit_with_options_async(request, runtime)

    def grant_instance_to_cbn_with_options(
        self,
        request: main_models.GrantInstanceToCbnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToCbnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not DaraCore.is_null(request.cen_uid):
            query['CenUid'] = request.cen_uid
        if not DaraCore.is_null(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToCbn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToCbnResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_instance_to_cbn_with_options_async(
        self,
        request: main_models.GrantInstanceToCbnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToCbnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not DaraCore.is_null(request.cen_uid):
            query['CenUid'] = request.cen_uid
        if not DaraCore.is_null(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToCbn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToCbnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_instance_to_cbn(
        self,
        request: main_models.GrantInstanceToCbnRequest,
    ) -> main_models.GrantInstanceToCbnResponse:
        runtime = RuntimeOptions()
        return self.grant_instance_to_cbn_with_options(request, runtime)

    async def grant_instance_to_cbn_async(
        self,
        request: main_models.GrantInstanceToCbnRequest,
    ) -> main_models.GrantInstanceToCbnResponse:
        runtime = RuntimeOptions()
        return await self.grant_instance_to_cbn_with_options_async(request, runtime)

    def grant_sag_instance_to_ccn_with_options(
        self,
        request: main_models.GrantSagInstanceToCcnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantSagInstanceToCcnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.ccn_uid):
            query['CcnUid'] = request.ccn_uid
        if not DaraCore.is_null(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantSagInstanceToCcn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSagInstanceToCcnResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_sag_instance_to_ccn_with_options_async(
        self,
        request: main_models.GrantSagInstanceToCcnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantSagInstanceToCcnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.ccn_uid):
            query['CcnUid'] = request.ccn_uid
        if not DaraCore.is_null(request.grant_traffic_service):
            query['GrantTrafficService'] = request.grant_traffic_service
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantSagInstanceToCcn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSagInstanceToCcnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_sag_instance_to_ccn(
        self,
        request: main_models.GrantSagInstanceToCcnRequest,
    ) -> main_models.GrantSagInstanceToCcnResponse:
        runtime = RuntimeOptions()
        return self.grant_sag_instance_to_ccn_with_options(request, runtime)

    async def grant_sag_instance_to_ccn_async(
        self,
        request: main_models.GrantSagInstanceToCcnRequest,
    ) -> main_models.GrantSagInstanceToCcnResponse:
        runtime = RuntimeOptions()
        return await self.grant_sag_instance_to_ccn_with_options_async(request, runtime)

    def grant_sag_instance_to_vbr_with_options(
        self,
        request: main_models.GrantSagInstanceToVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantSagInstanceToVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        if not DaraCore.is_null(request.vbr_uid):
            query['VbrUid'] = request.vbr_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantSagInstanceToVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSagInstanceToVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_sag_instance_to_vbr_with_options_async(
        self,
        request: main_models.GrantSagInstanceToVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantSagInstanceToVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        if not DaraCore.is_null(request.vbr_uid):
            query['VbrUid'] = request.vbr_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantSagInstanceToVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSagInstanceToVbrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_sag_instance_to_vbr(
        self,
        request: main_models.GrantSagInstanceToVbrRequest,
    ) -> main_models.GrantSagInstanceToVbrResponse:
        runtime = RuntimeOptions()
        return self.grant_sag_instance_to_vbr_with_options(request, runtime)

    async def grant_sag_instance_to_vbr_async(
        self,
        request: main_models.GrantSagInstanceToVbrRequest,
    ) -> main_models.GrantSagInstanceToVbrResponse:
        runtime = RuntimeOptions()
        return await self.grant_sag_instance_to_vbr_with_options_async(request, runtime)

    def kick_out_clients_with_options(
        self,
        request: main_models.KickOutClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickOutClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickOutClients',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickOutClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_out_clients_with_options_async(
        self,
        request: main_models.KickOutClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickOutClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickOutClients',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickOutClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_out_clients(
        self,
        request: main_models.KickOutClientsRequest,
    ) -> main_models.KickOutClientsResponse:
        runtime = RuntimeOptions()
        return self.kick_out_clients_with_options(request, runtime)

    async def kick_out_clients_async(
        self,
        request: main_models.KickOutClientsRequest,
    ) -> main_models.KickOutClientsResponse:
        runtime = RuntimeOptions()
        return await self.kick_out_clients_with_options_async(request, runtime)

    def list_access_point_network_qualities_with_options(
        self,
        request: main_models.ListAccessPointNetworkQualitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessPointNetworkQualitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessPointNetworkQualities',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessPointNetworkQualitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_point_network_qualities_with_options_async(
        self,
        request: main_models.ListAccessPointNetworkQualitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessPointNetworkQualitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessPointNetworkQualities',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessPointNetworkQualitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_point_network_qualities(
        self,
        request: main_models.ListAccessPointNetworkQualitiesRequest,
    ) -> main_models.ListAccessPointNetworkQualitiesResponse:
        runtime = RuntimeOptions()
        return self.list_access_point_network_qualities_with_options(request, runtime)

    async def list_access_point_network_qualities_async(
        self,
        request: main_models.ListAccessPointNetworkQualitiesRequest,
    ) -> main_models.ListAccessPointNetworkQualitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_access_point_network_qualities_with_options_async(request, runtime)

    def list_access_points_with_options(
        self,
        request: main_models.ListAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessPoints',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_points_with_options_async(
        self,
        request: main_models.ListAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessPoints',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_points(
        self,
        request: main_models.ListAccessPointsRequest,
    ) -> main_models.ListAccessPointsResponse:
        runtime = RuntimeOptions()
        return self.list_access_points_with_options(request, runtime)

    async def list_access_points_async(
        self,
        request: main_models.ListAccessPointsRequest,
    ) -> main_models.ListAccessPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_access_points_with_options_async(request, runtime)

    def list_available_service_address_with_options(
        self,
        request: main_models.ListAvailableServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableServiceAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_service_address_with_options_async(
        self,
        request: main_models.ListAvailableServiceAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableServiceAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableServiceAddress',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableServiceAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_service_address(
        self,
        request: main_models.ListAvailableServiceAddressRequest,
    ) -> main_models.ListAvailableServiceAddressResponse:
        runtime = RuntimeOptions()
        return self.list_available_service_address_with_options(request, runtime)

    async def list_available_service_address_async(
        self,
        request: main_models.ListAvailableServiceAddressRequest,
    ) -> main_models.ListAvailableServiceAddressResponse:
        runtime = RuntimeOptions()
        return await self.list_available_service_address_with_options_async(request, runtime)

    def list_dpi_config_error_with_options(
        self,
        request: main_models.ListDpiConfigErrorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiConfigErrorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_config_type):
            query['DpiConfigType'] = request.dpi_config_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_instance_id):
            query['RuleInstanceId'] = request.rule_instance_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiConfigError',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiConfigErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_config_error_with_options_async(
        self,
        request: main_models.ListDpiConfigErrorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiConfigErrorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_config_type):
            query['DpiConfigType'] = request.dpi_config_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_instance_id):
            query['RuleInstanceId'] = request.rule_instance_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiConfigError',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiConfigErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dpi_config_error(
        self,
        request: main_models.ListDpiConfigErrorRequest,
    ) -> main_models.ListDpiConfigErrorResponse:
        runtime = RuntimeOptions()
        return self.list_dpi_config_error_with_options(request, runtime)

    async def list_dpi_config_error_async(
        self,
        request: main_models.ListDpiConfigErrorRequest,
    ) -> main_models.ListDpiConfigErrorResponse:
        runtime = RuntimeOptions()
        return await self.list_dpi_config_error_with_options_async(request, runtime)

    def list_dpi_groups_with_options(
        self,
        request: main_models.ListDpiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_group_names):
            query['DpiGroupNames'] = request.dpi_group_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiGroups',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_groups_with_options_async(
        self,
        request: main_models.ListDpiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_group_names):
            query['DpiGroupNames'] = request.dpi_group_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiGroups',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dpi_groups(
        self,
        request: main_models.ListDpiGroupsRequest,
    ) -> main_models.ListDpiGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_dpi_groups_with_options(request, runtime)

    async def list_dpi_groups_async(
        self,
        request: main_models.ListDpiGroupsRequest,
    ) -> main_models.ListDpiGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_dpi_groups_with_options_async(request, runtime)

    def list_dpi_signatures_with_options(
        self,
        request: main_models.ListDpiSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_group_id):
            query['DpiGroupId'] = request.dpi_group_id
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.dpi_signature_names):
            query['DpiSignatureNames'] = request.dpi_signature_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiSignatures',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dpi_signatures_with_options_async(
        self,
        request: main_models.ListDpiSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDpiSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dpi_group_id):
            query['DpiGroupId'] = request.dpi_group_id
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.dpi_signature_names):
            query['DpiSignatureNames'] = request.dpi_signature_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDpiSignatures',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDpiSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dpi_signatures(
        self,
        request: main_models.ListDpiSignaturesRequest,
    ) -> main_models.ListDpiSignaturesResponse:
        runtime = RuntimeOptions()
        return self.list_dpi_signatures_with_options(request, runtime)

    async def list_dpi_signatures_async(
        self,
        request: main_models.ListDpiSignaturesRequest,
    ) -> main_models.ListDpiSignaturesResponse:
        runtime = RuntimeOptions()
        return await self.list_dpi_signatures_with_options_async(request, runtime)

    def list_enterprise_code_with_options(
        self,
        request: main_models.ListEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_code_with_options_async(
        self,
        request: main_models.ListEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_code(
        self,
        request: main_models.ListEnterpriseCodeRequest,
    ) -> main_models.ListEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return self.list_enterprise_code_with_options(request, runtime)

    async def list_enterprise_code_async(
        self,
        request: main_models.ListEnterpriseCodeRequest,
    ) -> main_models.ListEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return await self.list_enterprise_code_with_options_async(request, runtime)

    def list_probe_task_with_options(
        self,
        request: main_models.ListProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sag_name):
            query['SagName'] = request.sag_name
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_probe_task_with_options_async(
        self,
        request: main_models.ListProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sag_name):
            query['SagName'] = request.sag_name
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_probe_task(
        self,
        request: main_models.ListProbeTaskRequest,
    ) -> main_models.ListProbeTaskResponse:
        runtime = RuntimeOptions()
        return self.list_probe_task_with_options(request, runtime)

    async def list_probe_task_async(
        self,
        request: main_models.ListProbeTaskRequest,
    ) -> main_models.ListProbeTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_probe_task_with_options_async(request, runtime)

    def list_smart_agapi_unsupported_feature_with_options(
        self,
        request: main_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmartAGApiUnsupportedFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_api_name):
            query['OpenApiName'] = request.open_api_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmartAGApiUnsupportedFeature',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmartAGApiUnsupportedFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_smart_agapi_unsupported_feature_with_options_async(
        self,
        request: main_models.ListSmartAGApiUnsupportedFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmartAGApiUnsupportedFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_api_name):
            query['OpenApiName'] = request.open_api_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmartAGApiUnsupportedFeature',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmartAGApiUnsupportedFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_smart_agapi_unsupported_feature(
        self,
        request: main_models.ListSmartAGApiUnsupportedFeatureRequest,
    ) -> main_models.ListSmartAGApiUnsupportedFeatureResponse:
        runtime = RuntimeOptions()
        return self.list_smart_agapi_unsupported_feature_with_options(request, runtime)

    async def list_smart_agapi_unsupported_feature_async(
        self,
        request: main_models.ListSmartAGApiUnsupportedFeatureRequest,
    ) -> main_models.ListSmartAGApiUnsupportedFeatureResponse:
        runtime = RuntimeOptions()
        return await self.list_smart_agapi_unsupported_feature_with_options_async(request, runtime)

    def list_smart_agby_access_point_with_options(
        self,
        request: main_models.ListSmartAGByAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmartAGByAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agstatus):
            query['SmartAGStatus'] = request.smart_agstatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmartAGByAccessPoint',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmartAGByAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_smart_agby_access_point_with_options_async(
        self,
        request: main_models.ListSmartAGByAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmartAGByAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agstatus):
            query['SmartAGStatus'] = request.smart_agstatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmartAGByAccessPoint',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmartAGByAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_smart_agby_access_point(
        self,
        request: main_models.ListSmartAGByAccessPointRequest,
    ) -> main_models.ListSmartAGByAccessPointResponse:
        runtime = RuntimeOptions()
        return self.list_smart_agby_access_point_with_options(request, runtime)

    async def list_smart_agby_access_point_async(
        self,
        request: main_models.ListSmartAGByAccessPointRequest,
    ) -> main_models.ListSmartAGByAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.list_smart_agby_access_point_with_options_async(request, runtime)

    def modify_aclwith_options(
        self,
        request: main_models.ModifyACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aclwith_options_async(
        self,
        request: main_models.ModifyACLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyACL',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_acl(
        self,
        request: main_models.ModifyACLRequest,
    ) -> main_models.ModifyACLResponse:
        runtime = RuntimeOptions()
        return self.modify_aclwith_options(request, runtime)

    async def modify_acl_async(
        self,
        request: main_models.ModifyACLRequest,
    ) -> main_models.ModifyACLResponse:
        runtime = RuntimeOptions()
        return await self.modify_aclwith_options_async(request, runtime)

    def modify_aclrule_with_options(
        self,
        request: main_models.ModifyACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acr_id):
            query['AcrId'] = request.acr_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyACLRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aclrule_with_options_async(
        self,
        request: main_models.ModifyACLRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyACLRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acr_id):
            query['AcrId'] = request.acr_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyACLRule',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyACLRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_aclrule(
        self,
        request: main_models.ModifyACLRuleRequest,
    ) -> main_models.ModifyACLRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_aclrule_with_options(request, runtime)

    async def modify_aclrule_async(
        self,
        request: main_models.ModifyACLRuleRequest,
    ) -> main_models.ModifyACLRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_aclrule_with_options_async(request, runtime)

    def modify_client_user_dnswith_options(
        self,
        request: main_models.ModifyClientUserDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClientUserDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_dns):
            query['AppDNS'] = request.app_dns
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recovered_dns):
            query['RecoveredDNS'] = request.recovered_dns
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClientUserDNS',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClientUserDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_client_user_dnswith_options_async(
        self,
        request: main_models.ModifyClientUserDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClientUserDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_dns):
            query['AppDNS'] = request.app_dns
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recovered_dns):
            query['RecoveredDNS'] = request.recovered_dns
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClientUserDNS',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClientUserDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_client_user_dns(
        self,
        request: main_models.ModifyClientUserDNSRequest,
    ) -> main_models.ModifyClientUserDNSResponse:
        runtime = RuntimeOptions()
        return self.modify_client_user_dnswith_options(request, runtime)

    async def modify_client_user_dns_async(
        self,
        request: main_models.ModifyClientUserDNSRequest,
    ) -> main_models.ModifyClientUserDNSResponse:
        runtime = RuntimeOptions()
        return await self.modify_client_user_dnswith_options_async(request, runtime)

    def modify_cloud_connect_network_with_options(
        self,
        request: main_models.ModifyCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.interworking_status):
            query['InterworkingStatus'] = request.interworking_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudConnectNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_connect_network_with_options_async(
        self,
        request: main_models.ModifyCloudConnectNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudConnectNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.interworking_status):
            query['InterworkingStatus'] = request.interworking_status
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudConnectNetwork',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudConnectNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_connect_network(
        self,
        request: main_models.ModifyCloudConnectNetworkRequest,
    ) -> main_models.ModifyCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return self.modify_cloud_connect_network_with_options(request, runtime)

    async def modify_cloud_connect_network_async(
        self,
        request: main_models.ModifyCloudConnectNetworkRequest,
    ) -> main_models.ModifyCloudConnectNetworkResponse:
        runtime = RuntimeOptions()
        return await self.modify_cloud_connect_network_with_options_async(request, runtime)

    def modify_device_auto_upgrade_policy_with_options(
        self,
        request: main_models.ModifyDeviceAutoUpgradePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceAutoUpgradePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceAutoUpgradePolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceAutoUpgradePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_auto_upgrade_policy_with_options_async(
        self,
        request: main_models.ModifyDeviceAutoUpgradePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceAutoUpgradePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceAutoUpgradePolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceAutoUpgradePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_auto_upgrade_policy(
        self,
        request: main_models.ModifyDeviceAutoUpgradePolicyRequest,
    ) -> main_models.ModifyDeviceAutoUpgradePolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_device_auto_upgrade_policy_with_options(request, runtime)

    async def modify_device_auto_upgrade_policy_async(
        self,
        request: main_models.ModifyDeviceAutoUpgradePolicyRequest,
    ) -> main_models.ModifyDeviceAutoUpgradePolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_auto_upgrade_policy_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not DaraCore.is_null(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not DaraCore.is_null(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not DaraCore.is_null(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_aging):
            query['ActiveAging'] = request.active_aging
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.inactive_aging):
            query['InactiveAging'] = request.inactive_aging
        if not DaraCore.is_null(request.logstore_name):
            query['LogstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.netflow_server_ip):
            query['NetflowServerIp'] = request.netflow_server_ip
        if not DaraCore.is_null(request.netflow_server_port):
            query['NetflowServerPort'] = request.netflow_server_port
        if not DaraCore.is_null(request.netflow_version):
            query['NetflowVersion'] = request.netflow_version
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def modify_health_check_with_options(
        self,
        request: main_models.ModifyHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not DaraCore.is_null(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not DaraCore.is_null(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not DaraCore.is_null(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_health_check_with_options_async(
        self,
        request: main_models.ModifyHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_ip_addr):
            query['DstIpAddr'] = request.dst_ip_addr
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.fail_count_threshold):
            query['FailCountThreshold'] = request.fail_count_threshold
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.probe_count):
            query['ProbeCount'] = request.probe_count
        if not DaraCore.is_null(request.probe_interval):
            query['ProbeInterval'] = request.probe_interval
        if not DaraCore.is_null(request.probe_timeout):
            query['ProbeTimeout'] = request.probe_timeout
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rtt_fail_threshold):
            query['RttFailThreshold'] = request.rtt_fail_threshold
        if not DaraCore.is_null(request.rtt_threshold):
            query['RttThreshold'] = request.rtt_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.src_ip_addr):
            query['SrcIpAddr'] = request.src_ip_addr
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHealthCheck',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_health_check(
        self,
        request: main_models.ModifyHealthCheckRequest,
    ) -> main_models.ModifyHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.modify_health_check_with_options(request, runtime)

    async def modify_health_check_async(
        self,
        request: main_models.ModifyHealthCheckRequest,
    ) -> main_models.ModifyHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.modify_health_check_with_options_async(request, runtime)

    def modify_qos_with_options(
        self,
        request: main_models.ModifyQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_with_options_async(
        self,
        request: main_models.ModifyQosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_description):
            query['QosDescription'] = request.qos_description
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_name):
            query['QosName'] = request.qos_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQos',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qos(
        self,
        request: main_models.ModifyQosRequest,
    ) -> main_models.ModifyQosResponse:
        runtime = RuntimeOptions()
        return self.modify_qos_with_options(request, runtime)

    async def modify_qos_async(
        self,
        request: main_models.ModifyQosRequest,
    ) -> main_models.ModifyQosResponse:
        runtime = RuntimeOptions()
        return await self.modify_qos_with_options_async(request, runtime)

    def modify_qos_car_with_options(
        self,
        request: main_models.ModifyQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not DaraCore.is_null(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not DaraCore.is_null(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not DaraCore.is_null(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosCarResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_car_with_options_async(
        self,
        request: main_models.ModifyQosCarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosCarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.limit_type):
            query['LimitType'] = request.limit_type
        if not DaraCore.is_null(request.max_bandwidth_abs):
            query['MaxBandwidthAbs'] = request.max_bandwidth_abs
        if not DaraCore.is_null(request.max_bandwidth_percent):
            query['MaxBandwidthPercent'] = request.max_bandwidth_percent
        if not DaraCore.is_null(request.min_bandwidth_abs):
            query['MinBandwidthAbs'] = request.min_bandwidth_abs
        if not DaraCore.is_null(request.min_bandwidth_percent):
            query['MinBandwidthPercent'] = request.min_bandwidth_percent
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.percent_source_type):
            query['PercentSourceType'] = request.percent_source_type
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_car_id):
            query['QosCarId'] = request.qos_car_id
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosCar',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosCarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qos_car(
        self,
        request: main_models.ModifyQosCarRequest,
    ) -> main_models.ModifyQosCarResponse:
        runtime = RuntimeOptions()
        return self.modify_qos_car_with_options(request, runtime)

    async def modify_qos_car_async(
        self,
        request: main_models.ModifyQosCarRequest,
    ) -> main_models.ModifyQosCarResponse:
        runtime = RuntimeOptions()
        return await self.modify_qos_car_with_options_async(request, runtime)

    def modify_qos_policy_with_options(
        self,
        request: main_models.ModifyQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_policy_with_options_async(
        self,
        request: main_models.ModifyQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_cidr):
            query['DestCidr'] = request.dest_cidr
        if not DaraCore.is_null(request.dest_port_range):
            query['DestPortRange'] = request.dest_port_range
        if not DaraCore.is_null(request.dpi_group_ids):
            query['DpiGroupIds'] = request.dpi_group_ids
        if not DaraCore.is_null(request.dpi_signature_ids):
            query['DpiSignatureIds'] = request.dpi_signature_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.qos_id):
            query['QosId'] = request.qos_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not DaraCore.is_null(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosPolicy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qos_policy(
        self,
        request: main_models.ModifyQosPolicyRequest,
    ) -> main_models.ModifyQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_qos_policy_with_options(request, runtime)

    async def modify_qos_policy_async(
        self,
        request: main_models.ModifyQosPolicyRequest,
    ) -> main_models.ModifyQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_qos_policy_with_options_async(request, runtime)

    def modify_route_distribution_strategy_with_options(
        self,
        request: main_models.ModifyRouteDistributionStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRouteDistributionStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_distribution):
            query['RouteDistribution'] = request.route_distribution
        if not DaraCore.is_null(request.route_source):
            query['RouteSource'] = request.route_source
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRouteDistributionStrategy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRouteDistributionStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_route_distribution_strategy_with_options_async(
        self,
        request: main_models.ModifyRouteDistributionStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRouteDistributionStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_cidr_block):
            query['DestCidrBlock'] = request.dest_cidr_block
        if not DaraCore.is_null(request.hc_instance_id):
            query['HcInstanceId'] = request.hc_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_distribution):
            query['RouteDistribution'] = request.route_distribution
        if not DaraCore.is_null(request.route_source):
            query['RouteSource'] = request.route_source
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRouteDistributionStrategy',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRouteDistributionStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_route_distribution_strategy(
        self,
        request: main_models.ModifyRouteDistributionStrategyRequest,
    ) -> main_models.ModifyRouteDistributionStrategyResponse:
        runtime = RuntimeOptions()
        return self.modify_route_distribution_strategy_with_options(request, runtime)

    async def modify_route_distribution_strategy_async(
        self,
        request: main_models.ModifyRouteDistributionStrategyRequest,
    ) -> main_models.ModifyRouteDistributionStrategyResponse:
        runtime = RuntimeOptions()
        return await self.modify_route_distribution_strategy_with_options_async(request, runtime)

    def modify_sagadmin_password_with_options(
        self,
        request: main_models.ModifySAGAdminPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySAGAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySAGAdminPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySAGAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sagadmin_password_with_options_async(
        self,
        request: main_models.ModifySAGAdminPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySAGAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySAGAdminPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySAGAdminPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sagadmin_password(
        self,
        request: main_models.ModifySAGAdminPasswordRequest,
    ) -> main_models.ModifySAGAdminPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_sagadmin_password_with_options(request, runtime)

    async def modify_sagadmin_password_async(
        self,
        request: main_models.ModifySAGAdminPasswordRequest,
    ) -> main_models.ModifySAGAdminPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_sagadmin_password_with_options_async(request, runtime)

    def modify_sag_express_connect_interface_with_options(
        self,
        request: main_models.ModifySagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagExpressConnectInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_express_connect_interface_with_options_async(
        self,
        request: main_models.ModifySagExpressConnectInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagExpressConnectInterfaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagExpressConnectInterface',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagExpressConnectInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_express_connect_interface(
        self,
        request: main_models.ModifySagExpressConnectInterfaceRequest,
    ) -> main_models.ModifySagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_express_connect_interface_with_options(request, runtime)

    async def modify_sag_express_connect_interface_async(
        self,
        request: main_models.ModifySagExpressConnectInterfaceRequest,
    ) -> main_models.ModifySagExpressConnectInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_express_connect_interface_with_options_async(request, runtime)

    def modify_sag_global_route_protocol_with_options(
        self,
        request: main_models.ModifySagGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_global_route_protocol_with_options_async(
        self,
        request: main_models.ModifySagGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_global_route_protocol(
        self,
        request: main_models.ModifySagGlobalRouteProtocolRequest,
    ) -> main_models.ModifySagGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_global_route_protocol_with_options(request, runtime)

    async def modify_sag_global_route_protocol_async(
        self,
        request: main_models.ModifySagGlobalRouteProtocolRequest,
    ) -> main_models.ModifySagGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_global_route_protocol_with_options_async(request, runtime)

    def modify_sag_ha_with_options(
        self,
        request: main_models.ModifySagHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.virtual_ip):
            query['VirtualIp'] = request.virtual_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_ha_with_options_async(
        self,
        request: main_models.ModifySagHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.virtual_ip):
            query['VirtualIp'] = request.virtual_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagHa',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_ha(
        self,
        request: main_models.ModifySagHaRequest,
    ) -> main_models.ModifySagHaResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_ha_with_options(request, runtime)

    async def modify_sag_ha_async(
        self,
        request: main_models.ModifySagHaRequest,
    ) -> main_models.ModifySagHaResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_ha_with_options_async(request, runtime)

    def modify_sag_lan_with_options(
        self,
        request: main_models.ModifySagLanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagLanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_ip):
            query['EndIp'] = request.end_ip
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lease):
            query['Lease'] = request.lease
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.start_ip):
            query['StartIp'] = request.start_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagLan',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagLanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_lan_with_options_async(
        self,
        request: main_models.ModifySagLanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagLanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_ip):
            query['EndIp'] = request.end_ip
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lease):
            query['Lease'] = request.lease
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.start_ip):
            query['StartIp'] = request.start_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagLan',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagLanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_lan(
        self,
        request: main_models.ModifySagLanRequest,
    ) -> main_models.ModifySagLanResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_lan_with_options(request, runtime)

    async def modify_sag_lan_async(
        self,
        request: main_models.ModifySagLanRequest,
    ) -> main_models.ModifySagLanResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_lan_with_options_async(request, runtime)

    def modify_sag_management_port_with_options(
        self,
        request: main_models.ModifySagManagementPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagManagementPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagManagementPort',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagManagementPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_management_port_with_options_async(
        self,
        request: main_models.ModifySagManagementPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagManagementPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagManagementPort',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagManagementPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_management_port(
        self,
        request: main_models.ModifySagManagementPortRequest,
    ) -> main_models.ModifySagManagementPortResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_management_port_with_options(request, runtime)

    async def modify_sag_management_port_async(
        self,
        request: main_models.ModifySagManagementPortRequest,
    ) -> main_models.ModifySagManagementPortResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_management_port_with_options_async(request, runtime)

    def modify_sag_port_role_with_options(
        self,
        request: main_models.ModifySagPortRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagPortRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagPortRole',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagPortRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_port_role_with_options_async(
        self,
        request: main_models.ModifySagPortRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagPortRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagPortRole',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagPortRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_port_role(
        self,
        request: main_models.ModifySagPortRoleRequest,
    ) -> main_models.ModifySagPortRoleResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_port_role_with_options(request, runtime)

    async def modify_sag_port_role_async(
        self,
        request: main_models.ModifySagPortRoleRequest,
    ) -> main_models.ModifySagPortRoleResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_port_role_with_options_async(request, runtime)

    def modify_sag_port_route_protocol_with_options(
        self,
        request: main_models.ModifySagPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not DaraCore.is_null(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_port_route_protocol_with_options_async(
        self,
        request: main_models.ModifySagPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not DaraCore.is_null(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_port_route_protocol(
        self,
        request: main_models.ModifySagPortRouteProtocolRequest,
    ) -> main_models.ModifySagPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_port_route_protocol_with_options(request, runtime)

    async def modify_sag_port_route_protocol_async(
        self,
        request: main_models.ModifySagPortRouteProtocolRequest,
    ) -> main_models.ModifySagPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_port_route_protocol_with_options_async(request, runtime)

    def modify_sag_remote_access_with_options(
        self,
        request: main_models.ModifySagRemoteAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRemoteAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remote_access_ip):
            query['RemoteAccessIp'] = request.remote_access_ip
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRemoteAccess',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRemoteAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_remote_access_with_options_async(
        self,
        request: main_models.ModifySagRemoteAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRemoteAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remote_access_ip):
            query['RemoteAccessIp'] = request.remote_access_ip
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRemoteAccess',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRemoteAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_remote_access(
        self,
        request: main_models.ModifySagRemoteAccessRequest,
    ) -> main_models.ModifySagRemoteAccessResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_remote_access_with_options(request, runtime)

    async def modify_sag_remote_access_async(
        self,
        request: main_models.ModifySagRemoteAccessRequest,
    ) -> main_models.ModifySagRemoteAccessResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_remote_access_with_options_async(request, runtime)

    def modify_sag_route_protocol_bgp_with_options(
        self,
        request: main_models.ModifySagRouteProtocolBgpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRouteProtocolBgpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.local_as):
            query['LocalAs'] = request.local_as
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRouteProtocolBgp',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRouteProtocolBgpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_route_protocol_bgp_with_options_async(
        self,
        request: main_models.ModifySagRouteProtocolBgpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRouteProtocolBgpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.local_as):
            query['LocalAs'] = request.local_as
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRouteProtocolBgp',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRouteProtocolBgpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_route_protocol_bgp(
        self,
        request: main_models.ModifySagRouteProtocolBgpRequest,
    ) -> main_models.ModifySagRouteProtocolBgpResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_route_protocol_bgp_with_options(request, runtime)

    async def modify_sag_route_protocol_bgp_async(
        self,
        request: main_models.ModifySagRouteProtocolBgpRequest,
    ) -> main_models.ModifySagRouteProtocolBgpResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_route_protocol_bgp_with_options_async(request, runtime)

    def modify_sag_route_protocol_ospf_with_options(
        self,
        request: main_models.ModifySagRouteProtocolOspfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRouteProtocolOspfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area_id):
            query['AreaId'] = request.area_id
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not DaraCore.is_null(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not DaraCore.is_null(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not DaraCore.is_null(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRouteProtocolOspf',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRouteProtocolOspfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_route_protocol_ospf_with_options_async(
        self,
        request: main_models.ModifySagRouteProtocolOspfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagRouteProtocolOspfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area_id):
            query['AreaId'] = request.area_id
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not DaraCore.is_null(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not DaraCore.is_null(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not DaraCore.is_null(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagRouteProtocolOspf',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagRouteProtocolOspfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_route_protocol_ospf(
        self,
        request: main_models.ModifySagRouteProtocolOspfRequest,
    ) -> main_models.ModifySagRouteProtocolOspfResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_route_protocol_ospf_with_options(request, runtime)

    async def modify_sag_route_protocol_ospf_async(
        self,
        request: main_models.ModifySagRouteProtocolOspfRequest,
    ) -> main_models.ModifySagRouteProtocolOspfResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_route_protocol_ospf_with_options_async(request, runtime)

    def modify_sag_static_route_with_options(
        self,
        request: main_models.ModifySagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagStaticRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_static_route_with_options_async(
        self,
        request: main_models.ModifySagStaticRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagStaticRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_cidr):
            query['DestinationCidr'] = request.destination_cidr
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagStaticRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagStaticRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_static_route(
        self,
        request: main_models.ModifySagStaticRouteRequest,
    ) -> main_models.ModifySagStaticRouteResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_static_route_with_options(request, runtime)

    async def modify_sag_static_route_async(
        self,
        request: main_models.ModifySagStaticRouteRequest,
    ) -> main_models.ModifySagStaticRouteResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_static_route_with_options_async(request, runtime)

    def modify_sag_user_dns_with_options(
        self,
        request: main_models.ModifySagUserDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagUserDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagUserDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagUserDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_user_dns_with_options_async(
        self,
        request: main_models.ModifySagUserDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagUserDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagUserDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagUserDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_user_dns(
        self,
        request: main_models.ModifySagUserDnsRequest,
    ) -> main_models.ModifySagUserDnsResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_user_dns_with_options(request, runtime)

    async def modify_sag_user_dns_async(
        self,
        request: main_models.ModifySagUserDnsRequest,
    ) -> main_models.ModifySagUserDnsResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_user_dns_with_options_async(request, runtime)

    def modify_sag_wan_with_options(
        self,
        request: main_models.ModifySagWanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.isp):
            query['ISP'] = request.isp
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWan',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wan_with_options_async(
        self,
        request: main_models.ModifySagWanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.ip):
            query['IP'] = request.ip
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.isp):
            query['ISP'] = request.isp
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWan',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_wan(
        self,
        request: main_models.ModifySagWanRequest,
    ) -> main_models.ModifySagWanResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_wan_with_options(request, runtime)

    async def modify_sag_wan_async(
        self,
        request: main_models.ModifySagWanRequest,
    ) -> main_models.ModifySagWanResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_wan_with_options_async(request, runtime)

    def modify_sag_wan_snat_with_options(
        self,
        request: main_models.ModifySagWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.snat):
            query['Snat'] = request.snat
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wan_snat_with_options_async(
        self,
        request: main_models.ModifySagWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        if not DaraCore.is_null(request.snat):
            query['Snat'] = request.snat
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_wan_snat(
        self,
        request: main_models.ModifySagWanSnatRequest,
    ) -> main_models.ModifySagWanSnatResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_wan_snat_with_options(request, runtime)

    async def modify_sag_wan_snat_async(
        self,
        request: main_models.ModifySagWanSnatRequest,
    ) -> main_models.ModifySagWanSnatResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_wan_snat_with_options_async(request, runtime)

    def modify_sag_wifi_with_options(
        self,
        request: main_models.ModifySagWifiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWifiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not DaraCore.is_null(request.is_auth):
            query['IsAuth'] = request.is_auth
        if not DaraCore.is_null(request.is_broadcast):
            query['IsBroadcast'] = request.is_broadcast
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ssid):
            query['SSID'] = request.ssid
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWifi',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWifiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sag_wifi_with_options_async(
        self,
        request: main_models.ModifySagWifiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySagWifiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not DaraCore.is_null(request.is_auth):
            query['IsAuth'] = request.is_auth
        if not DaraCore.is_null(request.is_broadcast):
            query['IsBroadcast'] = request.is_broadcast
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ssid):
            query['SSID'] = request.ssid
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySagWifi',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySagWifiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sag_wifi(
        self,
        request: main_models.ModifySagWifiRequest,
    ) -> main_models.ModifySagWifiResponse:
        runtime = RuntimeOptions()
        return self.modify_sag_wifi_with_options(request, runtime)

    async def modify_sag_wifi_async(
        self,
        request: main_models.ModifySagWifiRequest,
    ) -> main_models.ModifySagWifiResponse:
        runtime = RuntimeOptions()
        return await self.modify_sag_wifi_with_options_async(request, runtime)

    def modify_smart_access_gateway_with_options(
        self,
        request: main_models.ModifySmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_software_connection_audit):
            query['EnableSoftwareConnectionAudit'] = request.enable_software_connection_audit
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.position):
            query['Position'] = request.position
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.routing_strategy):
            query['RoutingStrategy'] = request.routing_strategy
        if not DaraCore.is_null(request.security_lock_threshold):
            query['SecurityLockThreshold'] = request.security_lock_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_with_options_async(
        self,
        request: main_models.ModifySmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_software_connection_audit):
            query['EnableSoftwareConnectionAudit'] = request.enable_software_connection_audit
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.position):
            query['Position'] = request.position
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.routing_strategy):
            query['RoutingStrategy'] = request.routing_strategy
        if not DaraCore.is_null(request.security_lock_threshold):
            query['SecurityLockThreshold'] = request.security_lock_threshold
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_smart_access_gateway(
        self,
        request: main_models.ModifySmartAccessGatewayRequest,
    ) -> main_models.ModifySmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.modify_smart_access_gateway_with_options(request, runtime)

    async def modify_smart_access_gateway_async(
        self,
        request: main_models.ModifySmartAccessGatewayRequest,
    ) -> main_models.ModifySmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.modify_smart_access_gateway_with_options_async(request, runtime)

    def modify_smart_access_gateway_client_user_with_options(
        self,
        request: main_models.ModifySmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_client_user_with_options_async(
        self,
        request: main_models.ModifySmartAccessGatewayClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGatewayClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_smart_access_gateway_client_user(
        self,
        request: main_models.ModifySmartAccessGatewayClientUserRequest,
    ) -> main_models.ModifySmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return self.modify_smart_access_gateway_client_user_with_options(request, runtime)

    async def modify_smart_access_gateway_client_user_async(
        self,
        request: main_models.ModifySmartAccessGatewayClientUserRequest,
    ) -> main_models.ModifySmartAccessGatewayClientUserResponse:
        runtime = RuntimeOptions()
        return await self.modify_smart_access_gateway_client_user_with_options_async(request, runtime)

    def modify_smart_access_gateway_up_bandwidth_with_options(
        self,
        request: main_models.ModifySmartAccessGatewayUpBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayUpBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.up_bandwidth_4g):
            query['UpBandwidth4G'] = request.up_bandwidth_4g
        if not DaraCore.is_null(request.up_bandwidth_wan):
            query['UpBandwidthWan'] = request.up_bandwidth_wan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGatewayUpBandwidth',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayUpBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smart_access_gateway_up_bandwidth_with_options_async(
        self,
        request: main_models.ModifySmartAccessGatewayUpBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmartAccessGatewayUpBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.up_bandwidth_4g):
            query['UpBandwidth4G'] = request.up_bandwidth_4g
        if not DaraCore.is_null(request.up_bandwidth_wan):
            query['UpBandwidthWan'] = request.up_bandwidth_wan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmartAccessGatewayUpBandwidth',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmartAccessGatewayUpBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_smart_access_gateway_up_bandwidth(
        self,
        request: main_models.ModifySmartAccessGatewayUpBandwidthRequest,
    ) -> main_models.ModifySmartAccessGatewayUpBandwidthResponse:
        runtime = RuntimeOptions()
        return self.modify_smart_access_gateway_up_bandwidth_with_options(request, runtime)

    async def modify_smart_access_gateway_up_bandwidth_async(
        self,
        request: main_models.ModifySmartAccessGatewayUpBandwidthRequest,
    ) -> main_models.ModifySmartAccessGatewayUpBandwidthResponse:
        runtime = RuntimeOptions()
        return await self.modify_smart_access_gateway_up_bandwidth_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def probe_access_point_network_quality_with_options(
        self,
        request: main_models.ProbeAccessPointNetworkQualityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProbeAccessPointNetworkQualityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_ids):
            query['AccessPointIds'] = request.access_point_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProbeAccessPointNetworkQuality',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProbeAccessPointNetworkQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def probe_access_point_network_quality_with_options_async(
        self,
        request: main_models.ProbeAccessPointNetworkQualityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProbeAccessPointNetworkQualityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_ids):
            query['AccessPointIds'] = request.access_point_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProbeAccessPointNetworkQuality',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProbeAccessPointNetworkQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def probe_access_point_network_quality(
        self,
        request: main_models.ProbeAccessPointNetworkQualityRequest,
    ) -> main_models.ProbeAccessPointNetworkQualityResponse:
        runtime = RuntimeOptions()
        return self.probe_access_point_network_quality_with_options(request, runtime)

    async def probe_access_point_network_quality_async(
        self,
        request: main_models.ProbeAccessPointNetworkQualityRequest,
    ) -> main_models.ProbeAccessPointNetworkQualityResponse:
        runtime = RuntimeOptions()
        return await self.probe_access_point_network_quality_with_options_async(request, runtime)

    def reboot_smart_access_gateway_with_options(
        self,
        request: main_models.RebootSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_smart_access_gateway_with_options_async(
        self,
        request: main_models.RebootSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_smart_access_gateway(
        self,
        request: main_models.RebootSmartAccessGatewayRequest,
    ) -> main_models.RebootSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.reboot_smart_access_gateway_with_options(request, runtime)

    async def reboot_smart_access_gateway_async(
        self,
        request: main_models.RebootSmartAccessGatewayRequest,
    ) -> main_models.RebootSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.reboot_smart_access_gateway_with_options_async(request, runtime)

    def reset_smart_access_gateway_client_user_password_with_options(
        self,
        request: main_models.ResetSmartAccessGatewayClientUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSmartAccessGatewayClientUserPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSmartAccessGatewayClientUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_smart_access_gateway_client_user_password_with_options_async(
        self,
        request: main_models.ResetSmartAccessGatewayClientUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSmartAccessGatewayClientUserPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSmartAccessGatewayClientUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_smart_access_gateway_client_user_password(
        self,
        request: main_models.ResetSmartAccessGatewayClientUserPasswordRequest,
    ) -> main_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_smart_access_gateway_client_user_password_with_options(request, runtime)

    async def reset_smart_access_gateway_client_user_password_async(
        self,
        request: main_models.ResetSmartAccessGatewayClientUserPasswordRequest,
    ) -> main_models.ResetSmartAccessGatewayClientUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_smart_access_gateway_client_user_password_with_options_async(request, runtime)

    def revoke_instance_from_cbn_with_options(
        self,
        request: main_models.RevokeInstanceFromCbnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromCbnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromCbn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromCbnResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_cbn_with_options_async(
        self,
        request: main_models.RevokeInstanceFromCbnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromCbnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.cen_instance_id):
            query['CenInstanceId'] = request.cen_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromCbn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromCbnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_instance_from_cbn(
        self,
        request: main_models.RevokeInstanceFromCbnRequest,
    ) -> main_models.RevokeInstanceFromCbnResponse:
        runtime = RuntimeOptions()
        return self.revoke_instance_from_cbn_with_options(request, runtime)

    async def revoke_instance_from_cbn_async(
        self,
        request: main_models.RevokeInstanceFromCbnRequest,
    ) -> main_models.RevokeInstanceFromCbnResponse:
        runtime = RuntimeOptions()
        return await self.revoke_instance_from_cbn_with_options_async(request, runtime)

    def revoke_instance_from_vbr_with_options(
        self,
        request: main_models.RevokeInstanceFromVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_vbr_with_options_async(
        self,
        request: main_models.RevokeInstanceFromVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromVbrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_instance_from_vbr(
        self,
        request: main_models.RevokeInstanceFromVbrRequest,
    ) -> main_models.RevokeInstanceFromVbrResponse:
        runtime = RuntimeOptions()
        return self.revoke_instance_from_vbr_with_options(request, runtime)

    async def revoke_instance_from_vbr_async(
        self,
        request: main_models.RevokeInstanceFromVbrRequest,
    ) -> main_models.RevokeInstanceFromVbrResponse:
        runtime = RuntimeOptions()
        return await self.revoke_instance_from_vbr_with_options_async(request, runtime)

    def revoke_sag_instance_from_ccn_with_options(
        self,
        request: main_models.RevokeSagInstanceFromCcnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeSagInstanceFromCcnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeSagInstanceFromCcn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeSagInstanceFromCcnResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_sag_instance_from_ccn_with_options_async(
        self,
        request: main_models.RevokeSagInstanceFromCcnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeSagInstanceFromCcnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_instance_id):
            query['CcnInstanceId'] = request.ccn_instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeSagInstanceFromCcn',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeSagInstanceFromCcnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_sag_instance_from_ccn(
        self,
        request: main_models.RevokeSagInstanceFromCcnRequest,
    ) -> main_models.RevokeSagInstanceFromCcnResponse:
        runtime = RuntimeOptions()
        return self.revoke_sag_instance_from_ccn_with_options(request, runtime)

    async def revoke_sag_instance_from_ccn_async(
        self,
        request: main_models.RevokeSagInstanceFromCcnRequest,
    ) -> main_models.RevokeSagInstanceFromCcnResponse:
        runtime = RuntimeOptions()
        return await self.revoke_sag_instance_from_ccn_with_options_async(request, runtime)

    def roam_client_user_with_options(
        self,
        request: main_models.RoamClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RoamClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.origin_region_id):
            query['OriginRegionId'] = request.origin_region_id
        if not DaraCore.is_null(request.origin_smart_agid):
            query['OriginSmartAGId'] = request.origin_smart_agid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target_smart_agid):
            query['TargetSmartAGId'] = request.target_smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoamClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoamClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def roam_client_user_with_options_async(
        self,
        request: main_models.RoamClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RoamClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.origin_region_id):
            query['OriginRegionId'] = request.origin_region_id
        if not DaraCore.is_null(request.origin_smart_agid):
            query['OriginSmartAGId'] = request.origin_smart_agid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target_smart_agid):
            query['TargetSmartAGId'] = request.target_smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoamClientUser',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoamClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def roam_client_user(
        self,
        request: main_models.RoamClientUserRequest,
    ) -> main_models.RoamClientUserResponse:
        runtime = RuntimeOptions()
        return self.roam_client_user_with_options(request, runtime)

    async def roam_client_user_async(
        self,
        request: main_models.RoamClientUserRequest,
    ) -> main_models.RoamClientUserResponse:
        runtime = RuntimeOptions()
        return await self.roam_client_user_with_options_async(request, runtime)

    def set_advanced_monitor_state_with_options(
        self,
        request: main_models.SetAdvancedMonitorStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAdvancedMonitorStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAdvancedMonitorState',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAdvancedMonitorStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_advanced_monitor_state_with_options_async(
        self,
        request: main_models.SetAdvancedMonitorStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAdvancedMonitorStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAdvancedMonitorState',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAdvancedMonitorStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_advanced_monitor_state(
        self,
        request: main_models.SetAdvancedMonitorStateRequest,
    ) -> main_models.SetAdvancedMonitorStateResponse:
        runtime = RuntimeOptions()
        return self.set_advanced_monitor_state_with_options(request, runtime)

    async def set_advanced_monitor_state_async(
        self,
        request: main_models.SetAdvancedMonitorStateRequest,
    ) -> main_models.SetAdvancedMonitorStateResponse:
        runtime = RuntimeOptions()
        return await self.set_advanced_monitor_state_with_options_async(request, runtime)

    def synchronize_smart_agweb_config_with_options(
        self,
        request: main_models.SynchronizeSmartAGWebConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeSmartAGWebConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeSmartAGWebConfig',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeSmartAGWebConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_smart_agweb_config_with_options_async(
        self,
        request: main_models.SynchronizeSmartAGWebConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeSmartAGWebConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_agsn):
            query['SmartAGSn'] = request.smart_agsn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeSmartAGWebConfig',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeSmartAGWebConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_smart_agweb_config(
        self,
        request: main_models.SynchronizeSmartAGWebConfigRequest,
    ) -> main_models.SynchronizeSmartAGWebConfigResponse:
        runtime = RuntimeOptions()
        return self.synchronize_smart_agweb_config_with_options(request, runtime)

    async def synchronize_smart_agweb_config_async(
        self,
        request: main_models.SynchronizeSmartAGWebConfigRequest,
    ) -> main_models.SynchronizeSmartAGWebConfigResponse:
        runtime = RuntimeOptions()
        return await self.synchronize_smart_agweb_config_with_options_async(request, runtime)

    def unbind_serial_number_with_options(
        self,
        request: main_models.UnbindSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSerialNumber',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_serial_number_with_options_async(
        self,
        request: main_models.UnbindSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSerialNumber',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_serial_number(
        self,
        request: main_models.UnbindSerialNumberRequest,
    ) -> main_models.UnbindSerialNumberResponse:
        runtime = RuntimeOptions()
        return self.unbind_serial_number_with_options(request, runtime)

    async def unbind_serial_number_async(
        self,
        request: main_models.UnbindSerialNumberRequest,
    ) -> main_models.UnbindSerialNumberResponse:
        runtime = RuntimeOptions()
        return await self.unbind_serial_number_with_options_async(request, runtime)

    def unbind_smart_access_gateway_with_options(
        self,
        request: main_models.UnbindSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_smart_access_gateway_with_options_async(
        self,
        request: main_models.UnbindSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccn_id):
            query['CcnId'] = request.ccn_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_smart_access_gateway(
        self,
        request: main_models.UnbindSmartAccessGatewayRequest,
    ) -> main_models.UnbindSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.unbind_smart_access_gateway_with_options(request, runtime)

    async def unbind_smart_access_gateway_async(
        self,
        request: main_models.UnbindSmartAccessGatewayRequest,
    ) -> main_models.UnbindSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.unbind_smart_access_gateway_with_options_async(request, runtime)

    def unbind_vbr_with_options(
        self,
        request: main_models.UnbindVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindVbrResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_vbr_with_options_async(
        self,
        request: main_models.UnbindVbrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindVbrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.smart_aguid):
            query['SmartAGUid'] = request.smart_aguid
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_region_id):
            query['VbrRegionId'] = request.vbr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindVbr',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindVbrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_vbr(
        self,
        request: main_models.UnbindVbrRequest,
    ) -> main_models.UnbindVbrResponse:
        runtime = RuntimeOptions()
        return self.unbind_vbr_with_options(request, runtime)

    async def unbind_vbr_async(
        self,
        request: main_models.UnbindVbrRequest,
    ) -> main_models.UnbindVbrResponse:
        runtime = RuntimeOptions()
        return await self.unbind_vbr_with_options_async(request, runtime)

    def unlock_smart_access_gateway_with_options(
        self,
        request: main_models.UnlockSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_smart_access_gateway_with_options_async(
        self,
        request: main_models.UnlockSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_smart_access_gateway(
        self,
        request: main_models.UnlockSmartAccessGatewayRequest,
    ) -> main_models.UnlockSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.unlock_smart_access_gateway_with_options(request, runtime)

    async def unlock_smart_access_gateway_async(
        self,
        request: main_models.UnlockSmartAccessGatewayRequest,
    ) -> main_models.UnlockSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.unlock_smart_access_gateway_with_options_async(request, runtime)

    def update_enterprise_code_with_options(
        self,
        request: main_models.UpdateEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_code_with_options_async(
        self,
        request: main_models.UpdateEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_code(
        self,
        request: main_models.UpdateEnterpriseCodeRequest,
    ) -> main_models.UpdateEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return self.update_enterprise_code_with_options(request, runtime)

    async def update_enterprise_code_async(
        self,
        request: main_models.UpdateEnterpriseCodeRequest,
    ) -> main_models.UpdateEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return await self.update_enterprise_code_with_options_async(request, runtime)

    def update_probe_task_with_options(
        self,
        request: main_models.UpdateProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProbeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_probe_task_with_options_async(
        self,
        request: main_models.UpdateProbeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProbeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.packet_number):
            query['PacketNumber'] = request.packet_number
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.probe_task_id):
            query['ProbeTaskId'] = request.probe_task_id
        if not DaraCore.is_null(request.probe_task_source_address):
            query['ProbeTaskSourceAddress'] = request.probe_task_source_address
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_id):
            query['SagId'] = request.sag_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProbeTask',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProbeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_probe_task(
        self,
        request: main_models.UpdateProbeTaskRequest,
    ) -> main_models.UpdateProbeTaskResponse:
        runtime = RuntimeOptions()
        return self.update_probe_task_with_options(request, runtime)

    async def update_probe_task_async(
        self,
        request: main_models.UpdateProbeTaskRequest,
    ) -> main_models.UpdateProbeTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_probe_task_with_options_async(request, runtime)

    def update_smart_agaccess_point_with_options(
        self,
        request: main_models.UpdateSmartAGAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGAccessPoint',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agaccess_point_with_options_async(
        self,
        request: main_models.UpdateSmartAGAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGAccessPoint',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_agaccess_point(
        self,
        request: main_models.UpdateSmartAGAccessPointRequest,
    ) -> main_models.UpdateSmartAGAccessPointResponse:
        runtime = RuntimeOptions()
        return self.update_smart_agaccess_point_with_options(request, runtime)

    async def update_smart_agaccess_point_async(
        self,
        request: main_models.UpdateSmartAGAccessPointRequest,
    ) -> main_models.UpdateSmartAGAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_agaccess_point_with_options_async(request, runtime)

    def update_smart_agdpi_attribute_with_options(
        self,
        request: main_models.UpdateSmartAGDpiAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGDpiAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dpi_enabled):
            query['DpiEnabled'] = request.dpi_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGDpiAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGDpiAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agdpi_attribute_with_options_async(
        self,
        request: main_models.UpdateSmartAGDpiAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGDpiAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dpi_enabled):
            query['DpiEnabled'] = request.dpi_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGDpiAttribute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGDpiAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_agdpi_attribute(
        self,
        request: main_models.UpdateSmartAGDpiAttributeRequest,
    ) -> main_models.UpdateSmartAGDpiAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_smart_agdpi_attribute_with_options(request, runtime)

    async def update_smart_agdpi_attribute_async(
        self,
        request: main_models.UpdateSmartAGDpiAttributeRequest,
    ) -> main_models.UpdateSmartAGDpiAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_agdpi_attribute_with_options_async(request, runtime)

    def update_smart_agenterprise_code_with_options(
        self,
        request: main_models.UpdateSmartAGEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGEnterpriseCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_agenterprise_code_with_options_async(
        self,
        request: main_models.UpdateSmartAGEnterpriseCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGEnterpriseCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enterprise_code):
            query['EnterpriseCode'] = request.enterprise_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGEnterpriseCode',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGEnterpriseCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_agenterprise_code(
        self,
        request: main_models.UpdateSmartAGEnterpriseCodeRequest,
    ) -> main_models.UpdateSmartAGEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return self.update_smart_agenterprise_code_with_options(request, runtime)

    async def update_smart_agenterprise_code_async(
        self,
        request: main_models.UpdateSmartAGEnterpriseCodeRequest,
    ) -> main_models.UpdateSmartAGEnterpriseCodeResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_agenterprise_code_with_options_async(request, runtime)

    def update_smart_aguser_accelerate_config_with_options(
        self,
        request: main_models.UpdateSmartAGUserAccelerateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGUserAccelerateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGUserAccelerateConfig',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGUserAccelerateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_aguser_accelerate_config_with_options_async(
        self,
        request: main_models.UpdateSmartAGUserAccelerateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAGUserAccelerateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAGUserAccelerateConfig',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAGUserAccelerateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_aguser_accelerate_config(
        self,
        request: main_models.UpdateSmartAGUserAccelerateConfigRequest,
    ) -> main_models.UpdateSmartAGUserAccelerateConfigResponse:
        runtime = RuntimeOptions()
        return self.update_smart_aguser_accelerate_config_with_options(request, runtime)

    async def update_smart_aguser_accelerate_config_async(
        self,
        request: main_models.UpdateSmartAGUserAccelerateConfigRequest,
    ) -> main_models.UpdateSmartAGUserAccelerateConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_aguser_accelerate_config_with_options_async(request, runtime)

    def update_smart_access_gateway_admin_password_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayAdminPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayAdminPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_admin_password_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayAdminPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayAdminPassword',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayAdminPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_admin_password(
        self,
        request: main_models.UpdateSmartAccessGatewayAdminPasswordRequest,
    ) -> main_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_admin_password_with_options(request, runtime)

    async def update_smart_access_gateway_admin_password_async(
        self,
        request: main_models.UpdateSmartAccessGatewayAdminPasswordRequest,
    ) -> main_models.UpdateSmartAccessGatewayAdminPasswordResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_admin_password_with_options_async(request, runtime)

    def update_smart_access_gateway_bgp_route_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayBgpRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayBgpRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.local_as):
            query['LocalAs'] = request.local_as
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayBgpRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayBgpRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_bgp_route_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayBgpRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayBgpRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.hold_time):
            query['HoldTime'] = request.hold_time
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.local_as):
            query['LocalAs'] = request.local_as
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayBgpRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayBgpRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_bgp_route(
        self,
        request: main_models.UpdateSmartAccessGatewayBgpRouteRequest,
    ) -> main_models.UpdateSmartAccessGatewayBgpRouteResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_bgp_route_with_options(request, runtime)

    async def update_smart_access_gateway_bgp_route_async(
        self,
        request: main_models.UpdateSmartAccessGatewayBgpRouteRequest,
    ) -> main_models.UpdateSmartAccessGatewayBgpRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_bgp_route_with_options_async(request, runtime)

    def update_smart_access_gateway_dns_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_dns_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.master_dns):
            query['MasterDns'] = request.master_dns
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_dns):
            query['SlaveDns'] = request.slave_dns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_dns(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsRequest,
    ) -> main_models.UpdateSmartAccessGatewayDnsResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_dns_with_options(request, runtime)

    async def update_smart_access_gateway_dns_async(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsRequest,
    ) -> main_models.UpdateSmartAccessGatewayDnsResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_dns_with_options_async(request, runtime)

    def update_smart_access_gateway_dns_forward_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not DaraCore.is_null(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not DaraCore.is_null(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayDnsForwardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_dns_forward_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsForwardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayDnsForwardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.master_ip):
            query['MasterIp'] = request.master_ip
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.outbound_port_index):
            query['OutboundPortIndex'] = request.outbound_port_index
        if not DaraCore.is_null(request.outbound_port_name):
            query['OutboundPortName'] = request.outbound_port_name
        if not DaraCore.is_null(request.outbound_port_type):
            query['OutboundPortType'] = request.outbound_port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.slave_ip):
            query['SlaveIp'] = request.slave_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayDnsForward',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayDnsForwardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_dns_forward(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.UpdateSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_dns_forward_with_options(request, runtime)

    async def update_smart_access_gateway_dns_forward_async(
        self,
        request: main_models.UpdateSmartAccessGatewayDnsForwardRequest,
    ) -> main_models.UpdateSmartAccessGatewayDnsForwardResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_dns_forward_with_options_async(request, runtime)

    def update_smart_access_gateway_global_route_protocol_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_global_route_protocol_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_global_route_protocol(
        self,
        request: main_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_global_route_protocol_with_options(request, runtime)

    async def update_smart_access_gateway_global_route_protocol_async(
        self,
        request: main_models.UpdateSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> main_models.UpdateSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_global_route_protocol_with_options_async(request, runtime)

    def update_smart_access_gateway_ospf_route_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayOspfRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayOspfRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area_id):
            query['AreaId'] = request.area_id
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not DaraCore.is_null(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not DaraCore.is_null(request.interface_name):
            query['InterfaceName'] = request.interface_name
        if not DaraCore.is_null(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not DaraCore.is_null(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not DaraCore.is_null(request.networks):
            query['Networks'] = request.networks
        if not DaraCore.is_null(request.ospf_cost):
            query['OspfCost'] = request.ospf_cost
        if not DaraCore.is_null(request.ospf_network_type):
            query['OspfNetworkType'] = request.ospf_network_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.redistribute_protocol):
            query['RedistributeProtocol'] = request.redistribute_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayOspfRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayOspfRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_ospf_route_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayOspfRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayOspfRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area_id):
            query['AreaId'] = request.area_id
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.dead_time):
            query['DeadTime'] = request.dead_time
        if not DaraCore.is_null(request.hello_time):
            query['HelloTime'] = request.hello_time
        if not DaraCore.is_null(request.interface_name):
            query['InterfaceName'] = request.interface_name
        if not DaraCore.is_null(request.md_5key):
            query['Md5Key'] = request.md_5key
        if not DaraCore.is_null(request.md_5key_id):
            query['Md5KeyId'] = request.md_5key_id
        if not DaraCore.is_null(request.networks):
            query['Networks'] = request.networks
        if not DaraCore.is_null(request.ospf_cost):
            query['OspfCost'] = request.ospf_cost
        if not DaraCore.is_null(request.ospf_network_type):
            query['OspfNetworkType'] = request.ospf_network_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.redistribute_protocol):
            query['RedistributeProtocol'] = request.redistribute_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.router_id):
            query['RouterId'] = request.router_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayOspfRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayOspfRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_ospf_route(
        self,
        request: main_models.UpdateSmartAccessGatewayOspfRouteRequest,
    ) -> main_models.UpdateSmartAccessGatewayOspfRouteResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_ospf_route_with_options(request, runtime)

    async def update_smart_access_gateway_ospf_route_async(
        self,
        request: main_models.UpdateSmartAccessGatewayOspfRouteRequest,
    ) -> main_models.UpdateSmartAccessGatewayOspfRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_ospf_route_with_options_async(request, runtime)

    def update_smart_access_gateway_port_route_protocol_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not DaraCore.is_null(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_port_route_protocol_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.port_name):
            query['PortName'] = request.port_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remote_as):
            query['RemoteAs'] = request.remote_as
        if not DaraCore.is_null(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.route_protocol):
            query['RouteProtocol'] = request.route_protocol
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.vlan):
            query['Vlan'] = request.vlan
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_port_route_protocol(
        self,
        request: main_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
    ) -> main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_port_route_protocol_with_options(request, runtime)

    async def update_smart_access_gateway_port_route_protocol_async(
        self,
        request: main_models.UpdateSmartAccessGatewayPortRouteProtocolRequest,
    ) -> main_models.UpdateSmartAccessGatewayPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_port_route_protocol_with_options_async(request, runtime)

    def update_smart_access_gateway_version_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayVersion',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_version_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        if not DaraCore.is_null(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayVersion',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_version(
        self,
        request: main_models.UpdateSmartAccessGatewayVersionRequest,
    ) -> main_models.UpdateSmartAccessGatewayVersionResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_version_with_options(request, runtime)

    async def update_smart_access_gateway_version_async(
        self,
        request: main_models.UpdateSmartAccessGatewayVersionRequest,
    ) -> main_models.UpdateSmartAccessGatewayVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_version_with_options_async(request, runtime)

    def update_smart_access_gateway_wan_snat_with_options(
        self,
        request: main_models.UpdateSmartAccessGatewayWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.snat):
            query['Snat'] = request.snat
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_access_gateway_wan_snat_with_options_async(
        self,
        request: main_models.UpdateSmartAccessGatewayWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmartAccessGatewayWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        if not DaraCore.is_null(request.snat):
            query['Snat'] = request.snat
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmartAccessGatewayWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmartAccessGatewayWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_access_gateway_wan_snat(
        self,
        request: main_models.UpdateSmartAccessGatewayWanSnatRequest,
    ) -> main_models.UpdateSmartAccessGatewayWanSnatResponse:
        runtime = RuntimeOptions()
        return self.update_smart_access_gateway_wan_snat_with_options(request, runtime)

    async def update_smart_access_gateway_wan_snat_async(
        self,
        request: main_models.UpdateSmartAccessGatewayWanSnatRequest,
    ) -> main_models.UpdateSmartAccessGatewayWanSnatResponse:
        runtime = RuntimeOptions()
        return await self.update_smart_access_gateway_wan_snat_with_options_async(request, runtime)

    def upgrade_smart_access_gateway_with_options(
        self,
        request: main_models.UpgradeSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeSmartAccessGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_smart_access_gateway_with_options_async(
        self,
        request: main_models.UpgradeSmartAccessGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeSmartAccessGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.band_width_spec):
            query['BandWidthSpec'] = request.band_width_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeSmartAccessGateway',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeSmartAccessGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_smart_access_gateway(
        self,
        request: main_models.UpgradeSmartAccessGatewayRequest,
    ) -> main_models.UpgradeSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return self.upgrade_smart_access_gateway_with_options(request, runtime)

    async def upgrade_smart_access_gateway_async(
        self,
        request: main_models.UpgradeSmartAccessGatewayRequest,
    ) -> main_models.UpgradeSmartAccessGatewayResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_smart_access_gateway_with_options_async(request, runtime)

    def upgrade_smart_access_gateway_software_with_options(
        self,
        request: main_models.UpgradeSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeSmartAccessGatewaySoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_smart_access_gateway_software_with_options_async(
        self,
        request: main_models.UpgradeSmartAccessGatewaySoftwareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeSmartAccessGatewaySoftwareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.data_plan):
            query['DataPlan'] = request.data_plan
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.smart_agid):
            query['SmartAGId'] = request.smart_agid
        if not DaraCore.is_null(request.user_count):
            query['UserCount'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeSmartAccessGatewaySoftware',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeSmartAccessGatewaySoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_smart_access_gateway_software(
        self,
        request: main_models.UpgradeSmartAccessGatewaySoftwareRequest,
    ) -> main_models.UpgradeSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return self.upgrade_smart_access_gateway_software_with_options(request, runtime)

    async def upgrade_smart_access_gateway_software_async(
        self,
        request: main_models.UpgradeSmartAccessGatewaySoftwareRequest,
    ) -> main_models.UpgradeSmartAccessGatewaySoftwareResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_smart_access_gateway_software_with_options_async(request, runtime)

    def view_smart_access_gateway_bgp_route_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayBgpRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayBgpRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayBgpRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayBgpRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_bgp_route_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayBgpRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayBgpRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayBgpRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayBgpRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_bgp_route(
        self,
        request: main_models.ViewSmartAccessGatewayBgpRouteRequest,
    ) -> main_models.ViewSmartAccessGatewayBgpRouteResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_bgp_route_with_options(request, runtime)

    async def view_smart_access_gateway_bgp_route_async(
        self,
        request: main_models.ViewSmartAccessGatewayBgpRouteRequest,
    ) -> main_models.ViewSmartAccessGatewayBgpRouteResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_bgp_route_with_options_async(request, runtime)

    def view_smart_access_gateway_dns_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_dns_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayDns',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_dns(
        self,
        request: main_models.ViewSmartAccessGatewayDnsRequest,
    ) -> main_models.ViewSmartAccessGatewayDnsResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_dns_with_options(request, runtime)

    async def view_smart_access_gateway_dns_async(
        self,
        request: main_models.ViewSmartAccessGatewayDnsRequest,
    ) -> main_models.ViewSmartAccessGatewayDnsResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_dns_with_options_async(request, runtime)

    def view_smart_access_gateway_dns_forwards_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayDnsForwardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayDnsForwardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayDnsForwards',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayDnsForwardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_dns_forwards_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayDnsForwardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayDnsForwardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayDnsForwards',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayDnsForwardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_dns_forwards(
        self,
        request: main_models.ViewSmartAccessGatewayDnsForwardsRequest,
    ) -> main_models.ViewSmartAccessGatewayDnsForwardsResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_dns_forwards_with_options(request, runtime)

    async def view_smart_access_gateway_dns_forwards_async(
        self,
        request: main_models.ViewSmartAccessGatewayDnsForwardsRequest,
    ) -> main_models.ViewSmartAccessGatewayDnsForwardsResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_dns_forwards_with_options_async(request, runtime)

    def view_smart_access_gateway_global_route_protocol_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_global_route_protocol_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayGlobalRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_global_route_protocol(
        self,
        request: main_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_global_route_protocol_with_options(request, runtime)

    async def view_smart_access_gateway_global_route_protocol_async(
        self,
        request: main_models.ViewSmartAccessGatewayGlobalRouteProtocolRequest,
    ) -> main_models.ViewSmartAccessGatewayGlobalRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_global_route_protocol_with_options_async(request, runtime)

    def view_smart_access_gateway_ospf_route_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayOspfRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayOspfRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayOspfRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayOspfRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_ospf_route_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayOspfRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayOspfRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayOspfRoute',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayOspfRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_ospf_route(
        self,
        request: main_models.ViewSmartAccessGatewayOspfRouteRequest,
    ) -> main_models.ViewSmartAccessGatewayOspfRouteResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_ospf_route_with_options(request, runtime)

    async def view_smart_access_gateway_ospf_route_async(
        self,
        request: main_models.ViewSmartAccessGatewayOspfRouteRequest,
    ) -> main_models.ViewSmartAccessGatewayOspfRouteResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_ospf_route_with_options_async(request, runtime)

    def view_smart_access_gateway_port_route_protocol_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayPortRouteProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_port_route_protocol_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayPortRouteProtocol',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayPortRouteProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_port_route_protocol(
        self,
        request: main_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
    ) -> main_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_port_route_protocol_with_options(request, runtime)

    async def view_smart_access_gateway_port_route_protocol_async(
        self,
        request: main_models.ViewSmartAccessGatewayPortRouteProtocolRequest,
    ) -> main_models.ViewSmartAccessGatewayPortRouteProtocolResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_port_route_protocol_with_options_async(request, runtime)

    def view_smart_access_gateway_routes_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayRoutes',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_routes_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayRoutes',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_routes(
        self,
        request: main_models.ViewSmartAccessGatewayRoutesRequest,
    ) -> main_models.ViewSmartAccessGatewayRoutesResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_routes_with_options(request, runtime)

    async def view_smart_access_gateway_routes_async(
        self,
        request: main_models.ViewSmartAccessGatewayRoutesRequest,
    ) -> main_models.ViewSmartAccessGatewayRoutesResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_routes_with_options_async(request, runtime)

    def view_smart_access_gateway_wan_snat_with_options(
        self,
        request: main_models.ViewSmartAccessGatewayWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayWanSnatResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_smart_access_gateway_wan_snat_with_options_async(
        self,
        request: main_models.ViewSmartAccessGatewayWanSnatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewSmartAccessGatewayWanSnatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account):
            query['CrossAccount'] = request.cross_account
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not DaraCore.is_null(request.sag_ins_id):
            query['SagInsId'] = request.sag_ins_id
        if not DaraCore.is_null(request.sag_sn):
            query['SagSn'] = request.sag_sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ViewSmartAccessGatewayWanSnat',
            version = '2018-03-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewSmartAccessGatewayWanSnatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_smart_access_gateway_wan_snat(
        self,
        request: main_models.ViewSmartAccessGatewayWanSnatRequest,
    ) -> main_models.ViewSmartAccessGatewayWanSnatResponse:
        runtime = RuntimeOptions()
        return self.view_smart_access_gateway_wan_snat_with_options(request, runtime)

    async def view_smart_access_gateway_wan_snat_async(
        self,
        request: main_models.ViewSmartAccessGatewayWanSnatRequest,
    ) -> main_models.ViewSmartAccessGatewayWanSnatResponse:
        runtime = RuntimeOptions()
        return await self.view_smart_access_gateway_wan_snat_with_options_async(request, runtime)
