# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligeniessp_1_0 import models as ali_geniessp__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_device_id_by_identity(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders()
        return self.get_device_id_by_identity_with_options(request, headers, runtime)

    async def get_device_id_by_identity_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders()
        return await self.get_device_id_by_identity_with_options_async(request, headers, runtime)

    def get_device_id_by_identity_with_options(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
        headers: ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = headers.x_acs_aligenie_access_token
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = headers.authorization
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse(),
            self.do_roarequest('GetDeviceIdByIdentity', 'ssp_1.0', 'HTTPS', 'GET', 'AK', f'/v1.0/ssp/getDeviceIdByIdentity', 'json', req, runtime)
        )

    async def get_device_id_by_identity_with_options_async(
        self,
        request: ali_geniessp__1__0_models.GetDeviceIdByIdentityRequest,
        headers: ali_geniessp__1__0_models.GetDeviceIdByIdentityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.identity_id):
            query['IdentityId'] = request.identity_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.encode_key):
            query['EncodeKey'] = request.encode_key
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = headers.x_acs_aligenie_access_token
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = headers.authorization
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ali_geniessp__1__0_models.GetDeviceIdByIdentityResponse(),
            await self.do_roarequest_async('GetDeviceIdByIdentity', 'ssp_1.0', 'HTTPS', 'GET', 'AK', f'/v1.0/ssp/getDeviceIdByIdentity', 'json', req, runtime)
        )
