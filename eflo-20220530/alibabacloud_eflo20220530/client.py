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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def create_subnet_with_options(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def create_vpd_with_options(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def get_lni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def get_subnet_with_options(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def get_vpd_with_options(
        self,
        request: eflo_20220530_models.GetVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def list_vpds_with_options(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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

    def update_subnet_with_options(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
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
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
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
