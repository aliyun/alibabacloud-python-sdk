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

    def create_subnet_with_options(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
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
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
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

    def get_subnet_with_options(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
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
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
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
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        req = open_api_models.OpenApiRequest()
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

    def initialize_vcc(self) -> eflo_20220530_models.InitializeVccResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_vcc_with_options(runtime)

    async def initialize_vcc_async(self) -> eflo_20220530_models.InitializeVccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_vcc_with_options_async(runtime)

    def list_subnets_with_options(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
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
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
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
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
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

    def update_subnet_with_options(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
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
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
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
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
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
