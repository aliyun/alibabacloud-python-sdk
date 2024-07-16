# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cc5g20220314 import models as cc5g20220314_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cc5g', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dnsauthorization_rule_with_options(
        self,
        request: cc5g20220314_models.AddDNSAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddDNSAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例的DNS授权规则
        
        @param request: AddDNSAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDNSAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddDNSAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dnsauthorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.AddDNSAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddDNSAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例的DNS授权规则
        
        @param request: AddDNSAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDNSAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddDNSAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dnsauthorization_rule(
        self,
        request: cc5g20220314_models.AddDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.AddDNSAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例的DNS授权规则
        
        @param request: AddDNSAuthorizationRuleRequest
        @return: AddDNSAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dnsauthorization_rule_with_options(request, runtime)

    async def add_dnsauthorization_rule_async(
        self,
        request: cc5g20220314_models.AddDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.AddDNSAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例的DNS授权规则
        
        @param request: AddDNSAuthorizationRuleRequest
        @return: AddDNSAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dnsauthorization_rule_with_options_async(request, runtime)

    def add_group_dns_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.AddGroupDnsAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例组的DNS授权规则
        
        @param request: AddGroupDnsAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupDnsAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGroupDnsAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_group_dns_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.AddGroupDnsAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例组的DNS授权规则
        
        @param request: AddGroupDnsAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupDnsAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGroupDnsAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_group_dns_authorization_rule(
        self,
        request: cc5g20220314_models.AddGroupDnsAuthorizationRuleRequest,
    ) -> cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例组的DNS授权规则
        
        @param request: AddGroupDnsAuthorizationRuleRequest
        @return: AddGroupDnsAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_group_dns_authorization_rule_with_options(request, runtime)

    async def add_group_dns_authorization_rule_async(
        self,
        request: cc5g20220314_models.AddGroupDnsAuthorizationRuleRequest,
    ) -> cc5g20220314_models.AddGroupDnsAuthorizationRuleResponse:
        """
        @summary 添加5G高速上云服务实例组的DNS授权规则
        
        @param request: AddGroupDnsAuthorizationRuleRequest
        @return: AddGroupDnsAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_group_dns_authorization_rule_with_options_async(request, runtime)

    def add_wireless_cloud_connector_to_group_with_options(
        self,
        request: cc5g20220314_models.AddWirelessCloudConnectorToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse:
        """
        @summary 添加5G高速上云服务实例到组
        
        @param request: AddWirelessCloudConnectorToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWirelessCloudConnectorToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWirelessCloudConnectorToGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_wireless_cloud_connector_to_group_with_options_async(
        self,
        request: cc5g20220314_models.AddWirelessCloudConnectorToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse:
        """
        @summary 添加5G高速上云服务实例到组
        
        @param request: AddWirelessCloudConnectorToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWirelessCloudConnectorToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWirelessCloudConnectorToGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_wireless_cloud_connector_to_group(
        self,
        request: cc5g20220314_models.AddWirelessCloudConnectorToGroupRequest,
    ) -> cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse:
        """
        @summary 添加5G高速上云服务实例到组
        
        @param request: AddWirelessCloudConnectorToGroupRequest
        @return: AddWirelessCloudConnectorToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_wireless_cloud_connector_to_group_with_options(request, runtime)

    async def add_wireless_cloud_connector_to_group_async(
        self,
        request: cc5g20220314_models.AddWirelessCloudConnectorToGroupRequest,
    ) -> cc5g20220314_models.AddWirelessCloudConnectorToGroupResponse:
        """
        @summary 添加5G高速上云服务实例到组
        
        @param request: AddWirelessCloudConnectorToGroupRequest
        @return: AddWirelessCloudConnectorToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_wireless_cloud_connector_to_group_with_options_async(request, runtime)

    def attach_vpc_to_net_link_with_options(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
        """
        @summary 创建5G高速上云服务实例下的网络连接
        
        @param request: AttachVpcToNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVpcToNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switches):
            query['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVpcToNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AttachVpcToNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vpc_to_net_link_with_options_async(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
        """
        @summary 创建5G高速上云服务实例下的网络连接
        
        @param request: AttachVpcToNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVpcToNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switches):
            query['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVpcToNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AttachVpcToNetLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vpc_to_net_link(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
        """
        @summary 创建5G高速上云服务实例下的网络连接
        
        @param request: AttachVpcToNetLinkRequest
        @return: AttachVpcToNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_vpc_to_net_link_with_options(request, runtime)

    async def attach_vpc_to_net_link_async(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
        """
        @summary 创建5G高速上云服务实例下的网络连接
        
        @param request: AttachVpcToNetLinkRequest
        @return: AttachVpcToNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_vpc_to_net_link_with_options_async(request, runtime)

    def create_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例的授权规则
        
        @param request: CreateAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例的授权规则
        
        @param request: CreateAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_authorization_rule(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例的授权规则
        
        @param request: CreateAuthorizationRuleRequest
        @return: CreateAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    async def create_authorization_rule_async(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例的授权规则
        
        @param request: CreateAuthorizationRuleRequest
        @return: CreateAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_authorization_rule_with_options_async(request, runtime)

    def create_batch_operate_cards_task_with_options(
        self,
        request: cc5g20220314_models.CreateBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateBatchOperateCardsTaskResponse:
        """
        @summary 创建批量操作卡任务
        
        @param request: CreateBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_operate_cards_task_with_options_async(
        self,
        request: cc5g20220314_models.CreateBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateBatchOperateCardsTaskResponse:
        """
        @summary 创建批量操作卡任务
        
        @param request: CreateBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateBatchOperateCardsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_operate_cards_task(
        self,
        request: cc5g20220314_models.CreateBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.CreateBatchOperateCardsTaskResponse:
        """
        @summary 创建批量操作卡任务
        
        @param request: CreateBatchOperateCardsTaskRequest
        @return: CreateBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_operate_cards_task_with_options(request, runtime)

    async def create_batch_operate_cards_task_async(
        self,
        request: cc5g20220314_models.CreateBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.CreateBatchOperateCardsTaskResponse:
        """
        @summary 创建批量操作卡任务
        
        @param request: CreateBatchOperateCardsTaskRequest
        @return: CreateBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_operate_cards_task_with_options_async(request, runtime)

    def create_group_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.CreateGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateGroupAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例组的授权规则
        
        @param request: CreateGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateGroupAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.CreateGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateGroupAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例组的授权规则
        
        @param request: CreateGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateGroupAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_authorization_rule(
        self,
        request: cc5g20220314_models.CreateGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.CreateGroupAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例组的授权规则
        
        @param request: CreateGroupAuthorizationRuleRequest
        @return: CreateGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_authorization_rule_with_options(request, runtime)

    async def create_group_authorization_rule_async(
        self,
        request: cc5g20220314_models.CreateGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.CreateGroupAuthorizationRuleResponse:
        """
        @summary 创建5G高速上云服务实例组的授权规则
        
        @param request: CreateGroupAuthorizationRuleRequest
        @return: CreateGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_authorization_rule_with_options_async(request, runtime)

    def create_io_tcloud_connector_backhaul_route_with_options(
        self,
        request: cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 下发iotcc实例的回程路由
        
        @param request: CreateIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_io_tcloud_connector_backhaul_route_with_options_async(
        self,
        request: cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 下发iotcc实例的回程路由
        
        @param request: CreateIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_io_tcloud_connector_backhaul_route(
        self,
        request: cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 下发iotcc实例的回程路由
        
        @param request: CreateIoTCloudConnectorBackhaulRouteRequest
        @return: CreateIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    async def create_io_tcloud_connector_backhaul_route_async(
        self,
        request: cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 下发iotcc实例的回程路由
        
        @param request: CreateIoTCloudConnectorBackhaulRouteRequest
        @return: CreateIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_io_tcloud_connector_backhaul_route_with_options_async(request, runtime)

    def create_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        """
        @summary 创建5G高速上云服务实例
        
        @param request: CreateWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_links):
            query['NetLinks'] = request.net_links
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_case):
            query['UseCase'] = request.use_case
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wireless_cloud_connector_with_options_async(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        """
        @summary 创建5G高速上云服务实例
        
        @param request: CreateWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_links):
            query['NetLinks'] = request.net_links
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_case):
            query['UseCase'] = request.use_case
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateWirelessCloudConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wireless_cloud_connector(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        """
        @summary 创建5G高速上云服务实例
        
        @param request: CreateWirelessCloudConnectorRequest
        @return: CreateWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wireless_cloud_connector_with_options(request, runtime)

    async def create_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        """
        @summary 创建5G高速上云服务实例
        
        @param request: CreateWirelessCloudConnectorRequest
        @return: CreateWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wireless_cloud_connector_with_options_async(request, runtime)

    def create_wireless_cloud_connector_group_with_options(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse:
        """
        @summary 创建5G高速上云服务实例组
        
        @param request: CreateWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wireless_cloud_connector_group_with_options_async(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse:
        """
        @summary 创建5G高速上云服务实例组
        
        @param request: CreateWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wireless_cloud_connector_group(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse:
        """
        @summary 创建5G高速上云服务实例组
        
        @param request: CreateWirelessCloudConnectorGroupRequest
        @return: CreateWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wireless_cloud_connector_group_with_options(request, runtime)

    async def create_wireless_cloud_connector_group_async(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorGroupResponse:
        """
        @summary 创建5G高速上云服务实例组
        
        @param request: CreateWirelessCloudConnectorGroupRequest
        @return: CreateWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wireless_cloud_connector_group_with_options_async(request, runtime)

    def delete_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例的授权规则
        
        @param request: DeleteAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例的授权规则
        
        @param request: DeleteAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_authorization_rule(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例的授权规则
        
        @param request: DeleteAuthorizationRuleRequest
        @return: DeleteAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    async def delete_authorization_rule_async(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例的授权规则
        
        @param request: DeleteAuthorizationRuleRequest
        @return: DeleteAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_authorization_rule_with_options_async(request, runtime)

    def delete_batch_operate_cards_task_with_options(
        self,
        request: cc5g20220314_models.DeleteBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteBatchOperateCardsTaskResponse:
        """
        @summary 删除批量操作卡任务
        
        @param request: DeleteBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
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
            action='DeleteBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_operate_cards_task_with_options_async(
        self,
        request: cc5g20220314_models.DeleteBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteBatchOperateCardsTaskResponse:
        """
        @summary 删除批量操作卡任务
        
        @param request: DeleteBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
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
            action='DeleteBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteBatchOperateCardsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch_operate_cards_task(
        self,
        request: cc5g20220314_models.DeleteBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.DeleteBatchOperateCardsTaskResponse:
        """
        @summary 删除批量操作卡任务
        
        @param request: DeleteBatchOperateCardsTaskRequest
        @return: DeleteBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_operate_cards_task_with_options(request, runtime)

    async def delete_batch_operate_cards_task_async(
        self,
        request: cc5g20220314_models.DeleteBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.DeleteBatchOperateCardsTaskResponse:
        """
        @summary 删除批量操作卡任务
        
        @param request: DeleteBatchOperateCardsTaskRequest
        @return: DeleteBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_batch_operate_cards_task_with_options_async(request, runtime)

    def delete_group_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.DeleteGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteGroupAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例组的授权规则
        
        @param request: DeleteGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteGroupAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.DeleteGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteGroupAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例组的授权规则
        
        @param request: DeleteGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteGroupAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_authorization_rule(
        self,
        request: cc5g20220314_models.DeleteGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.DeleteGroupAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例组的授权规则
        
        @param request: DeleteGroupAuthorizationRuleRequest
        @return: DeleteGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_authorization_rule_with_options(request, runtime)

    async def delete_group_authorization_rule_async(
        self,
        request: cc5g20220314_models.DeleteGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.DeleteGroupAuthorizationRuleResponse:
        """
        @summary 删除5G高速上云服务实例组的授权规则
        
        @param request: DeleteGroupAuthorizationRuleRequest
        @return: DeleteGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_authorization_rule_with_options_async(request, runtime)

    def delete_io_tcloud_connector_backhaul_route_with_options(
        self,
        request: cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 删除iotcc实例的回程路由
        
        @param request: DeleteIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_io_tcloud_connector_backhaul_route_with_options_async(
        self,
        request: cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 删除iotcc实例的回程路由
        
        @param request: DeleteIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_io_tcloud_connector_backhaul_route(
        self,
        request: cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 删除iotcc实例的回程路由
        
        @param request: DeleteIoTCloudConnectorBackhaulRouteRequest
        @return: DeleteIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    async def delete_io_tcloud_connector_backhaul_route_async(
        self,
        request: cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 删除iotcc实例的回程路由
        
        @param request: DeleteIoTCloudConnectorBackhaulRouteRequest
        @return: DeleteIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_io_tcloud_connector_backhaul_route_with_options_async(request, runtime)

    def delete_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
        """
        @summary 删除5G高速上云服务实例
        
        @param request: DeleteWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_wireless_cloud_connector_with_options_async(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
        """
        @summary 删除5G高速上云服务实例
        
        @param request: DeleteWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteWirelessCloudConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_wireless_cloud_connector(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
        """
        @summary 删除5G高速上云服务实例
        
        @param request: DeleteWirelessCloudConnectorRequest
        @return: DeleteWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_wireless_cloud_connector_with_options(request, runtime)

    async def delete_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
        """
        @summary 删除5G高速上云服务实例
        
        @param request: DeleteWirelessCloudConnectorRequest
        @return: DeleteWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_wireless_cloud_connector_with_options_async(request, runtime)

    def delete_wireless_cloud_connector_group_with_options(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse:
        """
        @summary 删除5G高速上云服务实例分组
        
        @param request: DeleteWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_wireless_cloud_connector_group_with_options_async(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse:
        """
        @summary 删除5G高速上云服务实例分组
        
        @param request: DeleteWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_wireless_cloud_connector_group(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse:
        """
        @summary 删除5G高速上云服务实例分组
        
        @param request: DeleteWirelessCloudConnectorGroupRequest
        @return: DeleteWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_wireless_cloud_connector_group_with_options(request, runtime)

    async def delete_wireless_cloud_connector_group_async(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorGroupResponse:
        """
        @summary 删除5G高速上云服务实例分组
        
        @param request: DeleteWirelessCloudConnectorGroupRequest
        @return: DeleteWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_wireless_cloud_connector_group_with_options_async(request, runtime)

    def detach_vpc_from_net_link_with_options(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
        """
        @summary 解除5G高速上云服务实例下的网络连接和VPC的绑定
        
        @param request: DetachVpcFromNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVpcFromNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVpcFromNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DetachVpcFromNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vpc_from_net_link_with_options_async(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
        """
        @summary 解除5G高速上云服务实例下的网络连接和VPC的绑定
        
        @param request: DetachVpcFromNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVpcFromNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVpcFromNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DetachVpcFromNetLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vpc_from_net_link(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
        """
        @summary 解除5G高速上云服务实例下的网络连接和VPC的绑定
        
        @param request: DetachVpcFromNetLinkRequest
        @return: DetachVpcFromNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_vpc_from_net_link_with_options(request, runtime)

    async def detach_vpc_from_net_link_async(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
        """
        @summary 解除5G高速上云服务实例下的网络连接和VPC的绑定
        
        @param request: DetachVpcFromNetLinkRequest
        @return: DetachVpcFromNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_vpc_from_net_link_with_options_async(request, runtime)

    def fail_cards_with_options(
        self,
        request: cc5g20220314_models.FailCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.FailCardsResponse:
        """
        @summary 卡注销接口
        
        @param request: FailCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.FailCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fail_cards_with_options_async(
        self,
        request: cc5g20220314_models.FailCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.FailCardsResponse:
        """
        @summary 卡注销接口
        
        @param request: FailCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.FailCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fail_cards(
        self,
        request: cc5g20220314_models.FailCardsRequest,
    ) -> cc5g20220314_models.FailCardsResponse:
        """
        @summary 卡注销接口
        
        @param request: FailCardsRequest
        @return: FailCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fail_cards_with_options(request, runtime)

    async def fail_cards_async(
        self,
        request: cc5g20220314_models.FailCardsRequest,
    ) -> cc5g20220314_models.FailCardsResponse:
        """
        @summary 卡注销接口
        
        @param request: FailCardsRequest
        @return: FailCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fail_cards_with_options_async(request, runtime)

    def get_card_with_options(
        self,
        request: cc5g20220314_models.GetCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCardResponse:
        """
        @summary 查询5G高速上云服务实例的详细连接信息
        
        @param request: GetCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_with_options_async(
        self,
        request: cc5g20220314_models.GetCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCardResponse:
        """
        @summary 查询5G高速上云服务实例的详细连接信息
        
        @param request: GetCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card(
        self,
        request: cc5g20220314_models.GetCardRequest,
    ) -> cc5g20220314_models.GetCardResponse:
        """
        @summary 查询5G高速上云服务实例的详细连接信息
        
        @param request: GetCardRequest
        @return: GetCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_card_with_options(request, runtime)

    async def get_card_async(
        self,
        request: cc5g20220314_models.GetCardRequest,
    ) -> cc5g20220314_models.GetCardResponse:
        """
        @summary 查询5G高速上云服务实例的详细连接信息
        
        @param request: GetCardRequest
        @return: GetCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_card_with_options_async(request, runtime)

    def get_card_lock_reason_with_options(
        self,
        request: cc5g20220314_models.GetCardLockReasonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCardLockReasonResponse:
        """
        @summary 查询卡锁定停机的原因
        
        @param request: GetCardLockReasonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardLockReasonResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardLockReason',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardLockReasonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_lock_reason_with_options_async(
        self,
        request: cc5g20220314_models.GetCardLockReasonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCardLockReasonResponse:
        """
        @summary 查询卡锁定停机的原因
        
        @param request: GetCardLockReasonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardLockReasonResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardLockReason',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardLockReasonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_lock_reason(
        self,
        request: cc5g20220314_models.GetCardLockReasonRequest,
    ) -> cc5g20220314_models.GetCardLockReasonResponse:
        """
        @summary 查询卡锁定停机的原因
        
        @param request: GetCardLockReasonRequest
        @return: GetCardLockReasonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_card_lock_reason_with_options(request, runtime)

    async def get_card_lock_reason_async(
        self,
        request: cc5g20220314_models.GetCardLockReasonRequest,
    ) -> cc5g20220314_models.GetCardLockReasonResponse:
        """
        @summary 查询卡锁定停机的原因
        
        @param request: GetCardLockReasonRequest
        @return: GetCardLockReasonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_card_lock_reason_with_options_async(request, runtime)

    def get_create_customer_infomation_with_options(
        self,
        request: cc5g20220314_models.GetCreateCustomerInfomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCreateCustomerInfomationResponse:
        """
        @param request: GetCreateCustomerInfomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateCustomerInfomationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateCustomerInfomation',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCreateCustomerInfomationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_customer_infomation_with_options_async(
        self,
        request: cc5g20220314_models.GetCreateCustomerInfomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCreateCustomerInfomationResponse:
        """
        @param request: GetCreateCustomerInfomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateCustomerInfomationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateCustomerInfomation',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCreateCustomerInfomationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_customer_infomation(
        self,
        request: cc5g20220314_models.GetCreateCustomerInfomationRequest,
    ) -> cc5g20220314_models.GetCreateCustomerInfomationResponse:
        """
        @param request: GetCreateCustomerInfomationRequest
        @return: GetCreateCustomerInfomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_create_customer_infomation_with_options(request, runtime)

    async def get_create_customer_infomation_async(
        self,
        request: cc5g20220314_models.GetCreateCustomerInfomationRequest,
    ) -> cc5g20220314_models.GetCreateCustomerInfomationResponse:
        """
        @param request: GetCreateCustomerInfomationRequest
        @return: GetCreateCustomerInfomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_create_customer_infomation_with_options_async(request, runtime)

    def get_create_customer_information_with_options(
        self,
        request: cc5g20220314_models.GetCreateCustomerInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCreateCustomerInformationResponse:
        """
        @summary 获取录入客户资料的相关信息
        
        @param request: GetCreateCustomerInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateCustomerInformationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateCustomerInformation',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCreateCustomerInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_customer_information_with_options_async(
        self,
        request: cc5g20220314_models.GetCreateCustomerInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetCreateCustomerInformationResponse:
        """
        @summary 获取录入客户资料的相关信息
        
        @param request: GetCreateCustomerInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateCustomerInformationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateCustomerInformation',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCreateCustomerInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_customer_information(
        self,
        request: cc5g20220314_models.GetCreateCustomerInformationRequest,
    ) -> cc5g20220314_models.GetCreateCustomerInformationResponse:
        """
        @summary 获取录入客户资料的相关信息
        
        @param request: GetCreateCustomerInformationRequest
        @return: GetCreateCustomerInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_create_customer_information_with_options(request, runtime)

    async def get_create_customer_information_async(
        self,
        request: cc5g20220314_models.GetCreateCustomerInformationRequest,
    ) -> cc5g20220314_models.GetCreateCustomerInformationResponse:
        """
        @summary 获取录入客户资料的相关信息
        
        @param request: GetCreateCustomerInformationRequest
        @return: GetCreateCustomerInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_create_customer_information_with_options_async(request, runtime)

    def get_diagnose_result_for_single_card_with_options(
        self,
        request: cc5g20220314_models.GetDiagnoseResultForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetDiagnoseResultForSingleCardResponse:
        """
        @summary 查询单卡诊断结果
        
        @param request: GetDiagnoseResultForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnoseResultForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_task_id):
            query['DiagnoseTaskId'] = request.diagnose_task_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnoseResultForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetDiagnoseResultForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnose_result_for_single_card_with_options_async(
        self,
        request: cc5g20220314_models.GetDiagnoseResultForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetDiagnoseResultForSingleCardResponse:
        """
        @summary 查询单卡诊断结果
        
        @param request: GetDiagnoseResultForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnoseResultForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_task_id):
            query['DiagnoseTaskId'] = request.diagnose_task_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnoseResultForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetDiagnoseResultForSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnose_result_for_single_card(
        self,
        request: cc5g20220314_models.GetDiagnoseResultForSingleCardRequest,
    ) -> cc5g20220314_models.GetDiagnoseResultForSingleCardResponse:
        """
        @summary 查询单卡诊断结果
        
        @param request: GetDiagnoseResultForSingleCardRequest
        @return: GetDiagnoseResultForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_diagnose_result_for_single_card_with_options(request, runtime)

    async def get_diagnose_result_for_single_card_async(
        self,
        request: cc5g20220314_models.GetDiagnoseResultForSingleCardRequest,
    ) -> cc5g20220314_models.GetDiagnoseResultForSingleCardResponse:
        """
        @summary 查询单卡诊断结果
        
        @param request: GetDiagnoseResultForSingleCardRequest
        @return: GetDiagnoseResultForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnose_result_for_single_card_with_options_async(request, runtime)

    def get_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
        """
        @summary 查询5G高速上云服务实例详情
        
        @param request: GetWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_wireless_cloud_connector_with_options_async(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
        """
        @summary 查询5G高速上云服务实例详情
        
        @param request: GetWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetWirelessCloudConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_wireless_cloud_connector(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
        """
        @summary 查询5G高速上云服务实例详情
        
        @param request: GetWirelessCloudConnectorRequest
        @return: GetWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_wireless_cloud_connector_with_options(request, runtime)

    async def get_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
        """
        @summary 查询5G高速上云服务实例详情
        
        @param request: GetWirelessCloudConnectorRequest
        @return: GetWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_wireless_cloud_connector_with_options_async(request, runtime)

    def grant_net_link_with_options(
        self,
        request: cc5g20220314_models.GrantNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GrantNetLinkResponse:
        """
        @summary 分享授权网络连接
        
        @param request: GrantNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.grant_ali_uid):
            query['GrantAliUid'] = request.grant_ali_uid
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GrantNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_net_link_with_options_async(
        self,
        request: cc5g20220314_models.GrantNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GrantNetLinkResponse:
        """
        @summary 分享授权网络连接
        
        @param request: GrantNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.grant_ali_uid):
            query['GrantAliUid'] = request.grant_ali_uid
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GrantNetLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_net_link(
        self,
        request: cc5g20220314_models.GrantNetLinkRequest,
    ) -> cc5g20220314_models.GrantNetLinkResponse:
        """
        @summary 分享授权网络连接
        
        @param request: GrantNetLinkRequest
        @return: GrantNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_net_link_with_options(request, runtime)

    async def grant_net_link_async(
        self,
        request: cc5g20220314_models.GrantNetLinkRequest,
    ) -> cc5g20220314_models.GrantNetLinkResponse:
        """
        @summary 分享授权网络连接
        
        @param request: GrantNetLinkRequest
        @return: GrantNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_net_link_with_options_async(request, runtime)

    def inner_limit_rate_cards_with_options(
        self,
        request: cc5g20220314_models.InnerLimitRateCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.InnerLimitRateCardsResponse:
        """
        @param request: InnerLimitRateCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerLimitRateCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.inner_api):
            query['InnerApi'] = request.inner_api
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerLimitRateCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.InnerLimitRateCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def inner_limit_rate_cards_with_options_async(
        self,
        request: cc5g20220314_models.InnerLimitRateCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.InnerLimitRateCardsResponse:
        """
        @param request: InnerLimitRateCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerLimitRateCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.inner_api):
            query['InnerApi'] = request.inner_api
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerLimitRateCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.InnerLimitRateCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inner_limit_rate_cards(
        self,
        request: cc5g20220314_models.InnerLimitRateCardsRequest,
    ) -> cc5g20220314_models.InnerLimitRateCardsResponse:
        """
        @param request: InnerLimitRateCardsRequest
        @return: InnerLimitRateCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_limit_rate_cards_with_options(request, runtime)

    async def inner_limit_rate_cards_async(
        self,
        request: cc5g20220314_models.InnerLimitRateCardsRequest,
    ) -> cc5g20220314_models.InnerLimitRateCardsResponse:
        """
        @param request: InnerLimitRateCardsRequest
        @return: InnerLimitRateCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_limit_rate_cards_with_options_async(request, runtime)

    def inner_stop_cards_with_options(
        self,
        request: cc5g20220314_models.InnerStopCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.InnerStopCardsResponse:
        """
        @param request: InnerStopCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerStopCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.inner_api):
            query['InnerApi'] = request.inner_api
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerStopCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.InnerStopCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def inner_stop_cards_with_options_async(
        self,
        request: cc5g20220314_models.InnerStopCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.InnerStopCardsResponse:
        """
        @param request: InnerStopCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerStopCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.inner_api):
            query['InnerApi'] = request.inner_api
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerStopCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.InnerStopCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inner_stop_cards(
        self,
        request: cc5g20220314_models.InnerStopCardsRequest,
    ) -> cc5g20220314_models.InnerStopCardsResponse:
        """
        @param request: InnerStopCardsRequest
        @return: InnerStopCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_stop_cards_with_options(request, runtime)

    async def inner_stop_cards_async(
        self,
        request: cc5g20220314_models.InnerStopCardsRequest,
    ) -> cc5g20220314_models.InnerStopCardsResponse:
        """
        @param request: InnerStopCardsRequest
        @return: InnerStopCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_stop_cards_with_options_async(request, runtime)

    def list_apns_with_options(
        self,
        request: cc5g20220314_models.ListAPNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListAPNsResponse:
        """
        @summary 查询5G高速上云服务支持的APN列表
        
        @param request: ListAPNsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAPNsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAPNs',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAPNsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apns_with_options_async(
        self,
        request: cc5g20220314_models.ListAPNsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListAPNsResponse:
        """
        @summary 查询5G高速上云服务支持的APN列表
        
        @param request: ListAPNsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAPNsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAPNs',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAPNsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apns(
        self,
        request: cc5g20220314_models.ListAPNsRequest,
    ) -> cc5g20220314_models.ListAPNsResponse:
        """
        @summary 查询5G高速上云服务支持的APN列表
        
        @param request: ListAPNsRequest
        @return: ListAPNsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_apns_with_options(request, runtime)

    async def list_apns_async(
        self,
        request: cc5g20220314_models.ListAPNsRequest,
    ) -> cc5g20220314_models.ListAPNsResponse:
        """
        @summary 查询5G高速上云服务支持的APN列表
        
        @param request: ListAPNsRequest
        @return: ListAPNsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_apns_with_options_async(request, runtime)

    def list_authorization_rules_with_options(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例的授权规则列表
        
        @param request: ListAuthorizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizationRules',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorization_rules_with_options_async(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例的授权规则列表
        
        @param request: ListAuthorizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizationRules',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorization_rules(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例的授权规则列表
        
        @param request: ListAuthorizationRulesRequest
        @return: ListAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    async def list_authorization_rules_async(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例的授权规则列表
        
        @param request: ListAuthorizationRulesRequest
        @return: ListAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authorization_rules_with_options_async(request, runtime)

    def list_batch_operate_cards_tasks_with_options(
        self,
        request: cc5g20220314_models.ListBatchOperateCardsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListBatchOperateCardsTasksResponse:
        """
        @summary 查询批量操作卡任务列表
        
        @param request: ListBatchOperateCardsTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchOperateCardsTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatchOperateCardsTasks',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListBatchOperateCardsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batch_operate_cards_tasks_with_options_async(
        self,
        request: cc5g20220314_models.ListBatchOperateCardsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListBatchOperateCardsTasksResponse:
        """
        @summary 查询批量操作卡任务列表
        
        @param request: ListBatchOperateCardsTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchOperateCardsTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatchOperateCardsTasks',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListBatchOperateCardsTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batch_operate_cards_tasks(
        self,
        request: cc5g20220314_models.ListBatchOperateCardsTasksRequest,
    ) -> cc5g20220314_models.ListBatchOperateCardsTasksResponse:
        """
        @summary 查询批量操作卡任务列表
        
        @param request: ListBatchOperateCardsTasksRequest
        @return: ListBatchOperateCardsTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_batch_operate_cards_tasks_with_options(request, runtime)

    async def list_batch_operate_cards_tasks_async(
        self,
        request: cc5g20220314_models.ListBatchOperateCardsTasksRequest,
    ) -> cc5g20220314_models.ListBatchOperateCardsTasksResponse:
        """
        @summary 查询批量操作卡任务列表
        
        @param request: ListBatchOperateCardsTasksRequest
        @return: ListBatchOperateCardsTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_batch_operate_cards_tasks_with_options_async(request, runtime)

    def list_card_area_limit_support_area_with_options(
        self,
        request: cc5g20220314_models.ListCardAreaLimitSupportAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardAreaLimitSupportAreaResponse:
        """
        @summary 查询5G高速上云服务物联网卡区域解锁支持区域
        
        @param request: ListCardAreaLimitSupportAreaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardAreaLimitSupportAreaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardAreaLimitSupportArea',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardAreaLimitSupportAreaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_card_area_limit_support_area_with_options_async(
        self,
        request: cc5g20220314_models.ListCardAreaLimitSupportAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardAreaLimitSupportAreaResponse:
        """
        @summary 查询5G高速上云服务物联网卡区域解锁支持区域
        
        @param request: ListCardAreaLimitSupportAreaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardAreaLimitSupportAreaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardAreaLimitSupportArea',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardAreaLimitSupportAreaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_card_area_limit_support_area(
        self,
        request: cc5g20220314_models.ListCardAreaLimitSupportAreaRequest,
    ) -> cc5g20220314_models.ListCardAreaLimitSupportAreaResponse:
        """
        @summary 查询5G高速上云服务物联网卡区域解锁支持区域
        
        @param request: ListCardAreaLimitSupportAreaRequest
        @return: ListCardAreaLimitSupportAreaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_card_area_limit_support_area_with_options(request, runtime)

    async def list_card_area_limit_support_area_async(
        self,
        request: cc5g20220314_models.ListCardAreaLimitSupportAreaRequest,
    ) -> cc5g20220314_models.ListCardAreaLimitSupportAreaResponse:
        """
        @summary 查询5G高速上云服务物联网卡区域解锁支持区域
        
        @param request: ListCardAreaLimitSupportAreaRequest
        @return: ListCardAreaLimitSupportAreaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_card_area_limit_support_area_with_options_async(request, runtime)

    def list_card_day_usages_with_options(
        self,
        request: cc5g20220314_models.ListCardDayUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardDayUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的卡单日流量信息列表
        
        @param request: ListCardDayUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardDayUsagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardDayUsages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardDayUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_card_day_usages_with_options_async(
        self,
        request: cc5g20220314_models.ListCardDayUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardDayUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的卡单日流量信息列表
        
        @param request: ListCardDayUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardDayUsagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardDayUsages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardDayUsagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_card_day_usages(
        self,
        request: cc5g20220314_models.ListCardDayUsagesRequest,
    ) -> cc5g20220314_models.ListCardDayUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的卡单日流量信息列表
        
        @param request: ListCardDayUsagesRequest
        @return: ListCardDayUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_card_day_usages_with_options(request, runtime)

    async def list_card_day_usages_async(
        self,
        request: cc5g20220314_models.ListCardDayUsagesRequest,
    ) -> cc5g20220314_models.ListCardDayUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的卡单日流量信息列表
        
        @param request: ListCardDayUsagesRequest
        @return: ListCardDayUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_card_day_usages_with_options_async(request, runtime)

    def list_card_usages_with_options(
        self,
        request: cc5g20220314_models.ListCardUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的流量信息列表
        
        @param request: ListCardUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardUsagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardUsages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_card_usages_with_options_async(
        self,
        request: cc5g20220314_models.ListCardUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的流量信息列表
        
        @param request: ListCardUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardUsagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCardUsages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardUsagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_card_usages(
        self,
        request: cc5g20220314_models.ListCardUsagesRequest,
    ) -> cc5g20220314_models.ListCardUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的流量信息列表
        
        @param request: ListCardUsagesRequest
        @return: ListCardUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_card_usages_with_options(request, runtime)

    async def list_card_usages_async(
        self,
        request: cc5g20220314_models.ListCardUsagesRequest,
    ) -> cc5g20220314_models.ListCardUsagesResponse:
        """
        @summary 查询5G高速上云服务实例的流量信息列表
        
        @param request: ListCardUsagesRequest
        @return: ListCardUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_card_usages_with_options_async(request, runtime)

    def list_cards_with_options(
        self,
        request: cc5g20220314_models.ListCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardsResponse:
        """
        @summary 查询5G高速上云服务实例的连接列表
        
        @param request: ListCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cards_with_options_async(
        self,
        request: cc5g20220314_models.ListCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardsResponse:
        """
        @summary 查询5G高速上云服务实例的连接列表
        
        @param request: ListCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCardsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cards(
        self,
        request: cc5g20220314_models.ListCardsRequest,
    ) -> cc5g20220314_models.ListCardsResponse:
        """
        @summary 查询5G高速上云服务实例的连接列表
        
        @param request: ListCardsRequest
        @return: ListCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cards_with_options(request, runtime)

    async def list_cards_async(
        self,
        request: cc5g20220314_models.ListCardsRequest,
    ) -> cc5g20220314_models.ListCardsResponse:
        """
        @summary 查询5G高速上云服务实例的连接列表
        
        @param request: ListCardsRequest
        @return: ListCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cards_with_options_async(request, runtime)

    def list_data_packages_with_options(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
        """
        @summary 查询5G高速上云服务实例下的带宽包列表
        
        @param request: ListDataPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataPackagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataPackages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDataPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_packages_with_options_async(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
        """
        @summary 查询5G高速上云服务实例下的带宽包列表
        
        @param request: ListDataPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataPackagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataPackages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDataPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_packages(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
        """
        @summary 查询5G高速上云服务实例下的带宽包列表
        
        @param request: ListDataPackagesRequest
        @return: ListDataPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_packages_with_options(request, runtime)

    async def list_data_packages_async(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
        """
        @summary 查询5G高速上云服务实例下的带宽包列表
        
        @param request: ListDataPackagesRequest
        @return: ListDataPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_packages_with_options_async(request, runtime)

    def list_diagnose_info_for_single_card_with_options(
        self,
        request: cc5g20220314_models.ListDiagnoseInfoForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse:
        """
        @summary 查询单卡诊断信息列表
        
        @param request: ListDiagnoseInfoForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnoseInfoForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseInfoForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnose_info_for_single_card_with_options_async(
        self,
        request: cc5g20220314_models.ListDiagnoseInfoForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse:
        """
        @summary 查询单卡诊断信息列表
        
        @param request: ListDiagnoseInfoForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnoseInfoForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseInfoForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnose_info_for_single_card(
        self,
        request: cc5g20220314_models.ListDiagnoseInfoForSingleCardRequest,
    ) -> cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse:
        """
        @summary 查询单卡诊断信息列表
        
        @param request: ListDiagnoseInfoForSingleCardRequest
        @return: ListDiagnoseInfoForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_diagnose_info_for_single_card_with_options(request, runtime)

    async def list_diagnose_info_for_single_card_async(
        self,
        request: cc5g20220314_models.ListDiagnoseInfoForSingleCardRequest,
    ) -> cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse:
        """
        @summary 查询单卡诊断信息列表
        
        @param request: ListDiagnoseInfoForSingleCardRequest
        @return: ListDiagnoseInfoForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_diagnose_info_for_single_card_with_options_async(request, runtime)

    def list_group_authorization_rules_with_options(
        self,
        request: cc5g20220314_models.ListGroupAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListGroupAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例组的授权规则列表
        
        @param request: ListGroupAuthorizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupAuthorizationRules',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListGroupAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_authorization_rules_with_options_async(
        self,
        request: cc5g20220314_models.ListGroupAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListGroupAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例组的授权规则列表
        
        @param request: ListGroupAuthorizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupAuthorizationRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupAuthorizationRules',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListGroupAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_authorization_rules(
        self,
        request: cc5g20220314_models.ListGroupAuthorizationRulesRequest,
    ) -> cc5g20220314_models.ListGroupAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例组的授权规则列表
        
        @param request: ListGroupAuthorizationRulesRequest
        @return: ListGroupAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_group_authorization_rules_with_options(request, runtime)

    async def list_group_authorization_rules_async(
        self,
        request: cc5g20220314_models.ListGroupAuthorizationRulesRequest,
    ) -> cc5g20220314_models.ListGroupAuthorizationRulesResponse:
        """
        @summary 查询5G高速上云服务实例组的授权规则列表
        
        @param request: ListGroupAuthorizationRulesRequest
        @return: ListGroupAuthorizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_group_authorization_rules_with_options_async(request, runtime)

    def list_io_tcloud_connector_backhaul_route_with_options(
        self,
        request: cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 查询iotcc实例回程路由
        
        @param request: ListIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_io_tcloud_connector_backhaul_route_with_options_async(
        self,
        request: cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 查询iotcc实例回程路由
        
        @param request: ListIoTCloudConnectorBackhaulRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIoTCloudConnectorBackhaulRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_io_tcloud_connector_backhaul_route(
        self,
        request: cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 查询iotcc实例回程路由
        
        @param request: ListIoTCloudConnectorBackhaulRouteRequest
        @return: ListIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    async def list_io_tcloud_connector_backhaul_route_async(
        self,
        request: cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteRequest,
    ) -> cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse:
        """
        @summary 查询iotcc实例回程路由
        
        @param request: ListIoTCloudConnectorBackhaulRouteRequest
        @return: ListIoTCloudConnectorBackhaulRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_io_tcloud_connector_backhaul_route_with_options_async(request, runtime)

    def list_orders_with_options(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListOrdersResponse:
        """
        @summary 查询5G高速上云服务实例下的订单列表
        
        @param request: ListOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrdersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrders',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_orders_with_options_async(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListOrdersResponse:
        """
        @summary 查询5G高速上云服务实例下的订单列表
        
        @param request: ListOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrdersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrders',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_orders(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
    ) -> cc5g20220314_models.ListOrdersResponse:
        """
        @summary 查询5G高速上云服务实例下的订单列表
        
        @param request: ListOrdersRequest
        @return: ListOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_orders_with_options(request, runtime)

    async def list_orders_async(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
    ) -> cc5g20220314_models.ListOrdersResponse:
        """
        @summary 查询5G高速上云服务实例下的订单列表
        
        @param request: ListOrdersRequest
        @return: ListOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_orders_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListRegionsResponse:
        """
        @summary 查询5G高速上云服务支持的REGION
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListRegionsResponse:
        """
        @summary 查询5G高速上云服务支持的REGION
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
    ) -> cc5g20220314_models.ListRegionsResponse:
        """
        @summary 查询5G高速上云服务支持的REGION
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
    ) -> cc5g20220314_models.ListRegionsResponse:
        """
        @summary 查询5G高速上云服务支持的REGION
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_wireless_cloud_connector_groups_with_options(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse:
        """
        @summary 查询5G高速上云服务实例分组列表
        
        @param request: ListWirelessCloudConnectorGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWirelessCloudConnectorGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWirelessCloudConnectorGroups',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_wireless_cloud_connector_groups_with_options_async(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse:
        """
        @summary 查询5G高速上云服务实例分组列表
        
        @param request: ListWirelessCloudConnectorGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWirelessCloudConnectorGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWirelessCloudConnectorGroups',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_wireless_cloud_connector_groups(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorGroupsRequest,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse:
        """
        @summary 查询5G高速上云服务实例分组列表
        
        @param request: ListWirelessCloudConnectorGroupsRequest
        @return: ListWirelessCloudConnectorGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_wireless_cloud_connector_groups_with_options(request, runtime)

    async def list_wireless_cloud_connector_groups_async(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorGroupsRequest,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorGroupsResponse:
        """
        @summary 查询5G高速上云服务实例分组列表
        
        @param request: ListWirelessCloudConnectorGroupsRequest
        @return: ListWirelessCloudConnectorGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_wireless_cloud_connector_groups_with_options_async(request, runtime)

    def list_wireless_cloud_connectors_with_options(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
        """
        @summary 查询5G高速上云服务实例列表
        
        @param request: ListWirelessCloudConnectorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWirelessCloudConnectorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWirelessCloudConnectors',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListWirelessCloudConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_wireless_cloud_connectors_with_options_async(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
        """
        @summary 查询5G高速上云服务实例列表
        
        @param request: ListWirelessCloudConnectorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWirelessCloudConnectorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWirelessCloudConnectors',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListWirelessCloudConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_wireless_cloud_connectors(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
        """
        @summary 查询5G高速上云服务实例列表
        
        @param request: ListWirelessCloudConnectorsRequest
        @return: ListWirelessCloudConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_wireless_cloud_connectors_with_options(request, runtime)

    async def list_wireless_cloud_connectors_async(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
        """
        @summary 查询5G高速上云服务实例列表
        
        @param request: ListWirelessCloudConnectorsRequest
        @return: ListWirelessCloudConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_wireless_cloud_connectors_with_options_async(request, runtime)

    def list_zones_with_options(
        self,
        request: cc5g20220314_models.ListZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListZonesResponse:
        """
        @summary 查询5G高速上云服务支持的可用区
        
        @param request: ListZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        request: cc5g20220314_models.ListZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListZonesResponse:
        """
        @summary 查询5G高速上云服务支持的可用区
        
        @param request: ListZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(
        self,
        request: cc5g20220314_models.ListZonesRequest,
    ) -> cc5g20220314_models.ListZonesResponse:
        """
        @summary 查询5G高速上云服务支持的可用区
        
        @param request: ListZonesRequest
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_zones_with_options(request, runtime)

    async def list_zones_async(
        self,
        request: cc5g20220314_models.ListZonesRequest,
    ) -> cc5g20220314_models.ListZonesResponse:
        """
        @summary 查询5G高速上云服务支持的可用区
        
        @param request: ListZonesRequest
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_zones_with_options_async(request, runtime)

    def lock_cards_with_options(
        self,
        request: cc5g20220314_models.LockCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.LockCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: LockCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.LockCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_cards_with_options_async(
        self,
        request: cc5g20220314_models.LockCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.LockCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: LockCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.LockCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_cards(
        self,
        request: cc5g20220314_models.LockCardsRequest,
    ) -> cc5g20220314_models.LockCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: LockCardsRequest
        @return: LockCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_cards_with_options(request, runtime)

    async def lock_cards_async(
        self,
        request: cc5g20220314_models.LockCardsRequest,
    ) -> cc5g20220314_models.LockCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: LockCardsRequest
        @return: LockCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_cards_with_options_async(request, runtime)

    def modify_wireless_cloud_connector_feature_with_options(
        self,
        request: cc5g20220314_models.ModifyWirelessCloudConnectorFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse:
        """
        @summary 修改5G高速上云服务实例属性
        
        @param request: ModifyWirelessCloudConnectorFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWirelessCloudConnectorFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_value):
            query['FeatureValue'] = request.feature_value
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWirelessCloudConnectorFeature',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_wireless_cloud_connector_feature_with_options_async(
        self,
        request: cc5g20220314_models.ModifyWirelessCloudConnectorFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse:
        """
        @summary 修改5G高速上云服务实例属性
        
        @param request: ModifyWirelessCloudConnectorFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWirelessCloudConnectorFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_value):
            query['FeatureValue'] = request.feature_value
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWirelessCloudConnectorFeature',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_wireless_cloud_connector_feature(
        self,
        request: cc5g20220314_models.ModifyWirelessCloudConnectorFeatureRequest,
    ) -> cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse:
        """
        @summary 修改5G高速上云服务实例属性
        
        @param request: ModifyWirelessCloudConnectorFeatureRequest
        @return: ModifyWirelessCloudConnectorFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_wireless_cloud_connector_feature_with_options(request, runtime)

    async def modify_wireless_cloud_connector_feature_async(
        self,
        request: cc5g20220314_models.ModifyWirelessCloudConnectorFeatureRequest,
    ) -> cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse:
        """
        @summary 修改5G高速上云服务实例属性
        
        @param request: ModifyWirelessCloudConnectorFeatureRequest
        @return: ModifyWirelessCloudConnectorFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_wireless_cloud_connector_feature_with_options_async(request, runtime)

    def open_cc_5g_service_with_options(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
        """
        @summary 开通5G高速上云服务
        
        @param request: OpenCc5gServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCc5gServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCc5gService',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.OpenCc5gServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cc_5g_service_with_options_async(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
        """
        @summary 开通5G高速上云服务
        
        @param request: OpenCc5gServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCc5gServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCc5gService',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.OpenCc5gServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cc_5g_service(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
        """
        @summary 开通5G高速上云服务
        
        @param request: OpenCc5gServiceRequest
        @return: OpenCc5gServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_cc_5g_service_with_options(request, runtime)

    async def open_cc_5g_service_async(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
        """
        @summary 开通5G高速上云服务
        
        @param request: OpenCc5gServiceRequest
        @return: OpenCc5gServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_cc_5g_service_with_options_async(request, runtime)

    def rebind_cards_with_options(
        self,
        request: cc5g20220314_models.RebindCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RebindCardsResponse:
        """
        @summary 物联网卡换绑解锁操作
        
        @param request: RebindCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebindCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RebindCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebind_cards_with_options_async(
        self,
        request: cc5g20220314_models.RebindCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RebindCardsResponse:
        """
        @summary 物联网卡换绑解锁操作
        
        @param request: RebindCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebindCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RebindCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebind_cards(
        self,
        request: cc5g20220314_models.RebindCardsRequest,
    ) -> cc5g20220314_models.RebindCardsResponse:
        """
        @summary 物联网卡换绑解锁操作
        
        @param request: RebindCardsRequest
        @return: RebindCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebind_cards_with_options(request, runtime)

    async def rebind_cards_async(
        self,
        request: cc5g20220314_models.RebindCardsRequest,
    ) -> cc5g20220314_models.RebindCardsResponse:
        """
        @summary 物联网卡换绑解锁操作
        
        @param request: RebindCardsRequest
        @return: RebindCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rebind_cards_with_options_async(request, runtime)

    def remove_wireless_cloud_connector_from_group_with_options(
        self,
        request: cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse:
        """
        @summary 从组里移除5G高速上云服务实例
        
        @param request: RemoveWirelessCloudConnectorFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveWirelessCloudConnectorFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveWirelessCloudConnectorFromGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_wireless_cloud_connector_from_group_with_options_async(
        self,
        request: cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse:
        """
        @summary 从组里移除5G高速上云服务实例
        
        @param request: RemoveWirelessCloudConnectorFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveWirelessCloudConnectorFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveWirelessCloudConnectorFromGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_wireless_cloud_connector_from_group(
        self,
        request: cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupRequest,
    ) -> cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse:
        """
        @summary 从组里移除5G高速上云服务实例
        
        @param request: RemoveWirelessCloudConnectorFromGroupRequest
        @return: RemoveWirelessCloudConnectorFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_wireless_cloud_connector_from_group_with_options(request, runtime)

    async def remove_wireless_cloud_connector_from_group_async(
        self,
        request: cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupRequest,
    ) -> cc5g20220314_models.RemoveWirelessCloudConnectorFromGroupResponse:
        """
        @summary 从组里移除5G高速上云服务实例
        
        @param request: RemoveWirelessCloudConnectorFromGroupRequest
        @return: RemoveWirelessCloudConnectorFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_wireless_cloud_connector_from_group_with_options_async(request, runtime)

    def reset_area_limit_cards_with_options(
        self,
        request: cc5g20220314_models.ResetAreaLimitCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ResetAreaLimitCardsResponse:
        """
        @summary 重置单卡区域限制
        
        @param request: ResetAreaLimitCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAreaLimitCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAreaLimitCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ResetAreaLimitCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_area_limit_cards_with_options_async(
        self,
        request: cc5g20220314_models.ResetAreaLimitCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ResetAreaLimitCardsResponse:
        """
        @summary 重置单卡区域限制
        
        @param request: ResetAreaLimitCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAreaLimitCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAreaLimitCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ResetAreaLimitCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_area_limit_cards(
        self,
        request: cc5g20220314_models.ResetAreaLimitCardsRequest,
    ) -> cc5g20220314_models.ResetAreaLimitCardsResponse:
        """
        @summary 重置单卡区域限制
        
        @param request: ResetAreaLimitCardsRequest
        @return: ResetAreaLimitCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_area_limit_cards_with_options(request, runtime)

    async def reset_area_limit_cards_async(
        self,
        request: cc5g20220314_models.ResetAreaLimitCardsRequest,
    ) -> cc5g20220314_models.ResetAreaLimitCardsResponse:
        """
        @summary 重置单卡区域限制
        
        @param request: ResetAreaLimitCardsRequest
        @return: ResetAreaLimitCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_area_limit_cards_with_options_async(request, runtime)

    def resume_cards_with_options(
        self,
        request: cc5g20220314_models.ResumeCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ResumeCardsResponse:
        """
        @summary 激活单卡运营商侧卡状态恢复
        
        @param request: ResumeCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ResumeCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_cards_with_options_async(
        self,
        request: cc5g20220314_models.ResumeCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ResumeCardsResponse:
        """
        @summary 激活单卡运营商侧卡状态恢复
        
        @param request: ResumeCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ResumeCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_cards(
        self,
        request: cc5g20220314_models.ResumeCardsRequest,
    ) -> cc5g20220314_models.ResumeCardsResponse:
        """
        @summary 激活单卡运营商侧卡状态恢复
        
        @param request: ResumeCardsRequest
        @return: ResumeCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_cards_with_options(request, runtime)

    async def resume_cards_async(
        self,
        request: cc5g20220314_models.ResumeCardsRequest,
    ) -> cc5g20220314_models.ResumeCardsResponse:
        """
        @summary 激活单卡运营商侧卡状态恢复
        
        @param request: ResumeCardsRequest
        @return: ResumeCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_cards_with_options_async(request, runtime)

    def revoke_net_link_with_options(
        self,
        request: cc5g20220314_models.RevokeNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RevokeNetLinkResponse:
        """
        @summary 撤销分享授权网络连接
        
        @param request: RevokeNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RevokeNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_net_link_with_options_async(
        self,
        request: cc5g20220314_models.RevokeNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.RevokeNetLinkResponse:
        """
        @summary 撤销分享授权网络连接
        
        @param request: RevokeNetLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeNetLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RevokeNetLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_net_link(
        self,
        request: cc5g20220314_models.RevokeNetLinkRequest,
    ) -> cc5g20220314_models.RevokeNetLinkResponse:
        """
        @summary 撤销分享授权网络连接
        
        @param request: RevokeNetLinkRequest
        @return: RevokeNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_net_link_with_options(request, runtime)

    async def revoke_net_link_async(
        self,
        request: cc5g20220314_models.RevokeNetLinkRequest,
    ) -> cc5g20220314_models.RevokeNetLinkResponse:
        """
        @summary 撤销分享授权网络连接
        
        @param request: RevokeNetLinkRequest
        @return: RevokeNetLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_net_link_with_options_async(request, runtime)

    def stop_cards_with_options(
        self,
        request: cc5g20220314_models.StopCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.StopCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: StopCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.StopCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cards_with_options_async(
        self,
        request: cc5g20220314_models.StopCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.StopCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: StopCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.StopCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cards(
        self,
        request: cc5g20220314_models.StopCardsRequest,
    ) -> cc5g20220314_models.StopCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: StopCardsRequest
        @return: StopCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cards_with_options(request, runtime)

    async def stop_cards_async(
        self,
        request: cc5g20220314_models.StopCardsRequest,
    ) -> cc5g20220314_models.StopCardsResponse:
        """
        @summary 运营商侧卡停机
        
        @param request: StopCardsRequest
        @return: StopCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_cards_with_options_async(request, runtime)

    def submit_diagnose_task_for_single_card_with_options(
        self,
        request: cc5g20220314_models.SubmitDiagnoseTaskForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse:
        """
        @summary 开启cciot单卡一键诊断
        
        @param request: SubmitDiagnoseTaskForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDiagnoseTaskForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDiagnoseTaskForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_diagnose_task_for_single_card_with_options_async(
        self,
        request: cc5g20220314_models.SubmitDiagnoseTaskForSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse:
        """
        @summary 开启cciot单卡一键诊断
        
        @param request: SubmitDiagnoseTaskForSingleCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDiagnoseTaskForSingleCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDiagnoseTaskForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_diagnose_task_for_single_card(
        self,
        request: cc5g20220314_models.SubmitDiagnoseTaskForSingleCardRequest,
    ) -> cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse:
        """
        @summary 开启cciot单卡一键诊断
        
        @param request: SubmitDiagnoseTaskForSingleCardRequest
        @return: SubmitDiagnoseTaskForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_diagnose_task_for_single_card_with_options(request, runtime)

    async def submit_diagnose_task_for_single_card_async(
        self,
        request: cc5g20220314_models.SubmitDiagnoseTaskForSingleCardRequest,
    ) -> cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse:
        """
        @summary 开启cciot单卡一键诊断
        
        @param request: SubmitDiagnoseTaskForSingleCardRequest
        @return: SubmitDiagnoseTaskForSingleCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_diagnose_task_for_single_card_with_options_async(request, runtime)

    def switch_wireless_cloud_connector_to_business_with_options(
        self,
        request: cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse:
        """
        @summary 切换cc5g实例商业类型到商业版
        
        @param request: SwitchWirelessCloudConnectorToBusinessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchWirelessCloudConnectorToBusinessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchWirelessCloudConnectorToBusiness',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_wireless_cloud_connector_to_business_with_options_async(
        self,
        request: cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse:
        """
        @summary 切换cc5g实例商业类型到商业版
        
        @param request: SwitchWirelessCloudConnectorToBusinessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchWirelessCloudConnectorToBusinessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchWirelessCloudConnectorToBusiness',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_wireless_cloud_connector_to_business(
        self,
        request: cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessRequest,
    ) -> cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse:
        """
        @summary 切换cc5g实例商业类型到商业版
        
        @param request: SwitchWirelessCloudConnectorToBusinessRequest
        @return: SwitchWirelessCloudConnectorToBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_wireless_cloud_connector_to_business_with_options(request, runtime)

    async def switch_wireless_cloud_connector_to_business_async(
        self,
        request: cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessRequest,
    ) -> cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse:
        """
        @summary 切换cc5g实例商业类型到商业版
        
        @param request: SwitchWirelessCloudConnectorToBusinessRequest
        @return: SwitchWirelessCloudConnectorToBusinessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_wireless_cloud_connector_to_business_with_options_async(request, runtime)

    def unlock_cards_with_options(
        self,
        request: cc5g20220314_models.UnlockCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UnlockCardsResponse:
        """
        @summary 批量解锁卡
        
        @param request: UnlockCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UnlockCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_cards_with_options_async(
        self,
        request: cc5g20220314_models.UnlockCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UnlockCardsResponse:
        """
        @summary 批量解锁卡
        
        @param request: UnlockCardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockCardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UnlockCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_cards(
        self,
        request: cc5g20220314_models.UnlockCardsRequest,
    ) -> cc5g20220314_models.UnlockCardsResponse:
        """
        @summary 批量解锁卡
        
        @param request: UnlockCardsRequest
        @return: UnlockCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_cards_with_options(request, runtime)

    async def unlock_cards_async(
        self,
        request: cc5g20220314_models.UnlockCardsRequest,
    ) -> cc5g20220314_models.UnlockCardsResponse:
        """
        @summary 批量解锁卡
        
        @param request: UnlockCardsRequest
        @return: UnlockCardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_cards_with_options_async(request, runtime)

    def update_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的授权规则
        
        @param request: UpdateAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的授权规则
        
        @param request: UpdateAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_authorization_rule(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的授权规则
        
        @param request: UpdateAuthorizationRuleRequest
        @return: UpdateAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_with_options(request, runtime)

    async def update_authorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的授权规则
        
        @param request: UpdateAuthorizationRuleRequest
        @return: UpdateAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_authorization_rule_with_options_async(request, runtime)

    def update_batch_operate_cards_task_with_options(
        self,
        request: cc5g20220314_models.UpdateBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateBatchOperateCardsTaskResponse:
        """
        @summary 修改批量操作卡任务
        
        @param request: UpdateBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_operate_cards_task_with_options_async(
        self,
        request: cc5g20220314_models.UpdateBatchOperateCardsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateBatchOperateCardsTaskResponse:
        """
        @summary 修改批量操作卡任务
        
        @param request: UpdateBatchOperateCardsTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchOperateCardsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateBatchOperateCardsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch_operate_cards_task(
        self,
        request: cc5g20220314_models.UpdateBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.UpdateBatchOperateCardsTaskResponse:
        """
        @summary 修改批量操作卡任务
        
        @param request: UpdateBatchOperateCardsTaskRequest
        @return: UpdateBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_batch_operate_cards_task_with_options(request, runtime)

    async def update_batch_operate_cards_task_async(
        self,
        request: cc5g20220314_models.UpdateBatchOperateCardsTaskRequest,
    ) -> cc5g20220314_models.UpdateBatchOperateCardsTaskResponse:
        """
        @summary 修改批量操作卡任务
        
        @param request: UpdateBatchOperateCardsTaskRequest
        @return: UpdateBatchOperateCardsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_batch_operate_cards_task_with_options_async(request, runtime)

    def update_card_with_options(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateCardResponse:
        """
        @summary 修改5G高速上云服务实例的连接描述和名称信息
        
        @param request: UpdateCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_card_with_options_async(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateCardResponse:
        """
        @summary 修改5G高速上云服务实例的连接描述和名称信息
        
        @param request: UpdateCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_card(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
    ) -> cc5g20220314_models.UpdateCardResponse:
        """
        @summary 修改5G高速上云服务实例的连接描述和名称信息
        
        @param request: UpdateCardRequest
        @return: UpdateCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_card_with_options(request, runtime)

    async def update_card_async(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
    ) -> cc5g20220314_models.UpdateCardResponse:
        """
        @summary 修改5G高速上云服务实例的连接描述和名称信息
        
        @param request: UpdateCardRequest
        @return: UpdateCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_card_with_options_async(request, runtime)

    def update_dnsauthorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的DNS授权规则
        
        @param request: UpdateDNSAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDNSAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateDNSAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dnsauthorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的DNS授权规则
        
        @param request: UpdateDNSAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDNSAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateDNSAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dnsauthorization_rule(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的DNS授权规则
        
        @param request: UpdateDNSAuthorizationRuleRequest
        @return: UpdateDNSAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dnsauthorization_rule_with_options(request, runtime)

    async def update_dnsauthorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例的DNS授权规则
        
        @param request: UpdateDNSAuthorizationRuleRequest
        @return: UpdateDNSAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dnsauthorization_rule_with_options_async(request, runtime)

    def update_group_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateGroupAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的授权规则
        
        @param request: UpdateGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateGroupAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.UpdateGroupAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateGroupAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的授权规则
        
        @param request: UpdateGroupAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateGroupAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_authorization_rule(
        self,
        request: cc5g20220314_models.UpdateGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateGroupAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的授权规则
        
        @param request: UpdateGroupAuthorizationRuleRequest
        @return: UpdateGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_authorization_rule_with_options(request, runtime)

    async def update_group_authorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateGroupAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateGroupAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的授权规则
        
        @param request: UpdateGroupAuthorizationRuleRequest
        @return: UpdateGroupAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_authorization_rule_with_options_async(request, runtime)

    def update_group_dns_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateGroupDnsAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的DNS授权规则
        
        @param request: UpdateGroupDnsAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupDnsAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDnsAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_dns_authorization_rule_with_options_async(
        self,
        request: cc5g20220314_models.UpdateGroupDnsAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的DNS授权规则
        
        @param request: UpdateGroupDnsAuthorizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupDnsAuthorizationRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDnsAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_dns_authorization_rule(
        self,
        request: cc5g20220314_models.UpdateGroupDnsAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的DNS授权规则
        
        @param request: UpdateGroupDnsAuthorizationRuleRequest
        @return: UpdateGroupDnsAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_dns_authorization_rule_with_options(request, runtime)

    async def update_group_dns_authorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateGroupDnsAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateGroupDnsAuthorizationRuleResponse:
        """
        @summary 更新5G高速上云服务实例组的DNS授权规则
        
        @param request: UpdateGroupDnsAuthorizationRuleRequest
        @return: UpdateGroupDnsAuthorizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_dns_authorization_rule_with_options_async(request, runtime)

    def update_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
        """
        @summary 修改5G高速上云服务实例
        
        @param request: UpdateWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_wireless_cloud_connector_with_options_async(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
        """
        @summary 修改5G高速上云服务实例
        
        @param request: UpdateWirelessCloudConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWirelessCloudConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateWirelessCloudConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_wireless_cloud_connector(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
        """
        @summary 修改5G高速上云服务实例
        
        @param request: UpdateWirelessCloudConnectorRequest
        @return: UpdateWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_wireless_cloud_connector_with_options(request, runtime)

    async def update_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
        """
        @summary 修改5G高速上云服务实例
        
        @param request: UpdateWirelessCloudConnectorRequest
        @return: UpdateWirelessCloudConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_wireless_cloud_connector_with_options_async(request, runtime)

    def update_wireless_cloud_connector_group_with_options(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse:
        """
        @summary 修改5G高速上云服务实例分组
        
        @param request: UpdateWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_wireless_cloud_connector_group_with_options_async(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse:
        """
        @summary 修改5G高速上云服务实例分组
        
        @param request: UpdateWirelessCloudConnectorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWirelessCloudConnectorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_group_id):
            query['WirelessCloudConnectorGroupId'] = request.wireless_cloud_connector_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWirelessCloudConnectorGroup',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_wireless_cloud_connector_group(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse:
        """
        @summary 修改5G高速上云服务实例分组
        
        @param request: UpdateWirelessCloudConnectorGroupRequest
        @return: UpdateWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_wireless_cloud_connector_group_with_options(request, runtime)

    async def update_wireless_cloud_connector_group_async(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorGroupRequest,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorGroupResponse:
        """
        @summary 修改5G高速上云服务实例分组
        
        @param request: UpdateWirelessCloudConnectorGroupRequest
        @return: UpdateWirelessCloudConnectorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_wireless_cloud_connector_group_with_options_async(request, runtime)
