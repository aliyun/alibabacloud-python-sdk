# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eflo20220530 import models as eflo_20220530_models
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
        self._endpoint = self.get_endpoint('eflo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assign_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_private_ip_address(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_address_with_options(request, runtime)

    async def assign_private_ip_address_async(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_private_ip_address_with_options_async(request, runtime)

    def create_er_with_options(
        self,
        request: eflo_20220530_models.CreateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_with_options_async(
        self,
        request: eflo_20220530_models.CreateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er(
        self,
        request: eflo_20220530_models.CreateErRequest,
    ) -> eflo_20220530_models.CreateErResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_er_with_options(request, runtime)

    async def create_er_async(
        self,
        request: eflo_20220530_models.CreateErRequest,
    ) -> eflo_20220530_models.CreateErResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_er_with_options_async(request, runtime)

    def create_er_attachment_with_options(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_attachment(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_er_attachment_with_options(request, runtime)

    async def create_er_attachment_async(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_er_attachment_with_options_async(request, runtime)

    def create_er_route_map_with_options(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_route_map(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_er_route_map_with_options(request, runtime)

    async def create_er_route_map_async(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_er_route_map_with_options_async(request, runtime)

    def create_subnet_with_options(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subnet_with_options_async(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subnet(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subnet_with_options(request, runtime)

    async def create_subnet_async(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subnet_with_options_async(request, runtime)

    def create_vcc_with_options(
        self,
        request: eflo_20220530_models.CreateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc(
        self,
        request: eflo_20220530_models.CreateVccRequest,
    ) -> eflo_20220530_models.CreateVccResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_with_options(request, runtime)

    async def create_vcc_async(
        self,
        request: eflo_20220530_models.CreateVccRequest,
    ) -> eflo_20220530_models.CreateVccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_with_options_async(request, runtime)

    def create_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_grant_rule(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_grant_rule_with_options(request, runtime)

    async def create_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_grant_rule_with_options_async(request, runtime)

    def create_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_route_entry(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_route_entry_with_options(request, runtime)

    async def create_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_route_entry_with_options_async(request, runtime)

    def create_vpd_with_options(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_with_options_async(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
    ) -> eflo_20220530_models.CreateVpdResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_with_options(request, runtime)

    async def create_vpd_async(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
    ) -> eflo_20220530_models.CreateVpdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpd_with_options_async(request, runtime)

    def create_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd_grant_rule(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_grant_rule_with_options(request, runtime)

    async def create_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpd_grant_rule_with_options_async(request, runtime)

    def delete_er_with_options(
        self,
        request: eflo_20220530_models.DeleteErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er(
        self,
        request: eflo_20220530_models.DeleteErRequest,
    ) -> eflo_20220530_models.DeleteErResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_er_with_options(request, runtime)

    async def delete_er_async(
        self,
        request: eflo_20220530_models.DeleteErRequest,
    ) -> eflo_20220530_models.DeleteErResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_with_options_async(request, runtime)

    def delete_er_attachment_with_options(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_attachment(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_er_attachment_with_options(request, runtime)

    async def delete_er_attachment_async(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_attachment_with_options_async(request, runtime)

    def delete_er_route_map_with_options(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_route_map(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_er_route_map_with_options(request, runtime)

    async def delete_er_route_map_async(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_route_map_with_options_async(request, runtime)

    def delete_subnet_with_options(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subnet_with_options_async(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subnet(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_subnet_with_options(request, runtime)

    async def delete_subnet_async(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_subnet_with_options_async(request, runtime)

    def delete_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_grant_rule(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_grant_rule_with_options(request, runtime)

    async def delete_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vcc_grant_rule_with_options_async(request, runtime)

    def delete_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_route_entry(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_route_entry_with_options(request, runtime)

    async def delete_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vcc_route_entry_with_options_async(request, runtime)

    def delete_vpd_with_options(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_with_options(request, runtime)

    async def delete_vpd_async(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpd_with_options_async(request, runtime)

    def delete_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd_grant_rule(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_grant_rule_with_options(request, runtime)

    async def delete_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpd_grant_rule_with_options_async(request, runtime)

    def describe_slr_with_options(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DescribeSlrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slr_with_options_async(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DescribeSlrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slr(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slr_with_options(request, runtime)

    async def describe_slr_async(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slr_with_options_async(request, runtime)

    def get_er_with_options(
        self,
        request: eflo_20220530_models.GetErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_with_options_async(
        self,
        request: eflo_20220530_models.GetErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er(
        self,
        request: eflo_20220530_models.GetErRequest,
    ) -> eflo_20220530_models.GetErResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_er_with_options(request, runtime)

    async def get_er_async(
        self,
        request: eflo_20220530_models.GetErRequest,
    ) -> eflo_20220530_models.GetErResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_er_with_options_async(request, runtime)

    def get_er_attachment_with_options(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_attachment(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_er_attachment_with_options(request, runtime)

    async def get_er_attachment_async(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_er_attachment_with_options_async(request, runtime)

    def get_er_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_entry(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_entry_with_options(request, runtime)

    async def get_er_route_entry_async(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_er_route_entry_with_options_async(request, runtime)

    def get_er_route_map_with_options(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_map(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_map_with_options(request, runtime)

    async def get_er_route_map_async(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_er_route_map_with_options_async(request, runtime)

    def get_lni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lni_private_ip_address(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lni_private_ip_address_with_options(request, runtime)

    async def get_lni_private_ip_address_async(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lni_private_ip_address_with_options_async(request, runtime)

    def get_network_interface_with_options(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_interface(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_network_interface_with_options(request, runtime)

    async def get_network_interface_async(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_network_interface_with_options_async(request, runtime)

    def get_subnet_with_options(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subnet_with_options_async(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subnet(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
    ) -> eflo_20220530_models.GetSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_subnet_with_options(request, runtime)

    async def get_subnet_async(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
    ) -> eflo_20220530_models.GetSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_subnet_with_options_async(request, runtime)

    def get_vcc_with_options(
        self,
        request: eflo_20220530_models.GetVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_with_options_async(
        self,
        request: eflo_20220530_models.GetVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc(
        self,
        request: eflo_20220530_models.GetVccRequest,
    ) -> eflo_20220530_models.GetVccResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_with_options(request, runtime)

    async def get_vcc_async(
        self,
        request: eflo_20220530_models.GetVccRequest,
    ) -> eflo_20220530_models.GetVccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_with_options_async(request, runtime)

    def get_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_grant_rule(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_grant_rule_with_options(request, runtime)

    async def get_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_grant_rule_with_options_async(request, runtime)

    def get_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_route_entry(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_route_entry_with_options(request, runtime)

    async def get_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_route_entry_with_options_async(request, runtime)

    def get_vpd_with_options(
        self,
        request: eflo_20220530_models.GetVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd(
        self,
        request: eflo_20220530_models.GetVpdRequest,
    ) -> eflo_20220530_models.GetVpdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_with_options(request, runtime)

    async def get_vpd_async(
        self,
        request: eflo_20220530_models.GetVpdRequest,
    ) -> eflo_20220530_models.GetVpdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_with_options_async(request, runtime)

    def get_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_grant_rule(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_grant_rule_with_options(request, runtime)

    async def get_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_grant_rule_with_options_async(request, runtime)

    def get_vpd_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_route_entry(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_route_entry_with_options(request, runtime)

    async def get_vpd_route_entry_async(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_route_entry_with_options_async(request, runtime)

    def initialize_vcc_with_options(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.InitializeVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_vcc_with_options_async(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.InitializeVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_vcc(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
    ) -> eflo_20220530_models.InitializeVccResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_vcc_with_options(request, runtime)

    async def initialize_vcc_async(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
    ) -> eflo_20220530_models.InitializeVccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_vcc_with_options_async(request, runtime)

    def list_er_attachments_with_options(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErAttachments',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_attachments_with_options_async(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErAttachments',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_attachments(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_er_attachments_with_options(request, runtime)

    async def list_er_attachments_async(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_er_attachments_with_options_async(request, runtime)

    def list_er_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_entries(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_entries_with_options(request, runtime)

    async def list_er_route_entries_async(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_er_route_entries_with_options_async(request, runtime)

    def list_er_route_maps_with_options(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteMaps',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_maps_with_options_async(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteMaps',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_maps(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_maps_with_options(request, runtime)

    async def list_er_route_maps_async(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_er_route_maps_with_options_async(request, runtime)

    def list_ers_with_options(
        self,
        request: eflo_20220530_models.ListErsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ers_with_options_async(
        self,
        request: eflo_20220530_models.ListErsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ers(
        self,
        request: eflo_20220530_models.ListErsRequest,
    ) -> eflo_20220530_models.ListErsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ers_with_options(request, runtime)

    async def list_ers_async(
        self,
        request: eflo_20220530_models.ListErsRequest,
    ) -> eflo_20220530_models.ListErsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ers_with_options_async(request, runtime)

    def list_lni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lni_private_ip_address(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_lni_private_ip_address_with_options(request, runtime)

    async def list_lni_private_ip_address_async(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_lni_private_ip_address_with_options_async(request, runtime)

    def list_network_interfaces_with_options(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_interfaces_with_options_async(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_interfaces(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_network_interfaces_with_options(request, runtime)

    async def list_network_interfaces_async(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_network_interfaces_with_options_async(request, runtime)

    def list_subnets_with_options(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubnets',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListSubnetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subnets_with_options_async(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubnets',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListSubnetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subnets(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_subnets_with_options(request, runtime)

    async def list_subnets_async(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_subnets_with_options_async(request, runtime)

    def list_vcc_grant_rules_with_options(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_grant_rules_with_options_async(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_grant_rules(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_grant_rules_with_options(request, runtime)

    async def list_vcc_grant_rules_async(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vcc_grant_rules_with_options_async(request, runtime)

    def list_vcc_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_route_entries(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_route_entries_with_options(request, runtime)

    async def list_vcc_route_entries_async(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vcc_route_entries_with_options_async(request, runtime)

    def list_vccs_with_options(
        self,
        request: eflo_20220530_models.ListVccsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vccs_with_options_async(
        self,
        request: eflo_20220530_models.ListVccsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vccs(
        self,
        request: eflo_20220530_models.ListVccsRequest,
    ) -> eflo_20220530_models.ListVccsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vccs_with_options(request, runtime)

    async def list_vccs_async(
        self,
        request: eflo_20220530_models.ListVccsRequest,
    ) -> eflo_20220530_models.ListVccsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vccs_with_options_async(request, runtime)

    def list_vpd_grant_rules_with_options(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_grant_rules_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_grant_rules(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_grant_rules_with_options(request, runtime)

    async def list_vpd_grant_rules_async(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpd_grant_rules_with_options_async(request, runtime)

    def list_vpd_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_route_entries(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_route_entries_with_options(request, runtime)

    async def list_vpd_route_entries_async(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpd_route_entries_with_options_async(request, runtime)

    def list_vpds_with_options(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not UtilClient.is_unset(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not UtilClient.is_unset(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpds',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpds_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not UtilClient.is_unset(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not UtilClient.is_unset(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpds',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpds(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
    ) -> eflo_20220530_models.ListVpdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpds_with_options(request, runtime)

    async def list_vpds_async(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
    ) -> eflo_20220530_models.ListVpdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpds_with_options_async(request, runtime)

    def un_assign_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_assign_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_assign_private_ip_address(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_assign_private_ip_address_with_options(request, runtime)

    async def un_assign_private_ip_address_async(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_assign_private_ip_address_with_options_async(request, runtime)

    def update_er_with_options(
        self,
        request: eflo_20220530_models.UpdateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er(
        self,
        request: eflo_20220530_models.UpdateErRequest,
    ) -> eflo_20220530_models.UpdateErResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_er_with_options(request, runtime)

    async def update_er_async(
        self,
        request: eflo_20220530_models.UpdateErRequest,
    ) -> eflo_20220530_models.UpdateErResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_er_with_options_async(request, runtime)

    def update_er_attachment_with_options(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_attachment(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_er_attachment_with_options(request, runtime)

    async def update_er_attachment_async(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_er_attachment_with_options_async(request, runtime)

    def update_er_route_map_with_options(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_route_map(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_er_route_map_with_options(request, runtime)

    async def update_er_route_map_async(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_er_route_map_with_options_async(request, runtime)

    def update_subnet_with_options(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subnet_with_options_async(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subnet(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_subnet_with_options(request, runtime)

    async def update_subnet_async(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_subnet_with_options_async(request, runtime)

    def update_vcc_with_options(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vcc_with_options_async(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVccResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vcc(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
    ) -> eflo_20220530_models.UpdateVccResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vcc_with_options(request, runtime)

    async def update_vcc_async(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
    ) -> eflo_20220530_models.UpdateVccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vcc_with_options_async(request, runtime)

    def update_vpd_with_options(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpd_with_options_async(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpd(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpd_with_options(request, runtime)

    async def update_vpd_async(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpd_with_options_async(request, runtime)
