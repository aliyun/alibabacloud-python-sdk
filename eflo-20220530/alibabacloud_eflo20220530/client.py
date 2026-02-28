# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eflo20220530 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def assign_leni_private_ip_address_with_options(
        self,
        request: main_models.AssignLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_leni_private_ip_address_with_options_async(
        self,
        request: main_models.AssignLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_leni_private_ip_address(
        self,
        request: main_models.AssignLeniPrivateIpAddressRequest,
    ) -> main_models.AssignLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.assign_leni_private_ip_address_with_options(request, runtime)

    async def assign_leni_private_ip_address_async(
        self,
        request: main_models.AssignLeniPrivateIpAddressRequest,
    ) -> main_models.AssignLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.assign_leni_private_ip_address_with_options_async(request, runtime)

    def assign_private_ip_address_with_options(
        self,
        request: main_models.AssignPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_private_ip_address_with_options_async(
        self,
        request: main_models.AssignPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_private_ip_address(
        self,
        request: main_models.AssignPrivateIpAddressRequest,
    ) -> main_models.AssignPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.assign_private_ip_address_with_options(request, runtime)

    async def assign_private_ip_address_async(
        self,
        request: main_models.AssignPrivateIpAddressRequest,
    ) -> main_models.AssignPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.assign_private_ip_address_with_options_async(request, runtime)

    def associate_vpd_cidr_block_with_options(
        self,
        request: main_models.AssociateVpdCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateVpdCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateVpdCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateVpdCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_vpd_cidr_block_with_options_async(
        self,
        request: main_models.AssociateVpdCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateVpdCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateVpdCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateVpdCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_vpd_cidr_block(
        self,
        request: main_models.AssociateVpdCidrBlockRequest,
    ) -> main_models.AssociateVpdCidrBlockResponse:
        runtime = RuntimeOptions()
        return self.associate_vpd_cidr_block_with_options(request, runtime)

    async def associate_vpd_cidr_block_async(
        self,
        request: main_models.AssociateVpdCidrBlockRequest,
    ) -> main_models.AssociateVpdCidrBlockResponse:
        runtime = RuntimeOptions()
        return await self.associate_vpd_cidr_block_with_options_async(request, runtime)

    def attach_elastic_network_interface_with_options(
        self,
        request: main_models.AttachElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_elastic_network_interface_with_options_async(
        self,
        request: main_models.AttachElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_elastic_network_interface(
        self,
        request: main_models.AttachElasticNetworkInterfaceRequest,
    ) -> main_models.AttachElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.attach_elastic_network_interface_with_options(request, runtime)

    async def attach_elastic_network_interface_async(
        self,
        request: main_models.AttachElasticNetworkInterfaceRequest,
    ) -> main_models.AttachElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.attach_elastic_network_interface_with_options_async(request, runtime)

    def create_elastic_network_interface_with_options(
        self,
        request: main_models.CreateElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_network_interface_with_options_async(
        self,
        request: main_models.CreateElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_network_interface(
        self,
        request: main_models.CreateElasticNetworkInterfaceRequest,
    ) -> main_models.CreateElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.create_elastic_network_interface_with_options(request, runtime)

    async def create_elastic_network_interface_async(
        self,
        request: main_models.CreateElasticNetworkInterfaceRequest,
    ) -> main_models.CreateElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.create_elastic_network_interface_with_options_async(request, runtime)

    def create_er_with_options(
        self,
        request: main_models.CreateErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_with_options_async(
        self,
        request: main_models.CreateErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er(
        self,
        request: main_models.CreateErRequest,
    ) -> main_models.CreateErResponse:
        runtime = RuntimeOptions()
        return self.create_er_with_options(request, runtime)

    async def create_er_async(
        self,
        request: main_models.CreateErRequest,
    ) -> main_models.CreateErResponse:
        runtime = RuntimeOptions()
        return await self.create_er_with_options_async(request, runtime)

    def create_er_attachment_with_options(
        self,
        request: main_models.CreateErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_attachment_with_options_async(
        self,
        request: main_models.CreateErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_attachment(
        self,
        request: main_models.CreateErAttachmentRequest,
    ) -> main_models.CreateErAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_er_attachment_with_options(request, runtime)

    async def create_er_attachment_async(
        self,
        request: main_models.CreateErAttachmentRequest,
    ) -> main_models.CreateErAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_er_attachment_with_options_async(request, runtime)

    def create_er_route_map_with_options(
        self,
        request: main_models.CreateErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not DaraCore.is_null(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not DaraCore.is_null(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not DaraCore.is_null(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not DaraCore.is_null(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not DaraCore.is_null(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not DaraCore.is_null(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_route_map_with_options_async(
        self,
        request: main_models.CreateErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not DaraCore.is_null(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not DaraCore.is_null(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not DaraCore.is_null(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not DaraCore.is_null(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not DaraCore.is_null(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not DaraCore.is_null(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_route_map(
        self,
        request: main_models.CreateErRouteMapRequest,
    ) -> main_models.CreateErRouteMapResponse:
        runtime = RuntimeOptions()
        return self.create_er_route_map_with_options(request, runtime)

    async def create_er_route_map_async(
        self,
        request: main_models.CreateErRouteMapRequest,
    ) -> main_models.CreateErRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.create_er_route_map_with_options_async(request, runtime)

    def create_subnet_with_options(
        self,
        request: main_models.CreateSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr):
            body['Cidr'] = request.cidr
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subnet_with_options_async(
        self,
        request: main_models.CreateSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr):
            body['Cidr'] = request.cidr
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subnet(
        self,
        request: main_models.CreateSubnetRequest,
    ) -> main_models.CreateSubnetResponse:
        runtime = RuntimeOptions()
        return self.create_subnet_with_options(request, runtime)

    async def create_subnet_async(
        self,
        request: main_models.CreateSubnetRequest,
    ) -> main_models.CreateSubnetResponse:
        runtime = RuntimeOptions()
        return await self.create_subnet_with_options_async(request, runtime)

    def create_vcc_with_options(
        self,
        request: main_models.CreateVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bgp_asn):
            body['BgpAsn'] = request.bgp_asn
        if not DaraCore.is_null(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            body['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_with_options_async(
        self,
        request: main_models.CreateVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bgp_asn):
            body['BgpAsn'] = request.bgp_asn
        if not DaraCore.is_null(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            body['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc(
        self,
        request: main_models.CreateVccRequest,
    ) -> main_models.CreateVccResponse:
        runtime = RuntimeOptions()
        return self.create_vcc_with_options(request, runtime)

    async def create_vcc_async(
        self,
        request: main_models.CreateVccRequest,
    ) -> main_models.CreateVccResponse:
        runtime = RuntimeOptions()
        return await self.create_vcc_with_options_async(request, runtime)

    def create_vcc_grant_rule_with_options(
        self,
        request: main_models.CreateVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_grant_rule_with_options_async(
        self,
        request: main_models.CreateVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_grant_rule(
        self,
        request: main_models.CreateVccGrantRuleRequest,
    ) -> main_models.CreateVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.create_vcc_grant_rule_with_options(request, runtime)

    async def create_vcc_grant_rule_async(
        self,
        request: main_models.CreateVccGrantRuleRequest,
    ) -> main_models.CreateVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_vcc_grant_rule_with_options_async(request, runtime)

    def create_vcc_route_entry_with_options(
        self,
        request: main_models.CreateVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_route_entry_with_options_async(
        self,
        request: main_models.CreateVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_route_entry(
        self,
        request: main_models.CreateVccRouteEntryRequest,
    ) -> main_models.CreateVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.create_vcc_route_entry_with_options(request, runtime)

    async def create_vcc_route_entry_async(
        self,
        request: main_models.CreateVccRouteEntryRequest,
    ) -> main_models.CreateVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.create_vcc_route_entry_with_options_async(request, runtime)

    def create_vpd_with_options(
        self,
        request: main_models.CreateVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr):
            body['Cidr'] = request.cidr
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subnets):
            body['Subnets'] = request.subnets
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_with_options_async(
        self,
        request: main_models.CreateVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr):
            body['Cidr'] = request.cidr
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subnets):
            body['Subnets'] = request.subnets
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd(
        self,
        request: main_models.CreateVpdRequest,
    ) -> main_models.CreateVpdResponse:
        runtime = RuntimeOptions()
        return self.create_vpd_with_options(request, runtime)

    async def create_vpd_async(
        self,
        request: main_models.CreateVpdRequest,
    ) -> main_models.CreateVpdResponse:
        runtime = RuntimeOptions()
        return await self.create_vpd_with_options_async(request, runtime)

    def create_vpd_grant_rule_with_options(
        self,
        request: main_models.CreateVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_grant_rule_with_options_async(
        self,
        request: main_models.CreateVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd_grant_rule(
        self,
        request: main_models.CreateVpdGrantRuleRequest,
    ) -> main_models.CreateVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.create_vpd_grant_rule_with_options(request, runtime)

    async def create_vpd_grant_rule_async(
        self,
        request: main_models.CreateVpdGrantRuleRequest,
    ) -> main_models.CreateVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_vpd_grant_rule_with_options_async(request, runtime)

    def delete_elastic_network_interface_with_options(
        self,
        request: main_models.DeleteElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_network_interface_with_options_async(
        self,
        request: main_models.DeleteElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_network_interface(
        self,
        request: main_models.DeleteElasticNetworkInterfaceRequest,
    ) -> main_models.DeleteElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.delete_elastic_network_interface_with_options(request, runtime)

    async def delete_elastic_network_interface_async(
        self,
        request: main_models.DeleteElasticNetworkInterfaceRequest,
    ) -> main_models.DeleteElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_elastic_network_interface_with_options_async(request, runtime)

    def delete_er_with_options(
        self,
        request: main_models.DeleteErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_with_options_async(
        self,
        request: main_models.DeleteErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er(
        self,
        request: main_models.DeleteErRequest,
    ) -> main_models.DeleteErResponse:
        runtime = RuntimeOptions()
        return self.delete_er_with_options(request, runtime)

    async def delete_er_async(
        self,
        request: main_models.DeleteErRequest,
    ) -> main_models.DeleteErResponse:
        runtime = RuntimeOptions()
        return await self.delete_er_with_options_async(request, runtime)

    def delete_er_attachment_with_options(
        self,
        request: main_models.DeleteErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_attachment_with_options_async(
        self,
        request: main_models.DeleteErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_attachment(
        self,
        request: main_models.DeleteErAttachmentRequest,
    ) -> main_models.DeleteErAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_er_attachment_with_options(request, runtime)

    async def delete_er_attachment_async(
        self,
        request: main_models.DeleteErAttachmentRequest,
    ) -> main_models.DeleteErAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_er_attachment_with_options_async(request, runtime)

    def delete_er_route_map_with_options(
        self,
        request: main_models.DeleteErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_route_map_with_options_async(
        self,
        request: main_models.DeleteErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_route_map(
        self,
        request: main_models.DeleteErRouteMapRequest,
    ) -> main_models.DeleteErRouteMapResponse:
        runtime = RuntimeOptions()
        return self.delete_er_route_map_with_options(request, runtime)

    async def delete_er_route_map_async(
        self,
        request: main_models.DeleteErRouteMapRequest,
    ) -> main_models.DeleteErRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.delete_er_route_map_with_options_async(request, runtime)

    def delete_subnet_with_options(
        self,
        request: main_models.DeleteSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subnet_with_options_async(
        self,
        request: main_models.DeleteSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subnet(
        self,
        request: main_models.DeleteSubnetRequest,
    ) -> main_models.DeleteSubnetResponse:
        runtime = RuntimeOptions()
        return self.delete_subnet_with_options(request, runtime)

    async def delete_subnet_async(
        self,
        request: main_models.DeleteSubnetRequest,
    ) -> main_models.DeleteSubnetResponse:
        runtime = RuntimeOptions()
        return await self.delete_subnet_with_options_async(request, runtime)

    def delete_vcc_grant_rule_with_options(
        self,
        request: main_models.DeleteVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_grant_rule_with_options_async(
        self,
        request: main_models.DeleteVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_grant_rule(
        self,
        request: main_models.DeleteVccGrantRuleRequest,
    ) -> main_models.DeleteVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_vcc_grant_rule_with_options(request, runtime)

    async def delete_vcc_grant_rule_async(
        self,
        request: main_models.DeleteVccGrantRuleRequest,
    ) -> main_models.DeleteVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_vcc_grant_rule_with_options_async(request, runtime)

    def delete_vcc_route_entry_with_options(
        self,
        request: main_models.DeleteVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_route_entry_with_options_async(
        self,
        request: main_models.DeleteVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_route_entry(
        self,
        request: main_models.DeleteVccRouteEntryRequest,
    ) -> main_models.DeleteVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.delete_vcc_route_entry_with_options(request, runtime)

    async def delete_vcc_route_entry_async(
        self,
        request: main_models.DeleteVccRouteEntryRequest,
    ) -> main_models.DeleteVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.delete_vcc_route_entry_with_options_async(request, runtime)

    def delete_vpd_with_options(
        self,
        request: main_models.DeleteVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_with_options_async(
        self,
        request: main_models.DeleteVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd(
        self,
        request: main_models.DeleteVpdRequest,
    ) -> main_models.DeleteVpdResponse:
        runtime = RuntimeOptions()
        return self.delete_vpd_with_options(request, runtime)

    async def delete_vpd_async(
        self,
        request: main_models.DeleteVpdRequest,
    ) -> main_models.DeleteVpdResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpd_with_options_async(request, runtime)

    def delete_vpd_grant_rule_with_options(
        self,
        request: main_models.DeleteVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_grant_rule_with_options_async(
        self,
        request: main_models.DeleteVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd_grant_rule(
        self,
        request: main_models.DeleteVpdGrantRuleRequest,
    ) -> main_models.DeleteVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_vpd_grant_rule_with_options(request, runtime)

    async def delete_vpd_grant_rule_async(
        self,
        request: main_models.DeleteVpdGrantRuleRequest,
    ) -> main_models.DeleteVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpd_grant_rule_with_options_async(request, runtime)

    def describe_slr_with_options(
        self,
        request: main_models.DescribeSlrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlrResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slr_with_options_async(
        self,
        request: main_models.DescribeSlrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlrResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slr(
        self,
        request: main_models.DescribeSlrRequest,
    ) -> main_models.DescribeSlrResponse:
        runtime = RuntimeOptions()
        return self.describe_slr_with_options(request, runtime)

    async def describe_slr_async(
        self,
        request: main_models.DescribeSlrRequest,
    ) -> main_models.DescribeSlrResponse:
        runtime = RuntimeOptions()
        return await self.describe_slr_with_options_async(request, runtime)

    def detach_elastic_network_interface_with_options(
        self,
        request: main_models.DetachElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_elastic_network_interface_with_options_async(
        self,
        request: main_models.DetachElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_elastic_network_interface(
        self,
        request: main_models.DetachElasticNetworkInterfaceRequest,
    ) -> main_models.DetachElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.detach_elastic_network_interface_with_options(request, runtime)

    async def detach_elastic_network_interface_async(
        self,
        request: main_models.DetachElasticNetworkInterfaceRequest,
    ) -> main_models.DetachElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.detach_elastic_network_interface_with_options_async(request, runtime)

    def get_destination_cidr_block_with_options(
        self,
        request: main_models.GetDestinationCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDestinationCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDestinationCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDestinationCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_destination_cidr_block_with_options_async(
        self,
        request: main_models.GetDestinationCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDestinationCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDestinationCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDestinationCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_destination_cidr_block(
        self,
        request: main_models.GetDestinationCidrBlockRequest,
    ) -> main_models.GetDestinationCidrBlockResponse:
        runtime = RuntimeOptions()
        return self.get_destination_cidr_block_with_options(request, runtime)

    async def get_destination_cidr_block_async(
        self,
        request: main_models.GetDestinationCidrBlockRequest,
    ) -> main_models.GetDestinationCidrBlockResponse:
        runtime = RuntimeOptions()
        return await self.get_destination_cidr_block_with_options_async(request, runtime)

    def get_elastic_network_interface_with_options(
        self,
        request: main_models.GetElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elastic_network_interface_with_options_async(
        self,
        request: main_models.GetElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elastic_network_interface(
        self,
        request: main_models.GetElasticNetworkInterfaceRequest,
    ) -> main_models.GetElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.get_elastic_network_interface_with_options(request, runtime)

    async def get_elastic_network_interface_async(
        self,
        request: main_models.GetElasticNetworkInterfaceRequest,
    ) -> main_models.GetElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.get_elastic_network_interface_with_options_async(request, runtime)

    def get_er_with_options(
        self,
        request: main_models.GetErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_with_options_async(
        self,
        request: main_models.GetErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er(
        self,
        request: main_models.GetErRequest,
    ) -> main_models.GetErResponse:
        runtime = RuntimeOptions()
        return self.get_er_with_options(request, runtime)

    async def get_er_async(
        self,
        request: main_models.GetErRequest,
    ) -> main_models.GetErResponse:
        runtime = RuntimeOptions()
        return await self.get_er_with_options_async(request, runtime)

    def get_er_attachment_with_options(
        self,
        request: main_models.GetErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_attachment_with_options_async(
        self,
        request: main_models.GetErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_attachment(
        self,
        request: main_models.GetErAttachmentRequest,
    ) -> main_models.GetErAttachmentResponse:
        runtime = RuntimeOptions()
        return self.get_er_attachment_with_options(request, runtime)

    async def get_er_attachment_async(
        self,
        request: main_models.GetErAttachmentRequest,
    ) -> main_models.GetErAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.get_er_attachment_with_options_async(request, runtime)

    def get_er_route_entry_with_options(
        self,
        request: main_models.GetErRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_entry_with_options_async(
        self,
        request: main_models.GetErRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_entry(
        self,
        request: main_models.GetErRouteEntryRequest,
    ) -> main_models.GetErRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.get_er_route_entry_with_options(request, runtime)

    async def get_er_route_entry_async(
        self,
        request: main_models.GetErRouteEntryRequest,
    ) -> main_models.GetErRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.get_er_route_entry_with_options_async(request, runtime)

    def get_er_route_map_with_options(
        self,
        request: main_models.GetErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_map_with_options_async(
        self,
        request: main_models.GetErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_map(
        self,
        request: main_models.GetErRouteMapRequest,
    ) -> main_models.GetErRouteMapResponse:
        runtime = RuntimeOptions()
        return self.get_er_route_map_with_options(request, runtime)

    async def get_er_route_map_async(
        self,
        request: main_models.GetErRouteMapRequest,
    ) -> main_models.GetErRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.get_er_route_map_with_options_async(request, runtime)

    def get_fabric_topology_with_options(
        self,
        request: main_models.GetFabricTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFabricTopologyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.lni_ids):
            body['LniIds'] = request.lni_ids
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFabricTopology',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFabricTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fabric_topology_with_options_async(
        self,
        request: main_models.GetFabricTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFabricTopologyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.lni_ids):
            body['LniIds'] = request.lni_ids
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFabricTopology',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFabricTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fabric_topology(
        self,
        request: main_models.GetFabricTopologyRequest,
    ) -> main_models.GetFabricTopologyResponse:
        runtime = RuntimeOptions()
        return self.get_fabric_topology_with_options(request, runtime)

    async def get_fabric_topology_async(
        self,
        request: main_models.GetFabricTopologyRequest,
    ) -> main_models.GetFabricTopologyResponse:
        runtime = RuntimeOptions()
        return await self.get_fabric_topology_with_options_async(request, runtime)

    def get_leni_private_ip_address_with_options(
        self,
        request: main_models.GetLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_leni_private_ip_address_with_options_async(
        self,
        request: main_models.GetLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_leni_private_ip_address(
        self,
        request: main_models.GetLeniPrivateIpAddressRequest,
    ) -> main_models.GetLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.get_leni_private_ip_address_with_options(request, runtime)

    async def get_leni_private_ip_address_async(
        self,
        request: main_models.GetLeniPrivateIpAddressRequest,
    ) -> main_models.GetLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.get_leni_private_ip_address_with_options_async(request, runtime)

    def get_lni_private_ip_address_with_options(
        self,
        request: main_models.GetLniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lni_private_ip_address_with_options_async(
        self,
        request: main_models.GetLniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lni_private_ip_address(
        self,
        request: main_models.GetLniPrivateIpAddressRequest,
    ) -> main_models.GetLniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.get_lni_private_ip_address_with_options(request, runtime)

    async def get_lni_private_ip_address_async(
        self,
        request: main_models.GetLniPrivateIpAddressRequest,
    ) -> main_models.GetLniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.get_lni_private_ip_address_with_options_async(request, runtime)

    def get_network_interface_with_options(
        self,
        request: main_models.GetNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_interface_with_options_async(
        self,
        request: main_models.GetNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_interface(
        self,
        request: main_models.GetNetworkInterfaceRequest,
    ) -> main_models.GetNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.get_network_interface_with_options(request, runtime)

    async def get_network_interface_async(
        self,
        request: main_models.GetNetworkInterfaceRequest,
    ) -> main_models.GetNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.get_network_interface_with_options_async(request, runtime)

    def get_node_info_for_pod_with_options(
        self,
        request: main_models.GetNodeInfoForPodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeInfoForPodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeInfoForPod',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeInfoForPodResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_info_for_pod_with_options_async(
        self,
        request: main_models.GetNodeInfoForPodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeInfoForPodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeInfoForPod',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeInfoForPodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_info_for_pod(
        self,
        request: main_models.GetNodeInfoForPodRequest,
    ) -> main_models.GetNodeInfoForPodResponse:
        runtime = RuntimeOptions()
        return self.get_node_info_for_pod_with_options(request, runtime)

    async def get_node_info_for_pod_async(
        self,
        request: main_models.GetNodeInfoForPodRequest,
    ) -> main_models.GetNodeInfoForPodResponse:
        runtime = RuntimeOptions()
        return await self.get_node_info_for_pod_with_options_async(request, runtime)

    def get_subnet_with_options(
        self,
        request: main_models.GetSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subnet_with_options_async(
        self,
        request: main_models.GetSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subnet(
        self,
        request: main_models.GetSubnetRequest,
    ) -> main_models.GetSubnetResponse:
        runtime = RuntimeOptions()
        return self.get_subnet_with_options(request, runtime)

    async def get_subnet_async(
        self,
        request: main_models.GetSubnetRequest,
    ) -> main_models.GetSubnetResponse:
        runtime = RuntimeOptions()
        return await self.get_subnet_with_options_async(request, runtime)

    def get_vcc_with_options(
        self,
        request: main_models.GetVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_with_options_async(
        self,
        request: main_models.GetVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc(
        self,
        request: main_models.GetVccRequest,
    ) -> main_models.GetVccResponse:
        runtime = RuntimeOptions()
        return self.get_vcc_with_options(request, runtime)

    async def get_vcc_async(
        self,
        request: main_models.GetVccRequest,
    ) -> main_models.GetVccResponse:
        runtime = RuntimeOptions()
        return await self.get_vcc_with_options_async(request, runtime)

    def get_vcc_grant_rule_with_options(
        self,
        request: main_models.GetVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_grant_rule_with_options_async(
        self,
        request: main_models.GetVccGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVccGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_grant_rule(
        self,
        request: main_models.GetVccGrantRuleRequest,
    ) -> main_models.GetVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.get_vcc_grant_rule_with_options(request, runtime)

    async def get_vcc_grant_rule_async(
        self,
        request: main_models.GetVccGrantRuleRequest,
    ) -> main_models.GetVccGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_vcc_grant_rule_with_options_async(request, runtime)

    def get_vcc_route_entry_with_options(
        self,
        request: main_models.GetVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_route_entry_with_options_async(
        self,
        request: main_models.GetVccRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVccRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVccRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_route_entry(
        self,
        request: main_models.GetVccRouteEntryRequest,
    ) -> main_models.GetVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.get_vcc_route_entry_with_options(request, runtime)

    async def get_vcc_route_entry_async(
        self,
        request: main_models.GetVccRouteEntryRequest,
    ) -> main_models.GetVccRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.get_vcc_route_entry_with_options_async(request, runtime)

    def get_vpd_with_options(
        self,
        request: main_models.GetVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_with_options_async(
        self,
        request: main_models.GetVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd(
        self,
        request: main_models.GetVpdRequest,
    ) -> main_models.GetVpdResponse:
        runtime = RuntimeOptions()
        return self.get_vpd_with_options(request, runtime)

    async def get_vpd_async(
        self,
        request: main_models.GetVpdRequest,
    ) -> main_models.GetVpdResponse:
        runtime = RuntimeOptions()
        return await self.get_vpd_with_options_async(request, runtime)

    def get_vpd_grant_rule_with_options(
        self,
        request: main_models.GetVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_grant_rule_with_options_async(
        self,
        request: main_models.GetVpdGrantRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdGrantRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpdGrantRule',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_grant_rule(
        self,
        request: main_models.GetVpdGrantRuleRequest,
    ) -> main_models.GetVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return self.get_vpd_grant_rule_with_options(request, runtime)

    async def get_vpd_grant_rule_async(
        self,
        request: main_models.GetVpdGrantRuleRequest,
    ) -> main_models.GetVpdGrantRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_vpd_grant_rule_with_options_async(request, runtime)

    def get_vpd_route_entry_with_options(
        self,
        request: main_models.GetVpdRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpdRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_route_entry_with_options_async(
        self,
        request: main_models.GetVpdRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpdRouteEntryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpdRouteEntry',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpdRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_route_entry(
        self,
        request: main_models.GetVpdRouteEntryRequest,
    ) -> main_models.GetVpdRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.get_vpd_route_entry_with_options(request, runtime)

    async def get_vpd_route_entry_async(
        self,
        request: main_models.GetVpdRouteEntryRequest,
    ) -> main_models.GetVpdRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.get_vpd_route_entry_with_options_async(request, runtime)

    def initialize_vcc_with_options(
        self,
        request: main_models.InitializeVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitializeVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_vcc_with_options_async(
        self,
        request: main_models.InitializeVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitializeVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_vcc(
        self,
        request: main_models.InitializeVccRequest,
    ) -> main_models.InitializeVccResponse:
        runtime = RuntimeOptions()
        return self.initialize_vcc_with_options(request, runtime)

    async def initialize_vcc_async(
        self,
        request: main_models.InitializeVccRequest,
    ) -> main_models.InitializeVccResponse:
        runtime = RuntimeOptions()
        return await self.initialize_vcc_with_options_async(request, runtime)

    def list_elastic_network_interfaces_with_options(
        self,
        request: main_models.ListElasticNetworkInterfacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListElasticNetworkInterfacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.network_type):
            body['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListElasticNetworkInterfaces',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListElasticNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_elastic_network_interfaces_with_options_async(
        self,
        request: main_models.ListElasticNetworkInterfacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListElasticNetworkInterfacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.network_type):
            body['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListElasticNetworkInterfaces',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListElasticNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_elastic_network_interfaces(
        self,
        request: main_models.ListElasticNetworkInterfacesRequest,
    ) -> main_models.ListElasticNetworkInterfacesResponse:
        runtime = RuntimeOptions()
        return self.list_elastic_network_interfaces_with_options(request, runtime)

    async def list_elastic_network_interfaces_async(
        self,
        request: main_models.ListElasticNetworkInterfacesRequest,
    ) -> main_models.ListElasticNetworkInterfacesResponse:
        runtime = RuntimeOptions()
        return await self.list_elastic_network_interfaces_with_options_async(request, runtime)

    def list_er_attachments_with_options(
        self,
        request: main_models.ListErAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErAttachmentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErAttachments',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_attachments_with_options_async(
        self,
        request: main_models.ListErAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErAttachmentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErAttachments',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_attachments(
        self,
        request: main_models.ListErAttachmentsRequest,
    ) -> main_models.ListErAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_er_attachments_with_options(request, runtime)

    async def list_er_attachments_async(
        self,
        request: main_models.ListErAttachmentsRequest,
    ) -> main_models.ListErAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_er_attachments_with_options_async(request, runtime)

    def list_er_route_entries_with_options(
        self,
        request: main_models.ListErRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_entries_with_options_async(
        self,
        request: main_models.ListErRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_entries(
        self,
        request: main_models.ListErRouteEntriesRequest,
    ) -> main_models.ListErRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_er_route_entries_with_options(request, runtime)

    async def list_er_route_entries_async(
        self,
        request: main_models.ListErRouteEntriesRequest,
    ) -> main_models.ListErRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_er_route_entries_with_options_async(request, runtime)

    def list_er_route_maps_with_options(
        self,
        request: main_models.ListErRouteMapsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErRouteMapsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not DaraCore.is_null(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not DaraCore.is_null(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not DaraCore.is_null(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not DaraCore.is_null(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not DaraCore.is_null(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErRouteMaps',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_maps_with_options_async(
        self,
        request: main_models.ListErRouteMapsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErRouteMapsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not DaraCore.is_null(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not DaraCore.is_null(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not DaraCore.is_null(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not DaraCore.is_null(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not DaraCore.is_null(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErRouteMaps',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErRouteMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_maps(
        self,
        request: main_models.ListErRouteMapsRequest,
    ) -> main_models.ListErRouteMapsResponse:
        runtime = RuntimeOptions()
        return self.list_er_route_maps_with_options(request, runtime)

    async def list_er_route_maps_async(
        self,
        request: main_models.ListErRouteMapsRequest,
    ) -> main_models.ListErRouteMapsResponse:
        runtime = RuntimeOptions()
        return await self.list_er_route_maps_with_options_async(request, runtime)

    def list_ers_with_options(
        self,
        request: main_models.ListErsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErs',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ers_with_options_async(
        self,
        request: main_models.ListErsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListErsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListErs',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListErsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ers(
        self,
        request: main_models.ListErsRequest,
    ) -> main_models.ListErsResponse:
        runtime = RuntimeOptions()
        return self.list_ers_with_options(request, runtime)

    async def list_ers_async(
        self,
        request: main_models.ListErsRequest,
    ) -> main_models.ListErsResponse:
        runtime = RuntimeOptions()
        return await self.list_ers_with_options_async(request, runtime)

    def list_instances_by_ncd_with_options(
        self,
        request: main_models.ListInstancesByNcdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesByNcdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_ncd):
            body['MaxNcd'] = request.max_ncd
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesByNcd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesByNcdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_by_ncd_with_options_async(
        self,
        request: main_models.ListInstancesByNcdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesByNcdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_ncd):
            body['MaxNcd'] = request.max_ncd
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesByNcd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesByNcdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_by_ncd(
        self,
        request: main_models.ListInstancesByNcdRequest,
    ) -> main_models.ListInstancesByNcdResponse:
        runtime = RuntimeOptions()
        return self.list_instances_by_ncd_with_options(request, runtime)

    async def list_instances_by_ncd_async(
        self,
        request: main_models.ListInstancesByNcdRequest,
    ) -> main_models.ListInstancesByNcdResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_by_ncd_with_options_async(request, runtime)

    def list_leni_private_ip_addresses_with_options(
        self,
        request: main_models.ListLeniPrivateIpAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLeniPrivateIpAddressesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLeniPrivateIpAddresses',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLeniPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_leni_private_ip_addresses_with_options_async(
        self,
        request: main_models.ListLeniPrivateIpAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLeniPrivateIpAddressesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLeniPrivateIpAddresses',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLeniPrivateIpAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_leni_private_ip_addresses(
        self,
        request: main_models.ListLeniPrivateIpAddressesRequest,
    ) -> main_models.ListLeniPrivateIpAddressesResponse:
        runtime = RuntimeOptions()
        return self.list_leni_private_ip_addresses_with_options(request, runtime)

    async def list_leni_private_ip_addresses_async(
        self,
        request: main_models.ListLeniPrivateIpAddressesRequest,
    ) -> main_models.ListLeniPrivateIpAddressesResponse:
        runtime = RuntimeOptions()
        return await self.list_leni_private_ip_addresses_with_options_async(request, runtime)

    def list_lni_private_ip_address_with_options(
        self,
        request: main_models.ListLniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lni_private_ip_address_with_options_async(
        self,
        request: main_models.ListLniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lni_private_ip_address(
        self,
        request: main_models.ListLniPrivateIpAddressRequest,
    ) -> main_models.ListLniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.list_lni_private_ip_address_with_options(request, runtime)

    async def list_lni_private_ip_address_async(
        self,
        request: main_models.ListLniPrivateIpAddressRequest,
    ) -> main_models.ListLniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.list_lni_private_ip_address_with_options_async(request, runtime)

    def list_network_interfaces_with_options(
        self,
        request: main_models.ListNetworkInterfacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkInterfacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkInterfaces',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_interfaces_with_options_async(
        self,
        request: main_models.ListNetworkInterfacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkInterfacesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ip):
            body['Ip'] = request.ip
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkInterfaces',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_interfaces(
        self,
        request: main_models.ListNetworkInterfacesRequest,
    ) -> main_models.ListNetworkInterfacesResponse:
        runtime = RuntimeOptions()
        return self.list_network_interfaces_with_options(request, runtime)

    async def list_network_interfaces_async(
        self,
        request: main_models.ListNetworkInterfacesRequest,
    ) -> main_models.ListNetworkInterfacesResponse:
        runtime = RuntimeOptions()
        return await self.list_network_interfaces_with_options_async(request, runtime)

    def list_node_infos_for_pod_with_options(
        self,
        request: main_models.ListNodeInfosForPodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeInfosForPodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeInfosForPod',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeInfosForPodResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_infos_for_pod_with_options_async(
        self,
        request: main_models.ListNodeInfosForPodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeInfosForPodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeInfosForPod',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeInfosForPodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_infos_for_pod(
        self,
        request: main_models.ListNodeInfosForPodRequest,
    ) -> main_models.ListNodeInfosForPodResponse:
        runtime = RuntimeOptions()
        return self.list_node_infos_for_pod_with_options(request, runtime)

    async def list_node_infos_for_pod_async(
        self,
        request: main_models.ListNodeInfosForPodRequest,
    ) -> main_models.ListNodeInfosForPodResponse:
        runtime = RuntimeOptions()
        return await self.list_node_infos_for_pod_with_options_async(request, runtime)

    def list_subnets_with_options(
        self,
        request: main_models.ListSubnetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubnetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSubnets',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubnetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subnets_with_options_async(
        self,
        request: main_models.ListSubnetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubnetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSubnets',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubnetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subnets(
        self,
        request: main_models.ListSubnetsRequest,
    ) -> main_models.ListSubnetsResponse:
        runtime = RuntimeOptions()
        return self.list_subnets_with_options(request, runtime)

    async def list_subnets_async(
        self,
        request: main_models.ListSubnetsRequest,
    ) -> main_models.ListSubnetsResponse:
        runtime = RuntimeOptions()
        return await self.list_subnets_with_options_async(request, runtime)

    def list_vcc_flow_infos_with_options(
        self,
        request: main_models.ListVccFlowInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccFlowInfosResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.direction):
            body['Direction'] = request.direction
        if not DaraCore.is_null(request.from_):
            body['From'] = request.from_
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to):
            body['To'] = request.to
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccFlowInfos',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccFlowInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_flow_infos_with_options_async(
        self,
        request: main_models.ListVccFlowInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccFlowInfosResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.direction):
            body['Direction'] = request.direction
        if not DaraCore.is_null(request.from_):
            body['From'] = request.from_
        if not DaraCore.is_null(request.metric_name):
            body['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to):
            body['To'] = request.to
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccFlowInfos',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccFlowInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_flow_infos(
        self,
        request: main_models.ListVccFlowInfosRequest,
    ) -> main_models.ListVccFlowInfosResponse:
        runtime = RuntimeOptions()
        return self.list_vcc_flow_infos_with_options(request, runtime)

    async def list_vcc_flow_infos_async(
        self,
        request: main_models.ListVccFlowInfosRequest,
    ) -> main_models.ListVccFlowInfosResponse:
        runtime = RuntimeOptions()
        return await self.list_vcc_flow_infos_with_options_async(request, runtime)

    def list_vcc_grant_rules_with_options(
        self,
        request: main_models.ListVccGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccGrantRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccGrantRules',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_grant_rules_with_options_async(
        self,
        request: main_models.ListVccGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccGrantRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccGrantRules',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_grant_rules(
        self,
        request: main_models.ListVccGrantRulesRequest,
    ) -> main_models.ListVccGrantRulesResponse:
        runtime = RuntimeOptions()
        return self.list_vcc_grant_rules_with_options(request, runtime)

    async def list_vcc_grant_rules_async(
        self,
        request: main_models.ListVccGrantRulesRequest,
    ) -> main_models.ListVccGrantRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_vcc_grant_rules_with_options_async(request, runtime)

    def list_vcc_route_entries_with_options(
        self,
        request: main_models.ListVccRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_route_entries_with_options_async(
        self,
        request: main_models.ListVccRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_route_entries(
        self,
        request: main_models.ListVccRouteEntriesRequest,
    ) -> main_models.ListVccRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_vcc_route_entries_with_options(request, runtime)

    async def list_vcc_route_entries_async(
        self,
        request: main_models.ListVccRouteEntriesRequest,
    ) -> main_models.ListVccRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_vcc_route_entries_with_options_async(request, runtime)

    def list_vccs_with_options(
        self,
        request: main_models.ListVccsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not DaraCore.is_null(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccs',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vccs_with_options_async(
        self,
        request: main_models.ListVccsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVccsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not DaraCore.is_null(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVccs',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVccsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vccs(
        self,
        request: main_models.ListVccsRequest,
    ) -> main_models.ListVccsResponse:
        runtime = RuntimeOptions()
        return self.list_vccs_with_options(request, runtime)

    async def list_vccs_async(
        self,
        request: main_models.ListVccsRequest,
    ) -> main_models.ListVccsResponse:
        runtime = RuntimeOptions()
        return await self.list_vccs_with_options_async(request, runtime)

    def list_vpd_grant_rules_with_options(
        self,
        request: main_models.ListVpdGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdGrantRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpdGrantRules',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_grant_rules_with_options_async(
        self,
        request: main_models.ListVpdGrantRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdGrantRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not DaraCore.is_null(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpdGrantRules',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_grant_rules(
        self,
        request: main_models.ListVpdGrantRulesRequest,
    ) -> main_models.ListVpdGrantRulesResponse:
        runtime = RuntimeOptions()
        return self.list_vpd_grant_rules_with_options(request, runtime)

    async def list_vpd_grant_rules_async(
        self,
        request: main_models.ListVpdGrantRulesRequest,
    ) -> main_models.ListVpdGrantRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_vpd_grant_rules_with_options_async(request, runtime)

    def list_vpd_route_entries_with_options(
        self,
        request: main_models.ListVpdRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpdRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_route_entries_with_options_async(
        self,
        request: main_models.ListVpdRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdRouteEntriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not DaraCore.is_null(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not DaraCore.is_null(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.route_type):
            body['RouteType'] = request.route_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpdRouteEntries',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_route_entries(
        self,
        request: main_models.ListVpdRouteEntriesRequest,
    ) -> main_models.ListVpdRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_vpd_route_entries_with_options(request, runtime)

    async def list_vpd_route_entries_async(
        self,
        request: main_models.ListVpdRouteEntriesRequest,
    ) -> main_models.ListVpdRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_vpd_route_entries_with_options_async(request, runtime)

    def list_vpds_with_options(
        self,
        request: main_models.ListVpdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not DaraCore.is_null(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not DaraCore.is_null(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpds',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpds_with_options_async(
        self,
        request: main_models.ListVpdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not DaraCore.is_null(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not DaraCore.is_null(request.for_select):
            body['ForSelect'] = request.for_select
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not DaraCore.is_null(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not DaraCore.is_null(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpds',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpds(
        self,
        request: main_models.ListVpdsRequest,
    ) -> main_models.ListVpdsResponse:
        runtime = RuntimeOptions()
        return self.list_vpds_with_options(request, runtime)

    async def list_vpds_async(
        self,
        request: main_models.ListVpdsRequest,
    ) -> main_models.ListVpdsResponse:
        runtime = RuntimeOptions()
        return await self.list_vpds_with_options_async(request, runtime)

    def query_instance_ncd_with_options(
        self,
        request: main_models.QueryInstanceNcdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceNcdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id_1):
            body['InstanceId1'] = request.instance_id_1
        if not DaraCore.is_null(request.instance_id_2):
            body['InstanceId2'] = request.instance_id_2
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceNcd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceNcdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_ncd_with_options_async(
        self,
        request: main_models.QueryInstanceNcdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceNcdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id_1):
            body['InstanceId1'] = request.instance_id_1
        if not DaraCore.is_null(request.instance_id_2):
            body['InstanceId2'] = request.instance_id_2
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceNcd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceNcdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_ncd(
        self,
        request: main_models.QueryInstanceNcdRequest,
    ) -> main_models.QueryInstanceNcdResponse:
        runtime = RuntimeOptions()
        return self.query_instance_ncd_with_options(request, runtime)

    async def query_instance_ncd_async(
        self,
        request: main_models.QueryInstanceNcdRequest,
    ) -> main_models.QueryInstanceNcdResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_ncd_with_options_async(request, runtime)

    def refund_vcc_with_options(
        self,
        request: main_models.RefundVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefundVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_vcc_with_options_async(
        self,
        request: main_models.RefundVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefundVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_vcc(
        self,
        request: main_models.RefundVccRequest,
    ) -> main_models.RefundVccResponse:
        runtime = RuntimeOptions()
        return self.refund_vcc_with_options(request, runtime)

    async def refund_vcc_async(
        self,
        request: main_models.RefundVccRequest,
    ) -> main_models.RefundVccResponse:
        runtime = RuntimeOptions()
        return await self.refund_vcc_with_options_async(request, runtime)

    def retry_vcc_with_options(
        self,
        request: main_models.RetryVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_vcc_with_options_async(
        self,
        request: main_models.RetryVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_vcc(
        self,
        request: main_models.RetryVccRequest,
    ) -> main_models.RetryVccResponse:
        runtime = RuntimeOptions()
        return self.retry_vcc_with_options(request, runtime)

    async def retry_vcc_async(
        self,
        request: main_models.RetryVccRequest,
    ) -> main_models.RetryVccResponse:
        runtime = RuntimeOptions()
        return await self.retry_vcc_with_options_async(request, runtime)

    def switch_vcc_connection_with_options(
        self,
        request: main_models.SwitchVccConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchVccConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SwitchVccConnection',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchVccConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_vcc_connection_with_options_async(
        self,
        request: main_models.SwitchVccConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchVccConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SwitchVccConnection',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchVccConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_vcc_connection(
        self,
        request: main_models.SwitchVccConnectionRequest,
    ) -> main_models.SwitchVccConnectionResponse:
        runtime = RuntimeOptions()
        return self.switch_vcc_connection_with_options(request, runtime)

    async def switch_vcc_connection_async(
        self,
        request: main_models.SwitchVccConnectionRequest,
    ) -> main_models.SwitchVccConnectionResponse:
        runtime = RuntimeOptions()
        return await self.switch_vcc_connection_with_options_async(request, runtime)

    def un_assign_private_ip_address_with_options(
        self,
        request: main_models.UnAssignPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnAssignPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnAssignPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnAssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_assign_private_ip_address_with_options_async(
        self,
        request: main_models.UnAssignPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnAssignPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnAssignPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnAssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_assign_private_ip_address(
        self,
        request: main_models.UnAssignPrivateIpAddressRequest,
    ) -> main_models.UnAssignPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.un_assign_private_ip_address_with_options(request, runtime)

    async def un_assign_private_ip_address_async(
        self,
        request: main_models.UnAssignPrivateIpAddressRequest,
    ) -> main_models.UnAssignPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.un_assign_private_ip_address_with_options_async(request, runtime)

    def un_associate_vpd_cidr_block_with_options(
        self,
        request: main_models.UnAssociateVpdCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnAssociateVpdCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnAssociateVpdCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnAssociateVpdCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_associate_vpd_cidr_block_with_options_async(
        self,
        request: main_models.UnAssociateVpdCidrBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnAssociateVpdCidrBlockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnAssociateVpdCidrBlock',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnAssociateVpdCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_associate_vpd_cidr_block(
        self,
        request: main_models.UnAssociateVpdCidrBlockRequest,
    ) -> main_models.UnAssociateVpdCidrBlockResponse:
        runtime = RuntimeOptions()
        return self.un_associate_vpd_cidr_block_with_options(request, runtime)

    async def un_associate_vpd_cidr_block_async(
        self,
        request: main_models.UnAssociateVpdCidrBlockRequest,
    ) -> main_models.UnAssociateVpdCidrBlockResponse:
        runtime = RuntimeOptions()
        return await self.un_associate_vpd_cidr_block_with_options_async(request, runtime)

    def unassign_leni_private_ip_address_with_options(
        self,
        request: main_models.UnassignLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnassignLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnassignLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnassignLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassign_leni_private_ip_address_with_options_async(
        self,
        request: main_models.UnassignLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnassignLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnassignLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnassignLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassign_leni_private_ip_address(
        self,
        request: main_models.UnassignLeniPrivateIpAddressRequest,
    ) -> main_models.UnassignLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.unassign_leni_private_ip_address_with_options(request, runtime)

    async def unassign_leni_private_ip_address_async(
        self,
        request: main_models.UnassignLeniPrivateIpAddressRequest,
    ) -> main_models.UnassignLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.unassign_leni_private_ip_address_with_options_async(request, runtime)

    def update_elastic_network_interface_with_options(
        self,
        request: main_models.UpdateElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_elastic_network_interface_with_options_async(
        self,
        request: main_models.UpdateElasticNetworkInterfaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateElasticNetworkInterfaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateElasticNetworkInterface',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_elastic_network_interface(
        self,
        request: main_models.UpdateElasticNetworkInterfaceRequest,
    ) -> main_models.UpdateElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return self.update_elastic_network_interface_with_options(request, runtime)

    async def update_elastic_network_interface_async(
        self,
        request: main_models.UpdateElasticNetworkInterfaceRequest,
    ) -> main_models.UpdateElasticNetworkInterfaceResponse:
        runtime = RuntimeOptions()
        return await self.update_elastic_network_interface_with_options_async(request, runtime)

    def update_er_with_options(
        self,
        request: main_models.UpdateErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_with_options_async(
        self,
        request: main_models.UpdateErRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_name):
            body['ErName'] = request.er_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEr',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er(
        self,
        request: main_models.UpdateErRequest,
    ) -> main_models.UpdateErResponse:
        runtime = RuntimeOptions()
        return self.update_er_with_options(request, runtime)

    async def update_er_async(
        self,
        request: main_models.UpdateErRequest,
    ) -> main_models.UpdateErResponse:
        runtime = RuntimeOptions()
        return await self.update_er_with_options_async(request, runtime)

    def update_er_attachment_with_options(
        self,
        request: main_models.UpdateErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_attachment_with_options_async(
        self,
        request: main_models.UpdateErAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not DaraCore.is_null(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateErAttachment',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_attachment(
        self,
        request: main_models.UpdateErAttachmentRequest,
    ) -> main_models.UpdateErAttachmentResponse:
        runtime = RuntimeOptions()
        return self.update_er_attachment_with_options(request, runtime)

    async def update_er_attachment_async(
        self,
        request: main_models.UpdateErAttachmentRequest,
    ) -> main_models.UpdateErAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.update_er_attachment_with_options_async(request, runtime)

    def update_er_route_map_with_options(
        self,
        request: main_models.UpdateErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_route_map_with_options_async(
        self,
        request: main_models.UpdateErRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateErRouteMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.er_id):
            body['ErId'] = request.er_id
        if not DaraCore.is_null(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateErRouteMap',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_route_map(
        self,
        request: main_models.UpdateErRouteMapRequest,
    ) -> main_models.UpdateErRouteMapResponse:
        runtime = RuntimeOptions()
        return self.update_er_route_map_with_options(request, runtime)

    async def update_er_route_map_async(
        self,
        request: main_models.UpdateErRouteMapRequest,
    ) -> main_models.UpdateErRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.update_er_route_map_with_options_async(request, runtime)

    def update_leni_private_ip_address_with_options(
        self,
        request: main_models.UpdateLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_leni_private_ip_address_with_options_async(
        self,
        request: main_models.UpdateLeniPrivateIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLeniPrivateIpAddressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not DaraCore.is_null(request.ip_name):
            body['IpName'] = request.ip_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLeniPrivateIpAddress',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_leni_private_ip_address(
        self,
        request: main_models.UpdateLeniPrivateIpAddressRequest,
    ) -> main_models.UpdateLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return self.update_leni_private_ip_address_with_options(request, runtime)

    async def update_leni_private_ip_address_async(
        self,
        request: main_models.UpdateLeniPrivateIpAddressRequest,
    ) -> main_models.UpdateLeniPrivateIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.update_leni_private_ip_address_with_options_async(request, runtime)

    def update_subnet_with_options(
        self,
        request: main_models.UpdateSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subnet_with_options_async(
        self,
        request: main_models.UpdateSubnetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubnetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not DaraCore.is_null(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubnet',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subnet(
        self,
        request: main_models.UpdateSubnetRequest,
    ) -> main_models.UpdateSubnetResponse:
        runtime = RuntimeOptions()
        return self.update_subnet_with_options(request, runtime)

    async def update_subnet_async(
        self,
        request: main_models.UpdateSubnetRequest,
    ) -> main_models.UpdateSubnetResponse:
        runtime = RuntimeOptions()
        return await self.update_subnet_with_options_async(request, runtime)

    def update_vcc_with_options(
        self,
        request: main_models.UpdateVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.order_id):
            body['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vcc_with_options_async(
        self,
        request: main_models.UpdateVccRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVccResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.order_id):
            body['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not DaraCore.is_null(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVcc',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vcc(
        self,
        request: main_models.UpdateVccRequest,
    ) -> main_models.UpdateVccResponse:
        runtime = RuntimeOptions()
        return self.update_vcc_with_options(request, runtime)

    async def update_vcc_async(
        self,
        request: main_models.UpdateVccRequest,
    ) -> main_models.UpdateVccResponse:
        runtime = RuntimeOptions()
        return await self.update_vcc_with_options_async(request, runtime)

    def update_vpd_with_options(
        self,
        request: main_models.UpdateVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpd_with_options_async(
        self,
        request: main_models.UpdateVpdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVpdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not DaraCore.is_null(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVpd',
            version = '2022-05-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpd(
        self,
        request: main_models.UpdateVpdRequest,
    ) -> main_models.UpdateVpdResponse:
        runtime = RuntimeOptions()
        return self.update_vpd_with_options(request, runtime)

    async def update_vpd_async(
        self,
        request: main_models.UpdateVpdRequest,
    ) -> main_models.UpdateVpdResponse:
        runtime = RuntimeOptions()
        return await self.update_vpd_with_options_async(request, runtime)
