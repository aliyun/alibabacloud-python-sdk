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
        runtime = util_models.RuntimeOptions()
        return self.add_dnsauthorization_rule_with_options(request, runtime)

    async def add_dnsauthorization_rule_async(
        self,
        request: cc5g20220314_models.AddDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.AddDNSAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dnsauthorization_rule_with_options_async(request, runtime)

    def attach_vpc_to_net_link_with_options(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.attach_vpc_to_net_link_with_options(request, runtime)

    async def attach_vpc_to_net_link_async(
        self,
        request: cc5g20220314_models.AttachVpcToNetLinkRequest,
    ) -> cc5g20220314_models.AttachVpcToNetLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_vpc_to_net_link_with_options_async(request, runtime)

    def create_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    async def create_authorization_rule_async(
        self,
        request: cc5g20220314_models.CreateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.CreateAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_authorization_rule_with_options_async(request, runtime)

    def create_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_wireless_cloud_connector_with_options(request, runtime)

    async def create_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.CreateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.CreateWirelessCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_wireless_cloud_connector_with_options_async(request, runtime)

    def delete_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    async def delete_authorization_rule_async(
        self,
        request: cc5g20220314_models.DeleteAuthorizationRuleRequest,
    ) -> cc5g20220314_models.DeleteAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_authorization_rule_with_options_async(request, runtime)

    def delete_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_wireless_cloud_connector_with_options(request, runtime)

    async def delete_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.DeleteWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.DeleteWirelessCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_wireless_cloud_connector_with_options_async(request, runtime)

    def detach_vpc_from_net_link_with_options(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.detach_vpc_from_net_link_with_options(request, runtime)

    async def detach_vpc_from_net_link_async(
        self,
        request: cc5g20220314_models.DetachVpcFromNetLinkRequest,
    ) -> cc5g20220314_models.DetachVpcFromNetLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_vpc_from_net_link_with_options_async(request, runtime)

    def get_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_wireless_cloud_connector_with_options(request, runtime)

    async def get_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.GetWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.GetWirelessCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_wireless_cloud_connector_with_options_async(request, runtime)

    def list_authorization_rules_with_options(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    async def list_authorization_rules_async(
        self,
        request: cc5g20220314_models.ListAuthorizationRulesRequest,
    ) -> cc5g20220314_models.ListAuthorizationRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authorization_rules_with_options_async(request, runtime)

    def list_cards_with_options(
        self,
        request: cc5g20220314_models.ListCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListCardsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_cards_with_options(request, runtime)

    async def list_cards_async(
        self,
        request: cc5g20220314_models.ListCardsRequest,
    ) -> cc5g20220314_models.ListCardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cards_with_options_async(request, runtime)

    def list_data_packages_with_options(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_data_packages_with_options(request, runtime)

    async def list_data_packages_async(
        self,
        request: cc5g20220314_models.ListDataPackagesRequest,
    ) -> cc5g20220314_models.ListDataPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_packages_with_options_async(request, runtime)

    def list_orders_with_options(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListOrdersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_orders_with_options(request, runtime)

    async def list_orders_async(
        self,
        request: cc5g20220314_models.ListOrdersRequest,
    ) -> cc5g20220314_models.ListOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_orders_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: cc5g20220314_models.ListRegionsRequest,
    ) -> cc5g20220314_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_wireless_cloud_connectors_with_options(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_wireless_cloud_connectors_with_options(request, runtime)

    async def list_wireless_cloud_connectors_async(
        self,
        request: cc5g20220314_models.ListWirelessCloudConnectorsRequest,
    ) -> cc5g20220314_models.ListWirelessCloudConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_wireless_cloud_connectors_with_options_async(request, runtime)

    def list_zones_with_options(
        self,
        request: cc5g20220314_models.ListZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.ListZonesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_zones_with_options(request, runtime)

    async def list_zones_async(
        self,
        request: cc5g20220314_models.ListZonesRequest,
    ) -> cc5g20220314_models.ListZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_zones_with_options_async(request, runtime)

    def open_cc_5g_service_with_options(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.open_cc_5g_service_with_options(request, runtime)

    async def open_cc_5g_service_async(
        self,
        request: cc5g20220314_models.OpenCc5gServiceRequest,
    ) -> cc5g20220314_models.OpenCc5gServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cc_5g_service_with_options_async(request, runtime)

    def update_authorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
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
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_with_options(request, runtime)

    async def update_authorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_authorization_rule_with_options_async(request, runtime)

    def update_card_with_options(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateCardResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_card_with_options(request, runtime)

    async def update_card_async(
        self,
        request: cc5g20220314_models.UpdateCardRequest,
    ) -> cc5g20220314_models.UpdateCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_card_with_options_async(request, runtime)

    def update_dnsauthorization_rule_with_options(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dnsauthorization_rule_with_options(request, runtime)

    async def update_dnsauthorization_rule_async(
        self,
        request: cc5g20220314_models.UpdateDNSAuthorizationRuleRequest,
    ) -> cc5g20220314_models.UpdateDNSAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dnsauthorization_rule_with_options_async(request, runtime)

    def update_wireless_cloud_connector_with_options(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_wireless_cloud_connector_with_options(request, runtime)

    async def update_wireless_cloud_connector_async(
        self,
        request: cc5g20220314_models.UpdateWirelessCloudConnectorRequest,
    ) -> cc5g20220314_models.UpdateWirelessCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_wireless_cloud_connector_with_options_async(request, runtime)
