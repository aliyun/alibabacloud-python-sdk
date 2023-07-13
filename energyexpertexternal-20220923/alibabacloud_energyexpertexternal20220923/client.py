# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_energyexpertexternal20220923 import models as energy_expert_external_20220923_models
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
        self._endpoint = self.get_endpoint('energyexpertexternal', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_device_info_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_info_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_info(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_info_with_options(request, headers, runtime)

    async def get_device_info_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_device_info_with_options_async(request, headers, runtime)

    def get_device_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_list(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_list_with_options(request, headers, runtime)

    async def get_device_list_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_device_list_with_options_async(request, headers, runtime)

    def get_org_and_factory_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrgAndFactory',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getOrgAndFactory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgAndFactoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_org_and_factory_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrgAndFactory',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getOrgAndFactory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgAndFactoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_org_and_factory(self) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_org_and_factory_with_options(headers, runtime)

    async def get_org_and_factory_async(self) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_org_and_factory_with_options_async(headers, runtime)
