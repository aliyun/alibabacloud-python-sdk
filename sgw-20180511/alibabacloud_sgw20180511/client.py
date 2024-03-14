# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sgw20180511 import models as sgw_20180511_models
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
        self._endpoint_map = {
            'cn-qingdao': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-beijing': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-chengdu': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-zhangjiakou': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-huhehaote': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-hangzhou': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'sgw.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'sgw.cn-shanghai.aliyuncs.com',
            'us-east-1': 'sgw.us-west-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sgw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_all_in_one_gateway_with_options(
        self,
        request: sgw_20180511_models.ActivateAllInOneGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ActivateAllInOneGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.device_number):
            query['DeviceNumber'] = request.device_number
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateAllInOneGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ActivateAllInOneGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_all_in_one_gateway_with_options_async(
        self,
        request: sgw_20180511_models.ActivateAllInOneGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ActivateAllInOneGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.device_number):
            query['DeviceNumber'] = request.device_number
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateAllInOneGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ActivateAllInOneGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_all_in_one_gateway(
        self,
        request: sgw_20180511_models.ActivateAllInOneGatewayRequest,
    ) -> sgw_20180511_models.ActivateAllInOneGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_all_in_one_gateway_with_options(request, runtime)

    async def activate_all_in_one_gateway_async(
        self,
        request: sgw_20180511_models.ActivateAllInOneGatewayRequest,
    ) -> sgw_20180511_models.ActivateAllInOneGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_all_in_one_gateway_with_options_async(request, runtime)

    def activate_gateway_with_options(
        self,
        request: sgw_20180511_models.ActivateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ActivateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ActivateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_gateway_with_options_async(
        self,
        request: sgw_20180511_models.ActivateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ActivateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ActivateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_gateway(
        self,
        request: sgw_20180511_models.ActivateGatewayRequest,
    ) -> sgw_20180511_models.ActivateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_gateway_with_options(request, runtime)

    async def activate_gateway_async(
        self,
        request: sgw_20180511_models.ActivateGatewayRequest,
    ) -> sgw_20180511_models.ActivateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_gateway_with_options_async(request, runtime)

    def add_shares_to_express_sync_with_options(
        self,
        request: sgw_20180511_models.AddSharesToExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.AddSharesToExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.gateway_shares):
            query['GatewayShares'] = request.gateway_shares
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSharesToExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.AddSharesToExpressSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_shares_to_express_sync_with_options_async(
        self,
        request: sgw_20180511_models.AddSharesToExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.AddSharesToExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.gateway_shares):
            query['GatewayShares'] = request.gateway_shares
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSharesToExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.AddSharesToExpressSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_shares_to_express_sync(
        self,
        request: sgw_20180511_models.AddSharesToExpressSyncRequest,
    ) -> sgw_20180511_models.AddSharesToExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_shares_to_express_sync_with_options(request, runtime)

    async def add_shares_to_express_sync_async(
        self,
        request: sgw_20180511_models.AddSharesToExpressSyncRequest,
    ) -> sgw_20180511_models.AddSharesToExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_shares_to_express_sync_with_options_async(request, runtime)

    def add_tags_to_gateway_with_options(
        self,
        request: sgw_20180511_models.AddTagsToGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.AddTagsToGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsToGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.AddTagsToGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_to_gateway_with_options_async(
        self,
        request: sgw_20180511_models.AddTagsToGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.AddTagsToGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsToGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.AddTagsToGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags_to_gateway(
        self,
        request: sgw_20180511_models.AddTagsToGatewayRequest,
    ) -> sgw_20180511_models.AddTagsToGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_gateway_with_options(request, runtime)

    async def add_tags_to_gateway_async(
        self,
        request: sgw_20180511_models.AddTagsToGatewayRequest,
    ) -> sgw_20180511_models.AddTagsToGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_to_gateway_with_options_async(request, runtime)

    def check_activation_key_with_options(
        self,
        request: sgw_20180511_models.CheckActivationKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckActivationKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crypt_key):
            query['CryptKey'] = request.crypt_key
        if not UtilClient.is_unset(request.crypt_text):
            query['CryptText'] = request.crypt_text
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckActivationKey',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckActivationKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_activation_key_with_options_async(
        self,
        request: sgw_20180511_models.CheckActivationKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckActivationKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crypt_key):
            query['CryptKey'] = request.crypt_key
        if not UtilClient.is_unset(request.crypt_text):
            query['CryptText'] = request.crypt_text
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckActivationKey',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckActivationKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_activation_key(
        self,
        request: sgw_20180511_models.CheckActivationKeyRequest,
    ) -> sgw_20180511_models.CheckActivationKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_activation_key_with_options(request, runtime)

    async def check_activation_key_async(
        self,
        request: sgw_20180511_models.CheckActivationKeyRequest,
    ) -> sgw_20180511_models.CheckActivationKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_activation_key_with_options_async(request, runtime)

    def check_block_volume_name_with_options(
        self,
        request: sgw_20180511_models.CheckBlockVolumeNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckBlockVolumeNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.volume_name):
            query['VolumeName'] = request.volume_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBlockVolumeName',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckBlockVolumeNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_block_volume_name_with_options_async(
        self,
        request: sgw_20180511_models.CheckBlockVolumeNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckBlockVolumeNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.volume_name):
            query['VolumeName'] = request.volume_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBlockVolumeName',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckBlockVolumeNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_block_volume_name(
        self,
        request: sgw_20180511_models.CheckBlockVolumeNameRequest,
    ) -> sgw_20180511_models.CheckBlockVolumeNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_block_volume_name_with_options(request, runtime)

    async def check_block_volume_name_async(
        self,
        request: sgw_20180511_models.CheckBlockVolumeNameRequest,
    ) -> sgw_20180511_models.CheckBlockVolumeNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_block_volume_name_with_options_async(request, runtime)

    def check_gateway_essd_support_with_options(
        self,
        request: sgw_20180511_models.CheckGatewayEssdSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckGatewayEssdSupportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckGatewayEssdSupport',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckGatewayEssdSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_gateway_essd_support_with_options_async(
        self,
        request: sgw_20180511_models.CheckGatewayEssdSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckGatewayEssdSupportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckGatewayEssdSupport',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckGatewayEssdSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_gateway_essd_support(
        self,
        request: sgw_20180511_models.CheckGatewayEssdSupportRequest,
    ) -> sgw_20180511_models.CheckGatewayEssdSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_gateway_essd_support_with_options(request, runtime)

    async def check_gateway_essd_support_async(
        self,
        request: sgw_20180511_models.CheckGatewayEssdSupportRequest,
    ) -> sgw_20180511_models.CheckGatewayEssdSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_gateway_essd_support_with_options_async(request, runtime)

    def check_mns_service_with_options(
        self,
        request: sgw_20180511_models.CheckMnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckMnsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMnsService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckMnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mns_service_with_options_async(
        self,
        request: sgw_20180511_models.CheckMnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckMnsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMnsService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckMnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mns_service(
        self,
        request: sgw_20180511_models.CheckMnsServiceRequest,
    ) -> sgw_20180511_models.CheckMnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_mns_service_with_options(request, runtime)

    async def check_mns_service_async(
        self,
        request: sgw_20180511_models.CheckMnsServiceRequest,
    ) -> sgw_20180511_models.CheckMnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_mns_service_with_options_async(request, runtime)

    def check_role_with_options(
        self,
        request: sgw_20180511_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRole',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_role_with_options_async(
        self,
        request: sgw_20180511_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRole',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_role(
        self,
        request: sgw_20180511_models.CheckRoleRequest,
    ) -> sgw_20180511_models.CheckRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_role_with_options(request, runtime)

    async def check_role_async(
        self,
        request: sgw_20180511_models.CheckRoleRequest,
    ) -> sgw_20180511_models.CheckRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_role_with_options_async(request, runtime)

    def check_slr_role_with_options(
        self,
        request: sgw_20180511_models.CheckSlrRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckSlrRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_if_not_exist):
            query['CreateIfNotExist'] = request.create_if_not_exist
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSlrRole',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckSlrRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_slr_role_with_options_async(
        self,
        request: sgw_20180511_models.CheckSlrRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckSlrRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_if_not_exist):
            query['CreateIfNotExist'] = request.create_if_not_exist
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSlrRole',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckSlrRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_slr_role(
        self,
        request: sgw_20180511_models.CheckSlrRoleRequest,
    ) -> sgw_20180511_models.CheckSlrRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_slr_role_with_options(request, runtime)

    async def check_slr_role_async(
        self,
        request: sgw_20180511_models.CheckSlrRoleRequest,
    ) -> sgw_20180511_models.CheckSlrRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_slr_role_with_options_async(request, runtime)

    def check_upgrade_version_with_options(
        self,
        request: sgw_20180511_models.CheckUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_version):
            query['GatewayVersion'] = request.gateway_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUpgradeVersion',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckUpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_upgrade_version_with_options_async(
        self,
        request: sgw_20180511_models.CheckUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CheckUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_version):
            query['GatewayVersion'] = request.gateway_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUpgradeVersion',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CheckUpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_upgrade_version(
        self,
        request: sgw_20180511_models.CheckUpgradeVersionRequest,
    ) -> sgw_20180511_models.CheckUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_upgrade_version_with_options(request, runtime)

    async def check_upgrade_version_async(
        self,
        request: sgw_20180511_models.CheckUpgradeVersionRequest,
    ) -> sgw_20180511_models.CheckUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_upgrade_version_with_options_async(request, runtime)

    def create_cache_with_options(
        self,
        request: sgw_20180511_models.CreateCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCache',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cache_with_options_async(
        self,
        request: sgw_20180511_models.CreateCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCache',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cache(
        self,
        request: sgw_20180511_models.CreateCacheRequest,
    ) -> sgw_20180511_models.CreateCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cache_with_options(request, runtime)

    async def create_cache_async(
        self,
        request: sgw_20180511_models.CreateCacheRequest,
    ) -> sgw_20180511_models.CreateCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_with_options_async(request, runtime)

    def create_elastic_gateway_private_zone_with_options(
        self,
        request: sgw_20180511_models.CreateElasticGatewayPrivateZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticGatewayPrivateZone',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_gateway_private_zone_with_options_async(
        self,
        request: sgw_20180511_models.CreateElasticGatewayPrivateZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticGatewayPrivateZone',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_gateway_private_zone(
        self,
        request: sgw_20180511_models.CreateElasticGatewayPrivateZoneRequest,
    ) -> sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_gateway_private_zone_with_options(request, runtime)

    async def create_elastic_gateway_private_zone_async(
        self,
        request: sgw_20180511_models.CreateElasticGatewayPrivateZoneRequest,
    ) -> sgw_20180511_models.CreateElasticGatewayPrivateZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_elastic_gateway_private_zone_with_options_async(request, runtime)

    def create_express_sync_with_options(
        self,
        request: sgw_20180511_models.CreateExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateExpressSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_express_sync_with_options_async(
        self,
        request: sgw_20180511_models.CreateExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateExpressSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_express_sync(
        self,
        request: sgw_20180511_models.CreateExpressSyncRequest,
    ) -> sgw_20180511_models.CreateExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_express_sync_with_options(request, runtime)

    async def create_express_sync_async(
        self,
        request: sgw_20180511_models.CreateExpressSyncRequest,
    ) -> sgw_20180511_models.CreateExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_express_sync_with_options_async(request, runtime)

    def create_gateway_with_options(
        self,
        request: sgw_20180511_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.post_paid):
            query['PostPaid'] = request.post_paid
        if not UtilClient.is_unset(request.public_network_bandwidth):
            query['PublicNetworkBandwidth'] = request.public_network_bandwidth
        if not UtilClient.is_unset(request.release_after_expiration):
            query['ReleaseAfterExpiration'] = request.release_after_expiration
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.untrusted_env_id):
            query['UntrustedEnvId'] = request.untrusted_env_id
        if not UtilClient.is_unset(request.untrusted_env_instance_type):
            query['UntrustedEnvInstanceType'] = request.untrusted_env_instance_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.post_paid):
            query['PostPaid'] = request.post_paid
        if not UtilClient.is_unset(request.public_network_bandwidth):
            query['PublicNetworkBandwidth'] = request.public_network_bandwidth
        if not UtilClient.is_unset(request.release_after_expiration):
            query['ReleaseAfterExpiration'] = request.release_after_expiration
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.untrusted_env_id):
            query['UntrustedEnvId'] = request.untrusted_env_id
        if not UtilClient.is_unset(request.untrusted_env_instance_type):
            query['UntrustedEnvInstanceType'] = request.untrusted_env_instance_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: sgw_20180511_models.CreateGatewayRequest,
    ) -> sgw_20180511_models.CreateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_with_options(request, runtime)

    async def create_gateway_async(
        self,
        request: sgw_20180511_models.CreateGatewayRequest,
    ) -> sgw_20180511_models.CreateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_with_options_async(request, runtime)

    def create_gateway_block_volume_with_options(
        self,
        request: sgw_20180511_models.CreateGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.chap_enabled):
            query['ChapEnabled'] = request.chap_enabled
        if not UtilClient.is_unset(request.chap_in_password):
            query['ChapInPassword'] = request.chap_in_password
        if not UtilClient.is_unset(request.chap_in_user):
            query['ChapInUser'] = request.chap_in_user
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_ssl):
            query['OssBucketSsl'] = request.oss_bucket_ssl
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.recovery):
            query['Recovery'] = request.recovery
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.volume_protocol):
            query['VolumeProtocol'] = request.volume_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayBlockVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_block_volume_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.chap_enabled):
            query['ChapEnabled'] = request.chap_enabled
        if not UtilClient.is_unset(request.chap_in_password):
            query['ChapInPassword'] = request.chap_in_password
        if not UtilClient.is_unset(request.chap_in_user):
            query['ChapInUser'] = request.chap_in_user
        if not UtilClient.is_unset(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_ssl):
            query['OssBucketSsl'] = request.oss_bucket_ssl
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.recovery):
            query['Recovery'] = request.recovery
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.volume_protocol):
            query['VolumeProtocol'] = request.volume_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayBlockVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_block_volume(
        self,
        request: sgw_20180511_models.CreateGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.CreateGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_block_volume_with_options(request, runtime)

    async def create_gateway_block_volume_async(
        self,
        request: sgw_20180511_models.CreateGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.CreateGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_block_volume_with_options_async(request, runtime)

    def create_gateway_cache_disk_with_options(
        self,
        request: sgw_20180511_models.CreateGatewayCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_disk_category):
            query['CacheDiskCategory'] = request.cache_disk_category
        if not UtilClient.is_unset(request.cache_disk_size_in_gb):
            query['CacheDiskSizeInGB'] = request.cache_disk_size_in_gb
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayCacheDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_cache_disk_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewayCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_disk_category):
            query['CacheDiskCategory'] = request.cache_disk_category
        if not UtilClient.is_unset(request.cache_disk_size_in_gb):
            query['CacheDiskSizeInGB'] = request.cache_disk_size_in_gb
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayCacheDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_cache_disk(
        self,
        request: sgw_20180511_models.CreateGatewayCacheDiskRequest,
    ) -> sgw_20180511_models.CreateGatewayCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_cache_disk_with_options(request, runtime)

    async def create_gateway_cache_disk_async(
        self,
        request: sgw_20180511_models.CreateGatewayCacheDiskRequest,
    ) -> sgw_20180511_models.CreateGatewayCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_cache_disk_with_options_async(request, runtime)

    def create_gateway_file_share_with_options(
        self,
        request: sgw_20180511_models.CreateGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_based_enumeration):
            query['AccessBasedEnumeration'] = request.access_based_enumeration
        if not UtilClient.is_unset(request.backend_limit):
            query['BackendLimit'] = request.backend_limit
        if not UtilClient.is_unset(request.browsable):
            query['Browsable'] = request.browsable
        if not UtilClient.is_unset(request.bypass_cache_read):
            query['BypassCacheRead'] = request.bypass_cache_read
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.client_side_cmk):
            query['ClientSideCmk'] = request.client_side_cmk
        if not UtilClient.is_unset(request.client_side_encryption):
            query['ClientSideEncryption'] = request.client_side_encryption
        if not UtilClient.is_unset(request.direct_io):
            query['DirectIO'] = request.direct_io
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.fast_reclaim):
            query['FastReclaim'] = request.fast_reclaim
        if not UtilClient.is_unset(request.frontend_limit):
            query['FrontendLimit'] = request.frontend_limit
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.ignore_delete):
            query['IgnoreDelete'] = request.ignore_delete
        if not UtilClient.is_unset(request.in_place):
            query['InPlace'] = request.in_place
        if not UtilClient.is_unset(request.kms_rotate_period):
            query['KmsRotatePeriod'] = request.kms_rotate_period
        if not UtilClient.is_unset(request.lag_period):
            query['LagPeriod'] = request.lag_period
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nfs_v4optimization):
            query['NfsV4Optimization'] = request.nfs_v4optimization
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_ssl):
            query['OssBucketSsl'] = request.oss_bucket_ssl
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.partial_sync_paths):
            query['PartialSyncPaths'] = request.partial_sync_paths
        if not UtilClient.is_unset(request.path_prefix):
            query['PathPrefix'] = request.path_prefix
        if not UtilClient.is_unset(request.polling_interval):
            query['PollingInterval'] = request.polling_interval
        if not UtilClient.is_unset(request.read_only_client_list):
            query['ReadOnlyClientList'] = request.read_only_client_list
        if not UtilClient.is_unset(request.read_only_user_list):
            query['ReadOnlyUserList'] = request.read_only_user_list
        if not UtilClient.is_unset(request.read_write_client_list):
            query['ReadWriteClientList'] = request.read_write_client_list
        if not UtilClient.is_unset(request.read_write_user_list):
            query['ReadWriteUserList'] = request.read_write_user_list
        if not UtilClient.is_unset(request.remote_sync):
            query['RemoteSync'] = request.remote_sync
        if not UtilClient.is_unset(request.remote_sync_download):
            query['RemoteSyncDownload'] = request.remote_sync_download
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_side_algorithm):
            query['ServerSideAlgorithm'] = request.server_side_algorithm
        if not UtilClient.is_unset(request.server_side_cmk):
            query['ServerSideCmk'] = request.server_side_cmk
        if not UtilClient.is_unset(request.server_side_encryption):
            query['ServerSideEncryption'] = request.server_side_encryption
        if not UtilClient.is_unset(request.share_protocol):
            query['ShareProtocol'] = request.share_protocol
        if not UtilClient.is_unset(request.squash):
            query['Squash'] = request.squash
        if not UtilClient.is_unset(request.support_archive):
            query['SupportArchive'] = request.support_archive
        if not UtilClient.is_unset(request.transfer_acceleration):
            query['TransferAcceleration'] = request.transfer_acceleration
        if not UtilClient.is_unset(request.windows_acl):
            query['WindowsAcl'] = request.windows_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayFileShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_file_share_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_based_enumeration):
            query['AccessBasedEnumeration'] = request.access_based_enumeration
        if not UtilClient.is_unset(request.backend_limit):
            query['BackendLimit'] = request.backend_limit
        if not UtilClient.is_unset(request.browsable):
            query['Browsable'] = request.browsable
        if not UtilClient.is_unset(request.bypass_cache_read):
            query['BypassCacheRead'] = request.bypass_cache_read
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.client_side_cmk):
            query['ClientSideCmk'] = request.client_side_cmk
        if not UtilClient.is_unset(request.client_side_encryption):
            query['ClientSideEncryption'] = request.client_side_encryption
        if not UtilClient.is_unset(request.direct_io):
            query['DirectIO'] = request.direct_io
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.fast_reclaim):
            query['FastReclaim'] = request.fast_reclaim
        if not UtilClient.is_unset(request.frontend_limit):
            query['FrontendLimit'] = request.frontend_limit
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.ignore_delete):
            query['IgnoreDelete'] = request.ignore_delete
        if not UtilClient.is_unset(request.in_place):
            query['InPlace'] = request.in_place
        if not UtilClient.is_unset(request.kms_rotate_period):
            query['KmsRotatePeriod'] = request.kms_rotate_period
        if not UtilClient.is_unset(request.lag_period):
            query['LagPeriod'] = request.lag_period
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nfs_v4optimization):
            query['NfsV4Optimization'] = request.nfs_v4optimization
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_ssl):
            query['OssBucketSsl'] = request.oss_bucket_ssl
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.partial_sync_paths):
            query['PartialSyncPaths'] = request.partial_sync_paths
        if not UtilClient.is_unset(request.path_prefix):
            query['PathPrefix'] = request.path_prefix
        if not UtilClient.is_unset(request.polling_interval):
            query['PollingInterval'] = request.polling_interval
        if not UtilClient.is_unset(request.read_only_client_list):
            query['ReadOnlyClientList'] = request.read_only_client_list
        if not UtilClient.is_unset(request.read_only_user_list):
            query['ReadOnlyUserList'] = request.read_only_user_list
        if not UtilClient.is_unset(request.read_write_client_list):
            query['ReadWriteClientList'] = request.read_write_client_list
        if not UtilClient.is_unset(request.read_write_user_list):
            query['ReadWriteUserList'] = request.read_write_user_list
        if not UtilClient.is_unset(request.remote_sync):
            query['RemoteSync'] = request.remote_sync
        if not UtilClient.is_unset(request.remote_sync_download):
            query['RemoteSyncDownload'] = request.remote_sync_download
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_side_algorithm):
            query['ServerSideAlgorithm'] = request.server_side_algorithm
        if not UtilClient.is_unset(request.server_side_cmk):
            query['ServerSideCmk'] = request.server_side_cmk
        if not UtilClient.is_unset(request.server_side_encryption):
            query['ServerSideEncryption'] = request.server_side_encryption
        if not UtilClient.is_unset(request.share_protocol):
            query['ShareProtocol'] = request.share_protocol
        if not UtilClient.is_unset(request.squash):
            query['Squash'] = request.squash
        if not UtilClient.is_unset(request.support_archive):
            query['SupportArchive'] = request.support_archive
        if not UtilClient.is_unset(request.transfer_acceleration):
            query['TransferAcceleration'] = request.transfer_acceleration
        if not UtilClient.is_unset(request.windows_acl):
            query['WindowsAcl'] = request.windows_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayFileShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_file_share(
        self,
        request: sgw_20180511_models.CreateGatewayFileShareRequest,
    ) -> sgw_20180511_models.CreateGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_file_share_with_options(request, runtime)

    async def create_gateway_file_share_async(
        self,
        request: sgw_20180511_models.CreateGatewayFileShareRequest,
    ) -> sgw_20180511_models.CreateGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_file_share_with_options_async(request, runtime)

    def create_gateway_logging_with_options(
        self,
        request: sgw_20180511_models.CreateGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_logging_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewayLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_logging(
        self,
        request: sgw_20180511_models.CreateGatewayLoggingRequest,
    ) -> sgw_20180511_models.CreateGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_logging_with_options(request, runtime)

    async def create_gateway_logging_async(
        self,
        request: sgw_20180511_models.CreateGatewayLoggingRequest,
    ) -> sgw_20180511_models.CreateGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_logging_with_options_async(request, runtime)

    def create_gateway_smbuser_with_options(
        self,
        request: sgw_20180511_models.CreateGatewaySMBUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewaySMBUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewaySMBUser',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewaySMBUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_smbuser_with_options_async(
        self,
        request: sgw_20180511_models.CreateGatewaySMBUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateGatewaySMBUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewaySMBUser',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateGatewaySMBUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_smbuser(
        self,
        request: sgw_20180511_models.CreateGatewaySMBUserRequest,
    ) -> sgw_20180511_models.CreateGatewaySMBUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_smbuser_with_options(request, runtime)

    async def create_gateway_smbuser_async(
        self,
        request: sgw_20180511_models.CreateGatewaySMBUserRequest,
    ) -> sgw_20180511_models.CreateGatewaySMBUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_smbuser_with_options_async(request, runtime)

    def create_storage_bundle_with_options(
        self,
        request: sgw_20180511_models.CreateStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateStorageBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_bundle_with_options_async(
        self,
        request: sgw_20180511_models.CreateStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.CreateStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.CreateStorageBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_bundle(
        self,
        request: sgw_20180511_models.CreateStorageBundleRequest,
    ) -> sgw_20180511_models.CreateStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_storage_bundle_with_options(request, runtime)

    async def create_storage_bundle_async(
        self,
        request: sgw_20180511_models.CreateStorageBundleRequest,
    ) -> sgw_20180511_models.CreateStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_bundle_with_options_async(request, runtime)

    def delete_csgclients_with_options(
        self,
        tmp_req: sgw_20180511_models.DeleteCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteCSGClientsResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.DeleteCSGClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteCSGClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_csgclients_with_options_async(
        self,
        tmp_req: sgw_20180511_models.DeleteCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteCSGClientsResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.DeleteCSGClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteCSGClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_csgclients(
        self,
        request: sgw_20180511_models.DeleteCSGClientsRequest,
    ) -> sgw_20180511_models.DeleteCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_csgclients_with_options(request, runtime)

    async def delete_csgclients_async(
        self,
        request: sgw_20180511_models.DeleteCSGClientsRequest,
    ) -> sgw_20180511_models.DeleteCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_csgclients_with_options_async(request, runtime)

    def delete_elastic_gateway_private_zone_with_options(
        self,
        request: sgw_20180511_models.DeleteElasticGatewayPrivateZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticGatewayPrivateZone',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_gateway_private_zone_with_options_async(
        self,
        request: sgw_20180511_models.DeleteElasticGatewayPrivateZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticGatewayPrivateZone',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_gateway_private_zone(
        self,
        request: sgw_20180511_models.DeleteElasticGatewayPrivateZoneRequest,
    ) -> sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_gateway_private_zone_with_options(request, runtime)

    async def delete_elastic_gateway_private_zone_async(
        self,
        request: sgw_20180511_models.DeleteElasticGatewayPrivateZoneRequest,
    ) -> sgw_20180511_models.DeleteElasticGatewayPrivateZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_elastic_gateway_private_zone_with_options_async(request, runtime)

    def delete_express_sync_with_options(
        self,
        request: sgw_20180511_models.DeleteExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteExpressSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_express_sync_with_options_async(
        self,
        request: sgw_20180511_models.DeleteExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteExpressSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_express_sync(
        self,
        request: sgw_20180511_models.DeleteExpressSyncRequest,
    ) -> sgw_20180511_models.DeleteExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_express_sync_with_options(request, runtime)

    async def delete_express_sync_async(
        self,
        request: sgw_20180511_models.DeleteExpressSyncRequest,
    ) -> sgw_20180511_models.DeleteExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_express_sync_with_options_async(request, runtime)

    def delete_gateway_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.reason_detail):
            query['ReasonDetail'] = request.reason_detail
        if not UtilClient.is_unset(request.reason_type):
            query['ReasonType'] = request.reason_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.reason_detail):
            query['ReasonDetail'] = request.reason_detail
        if not UtilClient.is_unset(request.reason_type):
            query['ReasonType'] = request.reason_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        request: sgw_20180511_models.DeleteGatewayRequest,
    ) -> sgw_20180511_models.DeleteGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_with_options(request, runtime)

    async def delete_gateway_async(
        self,
        request: sgw_20180511_models.DeleteGatewayRequest,
    ) -> sgw_20180511_models.DeleteGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_with_options_async(request, runtime)

    def delete_gateway_block_volumes_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewayBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayBlockVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.is_source_deletion):
            query['IsSourceDeletion'] = request.is_source_deletion
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayBlockVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_block_volumes_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewayBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayBlockVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.is_source_deletion):
            query['IsSourceDeletion'] = request.is_source_deletion
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayBlockVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_block_volumes(
        self,
        request: sgw_20180511_models.DeleteGatewayBlockVolumesRequest,
    ) -> sgw_20180511_models.DeleteGatewayBlockVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_block_volumes_with_options(request, runtime)

    async def delete_gateway_block_volumes_async(
        self,
        request: sgw_20180511_models.DeleteGatewayBlockVolumesRequest,
    ) -> sgw_20180511_models.DeleteGatewayBlockVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_block_volumes_with_options_async(request, runtime)

    def delete_gateway_cache_disk_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewayCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_id):
            query['CacheId'] = request.cache_id
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayCacheDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_cache_disk_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewayCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_id):
            query['CacheId'] = request.cache_id
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayCacheDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_cache_disk(
        self,
        request: sgw_20180511_models.DeleteGatewayCacheDiskRequest,
    ) -> sgw_20180511_models.DeleteGatewayCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_cache_disk_with_options(request, runtime)

    async def delete_gateway_cache_disk_async(
        self,
        request: sgw_20180511_models.DeleteGatewayCacheDiskRequest,
    ) -> sgw_20180511_models.DeleteGatewayCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_cache_disk_with_options_async(request, runtime)

    def delete_gateway_file_shares_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewayFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayFileSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_file_shares_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewayFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayFileSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_file_shares(
        self,
        request: sgw_20180511_models.DeleteGatewayFileSharesRequest,
    ) -> sgw_20180511_models.DeleteGatewayFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_file_shares_with_options(request, runtime)

    async def delete_gateway_file_shares_async(
        self,
        request: sgw_20180511_models.DeleteGatewayFileSharesRequest,
    ) -> sgw_20180511_models.DeleteGatewayFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_file_shares_with_options_async(request, runtime)

    def delete_gateway_logging_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_logging_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewayLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_logging(
        self,
        request: sgw_20180511_models.DeleteGatewayLoggingRequest,
    ) -> sgw_20180511_models.DeleteGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_logging_with_options(request, runtime)

    async def delete_gateway_logging_async(
        self,
        request: sgw_20180511_models.DeleteGatewayLoggingRequest,
    ) -> sgw_20180511_models.DeleteGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_logging_with_options_async(request, runtime)

    def delete_gateway_smbuser_with_options(
        self,
        request: sgw_20180511_models.DeleteGatewaySMBUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewaySMBUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySMBUser',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewaySMBUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_smbuser_with_options_async(
        self,
        request: sgw_20180511_models.DeleteGatewaySMBUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteGatewaySMBUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySMBUser',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteGatewaySMBUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_smbuser(
        self,
        request: sgw_20180511_models.DeleteGatewaySMBUserRequest,
    ) -> sgw_20180511_models.DeleteGatewaySMBUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_smbuser_with_options(request, runtime)

    async def delete_gateway_smbuser_async(
        self,
        request: sgw_20180511_models.DeleteGatewaySMBUserRequest,
    ) -> sgw_20180511_models.DeleteGatewaySMBUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_smbuser_with_options_async(request, runtime)

    def delete_storage_bundle_with_options(
        self,
        request: sgw_20180511_models.DeleteStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteStorageBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_storage_bundle_with_options_async(
        self,
        request: sgw_20180511_models.DeleteStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeleteStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeleteStorageBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_storage_bundle(
        self,
        request: sgw_20180511_models.DeleteStorageBundleRequest,
    ) -> sgw_20180511_models.DeleteStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_storage_bundle_with_options(request, runtime)

    async def delete_storage_bundle_async(
        self,
        request: sgw_20180511_models.DeleteStorageBundleRequest,
    ) -> sgw_20180511_models.DeleteStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_storage_bundle_with_options_async(request, runtime)

    def deploy_csgclients_with_options(
        self,
        tmp_req: sgw_20180511_models.DeployCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployCSGClientsResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.DeployCSGClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecs_instance_ids):
            request.ecs_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecs_instance_ids, 'EcsInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.ecs_instance_ids_shrink):
            query['EcsInstanceIds'] = request.ecs_instance_ids_shrink
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployCSGClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_csgclients_with_options_async(
        self,
        tmp_req: sgw_20180511_models.DeployCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployCSGClientsResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.DeployCSGClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecs_instance_ids):
            request.ecs_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecs_instance_ids, 'EcsInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.ecs_instance_ids_shrink):
            query['EcsInstanceIds'] = request.ecs_instance_ids_shrink
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployCSGClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_csgclients(
        self,
        request: sgw_20180511_models.DeployCSGClientsRequest,
    ) -> sgw_20180511_models.DeployCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_csgclients_with_options(request, runtime)

    async def deploy_csgclients_async(
        self,
        request: sgw_20180511_models.DeployCSGClientsRequest,
    ) -> sgw_20180511_models.DeployCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_csgclients_with_options_async(request, runtime)

    def deploy_cache_disk_with_options(
        self,
        request: sgw_20180511_models.DeployCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployCacheDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_cache_disk_with_options_async(
        self,
        request: sgw_20180511_models.DeployCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployCacheDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_cache_disk(
        self,
        request: sgw_20180511_models.DeployCacheDiskRequest,
    ) -> sgw_20180511_models.DeployCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_cache_disk_with_options(request, runtime)

    async def deploy_cache_disk_async(
        self,
        request: sgw_20180511_models.DeployCacheDiskRequest,
    ) -> sgw_20180511_models.DeployCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_cache_disk_with_options_async(request, runtime)

    def deploy_gateway_with_options(
        self,
        request: sgw_20180511_models.DeployGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_gateway_with_options_async(
        self,
        request: sgw_20180511_models.DeployGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DeployGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DeployGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_gateway(
        self,
        request: sgw_20180511_models.DeployGatewayRequest,
    ) -> sgw_20180511_models.DeployGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_gateway_with_options(request, runtime)

    async def deploy_gateway_async(
        self,
        request: sgw_20180511_models.DeployGatewayRequest,
    ) -> sgw_20180511_models.DeployGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_gateway_with_options_async(request, runtime)

    def describe_account_config_with_options(
        self,
        request: sgw_20180511_models.DescribeAccountConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeAccountConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeAccountConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_config_with_options_async(
        self,
        request: sgw_20180511_models.DescribeAccountConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeAccountConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeAccountConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_config(
        self,
        request: sgw_20180511_models.DescribeAccountConfigRequest,
    ) -> sgw_20180511_models.DescribeAccountConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_config_with_options(request, runtime)

    async def describe_account_config_async(
        self,
        request: sgw_20180511_models.DescribeAccountConfigRequest,
    ) -> sgw_20180511_models.DescribeAccountConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_config_with_options_async(request, runtime)

    def describe_block_volume_snapshots_with_options(
        self,
        request: sgw_20180511_models.DescribeBlockVolumeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockVolumeSnapshots',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_block_volume_snapshots_with_options_async(
        self,
        request: sgw_20180511_models.DescribeBlockVolumeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockVolumeSnapshots',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_block_volume_snapshots(
        self,
        request: sgw_20180511_models.DescribeBlockVolumeSnapshotsRequest,
    ) -> sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_block_volume_snapshots_with_options(request, runtime)

    async def describe_block_volume_snapshots_async(
        self,
        request: sgw_20180511_models.DescribeBlockVolumeSnapshotsRequest,
    ) -> sgw_20180511_models.DescribeBlockVolumeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_block_volume_snapshots_with_options_async(request, runtime)

    def describe_csgclient_tasks_with_options(
        self,
        request: sgw_20180511_models.DescribeCSGClientTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeCSGClientTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSGClientTasks',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeCSGClientTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_csgclient_tasks_with_options_async(
        self,
        request: sgw_20180511_models.DescribeCSGClientTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeCSGClientTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSGClientTasks',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeCSGClientTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_csgclient_tasks(
        self,
        request: sgw_20180511_models.DescribeCSGClientTasksRequest,
    ) -> sgw_20180511_models.DescribeCSGClientTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_csgclient_tasks_with_options(request, runtime)

    async def describe_csgclient_tasks_async(
        self,
        request: sgw_20180511_models.DescribeCSGClientTasksRequest,
    ) -> sgw_20180511_models.DescribeCSGClientTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_csgclient_tasks_with_options_async(request, runtime)

    def describe_csgclients_with_options(
        self,
        request: sgw_20180511_models.DescribeCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeCSGClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeCSGClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_csgclients_with_options_async(
        self,
        request: sgw_20180511_models.DescribeCSGClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeCSGClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSGClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeCSGClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_csgclients(
        self,
        request: sgw_20180511_models.DescribeCSGClientsRequest,
    ) -> sgw_20180511_models.DescribeCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_csgclients_with_options(request, runtime)

    async def describe_csgclients_async(
        self,
        request: sgw_20180511_models.DescribeCSGClientsRequest,
    ) -> sgw_20180511_models.DescribeCSGClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_csgclients_with_options_async(request, runtime)

    def describe_dashboard_with_options(
        self,
        request: sgw_20180511_models.DescribeDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeDashboardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboard',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_with_options_async(
        self,
        request: sgw_20180511_models.DescribeDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeDashboardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboard',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard(
        self,
        request: sgw_20180511_models.DescribeDashboardRequest,
    ) -> sgw_20180511_models.DescribeDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_with_options(request, runtime)

    async def describe_dashboard_async(
        self,
        request: sgw_20180511_models.DescribeDashboardRequest,
    ) -> sgw_20180511_models.DescribeDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_with_options_async(request, runtime)

    def describe_expire_caches_with_options(
        self,
        request: sgw_20180511_models.DescribeExpireCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpireCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpireCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpireCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expire_caches_with_options_async(
        self,
        request: sgw_20180511_models.DescribeExpireCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpireCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpireCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpireCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expire_caches(
        self,
        request: sgw_20180511_models.DescribeExpireCachesRequest,
    ) -> sgw_20180511_models.DescribeExpireCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_expire_caches_with_options(request, runtime)

    async def describe_expire_caches_async(
        self,
        request: sgw_20180511_models.DescribeExpireCachesRequest,
    ) -> sgw_20180511_models.DescribeExpireCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_expire_caches_with_options_async(request, runtime)

    def describe_express_sync_shares_with_options(
        self,
        request: sgw_20180511_models.DescribeExpressSyncSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpressSyncSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_ids):
            query['ExpressSyncIds'] = request.express_sync_ids
        if not UtilClient.is_unset(request.is_external):
            query['IsExternal'] = request.is_external
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressSyncShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpressSyncSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_sync_shares_with_options_async(
        self,
        request: sgw_20180511_models.DescribeExpressSyncSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpressSyncSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_ids):
            query['ExpressSyncIds'] = request.express_sync_ids
        if not UtilClient.is_unset(request.is_external):
            query['IsExternal'] = request.is_external
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressSyncShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpressSyncSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_sync_shares(
        self,
        request: sgw_20180511_models.DescribeExpressSyncSharesRequest,
    ) -> sgw_20180511_models.DescribeExpressSyncSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_express_sync_shares_with_options(request, runtime)

    async def describe_express_sync_shares_async(
        self,
        request: sgw_20180511_models.DescribeExpressSyncSharesRequest,
    ) -> sgw_20180511_models.DescribeExpressSyncSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_express_sync_shares_with_options_async(request, runtime)

    def describe_express_syncs_with_options(
        self,
        request: sgw_20180511_models.DescribeExpressSyncsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpressSyncsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressSyncs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpressSyncsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_syncs_with_options_async(
        self,
        request: sgw_20180511_models.DescribeExpressSyncsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeExpressSyncsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressSyncs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeExpressSyncsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_syncs(
        self,
        request: sgw_20180511_models.DescribeExpressSyncsRequest,
    ) -> sgw_20180511_models.DescribeExpressSyncsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_express_syncs_with_options(request, runtime)

    async def describe_express_syncs_async(
        self,
        request: sgw_20180511_models.DescribeExpressSyncsRequest,
    ) -> sgw_20180511_models.DescribeExpressSyncsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_express_syncs_with_options_async(request, runtime)

    def describe_gateway_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway(
        self,
        request: sgw_20180511_models.DescribeGatewayRequest,
    ) -> sgw_20180511_models.DescribeGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_with_options(request, runtime)

    async def describe_gateway_async(
        self,
        request: sgw_20180511_models.DescribeGatewayRequest,
    ) -> sgw_20180511_models.DescribeGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_with_options_async(request, runtime)

    def describe_gateway_adinfo_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayADInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayADInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayADInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayADInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_adinfo_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayADInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayADInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayADInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayADInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_adinfo(
        self,
        request: sgw_20180511_models.DescribeGatewayADInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayADInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_adinfo_with_options(request, runtime)

    async def describe_gateway_adinfo_async(
        self,
        request: sgw_20180511_models.DescribeGatewayADInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayADInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_adinfo_with_options_async(request, runtime)

    def describe_gateway_actions_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayActionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayActions',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_actions_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayActionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayActions',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_actions(
        self,
        request: sgw_20180511_models.DescribeGatewayActionsRequest,
    ) -> sgw_20180511_models.DescribeGatewayActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_actions_with_options(request, runtime)

    async def describe_gateway_actions_async(
        self,
        request: sgw_20180511_models.DescribeGatewayActionsRequest,
    ) -> sgw_20180511_models.DescribeGatewayActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_actions_with_options_async(request, runtime)

    def describe_gateway_auth_info_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAuthInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAuthInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_auth_info_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAuthInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAuthInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_auth_info(
        self,
        request: sgw_20180511_models.DescribeGatewayAuthInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_auth_info_with_options(request, runtime)

    async def describe_gateway_auth_info_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAuthInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_auth_info_with_options_async(request, runtime)

    def describe_gateway_auto_plans_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAutoPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAutoPlans',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAutoPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_auto_plans_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAutoPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAutoPlans',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAutoPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_auto_plans(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoPlansRequest,
    ) -> sgw_20180511_models.DescribeGatewayAutoPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_auto_plans_with_options(request, runtime)

    async def describe_gateway_auto_plans_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoPlansRequest,
    ) -> sgw_20180511_models.DescribeGatewayAutoPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_auto_plans_with_options_async(request, runtime)

    def describe_gateway_auto_upgrade_configuration_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAutoUpgradeConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_auto_upgrade_configuration_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayAutoUpgradeConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_auto_upgrade_configuration(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationRequest,
    ) -> sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_auto_upgrade_configuration_with_options(request, runtime)

    async def describe_gateway_auto_upgrade_configuration_async(
        self,
        request: sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationRequest,
    ) -> sgw_20180511_models.DescribeGatewayAutoUpgradeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_auto_upgrade_configuration_with_options_async(request, runtime)

    def describe_gateway_block_volumes_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayBlockVolumesResponse:
        """
        ***\
        
        @param request: DescribeGatewayBlockVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewayBlockVolumesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayBlockVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_block_volumes_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayBlockVolumesResponse:
        """
        ***\
        
        @param request: DescribeGatewayBlockVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewayBlockVolumesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayBlockVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_block_volumes(
        self,
        request: sgw_20180511_models.DescribeGatewayBlockVolumesRequest,
    ) -> sgw_20180511_models.DescribeGatewayBlockVolumesResponse:
        """
        ***\
        
        @param request: DescribeGatewayBlockVolumesRequest
        @return: DescribeGatewayBlockVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_block_volumes_with_options(request, runtime)

    async def describe_gateway_block_volumes_async(
        self,
        request: sgw_20180511_models.DescribeGatewayBlockVolumesRequest,
    ) -> sgw_20180511_models.DescribeGatewayBlockVolumesResponse:
        """
        ***\
        
        @param request: DescribeGatewayBlockVolumesRequest
        @return: DescribeGatewayBlockVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_block_volumes_with_options_async(request, runtime)

    def describe_gateway_bucket_caches_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayBucketCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayBucketCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayBucketCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayBucketCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_bucket_caches_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayBucketCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayBucketCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayBucketCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayBucketCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_bucket_caches(
        self,
        request: sgw_20180511_models.DescribeGatewayBucketCachesRequest,
    ) -> sgw_20180511_models.DescribeGatewayBucketCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_bucket_caches_with_options(request, runtime)

    async def describe_gateway_bucket_caches_async(
        self,
        request: sgw_20180511_models.DescribeGatewayBucketCachesRequest,
    ) -> sgw_20180511_models.DescribeGatewayBucketCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_bucket_caches_with_options_async(request, runtime)

    def describe_gateway_caches_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_caches_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCaches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_caches(
        self,
        request: sgw_20180511_models.DescribeGatewayCachesRequest,
    ) -> sgw_20180511_models.DescribeGatewayCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_caches_with_options(request, runtime)

    async def describe_gateway_caches_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCachesRequest,
    ) -> sgw_20180511_models.DescribeGatewayCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_caches_with_options_async(request, runtime)

    def describe_gateway_capacity_limit_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayCapacityLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCapacityLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCapacityLimit',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCapacityLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_capacity_limit_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCapacityLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCapacityLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size_in_gb):
            query['SizeInGB'] = request.size_in_gb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCapacityLimit',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCapacityLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_capacity_limit(
        self,
        request: sgw_20180511_models.DescribeGatewayCapacityLimitRequest,
    ) -> sgw_20180511_models.DescribeGatewayCapacityLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_capacity_limit_with_options(request, runtime)

    async def describe_gateway_capacity_limit_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCapacityLimitRequest,
    ) -> sgw_20180511_models.DescribeGatewayCapacityLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_capacity_limit_with_options_async(request, runtime)

    def describe_gateway_categories_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCategories',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_categories_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCategories',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_categories(
        self,
        request: sgw_20180511_models.DescribeGatewayCategoriesRequest,
    ) -> sgw_20180511_models.DescribeGatewayCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_categories_with_options(request, runtime)

    async def describe_gateway_categories_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCategoriesRequest,
    ) -> sgw_20180511_models.DescribeGatewayCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_categories_with_options_async(request, runtime)

    def describe_gateway_classes_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayClasses',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_classes_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayClasses',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_classes(
        self,
        request: sgw_20180511_models.DescribeGatewayClassesRequest,
    ) -> sgw_20180511_models.DescribeGatewayClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_classes_with_options(request, runtime)

    async def describe_gateway_classes_async(
        self,
        request: sgw_20180511_models.DescribeGatewayClassesRequest,
    ) -> sgw_20180511_models.DescribeGatewayClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_classes_with_options_async(request, runtime)

    def describe_gateway_credential_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCredential',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_credential_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayCredential',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_credential(
        self,
        request: sgw_20180511_models.DescribeGatewayCredentialRequest,
    ) -> sgw_20180511_models.DescribeGatewayCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_credential_with_options(request, runtime)

    async def describe_gateway_credential_async(
        self,
        request: sgw_20180511_models.DescribeGatewayCredentialRequest,
    ) -> sgw_20180511_models.DescribeGatewayCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_credential_with_options_async(request, runtime)

    def describe_gateway_dnswith_options(
        self,
        request: sgw_20180511_models.DescribeGatewayDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayDNS',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_dnswith_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayDNS',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_dns(
        self,
        request: sgw_20180511_models.DescribeGatewayDNSRequest,
    ) -> sgw_20180511_models.DescribeGatewayDNSResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_dnswith_options(request, runtime)

    async def describe_gateway_dns_async(
        self,
        request: sgw_20180511_models.DescribeGatewayDNSRequest,
    ) -> sgw_20180511_models.DescribeGatewayDNSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_dnswith_options_async(request, runtime)

    def describe_gateway_file_shares_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayFileSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_file_shares_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayFileSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_file_shares(
        self,
        request: sgw_20180511_models.DescribeGatewayFileSharesRequest,
    ) -> sgw_20180511_models.DescribeGatewayFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_file_shares_with_options(request, runtime)

    async def describe_gateway_file_shares_async(
        self,
        request: sgw_20180511_models.DescribeGatewayFileSharesRequest,
    ) -> sgw_20180511_models.DescribeGatewayFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_file_shares_with_options_async(request, runtime)

    def describe_gateway_file_status_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayFileStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayFileStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayFileStatus',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayFileStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_file_status_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayFileStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayFileStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayFileStatus',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayFileStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_file_status(
        self,
        request: sgw_20180511_models.DescribeGatewayFileStatusRequest,
    ) -> sgw_20180511_models.DescribeGatewayFileStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_file_status_with_options(request, runtime)

    async def describe_gateway_file_status_async(
        self,
        request: sgw_20180511_models.DescribeGatewayFileStatusRequest,
    ) -> sgw_20180511_models.DescribeGatewayFileStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_file_status_with_options_async(request, runtime)

    def describe_gateway_images_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayImages',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_images_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayImages',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_images(
        self,
        request: sgw_20180511_models.DescribeGatewayImagesRequest,
    ) -> sgw_20180511_models.DescribeGatewayImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_images_with_options(request, runtime)

    async def describe_gateway_images_async(
        self,
        request: sgw_20180511_models.DescribeGatewayImagesRequest,
    ) -> sgw_20180511_models.DescribeGatewayImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_images_with_options_async(request, runtime)

    def describe_gateway_info_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_info_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_info(
        self,
        request: sgw_20180511_models.DescribeGatewayInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_info_with_options(request, runtime)

    async def describe_gateway_info_async(
        self,
        request: sgw_20180511_models.DescribeGatewayInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_info_with_options_async(request, runtime)

    def describe_gateway_ldapinfo_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayLDAPInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLDAPInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLDAPInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLDAPInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_ldapinfo_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLDAPInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLDAPInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLDAPInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLDAPInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_ldapinfo(
        self,
        request: sgw_20180511_models.DescribeGatewayLDAPInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayLDAPInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_ldapinfo_with_options(request, runtime)

    async def describe_gateway_ldapinfo_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLDAPInfoRequest,
    ) -> sgw_20180511_models.DescribeGatewayLDAPInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_ldapinfo_with_options_async(request, runtime)

    def describe_gateway_locations_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayLocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLocations',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_locations_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLocations',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_locations(
        self,
        request: sgw_20180511_models.DescribeGatewayLocationsRequest,
    ) -> sgw_20180511_models.DescribeGatewayLocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_locations_with_options(request, runtime)

    async def describe_gateway_locations_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLocationsRequest,
    ) -> sgw_20180511_models.DescribeGatewayLocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_locations_with_options_async(request, runtime)

    def describe_gateway_logging_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_logging_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_logging(
        self,
        request: sgw_20180511_models.DescribeGatewayLoggingRequest,
    ) -> sgw_20180511_models.DescribeGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_logging_with_options(request, runtime)

    async def describe_gateway_logging_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLoggingRequest,
    ) -> sgw_20180511_models.DescribeGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_logging_with_options_async(request, runtime)

    def describe_gateway_logs_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.log_file_path):
            query['LogFilePath'] = request.log_file_path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLogs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_logs_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.log_file_path):
            query['LogFilePath'] = request.log_file_path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayLogs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_logs(
        self,
        request: sgw_20180511_models.DescribeGatewayLogsRequest,
    ) -> sgw_20180511_models.DescribeGatewayLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_logs_with_options(request, runtime)

    async def describe_gateway_logs_async(
        self,
        request: sgw_20180511_models.DescribeGatewayLogsRequest,
    ) -> sgw_20180511_models.DescribeGatewayLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_logs_with_options_async(request, runtime)

    def describe_gateway_modification_classes_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayModificationClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayModificationClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayModificationClasses',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayModificationClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_modification_classes_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayModificationClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayModificationClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayModificationClasses',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayModificationClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_modification_classes(
        self,
        request: sgw_20180511_models.DescribeGatewayModificationClassesRequest,
    ) -> sgw_20180511_models.DescribeGatewayModificationClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_modification_classes_with_options(request, runtime)

    async def describe_gateway_modification_classes_async(
        self,
        request: sgw_20180511_models.DescribeGatewayModificationClassesRequest,
    ) -> sgw_20180511_models.DescribeGatewayModificationClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_modification_classes_with_options_async(request, runtime)

    def describe_gateway_nfsclients_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayNFSClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayNFSClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayNFSClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayNFSClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_nfsclients_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayNFSClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayNFSClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayNFSClients',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayNFSClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_nfsclients(
        self,
        request: sgw_20180511_models.DescribeGatewayNFSClientsRequest,
    ) -> sgw_20180511_models.DescribeGatewayNFSClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_nfsclients_with_options(request, runtime)

    async def describe_gateway_nfsclients_async(
        self,
        request: sgw_20180511_models.DescribeGatewayNFSClientsRequest,
    ) -> sgw_20180511_models.DescribeGatewayNFSClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_nfsclients_with_options_async(request, runtime)

    def describe_gateway_smbusers_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewaySMBUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaySMBUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySMBUsers',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaySMBUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_smbusers_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewaySMBUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaySMBUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySMBUsers',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaySMBUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_smbusers(
        self,
        request: sgw_20180511_models.DescribeGatewaySMBUsersRequest,
    ) -> sgw_20180511_models.DescribeGatewaySMBUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_smbusers_with_options(request, runtime)

    async def describe_gateway_smbusers_async(
        self,
        request: sgw_20180511_models.DescribeGatewaySMBUsersRequest,
    ) -> sgw_20180511_models.DescribeGatewaySMBUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_smbusers_with_options_async(request, runtime)

    def describe_gateway_statistics_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.gateway_category):
            query['GatewayCategory'] = request.gateway_category
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.target_account_id):
            query['TargetAccountId'] = request.target_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayStatistics',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_statistics_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.gateway_category):
            query['GatewayCategory'] = request.gateway_category
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.target_account_id):
            query['TargetAccountId'] = request.target_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayStatistics',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_statistics(
        self,
        request: sgw_20180511_models.DescribeGatewayStatisticsRequest,
    ) -> sgw_20180511_models.DescribeGatewayStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_statistics_with_options(request, runtime)

    async def describe_gateway_statistics_async(
        self,
        request: sgw_20180511_models.DescribeGatewayStatisticsRequest,
    ) -> sgw_20180511_models.DescribeGatewayStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_statistics_with_options_async(request, runtime)

    def describe_gateway_stock_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_region_id):
            query['GatewayRegionId'] = request.gateway_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayStock',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_stock_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_region_id):
            query['GatewayRegionId'] = request.gateway_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayStock',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_stock(
        self,
        request: sgw_20180511_models.DescribeGatewayStockRequest,
    ) -> sgw_20180511_models.DescribeGatewayStockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_stock_with_options(request, runtime)

    async def describe_gateway_stock_async(
        self,
        request: sgw_20180511_models.DescribeGatewayStockRequest,
    ) -> sgw_20180511_models.DescribeGatewayStockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_stock_with_options_async(request, runtime)

    def describe_gateway_types_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewayTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayTypes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_types_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewayTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewayTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_location):
            query['GatewayLocation'] = request.gateway_location
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewayTypes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewayTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_types(
        self,
        request: sgw_20180511_models.DescribeGatewayTypesRequest,
    ) -> sgw_20180511_models.DescribeGatewayTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_types_with_options(request, runtime)

    async def describe_gateway_types_async(
        self,
        request: sgw_20180511_models.DescribeGatewayTypesRequest,
    ) -> sgw_20180511_models.DescribeGatewayTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_types_with_options_async(request, runtime)

    def describe_gateways_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGateways',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateways_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGateways',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateways(
        self,
        request: sgw_20180511_models.DescribeGatewaysRequest,
    ) -> sgw_20180511_models.DescribeGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateways_with_options(request, runtime)

    async def describe_gateways_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysRequest,
    ) -> sgw_20180511_models.DescribeGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateways_with_options_async(request, runtime)

    def describe_gateways_for_cms_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewaysForCmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysForCmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_region_id):
            query['GatewayRegionId'] = request.gateway_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaysForCms',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysForCmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateways_for_cms_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysForCmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysForCmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_region_id):
            query['GatewayRegionId'] = request.gateway_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaysForCms',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysForCmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateways_for_cms(
        self,
        request: sgw_20180511_models.DescribeGatewaysForCmsRequest,
    ) -> sgw_20180511_models.DescribeGatewaysForCmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateways_for_cms_with_options(request, runtime)

    async def describe_gateways_for_cms_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysForCmsRequest,
    ) -> sgw_20180511_models.DescribeGatewaysForCmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateways_for_cms_with_options_async(request, runtime)

    def describe_gateways_tags_with_options(
        self,
        request: sgw_20180511_models.DescribeGatewaysTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_ids):
            query['GatewayIds'] = request.gateway_ids
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.tag_category):
            query['TagCategory'] = request.tag_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaysTags',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateways_tags_with_options_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeGatewaysTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_ids):
            query['GatewayIds'] = request.gateway_ids
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.tag_category):
            query['TagCategory'] = request.tag_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGatewaysTags',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeGatewaysTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateways_tags(
        self,
        request: sgw_20180511_models.DescribeGatewaysTagsRequest,
    ) -> sgw_20180511_models.DescribeGatewaysTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateways_tags_with_options(request, runtime)

    async def describe_gateways_tags_async(
        self,
        request: sgw_20180511_models.DescribeGatewaysTagsRequest,
    ) -> sgw_20180511_models.DescribeGatewaysTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateways_tags_with_options_async(request, runtime)

    def describe_kms_key_with_options(
        self,
        request: sgw_20180511_models.DescribeKmsKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeKmsKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.kms_key):
            query['KmsKey'] = request.kms_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKey',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeKmsKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_key_with_options_async(
        self,
        request: sgw_20180511_models.DescribeKmsKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeKmsKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.kms_key):
            query['KmsKey'] = request.kms_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKey',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeKmsKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_key(
        self,
        request: sgw_20180511_models.DescribeKmsKeyRequest,
    ) -> sgw_20180511_models.DescribeKmsKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_kms_key_with_options(request, runtime)

    async def describe_kms_key_async(
        self,
        request: sgw_20180511_models.DescribeKmsKeyRequest,
    ) -> sgw_20180511_models.DescribeKmsKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_kms_key_with_options_async(request, runtime)

    def describe_mqtt_config_with_options(
        self,
        request: sgw_20180511_models.DescribeMqttConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeMqttConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMqttConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeMqttConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mqtt_config_with_options_async(
        self,
        request: sgw_20180511_models.DescribeMqttConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeMqttConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMqttConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeMqttConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mqtt_config(
        self,
        request: sgw_20180511_models.DescribeMqttConfigRequest,
    ) -> sgw_20180511_models.DescribeMqttConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_config_with_options(request, runtime)

    async def describe_mqtt_config_async(
        self,
        request: sgw_20180511_models.DescribeMqttConfigRequest,
    ) -> sgw_20180511_models.DescribeMqttConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mqtt_config_with_options_async(request, runtime)

    def describe_oss_bucket_info_with_options(
        self,
        request: sgw_20180511_models.DescribeOssBucketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeOssBucketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeOssBucketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_bucket_info_with_options_async(
        self,
        request: sgw_20180511_models.DescribeOssBucketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeOssBucketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeOssBucketInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_bucket_info(
        self,
        request: sgw_20180511_models.DescribeOssBucketInfoRequest,
    ) -> sgw_20180511_models.DescribeOssBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_bucket_info_with_options(request, runtime)

    async def describe_oss_bucket_info_async(
        self,
        request: sgw_20180511_models.DescribeOssBucketInfoRequest,
    ) -> sgw_20180511_models.DescribeOssBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_bucket_info_with_options_async(request, runtime)

    def describe_oss_buckets_with_options(
        self,
        request: sgw_20180511_models.DescribeOssBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeOssBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBuckets',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeOssBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_buckets_with_options_async(
        self,
        request: sgw_20180511_models.DescribeOssBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeOssBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_endpoint):
            query['BucketEndpoint'] = request.bucket_endpoint
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBuckets',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeOssBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_buckets(
        self,
        request: sgw_20180511_models.DescribeOssBucketsRequest,
    ) -> sgw_20180511_models.DescribeOssBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_buckets_with_options(request, runtime)

    async def describe_oss_buckets_async(
        self,
        request: sgw_20180511_models.DescribeOssBucketsRequest,
    ) -> sgw_20180511_models.DescribeOssBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_buckets_with_options_async(request, runtime)

    def describe_pay_as_you_go_price_with_options(
        self,
        request: sgw_20180511_models.DescribePayAsYouGoPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribePayAsYouGoPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePayAsYouGoPrice',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribePayAsYouGoPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pay_as_you_go_price_with_options_async(
        self,
        request: sgw_20180511_models.DescribePayAsYouGoPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribePayAsYouGoPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePayAsYouGoPrice',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribePayAsYouGoPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pay_as_you_go_price(
        self,
        request: sgw_20180511_models.DescribePayAsYouGoPriceRequest,
    ) -> sgw_20180511_models.DescribePayAsYouGoPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pay_as_you_go_price_with_options(request, runtime)

    async def describe_pay_as_you_go_price_async(
        self,
        request: sgw_20180511_models.DescribePayAsYouGoPriceRequest,
    ) -> sgw_20180511_models.DescribePayAsYouGoPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pay_as_you_go_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: sgw_20180511_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: sgw_20180511_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: sgw_20180511_models.DescribeRegionsRequest,
    ) -> sgw_20180511_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: sgw_20180511_models.DescribeRegionsRequest,
    ) -> sgw_20180511_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_shares_bucket_info_for_express_sync_with_options(
        self,
        request: sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSharesBucketInfoForExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_shares_bucket_info_for_express_sync_with_options_async(
        self,
        request: sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSharesBucketInfoForExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_shares_bucket_info_for_express_sync(
        self,
        request: sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncRequest,
    ) -> sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shares_bucket_info_for_express_sync_with_options(request, runtime)

    async def describe_shares_bucket_info_for_express_sync_async(
        self,
        request: sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncRequest,
    ) -> sgw_20180511_models.DescribeSharesBucketInfoForExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shares_bucket_info_for_express_sync_with_options_async(request, runtime)

    def describe_storage_bundle_with_options(
        self,
        request: sgw_20180511_models.DescribeStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeStorageBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_bundle_with_options_async(
        self,
        request: sgw_20180511_models.DescribeStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeStorageBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_bundle(
        self,
        request: sgw_20180511_models.DescribeStorageBundleRequest,
    ) -> sgw_20180511_models.DescribeStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_bundle_with_options(request, runtime)

    async def describe_storage_bundle_async(
        self,
        request: sgw_20180511_models.DescribeStorageBundleRequest,
    ) -> sgw_20180511_models.DescribeStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_bundle_with_options_async(request, runtime)

    def describe_storage_bundles_with_options(
        self,
        request: sgw_20180511_models.DescribeStorageBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeStorageBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageBundles',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeStorageBundlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_bundles_with_options_async(
        self,
        request: sgw_20180511_models.DescribeStorageBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeStorageBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_bucket_region_id):
            query['BackendBucketRegionId'] = request.backend_bucket_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageBundles',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeStorageBundlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_bundles(
        self,
        request: sgw_20180511_models.DescribeStorageBundlesRequest,
    ) -> sgw_20180511_models.DescribeStorageBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_bundles_with_options(request, runtime)

    async def describe_storage_bundles_async(
        self,
        request: sgw_20180511_models.DescribeStorageBundlesRequest,
    ) -> sgw_20180511_models.DescribeStorageBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_bundles_with_options_async(request, runtime)

    def describe_subscription_price_with_options(
        self,
        request: sgw_20180511_models.DescribeSubscriptionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeSubscriptionPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_cloud_efficiency_size):
            query['CacheCloudEfficiencySize'] = request.cache_cloud_efficiency_size
        if not UtilClient.is_unset(request.cache_essdpl_1size):
            query['CacheESSDPl1Size'] = request.cache_essdpl_1size
        if not UtilClient.is_unset(request.cache_ssdsize):
            query['CacheSSDSize'] = request.cache_ssdsize
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.period_quantity):
            query['PeriodQuantity'] = request.period_quantity
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionPrice',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeSubscriptionPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_price_with_options_async(
        self,
        request: sgw_20180511_models.DescribeSubscriptionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeSubscriptionPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_cloud_efficiency_size):
            query['CacheCloudEfficiencySize'] = request.cache_cloud_efficiency_size
        if not UtilClient.is_unset(request.cache_essdpl_1size):
            query['CacheESSDPl1Size'] = request.cache_essdpl_1size
        if not UtilClient.is_unset(request.cache_ssdsize):
            query['CacheSSDSize'] = request.cache_ssdsize
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.period_quantity):
            query['PeriodQuantity'] = request.period_quantity
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionPrice',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeSubscriptionPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_price(
        self,
        request: sgw_20180511_models.DescribeSubscriptionPriceRequest,
    ) -> sgw_20180511_models.DescribeSubscriptionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_price_with_options(request, runtime)

    async def describe_subscription_price_async(
        self,
        request: sgw_20180511_models.DescribeSubscriptionPriceRequest,
    ) -> sgw_20180511_models.DescribeSubscriptionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_price_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: sgw_20180511_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: sgw_20180511_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: sgw_20180511_models.DescribeTasksRequest,
    ) -> sgw_20180511_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: sgw_20180511_models.DescribeTasksRequest,
    ) -> sgw_20180511_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_business_status_with_options(
        self,
        request: sgw_20180511_models.DescribeUserBusinessStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeUserBusinessStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBusinessStatus',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeUserBusinessStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_business_status_with_options_async(
        self,
        request: sgw_20180511_models.DescribeUserBusinessStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeUserBusinessStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBusinessStatus',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeUserBusinessStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_business_status(
        self,
        request: sgw_20180511_models.DescribeUserBusinessStatusRequest,
    ) -> sgw_20180511_models.DescribeUserBusinessStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_status_with_options(request, runtime)

    async def describe_user_business_status_async(
        self,
        request: sgw_20180511_models.DescribeUserBusinessStatusRequest,
    ) -> sgw_20180511_models.DescribeUserBusinessStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_business_status_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: sgw_20180511_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: sgw_20180511_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: sgw_20180511_models.DescribeVSwitchesRequest,
    ) -> sgw_20180511_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: sgw_20180511_models.DescribeVSwitchesRequest,
    ) -> sgw_20180511_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: sgw_20180511_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: sgw_20180511_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: sgw_20180511_models.DescribeVpcsRequest,
    ) -> sgw_20180511_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: sgw_20180511_models.DescribeVpcsRequest,
    ) -> sgw_20180511_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: sgw_20180511_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: sgw_20180511_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: sgw_20180511_models.DescribeZonesRequest,
    ) -> sgw_20180511_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: sgw_20180511_models.DescribeZonesRequest,
    ) -> sgw_20180511_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def disable_gateway_logging_with_options(
        self,
        request: sgw_20180511_models.DisableGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DisableGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DisableGatewayLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_gateway_logging_with_options_async(
        self,
        request: sgw_20180511_models.DisableGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DisableGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DisableGatewayLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_gateway_logging(
        self,
        request: sgw_20180511_models.DisableGatewayLoggingRequest,
    ) -> sgw_20180511_models.DisableGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_gateway_logging_with_options(request, runtime)

    async def disable_gateway_logging_async(
        self,
        request: sgw_20180511_models.DisableGatewayLoggingRequest,
    ) -> sgw_20180511_models.DisableGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_gateway_logging_with_options_async(request, runtime)

    def disable_gateway_nfsversion_with_options(
        self,
        request: sgw_20180511_models.DisableGatewayNFSVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DisableGatewayNFSVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.nfsversion):
            query['NFSVersion'] = request.nfsversion
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableGatewayNFSVersion',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DisableGatewayNFSVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_gateway_nfsversion_with_options_async(
        self,
        request: sgw_20180511_models.DisableGatewayNFSVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.DisableGatewayNFSVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.nfsversion):
            query['NFSVersion'] = request.nfsversion
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableGatewayNFSVersion',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.DisableGatewayNFSVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_gateway_nfsversion(
        self,
        request: sgw_20180511_models.DisableGatewayNFSVersionRequest,
    ) -> sgw_20180511_models.DisableGatewayNFSVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_gateway_nfsversion_with_options(request, runtime)

    async def disable_gateway_nfsversion_async(
        self,
        request: sgw_20180511_models.DisableGatewayNFSVersionRequest,
    ) -> sgw_20180511_models.DisableGatewayNFSVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_gateway_nfsversion_with_options_async(request, runtime)

    def enable_gateway_ipv_6with_options(
        self,
        request: sgw_20180511_models.EnableGatewayIpv6Request,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.EnableGatewayIpv6Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGatewayIpv6',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.EnableGatewayIpv6Response(),
            self.call_api(params, req, runtime)
        )

    async def enable_gateway_ipv_6with_options_async(
        self,
        request: sgw_20180511_models.EnableGatewayIpv6Request,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.EnableGatewayIpv6Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGatewayIpv6',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.EnableGatewayIpv6Response(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_gateway_ipv_6(
        self,
        request: sgw_20180511_models.EnableGatewayIpv6Request,
    ) -> sgw_20180511_models.EnableGatewayIpv6Response:
        runtime = util_models.RuntimeOptions()
        return self.enable_gateway_ipv_6with_options(request, runtime)

    async def enable_gateway_ipv_6_async(
        self,
        request: sgw_20180511_models.EnableGatewayIpv6Request,
    ) -> sgw_20180511_models.EnableGatewayIpv6Response:
        runtime = util_models.RuntimeOptions()
        return await self.enable_gateway_ipv_6with_options_async(request, runtime)

    def enable_gateway_logging_with_options(
        self,
        request: sgw_20180511_models.EnableGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.EnableGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.EnableGatewayLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_gateway_logging_with_options_async(
        self,
        request: sgw_20180511_models.EnableGatewayLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.EnableGatewayLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGatewayLogging',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.EnableGatewayLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_gateway_logging(
        self,
        request: sgw_20180511_models.EnableGatewayLoggingRequest,
    ) -> sgw_20180511_models.EnableGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_gateway_logging_with_options(request, runtime)

    async def enable_gateway_logging_async(
        self,
        request: sgw_20180511_models.EnableGatewayLoggingRequest,
    ) -> sgw_20180511_models.EnableGatewayLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_gateway_logging_with_options_async(request, runtime)

    def expand_cache_disk_with_options(
        self,
        request: sgw_20180511_models.ExpandCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.new_size_in_gb):
            query['NewSizeInGB'] = request.new_size_in_gb
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandCacheDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_cache_disk_with_options_async(
        self,
        request: sgw_20180511_models.ExpandCacheDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandCacheDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.local_file_path):
            query['LocalFilePath'] = request.local_file_path
        if not UtilClient.is_unset(request.new_size_in_gb):
            query['NewSizeInGB'] = request.new_size_in_gb
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandCacheDisk',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandCacheDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_cache_disk(
        self,
        request: sgw_20180511_models.ExpandCacheDiskRequest,
    ) -> sgw_20180511_models.ExpandCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.expand_cache_disk_with_options(request, runtime)

    async def expand_cache_disk_async(
        self,
        request: sgw_20180511_models.ExpandCacheDiskRequest,
    ) -> sgw_20180511_models.ExpandCacheDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.expand_cache_disk_with_options_async(request, runtime)

    def expand_gateway_file_share_with_options(
        self,
        request: sgw_20180511_models.ExpandGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandGatewayFileShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_gateway_file_share_with_options_async(
        self,
        request: sgw_20180511_models.ExpandGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandGatewayFileShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_gateway_file_share(
        self,
        request: sgw_20180511_models.ExpandGatewayFileShareRequest,
    ) -> sgw_20180511_models.ExpandGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.expand_gateway_file_share_with_options(request, runtime)

    async def expand_gateway_file_share_async(
        self,
        request: sgw_20180511_models.ExpandGatewayFileShareRequest,
    ) -> sgw_20180511_models.ExpandGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.expand_gateway_file_share_with_options_async(request, runtime)

    def expand_gateway_network_bandwidth_with_options(
        self,
        request: sgw_20180511_models.ExpandGatewayNetworkBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.new_network_bandwidth):
            query['NewNetworkBandwidth'] = request.new_network_bandwidth
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandGatewayNetworkBandwidth',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_gateway_network_bandwidth_with_options_async(
        self,
        request: sgw_20180511_models.ExpandGatewayNetworkBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.new_network_bandwidth):
            query['NewNetworkBandwidth'] = request.new_network_bandwidth
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandGatewayNetworkBandwidth',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_gateway_network_bandwidth(
        self,
        request: sgw_20180511_models.ExpandGatewayNetworkBandwidthRequest,
    ) -> sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.expand_gateway_network_bandwidth_with_options(request, runtime)

    async def expand_gateway_network_bandwidth_async(
        self,
        request: sgw_20180511_models.ExpandGatewayNetworkBandwidthRequest,
    ) -> sgw_20180511_models.ExpandGatewayNetworkBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.expand_gateway_network_bandwidth_with_options_async(request, runtime)

    def generate_gateway_token_with_options(
        self,
        request: sgw_20180511_models.GenerateGatewayTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateGatewayTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateGatewayToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateGatewayTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_gateway_token_with_options_async(
        self,
        request: sgw_20180511_models.GenerateGatewayTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateGatewayTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateGatewayToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateGatewayTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_gateway_token(
        self,
        request: sgw_20180511_models.GenerateGatewayTokenRequest,
    ) -> sgw_20180511_models.GenerateGatewayTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_gateway_token_with_options(request, runtime)

    async def generate_gateway_token_async(
        self,
        request: sgw_20180511_models.GenerateGatewayTokenRequest,
    ) -> sgw_20180511_models.GenerateGatewayTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_gateway_token_with_options_async(request, runtime)

    def generate_mqtt_token_with_options(
        self,
        request: sgw_20180511_models.GenerateMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateMqttToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateMqttTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_mqtt_token_with_options_async(
        self,
        request: sgw_20180511_models.GenerateMqttTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateMqttTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateMqttToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateMqttTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_mqtt_token(
        self,
        request: sgw_20180511_models.GenerateMqttTokenRequest,
    ) -> sgw_20180511_models.GenerateMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_mqtt_token_with_options(request, runtime)

    async def generate_mqtt_token_async(
        self,
        request: sgw_20180511_models.GenerateMqttTokenRequest,
    ) -> sgw_20180511_models.GenerateMqttTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_mqtt_token_with_options_async(request, runtime)

    def generate_sts_token_with_options(
        self,
        request: sgw_20180511_models.GenerateStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_in_seconds):
            query['ExpireInSeconds'] = request.expire_in_seconds
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateStsToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_sts_token_with_options_async(
        self,
        request: sgw_20180511_models.GenerateStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.GenerateStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_in_seconds):
            query['ExpireInSeconds'] = request.expire_in_seconds
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateStsToken',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.GenerateStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_sts_token(
        self,
        request: sgw_20180511_models.GenerateStsTokenRequest,
    ) -> sgw_20180511_models.GenerateStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_sts_token_with_options(request, runtime)

    async def generate_sts_token_async(
        self,
        request: sgw_20180511_models.GenerateStsTokenRequest,
    ) -> sgw_20180511_models.GenerateStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_sts_token_with_options_async(request, runtime)

    def handle_gateway_auto_plan_with_options(
        self,
        request: sgw_20180511_models.HandleGatewayAutoPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.HandleGatewayAutoPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel):
            query['Cancel'] = request.cancel
        if not UtilClient.is_unset(request.delay_hours):
            query['DelayHours'] = request.delay_hours
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleGatewayAutoPlan',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.HandleGatewayAutoPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_gateway_auto_plan_with_options_async(
        self,
        request: sgw_20180511_models.HandleGatewayAutoPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.HandleGatewayAutoPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel):
            query['Cancel'] = request.cancel
        if not UtilClient.is_unset(request.delay_hours):
            query['DelayHours'] = request.delay_hours
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleGatewayAutoPlan',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.HandleGatewayAutoPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_gateway_auto_plan(
        self,
        request: sgw_20180511_models.HandleGatewayAutoPlanRequest,
    ) -> sgw_20180511_models.HandleGatewayAutoPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_gateway_auto_plan_with_options(request, runtime)

    async def handle_gateway_auto_plan_async(
        self,
        request: sgw_20180511_models.HandleGatewayAutoPlanRequest,
    ) -> sgw_20180511_models.HandleGatewayAutoPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_gateway_auto_plan_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: sgw_20180511_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: sgw_20180511_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: sgw_20180511_models.ListTagResourcesRequest,
    ) -> sgw_20180511_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: sgw_20180511_models.ListTagResourcesRequest,
    ) -> sgw_20180511_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_gateway_with_options(
        self,
        request: sgw_20180511_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_with_options_async(
        self,
        request: sgw_20180511_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway(
        self,
        request: sgw_20180511_models.ModifyGatewayRequest,
    ) -> sgw_20180511_models.ModifyGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_with_options(request, runtime)

    async def modify_gateway_async(
        self,
        request: sgw_20180511_models.ModifyGatewayRequest,
    ) -> sgw_20180511_models.ModifyGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_with_options_async(request, runtime)

    def modify_gateway_block_volume_with_options(
        self,
        request: sgw_20180511_models.ModifyGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayBlockVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_block_volume_with_options_async(
        self,
        request: sgw_20180511_models.ModifyGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayBlockVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway_block_volume(
        self,
        request: sgw_20180511_models.ModifyGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.ModifyGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_block_volume_with_options(request, runtime)

    async def modify_gateway_block_volume_async(
        self,
        request: sgw_20180511_models.ModifyGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.ModifyGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_block_volume_with_options_async(request, runtime)

    def modify_gateway_class_with_options(
        self,
        request: sgw_20180511_models.ModifyGatewayClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayClass',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_class_with_options_async(
        self,
        request: sgw_20180511_models.ModifyGatewayClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_class):
            query['GatewayClass'] = request.gateway_class
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayClass',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway_class(
        self,
        request: sgw_20180511_models.ModifyGatewayClassRequest,
    ) -> sgw_20180511_models.ModifyGatewayClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_class_with_options(request, runtime)

    async def modify_gateway_class_async(
        self,
        request: sgw_20180511_models.ModifyGatewayClassRequest,
    ) -> sgw_20180511_models.ModifyGatewayClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_class_with_options_async(request, runtime)

    def modify_gateway_file_share_with_options(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayFileShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_file_share_with_options_async(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_config):
            query['CacheConfig'] = request.cache_config
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayFileShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway_file_share(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareRequest,
    ) -> sgw_20180511_models.ModifyGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_file_share_with_options(request, runtime)

    async def modify_gateway_file_share_async(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareRequest,
    ) -> sgw_20180511_models.ModifyGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_file_share_with_options_async(request, runtime)

    def modify_gateway_file_share_watermark_with_options(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayFileShareWatermark',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_file_share_watermark_with_options_async(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGatewayFileShareWatermark',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway_file_share_watermark(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareWatermarkRequest,
    ) -> sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_file_share_watermark_with_options(request, runtime)

    async def modify_gateway_file_share_watermark_async(
        self,
        request: sgw_20180511_models.ModifyGatewayFileShareWatermarkRequest,
    ) -> sgw_20180511_models.ModifyGatewayFileShareWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_file_share_watermark_with_options_async(request, runtime)

    def modify_storage_bundle_with_options(
        self,
        request: sgw_20180511_models.ModifyStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyStorageBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_storage_bundle_with_options_async(
        self,
        request: sgw_20180511_models.ModifyStorageBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ModifyStorageBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageBundle',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ModifyStorageBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_storage_bundle(
        self,
        request: sgw_20180511_models.ModifyStorageBundleRequest,
    ) -> sgw_20180511_models.ModifyStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_bundle_with_options(request, runtime)

    async def modify_storage_bundle_async(
        self,
        request: sgw_20180511_models.ModifyStorageBundleRequest,
    ) -> sgw_20180511_models.ModifyStorageBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_bundle_with_options_async(request, runtime)

    def open_sgw_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.OpenSgwServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenSgwService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.OpenSgwServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_sgw_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.OpenSgwServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenSgwService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.OpenSgwServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_sgw_service(self) -> sgw_20180511_models.OpenSgwServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_sgw_service_with_options(runtime)

    async def open_sgw_service_async(self) -> sgw_20180511_models.OpenSgwServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_sgw_service_with_options_async(runtime)

    def operate_gateway_with_options(
        self,
        request: sgw_20180511_models.OperateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.OperateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.operate_action):
            query['OperateAction'] = request.operate_action
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.OperateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_gateway_with_options_async(
        self,
        request: sgw_20180511_models.OperateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.OperateGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.operate_action):
            query['OperateAction'] = request.operate_action
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.OperateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_gateway(
        self,
        request: sgw_20180511_models.OperateGatewayRequest,
    ) -> sgw_20180511_models.OperateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_gateway_with_options(request, runtime)

    async def operate_gateway_async(
        self,
        request: sgw_20180511_models.OperateGatewayRequest,
    ) -> sgw_20180511_models.OperateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_gateway_with_options_async(request, runtime)

    def release_service_with_options(
        self,
        request: sgw_20180511_models.ReleaseServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReleaseServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReleaseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_service_with_options_async(
        self,
        request: sgw_20180511_models.ReleaseServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReleaseServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReleaseServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_service(
        self,
        request: sgw_20180511_models.ReleaseServiceRequest,
    ) -> sgw_20180511_models.ReleaseServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_service_with_options(request, runtime)

    async def release_service_async(
        self,
        request: sgw_20180511_models.ReleaseServiceRequest,
    ) -> sgw_20180511_models.ReleaseServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_service_with_options_async(request, runtime)

    def remove_shares_from_express_sync_with_options(
        self,
        request: sgw_20180511_models.RemoveSharesFromExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RemoveSharesFromExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.gateway_shares):
            query['GatewayShares'] = request.gateway_shares
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSharesFromExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RemoveSharesFromExpressSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_shares_from_express_sync_with_options_async(
        self,
        request: sgw_20180511_models.RemoveSharesFromExpressSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RemoveSharesFromExpressSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_sync_id):
            query['ExpressSyncId'] = request.express_sync_id
        if not UtilClient.is_unset(request.gateway_shares):
            query['GatewayShares'] = request.gateway_shares
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSharesFromExpressSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RemoveSharesFromExpressSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_shares_from_express_sync(
        self,
        request: sgw_20180511_models.RemoveSharesFromExpressSyncRequest,
    ) -> sgw_20180511_models.RemoveSharesFromExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_shares_from_express_sync_with_options(request, runtime)

    async def remove_shares_from_express_sync_async(
        self,
        request: sgw_20180511_models.RemoveSharesFromExpressSyncRequest,
    ) -> sgw_20180511_models.RemoveSharesFromExpressSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_shares_from_express_sync_with_options_async(request, runtime)

    def remove_tags_from_gateway_with_options(
        self,
        request: sgw_20180511_models.RemoveTagsFromGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RemoveTagsFromGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RemoveTagsFromGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_from_gateway_with_options_async(
        self,
        request: sgw_20180511_models.RemoveTagsFromGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RemoveTagsFromGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RemoveTagsFromGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tags_from_gateway(
        self,
        request: sgw_20180511_models.RemoveTagsFromGatewayRequest,
    ) -> sgw_20180511_models.RemoveTagsFromGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_gateway_with_options(request, runtime)

    async def remove_tags_from_gateway_async(
        self,
        request: sgw_20180511_models.RemoveTagsFromGatewayRequest,
    ) -> sgw_20180511_models.RemoveTagsFromGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_from_gateway_with_options_async(request, runtime)

    def report_block_volumes_with_options(
        self,
        request: sgw_20180511_models.ReportBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportBlockVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportBlockVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_block_volumes_with_options_async(
        self,
        request: sgw_20180511_models.ReportBlockVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportBlockVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportBlockVolumes',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportBlockVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_block_volumes(
        self,
        request: sgw_20180511_models.ReportBlockVolumesRequest,
    ) -> sgw_20180511_models.ReportBlockVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_block_volumes_with_options(request, runtime)

    async def report_block_volumes_async(
        self,
        request: sgw_20180511_models.ReportBlockVolumesRequest,
    ) -> sgw_20180511_models.ReportBlockVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_block_volumes_with_options_async(request, runtime)

    def report_file_shares_with_options(
        self,
        request: sgw_20180511_models.ReportFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportFileSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_file_shares_with_options_async(
        self,
        request: sgw_20180511_models.ReportFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportFileSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_file_shares(
        self,
        request: sgw_20180511_models.ReportFileSharesRequest,
    ) -> sgw_20180511_models.ReportFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_file_shares_with_options(request, runtime)

    async def report_file_shares_async(
        self,
        request: sgw_20180511_models.ReportFileSharesRequest,
    ) -> sgw_20180511_models.ReportFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_file_shares_with_options_async(request, runtime)

    def report_gateway_info_with_options(
        self,
        request: sgw_20180511_models.ReportGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportGatewayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_status):
            query['GatewayStatus'] = request.gateway_status
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportGatewayInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportGatewayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_gateway_info_with_options_async(
        self,
        request: sgw_20180511_models.ReportGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportGatewayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_status):
            query['GatewayStatus'] = request.gateway_status
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportGatewayInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportGatewayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_gateway_info(
        self,
        request: sgw_20180511_models.ReportGatewayInfoRequest,
    ) -> sgw_20180511_models.ReportGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_gateway_info_with_options(request, runtime)

    async def report_gateway_info_async(
        self,
        request: sgw_20180511_models.ReportGatewayInfoRequest,
    ) -> sgw_20180511_models.ReportGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_gateway_info_with_options_async(request, runtime)

    def report_gateway_usage_with_options(
        self,
        request: sgw_20180511_models.ReportGatewayUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportGatewayUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportGatewayUsage',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportGatewayUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_gateway_usage_with_options_async(
        self,
        request: sgw_20180511_models.ReportGatewayUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ReportGatewayUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_uuid):
            query['ClientUUID'] = request.client_uuid
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportGatewayUsage',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ReportGatewayUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_gateway_usage(
        self,
        request: sgw_20180511_models.ReportGatewayUsageRequest,
    ) -> sgw_20180511_models.ReportGatewayUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_gateway_usage_with_options(request, runtime)

    async def report_gateway_usage_async(
        self,
        request: sgw_20180511_models.ReportGatewayUsageRequest,
    ) -> sgw_20180511_models.ReportGatewayUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_gateway_usage_with_options_async(request, runtime)

    def reset_gateway_password_with_options(
        self,
        request: sgw_20180511_models.ResetGatewayPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ResetGatewayPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetGatewayPassword',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ResetGatewayPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_gateway_password_with_options_async(
        self,
        request: sgw_20180511_models.ResetGatewayPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ResetGatewayPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetGatewayPassword',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ResetGatewayPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_gateway_password(
        self,
        request: sgw_20180511_models.ResetGatewayPasswordRequest,
    ) -> sgw_20180511_models.ResetGatewayPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_gateway_password_with_options(request, runtime)

    async def reset_gateway_password_async(
        self,
        request: sgw_20180511_models.ResetGatewayPasswordRequest,
    ) -> sgw_20180511_models.ResetGatewayPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_gateway_password_with_options_async(request, runtime)

    def restart_file_shares_with_options(
        self,
        request: sgw_20180511_models.RestartFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RestartFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.share_protocol):
            query['ShareProtocol'] = request.share_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RestartFileSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_file_shares_with_options_async(
        self,
        request: sgw_20180511_models.RestartFileSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.RestartFileSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.share_protocol):
            query['ShareProtocol'] = request.share_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartFileShares',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.RestartFileSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_file_shares(
        self,
        request: sgw_20180511_models.RestartFileSharesRequest,
    ) -> sgw_20180511_models.RestartFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_file_shares_with_options(request, runtime)

    async def restart_file_shares_async(
        self,
        request: sgw_20180511_models.RestartFileSharesRequest,
    ) -> sgw_20180511_models.RestartFileSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_file_shares_with_options_async(request, runtime)

    def set_gateway_adinfo_with_options(
        self,
        request: sgw_20180511_models.SetGatewayADInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayADInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayADInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayADInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gateway_adinfo_with_options_async(
        self,
        request: sgw_20180511_models.SetGatewayADInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayADInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayADInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayADInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gateway_adinfo(
        self,
        request: sgw_20180511_models.SetGatewayADInfoRequest,
    ) -> sgw_20180511_models.SetGatewayADInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gateway_adinfo_with_options(request, runtime)

    async def set_gateway_adinfo_async(
        self,
        request: sgw_20180511_models.SetGatewayADInfoRequest,
    ) -> sgw_20180511_models.SetGatewayADInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gateway_adinfo_with_options_async(request, runtime)

    def set_gateway_auto_upgrade_configuration_with_options(
        self,
        request: sgw_20180511_models.SetGatewayAutoUpgradeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_upgrade_end_hour):
            query['AutoUpgradeEndHour'] = request.auto_upgrade_end_hour
        if not UtilClient.is_unset(request.auto_upgrade_start_hour):
            query['AutoUpgradeStartHour'] = request.auto_upgrade_start_hour
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_auto_upgrade):
            query['IsAutoUpgrade'] = request.is_auto_upgrade
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayAutoUpgradeConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gateway_auto_upgrade_configuration_with_options_async(
        self,
        request: sgw_20180511_models.SetGatewayAutoUpgradeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_upgrade_end_hour):
            query['AutoUpgradeEndHour'] = request.auto_upgrade_end_hour
        if not UtilClient.is_unset(request.auto_upgrade_start_hour):
            query['AutoUpgradeStartHour'] = request.auto_upgrade_start_hour
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_auto_upgrade):
            query['IsAutoUpgrade'] = request.is_auto_upgrade
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayAutoUpgradeConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gateway_auto_upgrade_configuration(
        self,
        request: sgw_20180511_models.SetGatewayAutoUpgradeConfigurationRequest,
    ) -> sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gateway_auto_upgrade_configuration_with_options(request, runtime)

    async def set_gateway_auto_upgrade_configuration_async(
        self,
        request: sgw_20180511_models.SetGatewayAutoUpgradeConfigurationRequest,
    ) -> sgw_20180511_models.SetGatewayAutoUpgradeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gateway_auto_upgrade_configuration_with_options_async(request, runtime)

    def set_gateway_dnswith_options(
        self,
        request: sgw_20180511_models.SetGatewayDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_server):
            query['DnsServer'] = request.dns_server
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayDNS',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gateway_dnswith_options_async(
        self,
        request: sgw_20180511_models.SetGatewayDNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayDNSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_server):
            query['DnsServer'] = request.dns_server
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayDNS',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gateway_dns(
        self,
        request: sgw_20180511_models.SetGatewayDNSRequest,
    ) -> sgw_20180511_models.SetGatewayDNSResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gateway_dnswith_options(request, runtime)

    async def set_gateway_dns_async(
        self,
        request: sgw_20180511_models.SetGatewayDNSRequest,
    ) -> sgw_20180511_models.SetGatewayDNSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gateway_dnswith_options_async(request, runtime)

    def set_gateway_ldapinfo_with_options(
        self,
        request: sgw_20180511_models.SetGatewayLDAPInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayLDAPInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.is_tls):
            query['IsTls'] = request.is_tls
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.root_dn):
            query['RootDN'] = request.root_dn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayLDAPInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayLDAPInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gateway_ldapinfo_with_options_async(
        self,
        request: sgw_20180511_models.SetGatewayLDAPInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SetGatewayLDAPInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.is_tls):
            query['IsTls'] = request.is_tls
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.root_dn):
            query['RootDN'] = request.root_dn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGatewayLDAPInfo',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SetGatewayLDAPInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gateway_ldapinfo(
        self,
        request: sgw_20180511_models.SetGatewayLDAPInfoRequest,
    ) -> sgw_20180511_models.SetGatewayLDAPInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gateway_ldapinfo_with_options(request, runtime)

    async def set_gateway_ldapinfo_async(
        self,
        request: sgw_20180511_models.SetGatewayLDAPInfoRequest,
    ) -> sgw_20180511_models.SetGatewayLDAPInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gateway_ldapinfo_with_options_async(request, runtime)

    def switch_csgclients_reverse_sync_configuration_with_options(
        self,
        tmp_req: sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.is_reverse_sync):
            query['IsReverseSync'] = request.is_reverse_sync
        if not UtilClient.is_unset(request.reverse_sync_internal_second):
            query['ReverseSyncInternalSecond'] = request.reverse_sync_internal_second
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchCSGClientsReverseSyncConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_csgclients_reverse_sync_configuration_with_options_async(
        self,
        tmp_req: sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse:
        UtilClient.validate_model(tmp_req)
        request = sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.is_reverse_sync):
            query['IsReverseSync'] = request.is_reverse_sync
        if not UtilClient.is_unset(request.reverse_sync_internal_second):
            query['ReverseSyncInternalSecond'] = request.reverse_sync_internal_second
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchCSGClientsReverseSyncConfiguration',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_csgclients_reverse_sync_configuration(
        self,
        request: sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationRequest,
    ) -> sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_csgclients_reverse_sync_configuration_with_options(request, runtime)

    async def switch_csgclients_reverse_sync_configuration_async(
        self,
        request: sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationRequest,
    ) -> sgw_20180511_models.SwitchCSGClientsReverseSyncConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_csgclients_reverse_sync_configuration_with_options_async(request, runtime)

    def switch_gateway_expiration_policy_with_options(
        self,
        request: sgw_20180511_models.SwitchGatewayExpirationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchGatewayExpirationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGatewayExpirationPolicy',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchGatewayExpirationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_gateway_expiration_policy_with_options_async(
        self,
        request: sgw_20180511_models.SwitchGatewayExpirationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchGatewayExpirationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGatewayExpirationPolicy',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchGatewayExpirationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_gateway_expiration_policy(
        self,
        request: sgw_20180511_models.SwitchGatewayExpirationPolicyRequest,
    ) -> sgw_20180511_models.SwitchGatewayExpirationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_gateway_expiration_policy_with_options(request, runtime)

    async def switch_gateway_expiration_policy_async(
        self,
        request: sgw_20180511_models.SwitchGatewayExpirationPolicyRequest,
    ) -> sgw_20180511_models.SwitchGatewayExpirationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_gateway_expiration_policy_with_options_async(request, runtime)

    def switch_to_subscription_with_options(
        self,
        request: sgw_20180511_models.SwitchToSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchToSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToSubscription',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchToSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_to_subscription_with_options_async(
        self,
        request: sgw_20180511_models.SwitchToSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.SwitchToSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToSubscription',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.SwitchToSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_to_subscription(
        self,
        request: sgw_20180511_models.SwitchToSubscriptionRequest,
    ) -> sgw_20180511_models.SwitchToSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_to_subscription_with_options(request, runtime)

    async def switch_to_subscription_async(
        self,
        request: sgw_20180511_models.SwitchToSubscriptionRequest,
    ) -> sgw_20180511_models.SwitchToSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_to_subscription_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: sgw_20180511_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: sgw_20180511_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: sgw_20180511_models.TagResourcesRequest,
    ) -> sgw_20180511_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: sgw_20180511_models.TagResourcesRequest,
    ) -> sgw_20180511_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def trigger_gateway_remote_sync_with_options(
        self,
        request: sgw_20180511_models.TriggerGatewayRemoteSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.TriggerGatewayRemoteSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerGatewayRemoteSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.TriggerGatewayRemoteSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_gateway_remote_sync_with_options_async(
        self,
        request: sgw_20180511_models.TriggerGatewayRemoteSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.TriggerGatewayRemoteSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerGatewayRemoteSync',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.TriggerGatewayRemoteSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_gateway_remote_sync(
        self,
        request: sgw_20180511_models.TriggerGatewayRemoteSyncRequest,
    ) -> sgw_20180511_models.TriggerGatewayRemoteSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_gateway_remote_sync_with_options(request, runtime)

    async def trigger_gateway_remote_sync_async(
        self,
        request: sgw_20180511_models.TriggerGatewayRemoteSyncRequest,
    ) -> sgw_20180511_models.TriggerGatewayRemoteSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_gateway_remote_sync_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: sgw_20180511_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: sgw_20180511_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: sgw_20180511_models.UntagResourcesRequest,
    ) -> sgw_20180511_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: sgw_20180511_models.UntagResourcesRequest,
    ) -> sgw_20180511_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_gateway_block_volume_with_options(
        self,
        request: sgw_20180511_models.UpdateGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpdateGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chap_enabled):
            query['ChapEnabled'] = request.chap_enabled
        if not UtilClient.is_unset(request.chap_in_password):
            query['ChapInPassword'] = request.chap_in_password
        if not UtilClient.is_unset(request.chap_in_user):
            query['ChapInUser'] = request.chap_in_user
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpdateGatewayBlockVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_block_volume_with_options_async(
        self,
        request: sgw_20180511_models.UpdateGatewayBlockVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpdateGatewayBlockVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chap_enabled):
            query['ChapEnabled'] = request.chap_enabled
        if not UtilClient.is_unset(request.chap_in_password):
            query['ChapInPassword'] = request.chap_in_password
        if not UtilClient.is_unset(request.chap_in_user):
            query['ChapInUser'] = request.chap_in_user
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayBlockVolume',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpdateGatewayBlockVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_block_volume(
        self,
        request: sgw_20180511_models.UpdateGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.UpdateGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_block_volume_with_options(request, runtime)

    async def update_gateway_block_volume_async(
        self,
        request: sgw_20180511_models.UpdateGatewayBlockVolumeRequest,
    ) -> sgw_20180511_models.UpdateGatewayBlockVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_block_volume_with_options_async(request, runtime)

    def update_gateway_file_share_with_options(
        self,
        request: sgw_20180511_models.UpdateGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpdateGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_based_enumeration):
            query['AccessBasedEnumeration'] = request.access_based_enumeration
        if not UtilClient.is_unset(request.backend_limit):
            query['BackendLimit'] = request.backend_limit
        if not UtilClient.is_unset(request.browsable):
            query['Browsable'] = request.browsable
        if not UtilClient.is_unset(request.bypass_cache_read):
            query['BypassCacheRead'] = request.bypass_cache_read
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.client_side_cmk):
            query['ClientSideCmk'] = request.client_side_cmk
        if not UtilClient.is_unset(request.client_side_encryption):
            query['ClientSideEncryption'] = request.client_side_encryption
        if not UtilClient.is_unset(request.direct_io):
            query['DirectIO'] = request.direct_io
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.fast_reclaim):
            query['FastReclaim'] = request.fast_reclaim
        if not UtilClient.is_unset(request.frontend_limit):
            query['FrontendLimit'] = request.frontend_limit
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.ignore_delete):
            query['IgnoreDelete'] = request.ignore_delete
        if not UtilClient.is_unset(request.in_place):
            query['InPlace'] = request.in_place
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.kms_rotate_period):
            query['KmsRotatePeriod'] = request.kms_rotate_period
        if not UtilClient.is_unset(request.lag_period):
            query['LagPeriod'] = request.lag_period
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nfs_v4optimization):
            query['NfsV4Optimization'] = request.nfs_v4optimization
        if not UtilClient.is_unset(request.polling_interval):
            query['PollingInterval'] = request.polling_interval
        if not UtilClient.is_unset(request.read_only_client_list):
            query['ReadOnlyClientList'] = request.read_only_client_list
        if not UtilClient.is_unset(request.read_only_user_list):
            query['ReadOnlyUserList'] = request.read_only_user_list
        if not UtilClient.is_unset(request.read_write_client_list):
            query['ReadWriteClientList'] = request.read_write_client_list
        if not UtilClient.is_unset(request.read_write_user_list):
            query['ReadWriteUserList'] = request.read_write_user_list
        if not UtilClient.is_unset(request.remote_sync):
            query['RemoteSync'] = request.remote_sync
        if not UtilClient.is_unset(request.remote_sync_download):
            query['RemoteSyncDownload'] = request.remote_sync_download
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_side_cmk):
            query['ServerSideCmk'] = request.server_side_cmk
        if not UtilClient.is_unset(request.server_side_encryption):
            query['ServerSideEncryption'] = request.server_side_encryption
        if not UtilClient.is_unset(request.squash):
            query['Squash'] = request.squash
        if not UtilClient.is_unset(request.transfer_acceleration):
            query['TransferAcceleration'] = request.transfer_acceleration
        if not UtilClient.is_unset(request.windows_acl):
            query['WindowsAcl'] = request.windows_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpdateGatewayFileShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_file_share_with_options_async(
        self,
        request: sgw_20180511_models.UpdateGatewayFileShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpdateGatewayFileShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_based_enumeration):
            query['AccessBasedEnumeration'] = request.access_based_enumeration
        if not UtilClient.is_unset(request.backend_limit):
            query['BackendLimit'] = request.backend_limit
        if not UtilClient.is_unset(request.browsable):
            query['Browsable'] = request.browsable
        if not UtilClient.is_unset(request.bypass_cache_read):
            query['BypassCacheRead'] = request.bypass_cache_read
        if not UtilClient.is_unset(request.cache_mode):
            query['CacheMode'] = request.cache_mode
        if not UtilClient.is_unset(request.client_side_cmk):
            query['ClientSideCmk'] = request.client_side_cmk
        if not UtilClient.is_unset(request.client_side_encryption):
            query['ClientSideEncryption'] = request.client_side_encryption
        if not UtilClient.is_unset(request.direct_io):
            query['DirectIO'] = request.direct_io
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.fast_reclaim):
            query['FastReclaim'] = request.fast_reclaim
        if not UtilClient.is_unset(request.frontend_limit):
            query['FrontendLimit'] = request.frontend_limit
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.ignore_delete):
            query['IgnoreDelete'] = request.ignore_delete
        if not UtilClient.is_unset(request.in_place):
            query['InPlace'] = request.in_place
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.kms_rotate_period):
            query['KmsRotatePeriod'] = request.kms_rotate_period
        if not UtilClient.is_unset(request.lag_period):
            query['LagPeriod'] = request.lag_period
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nfs_v4optimization):
            query['NfsV4Optimization'] = request.nfs_v4optimization
        if not UtilClient.is_unset(request.polling_interval):
            query['PollingInterval'] = request.polling_interval
        if not UtilClient.is_unset(request.read_only_client_list):
            query['ReadOnlyClientList'] = request.read_only_client_list
        if not UtilClient.is_unset(request.read_only_user_list):
            query['ReadOnlyUserList'] = request.read_only_user_list
        if not UtilClient.is_unset(request.read_write_client_list):
            query['ReadWriteClientList'] = request.read_write_client_list
        if not UtilClient.is_unset(request.read_write_user_list):
            query['ReadWriteUserList'] = request.read_write_user_list
        if not UtilClient.is_unset(request.remote_sync):
            query['RemoteSync'] = request.remote_sync
        if not UtilClient.is_unset(request.remote_sync_download):
            query['RemoteSyncDownload'] = request.remote_sync_download
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_side_cmk):
            query['ServerSideCmk'] = request.server_side_cmk
        if not UtilClient.is_unset(request.server_side_encryption):
            query['ServerSideEncryption'] = request.server_side_encryption
        if not UtilClient.is_unset(request.squash):
            query['Squash'] = request.squash
        if not UtilClient.is_unset(request.transfer_acceleration):
            query['TransferAcceleration'] = request.transfer_acceleration
        if not UtilClient.is_unset(request.windows_acl):
            query['WindowsAcl'] = request.windows_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayFileShare',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpdateGatewayFileShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_file_share(
        self,
        request: sgw_20180511_models.UpdateGatewayFileShareRequest,
    ) -> sgw_20180511_models.UpdateGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_file_share_with_options(request, runtime)

    async def update_gateway_file_share_async(
        self,
        request: sgw_20180511_models.UpdateGatewayFileShareRequest,
    ) -> sgw_20180511_models.UpdateGatewayFileShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_file_share_with_options_async(request, runtime)

    def upgrade_gateway_with_options(
        self,
        request: sgw_20180511_models.UpgradeGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpgradeGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpgradeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_gateway_with_options_async(
        self,
        request: sgw_20180511_models.UpgradeGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UpgradeGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeGateway',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UpgradeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_gateway(
        self,
        request: sgw_20180511_models.UpgradeGatewayRequest,
    ) -> sgw_20180511_models.UpgradeGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_gateway_with_options(request, runtime)

    async def upgrade_gateway_async(
        self,
        request: sgw_20180511_models.UpgradeGatewayRequest,
    ) -> sgw_20180511_models.UpgradeGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_gateway_with_options_async(request, runtime)

    def upload_csgclient_log_with_options(
        self,
        request: sgw_20180511_models.UploadCSGClientLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UploadCSGClientLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCSGClientLog',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UploadCSGClientLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_csgclient_log_with_options_async(
        self,
        request: sgw_20180511_models.UploadCSGClientLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UploadCSGClientLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_region_id):
            query['ClientRegionId'] = request.client_region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCSGClientLog',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UploadCSGClientLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_csgclient_log(
        self,
        request: sgw_20180511_models.UploadCSGClientLogRequest,
    ) -> sgw_20180511_models.UploadCSGClientLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_csgclient_log_with_options(request, runtime)

    async def upload_csgclient_log_async(
        self,
        request: sgw_20180511_models.UploadCSGClientLogRequest,
    ) -> sgw_20180511_models.UploadCSGClientLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_csgclient_log_with_options_async(request, runtime)

    def upload_gateway_log_with_options(
        self,
        request: sgw_20180511_models.UploadGatewayLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UploadGatewayLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadGatewayLog',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UploadGatewayLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_gateway_log_with_options_async(
        self,
        request: sgw_20180511_models.UploadGatewayLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.UploadGatewayLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadGatewayLog',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.UploadGatewayLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_gateway_log(
        self,
        request: sgw_20180511_models.UploadGatewayLogRequest,
    ) -> sgw_20180511_models.UploadGatewayLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_gateway_log_with_options(request, runtime)

    async def upload_gateway_log_async(
        self,
        request: sgw_20180511_models.UploadGatewayLogRequest,
    ) -> sgw_20180511_models.UploadGatewayLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_gateway_log_with_options_async(request, runtime)

    def validate_express_sync_config_with_options(
        self,
        request: sgw_20180511_models.ValidateExpressSyncConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ValidateExpressSyncConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateExpressSyncConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ValidateExpressSyncConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_express_sync_config_with_options_async(
        self,
        request: sgw_20180511_models.ValidateExpressSyncConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ValidateExpressSyncConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.bucket_prefix):
            query['BucketPrefix'] = request.bucket_prefix
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateExpressSyncConfig',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ValidateExpressSyncConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_express_sync_config(
        self,
        request: sgw_20180511_models.ValidateExpressSyncConfigRequest,
    ) -> sgw_20180511_models.ValidateExpressSyncConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_express_sync_config_with_options(request, runtime)

    async def validate_express_sync_config_async(
        self,
        request: sgw_20180511_models.ValidateExpressSyncConfigRequest,
    ) -> sgw_20180511_models.ValidateExpressSyncConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_express_sync_config_with_options_async(request, runtime)

    def validate_gateway_name_with_options(
        self,
        request: sgw_20180511_models.ValidateGatewayNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ValidateGatewayNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateGatewayName',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ValidateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_gateway_name_with_options_async(
        self,
        request: sgw_20180511_models.ValidateGatewayNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sgw_20180511_models.ValidateGatewayNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.storage_bundle_id):
            query['StorageBundleId'] = request.storage_bundle_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateGatewayName',
            version='2018-05-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sgw_20180511_models.ValidateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_gateway_name(
        self,
        request: sgw_20180511_models.ValidateGatewayNameRequest,
    ) -> sgw_20180511_models.ValidateGatewayNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_gateway_name_with_options(request, runtime)

    async def validate_gateway_name_async(
        self,
        request: sgw_20180511_models.ValidateGatewayNameRequest,
    ) -> sgw_20180511_models.ValidateGatewayNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_gateway_name_with_options_async(request, runtime)
