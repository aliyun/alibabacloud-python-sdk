# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_kms20160120 import models as main_models
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
        self._product_id = 'Kms'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'us-west-1': 'kms.us-west-1.aliyuncs.com',
            'us-east-1': 'kms.us-east-1.aliyuncs.com',
            'me-east-1': 'kms.me-east-1.aliyuncs.com',
            'me-central-1': 'kms.me-central-1.aliyuncs.com',
            'eu-west-1': 'kms.eu-west-1.aliyuncs.com',
            'eu-central-1': 'kms.eu-central-1.aliyuncs.com',
            'cn-zhengzhou-jva': 'kms.cn-zhengzhou-jva.aliyuncs.com',
            'cn-zhangjiakou': 'kms.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'kms.cn-wulanchabu.aliyuncs.com',
            'cn-wuhan-lr': 'kms.cn-wuhan-lr.aliyuncs.com',
            'cn-shenzhen-finance-1': 'kms.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen': 'kms.cn-shenzhen.aliyuncs.com',
            'cn-shanghai-finance-1': 'kms.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai': 'kms.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'kms.cn-qingdao.aliyuncs.com',
            'cn-huhehaote': 'kms.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'kms.cn-hongkong.aliyuncs.com',
            'cn-heyuan': 'kms.cn-heyuan.aliyuncs.com',
            'cn-hangzhou-finance': 'kms.cn-hangzhou-finance.aliyuncs.com',
            'cn-hangzhou': 'kms.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'kms.cn-guangzhou.aliyuncs.com',
            'cn-fuzhou': 'kms.cn-fuzhou.aliyuncs.com',
            'cn-chengdu': 'kms.cn-chengdu.aliyuncs.com',
            'cn-beijing-finance-1': 'kms.cn-beijing-finance-1.aliyuncs.com',
            'cn-beijing': 'kms.cn-beijing.aliyuncs.com',
            'ap-southeast-7': 'kms.ap-southeast-7.aliyuncs.com',
            'ap-southeast-6': 'kms.ap-southeast-6.aliyuncs.com',
            'ap-southeast-5': 'kms.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'kms.ap-southeast-3.aliyuncs.com',
            'ap-southeast-2': 'kms.ap-southeast-2.aliyuncs.com',
            'ap-southeast-1': 'kms.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'kms.ap-south-1.aliyuncs.com',
            'ap-northeast-2': 'kms.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'kms.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('kms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def asymmetric_decrypt_with_options(
        self,
        request: main_models.AsymmetricDecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricDecryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricDecrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricDecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_decrypt_with_options_async(
        self,
        request: main_models.AsymmetricDecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricDecryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricDecrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricDecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_decrypt(
        self,
        request: main_models.AsymmetricDecryptRequest,
    ) -> main_models.AsymmetricDecryptResponse:
        runtime = RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    async def asymmetric_decrypt_async(
        self,
        request: main_models.AsymmetricDecryptRequest,
    ) -> main_models.AsymmetricDecryptResponse:
        runtime = RuntimeOptions()
        return await self.asymmetric_decrypt_with_options_async(request, runtime)

    def asymmetric_encrypt_with_options(
        self,
        request: main_models.AsymmetricEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricEncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricEncrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_encrypt_with_options_async(
        self,
        request: main_models.AsymmetricEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricEncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricEncrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_encrypt(
        self,
        request: main_models.AsymmetricEncryptRequest,
    ) -> main_models.AsymmetricEncryptResponse:
        runtime = RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    async def asymmetric_encrypt_async(
        self,
        request: main_models.AsymmetricEncryptRequest,
    ) -> main_models.AsymmetricEncryptResponse:
        runtime = RuntimeOptions()
        return await self.asymmetric_encrypt_with_options_async(request, runtime)

    def asymmetric_sign_with_options(
        self,
        request: main_models.AsymmetricSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricSign',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_sign_with_options_async(
        self,
        request: main_models.AsymmetricSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricSign',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_sign(
        self,
        request: main_models.AsymmetricSignRequest,
    ) -> main_models.AsymmetricSignResponse:
        runtime = RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    async def asymmetric_sign_async(
        self,
        request: main_models.AsymmetricSignRequest,
    ) -> main_models.AsymmetricSignResponse:
        runtime = RuntimeOptions()
        return await self.asymmetric_sign_with_options_async(request, runtime)

    def asymmetric_verify_with_options(
        self,
        request: main_models.AsymmetricVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricVerify',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_verify_with_options_async(
        self,
        request: main_models.AsymmetricVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsymmetricVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AsymmetricVerify',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsymmetricVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_verify(
        self,
        request: main_models.AsymmetricVerifyRequest,
    ) -> main_models.AsymmetricVerifyResponse:
        runtime = RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    async def asymmetric_verify_async(
        self,
        request: main_models.AsymmetricVerifyRequest,
    ) -> main_models.AsymmetricVerifyResponse:
        runtime = RuntimeOptions()
        return await self.asymmetric_verify_with_options_async(request, runtime)

    def cancel_key_deletion_with_options(
        self,
        request: main_models.CancelKeyDeletionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelKeyDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelKeyDeletion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_key_deletion_with_options_async(
        self,
        request: main_models.CancelKeyDeletionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelKeyDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelKeyDeletion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelKeyDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_key_deletion(
        self,
        request: main_models.CancelKeyDeletionRequest,
    ) -> main_models.CancelKeyDeletionResponse:
        runtime = RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    async def cancel_key_deletion_async(
        self,
        request: main_models.CancelKeyDeletionRequest,
    ) -> main_models.CancelKeyDeletionResponse:
        runtime = RuntimeOptions()
        return await self.cancel_key_deletion_with_options_async(request, runtime)

    def connect_kms_instance_with_options(
        self,
        request: main_models.ConnectKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConnectKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kmprovider):
            query['KMProvider'] = request.kmprovider
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConnectKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConnectKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def connect_kms_instance_with_options_async(
        self,
        request: main_models.ConnectKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConnectKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kmprovider):
            query['KMProvider'] = request.kmprovider
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConnectKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConnectKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def connect_kms_instance(
        self,
        request: main_models.ConnectKmsInstanceRequest,
    ) -> main_models.ConnectKmsInstanceResponse:
        runtime = RuntimeOptions()
        return self.connect_kms_instance_with_options(request, runtime)

    async def connect_kms_instance_async(
        self,
        request: main_models.ConnectKmsInstanceRequest,
    ) -> main_models.ConnectKmsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.connect_kms_instance_with_options_async(request, runtime)

    def create_alias_with_options(
        self,
        request: main_models.CreateAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        request: main_models.CreateAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        request: main_models.CreateAliasRequest,
    ) -> main_models.CreateAliasResponse:
        runtime = RuntimeOptions()
        return self.create_alias_with_options(request, runtime)

    async def create_alias_async(
        self,
        request: main_models.CreateAliasRequest,
    ) -> main_models.CreateAliasResponse:
        runtime = RuntimeOptions()
        return await self.create_alias_with_options_async(request, runtime)

    def create_application_access_point_with_options(
        self,
        request: main_models.CreateApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_method):
            query['AuthenticationMethod'] = request.authentication_method
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_access_point_with_options_async(
        self,
        request: main_models.CreateApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_method):
            query['AuthenticationMethod'] = request.authentication_method
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_access_point(
        self,
        request: main_models.CreateApplicationAccessPointRequest,
    ) -> main_models.CreateApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return self.create_application_access_point_with_options(request, runtime)

    async def create_application_access_point_async(
        self,
        request: main_models.CreateApplicationAccessPointRequest,
    ) -> main_models.CreateApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.create_application_access_point_with_options_async(request, runtime)

    def create_client_key_with_options(
        self,
        request: main_models.CreateClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aap_name):
            query['AapName'] = request.aap_name
        if not DaraCore.is_null(request.not_after):
            query['NotAfter'] = request.not_after
        if not DaraCore.is_null(request.not_before):
            query['NotBefore'] = request.not_before
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_key_with_options_async(
        self,
        request: main_models.CreateClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aap_name):
            query['AapName'] = request.aap_name
        if not DaraCore.is_null(request.not_after):
            query['NotAfter'] = request.not_after
        if not DaraCore.is_null(request.not_before):
            query['NotBefore'] = request.not_before
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_key(
        self,
        request: main_models.CreateClientKeyRequest,
    ) -> main_models.CreateClientKeyResponse:
        runtime = RuntimeOptions()
        return self.create_client_key_with_options(request, runtime)

    async def create_client_key_async(
        self,
        request: main_models.CreateClientKeyRequest,
    ) -> main_models.CreateClientKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_client_key_with_options_async(request, runtime)

    def create_key_with_options(
        self,
        request: main_models.CreateKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.key_storage_mechanism):
            query['KeyStorageMechanism'] = request.key_storage_mechanism
        if not DaraCore.is_null(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_with_options_async(
        self,
        request: main_models.CreateKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.key_storage_mechanism):
            query['KeyStorageMechanism'] = request.key_storage_mechanism
        if not DaraCore.is_null(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key(
        self,
        request: main_models.CreateKeyRequest,
    ) -> main_models.CreateKeyResponse:
        runtime = RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    async def create_key_async(
        self,
        request: main_models.CreateKeyRequest,
    ) -> main_models.CreateKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_key_with_options_async(request, runtime)

    def create_key_version_with_options(
        self,
        request: main_models.CreateKeyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyVersion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_version_with_options_async(
        self,
        request: main_models.CreateKeyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyVersion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_version(
        self,
        request: main_models.CreateKeyVersionRequest,
    ) -> main_models.CreateKeyVersionResponse:
        runtime = RuntimeOptions()
        return self.create_key_version_with_options(request, runtime)

    async def create_key_version_async(
        self,
        request: main_models.CreateKeyVersionRequest,
    ) -> main_models.CreateKeyVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_key_version_with_options_async(request, runtime)

    def create_network_rule_with_options(
        self,
        request: main_models.CreateNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_rule_with_options_async(
        self,
        request: main_models.CreateNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_rule(
        self,
        request: main_models.CreateNetworkRuleRequest,
    ) -> main_models.CreateNetworkRuleResponse:
        runtime = RuntimeOptions()
        return self.create_network_rule_with_options(request, runtime)

    async def create_network_rule_async(
        self,
        request: main_models.CreateNetworkRuleRequest,
    ) -> main_models.CreateNetworkRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_network_rule_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kms_instance):
            query['KmsInstance'] = request.kms_instance
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kms_instance):
            query['KmsInstance'] = request.kms_instance
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_secret_with_options(
        self,
        tmp_req: main_models.CreateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        tmp_req.validate()
        request = main_models.CreateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extended_config):
            request.extended_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.secret_data):
            query['SecretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        tmp_req: main_models.CreateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        tmp_req.validate()
        request = main_models.CreateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extended_config):
            request.extended_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.secret_data):
            query['SecretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    async def create_secret_async(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        return await self.create_secret_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        tmp_req: main_models.DecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptResponse:
        tmp_req.validate()
        request = main_models.DecryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.recipient):
            query['Recipient'] = request.recipient
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Decrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_with_options_async(
        self,
        tmp_req: main_models.DecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptResponse:
        tmp_req.validate()
        request = main_models.DecryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.recipient):
            query['Recipient'] = request.recipient
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Decrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrypt(
        self,
        request: main_models.DecryptRequest,
    ) -> main_models.DecryptResponse:
        runtime = RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: main_models.DecryptRequest,
    ) -> main_models.DecryptResponse:
        runtime = RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_alias_with_options(
        self,
        request: main_models.DeleteAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        request: main_models.DeleteAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        request: main_models.DeleteAliasRequest,
    ) -> main_models.DeleteAliasResponse:
        runtime = RuntimeOptions()
        return self.delete_alias_with_options(request, runtime)

    async def delete_alias_async(
        self,
        request: main_models.DeleteAliasRequest,
    ) -> main_models.DeleteAliasResponse:
        runtime = RuntimeOptions()
        return await self.delete_alias_with_options_async(request, runtime)

    def delete_application_access_point_with_options(
        self,
        request: main_models.DeleteApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_access_point_with_options_async(
        self,
        request: main_models.DeleteApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_access_point(
        self,
        request: main_models.DeleteApplicationAccessPointRequest,
    ) -> main_models.DeleteApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return self.delete_application_access_point_with_options(request, runtime)

    async def delete_application_access_point_async(
        self,
        request: main_models.DeleteApplicationAccessPointRequest,
    ) -> main_models.DeleteApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_access_point_with_options_async(request, runtime)

    def delete_client_key_with_options(
        self,
        request: main_models.DeleteClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_key_id):
            query['ClientKeyId'] = request.client_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_key_with_options_async(
        self,
        request: main_models.DeleteClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_key_id):
            query['ClientKeyId'] = request.client_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_key(
        self,
        request: main_models.DeleteClientKeyRequest,
    ) -> main_models.DeleteClientKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_client_key_with_options(request, runtime)

    async def delete_client_key_async(
        self,
        request: main_models.DeleteClientKeyRequest,
    ) -> main_models.DeleteClientKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_key_with_options_async(request, runtime)

    def delete_key_material_with_options(
        self,
        request: main_models.DeleteKeyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyMaterial',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_material_with_options_async(
        self,
        request: main_models.DeleteKeyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyMaterial',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_material(
        self,
        request: main_models.DeleteKeyMaterialRequest,
    ) -> main_models.DeleteKeyMaterialResponse:
        runtime = RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    async def delete_key_material_async(
        self,
        request: main_models.DeleteKeyMaterialRequest,
    ) -> main_models.DeleteKeyMaterialResponse:
        runtime = RuntimeOptions()
        return await self.delete_key_material_with_options_async(request, runtime)

    def delete_network_rule_with_options(
        self,
        request: main_models.DeleteNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_rule_with_options_async(
        self,
        request: main_models.DeleteNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_rule(
        self,
        request: main_models.DeleteNetworkRuleRequest,
    ) -> main_models.DeleteNetworkRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    async def delete_network_rule_async(
        self,
        request: main_models.DeleteNetworkRuleRequest,
    ) -> main_models.DeleteNetworkRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_rule_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_secret_with_options(
        self,
        request: main_models.DeleteSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_without_recovery):
            query['ForceDeleteWithoutRecovery'] = request.force_delete_without_recovery
        if not DaraCore.is_null(request.recovery_window_in_days):
            query['RecoveryWindowInDays'] = request.recovery_window_in_days
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: main_models.DeleteSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_without_recovery):
            query['ForceDeleteWithoutRecovery'] = request.force_delete_without_recovery
        if not DaraCore.is_null(request.recovery_window_in_days):
            query['RecoveryWindowInDays'] = request.recovery_window_in_days
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    async def delete_secret_async(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        return await self.delete_secret_with_options_async(request, runtime)

    def describe_account_kms_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountKmsStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAccountKmsStatus',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountKmsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_kms_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountKmsStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAccountKmsStatus',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountKmsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_kms_status(self) -> main_models.DescribeAccountKmsStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_account_kms_status_with_options(runtime)

    async def describe_account_kms_status_async(self) -> main_models.DescribeAccountKmsStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_kms_status_with_options_async(runtime)

    def describe_application_access_point_with_options(
        self,
        request: main_models.DescribeApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_access_point_with_options_async(
        self,
        request: main_models.DescribeApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_access_point(
        self,
        request: main_models.DescribeApplicationAccessPointRequest,
    ) -> main_models.DescribeApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return self.describe_application_access_point_with_options(request, runtime)

    async def describe_application_access_point_async(
        self,
        request: main_models.DescribeApplicationAccessPointRequest,
    ) -> main_models.DescribeApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.describe_application_access_point_with_options_async(request, runtime)

    def describe_key_with_options(
        self,
        request: main_models.DescribeKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_with_options_async(
        self,
        request: main_models.DescribeKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key(
        self,
        request: main_models.DescribeKeyRequest,
    ) -> main_models.DescribeKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    async def describe_key_async(
        self,
        request: main_models.DescribeKeyRequest,
    ) -> main_models.DescribeKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_key_with_options_async(request, runtime)

    def describe_key_version_with_options(
        self,
        request: main_models.DescribeKeyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKeyVersion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_version_with_options_async(
        self,
        request: main_models.DescribeKeyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKeyVersion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key_version(
        self,
        request: main_models.DescribeKeyVersionRequest,
    ) -> main_models.DescribeKeyVersionResponse:
        runtime = RuntimeOptions()
        return self.describe_key_version_with_options(request, runtime)

    async def describe_key_version_async(
        self,
        request: main_models.DescribeKeyVersionRequest,
    ) -> main_models.DescribeKeyVersionResponse:
        runtime = RuntimeOptions()
        return await self.describe_key_version_with_options_async(request, runtime)

    def describe_network_rule_with_options(
        self,
        request: main_models.DescribeNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rule_with_options_async(
        self,
        request: main_models.DescribeNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_rule(
        self,
        request: main_models.DescribeNetworkRuleRequest,
    ) -> main_models.DescribeNetworkRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_network_rule_with_options(request, runtime)

    async def describe_network_rule_async(
        self,
        request: main_models.DescribeNetworkRuleRequest,
    ) -> main_models.DescribeNetworkRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_rule_with_options_async(request, runtime)

    def describe_policy_with_options(
        self,
        request: main_models.DescribePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_with_options_async(
        self,
        request: main_models.DescribePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy(
        self,
        request: main_models.DescribePolicyRequest,
    ) -> main_models.DescribePolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_policy_with_options(request, runtime)

    async def describe_policy_async(
        self,
        request: main_models.DescribePolicyRequest,
    ) -> main_models.DescribePolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_policy_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-01-20',
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
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-01-20',
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

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_secret_with_options(
        self,
        request: main_models.DescribeSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: main_models.DescribeSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret(
        self,
        request: main_models.DescribeSecretRequest,
    ) -> main_models.DescribeSecretResponse:
        runtime = RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    async def describe_secret_async(
        self,
        request: main_models.DescribeSecretRequest,
    ) -> main_models.DescribeSecretResponse:
        runtime = RuntimeOptions()
        return await self.describe_secret_with_options_async(request, runtime)

    def disable_key_with_options(
        self,
        request: main_models.DisableKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_key_with_options_async(
        self,
        request: main_models.DisableKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_key(
        self,
        request: main_models.DisableKeyRequest,
    ) -> main_models.DisableKeyResponse:
        runtime = RuntimeOptions()
        return self.disable_key_with_options(request, runtime)

    async def disable_key_async(
        self,
        request: main_models.DisableKeyRequest,
    ) -> main_models.DisableKeyResponse:
        runtime = RuntimeOptions()
        return await self.disable_key_with_options_async(request, runtime)

    def enable_key_with_options(
        self,
        request: main_models.EnableKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_key_with_options_async(
        self,
        request: main_models.EnableKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_key(
        self,
        request: main_models.EnableKeyRequest,
    ) -> main_models.EnableKeyResponse:
        runtime = RuntimeOptions()
        return self.enable_key_with_options(request, runtime)

    async def enable_key_async(
        self,
        request: main_models.EnableKeyRequest,
    ) -> main_models.EnableKeyResponse:
        runtime = RuntimeOptions()
        return await self.enable_key_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        tmp_req: main_models.EncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptResponse:
        tmp_req.validate()
        request = main_models.EncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Encrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_with_options_async(
        self,
        tmp_req: main_models.EncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptResponse:
        tmp_req.validate()
        request = main_models.EncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Encrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt(
        self,
        request: main_models.EncryptRequest,
    ) -> main_models.EncryptResponse:
        runtime = RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: main_models.EncryptRequest,
    ) -> main_models.EncryptResponse:
        runtime = RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def export_data_key_with_options(
        self,
        tmp_req: main_models.ExportDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportDataKeyResponse:
        tmp_req.validate()
        request = main_models.ExportDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_data_key_with_options_async(
        self,
        tmp_req: main_models.ExportDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportDataKeyResponse:
        tmp_req.validate()
        request = main_models.ExportDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_data_key(
        self,
        request: main_models.ExportDataKeyRequest,
    ) -> main_models.ExportDataKeyResponse:
        runtime = RuntimeOptions()
        return self.export_data_key_with_options(request, runtime)

    async def export_data_key_async(
        self,
        request: main_models.ExportDataKeyRequest,
    ) -> main_models.ExportDataKeyResponse:
        runtime = RuntimeOptions()
        return await self.export_data_key_with_options_async(request, runtime)

    def generate_and_export_data_key_with_options(
        self,
        tmp_req: main_models.GenerateAndExportDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAndExportDataKeyResponse:
        tmp_req.validate()
        request = main_models.GenerateAndExportDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not DaraCore.is_null(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAndExportDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAndExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_and_export_data_key_with_options_async(
        self,
        tmp_req: main_models.GenerateAndExportDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAndExportDataKeyResponse:
        tmp_req.validate()
        request = main_models.GenerateAndExportDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not DaraCore.is_null(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAndExportDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAndExportDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_and_export_data_key(
        self,
        request: main_models.GenerateAndExportDataKeyRequest,
    ) -> main_models.GenerateAndExportDataKeyResponse:
        runtime = RuntimeOptions()
        return self.generate_and_export_data_key_with_options(request, runtime)

    async def generate_and_export_data_key_async(
        self,
        request: main_models.GenerateAndExportDataKeyRequest,
    ) -> main_models.GenerateAndExportDataKeyResponse:
        runtime = RuntimeOptions()
        return await self.generate_and_export_data_key_with_options_async(request, runtime)

    def generate_data_key_with_options(
        self,
        tmp_req: main_models.GenerateDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDataKeyResponse:
        tmp_req.validate()
        request = main_models.GenerateDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not DaraCore.is_null(request.recipient):
            query['Recipient'] = request.recipient
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_data_key_with_options_async(
        self,
        tmp_req: main_models.GenerateDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDataKeyResponse:
        tmp_req.validate()
        request = main_models.GenerateDataKeyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not DaraCore.is_null(request.recipient):
            query['Recipient'] = request.recipient
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDataKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_data_key(
        self,
        request: main_models.GenerateDataKeyRequest,
    ) -> main_models.GenerateDataKeyResponse:
        runtime = RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    async def generate_data_key_async(
        self,
        request: main_models.GenerateDataKeyRequest,
    ) -> main_models.GenerateDataKeyResponse:
        runtime = RuntimeOptions()
        return await self.generate_data_key_with_options_async(request, runtime)

    def generate_data_key_without_plaintext_with_options(
        self,
        tmp_req: main_models.GenerateDataKeyWithoutPlaintextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDataKeyWithoutPlaintextResponse:
        tmp_req.validate()
        request = main_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDataKeyWithoutPlaintext',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDataKeyWithoutPlaintextResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_data_key_without_plaintext_with_options_async(
        self,
        tmp_req: main_models.GenerateDataKeyWithoutPlaintextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDataKeyWithoutPlaintextResponse:
        tmp_req.validate()
        request = main_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.encryption_context):
            request.encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not DaraCore.is_null(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDataKeyWithoutPlaintext',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDataKeyWithoutPlaintextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_data_key_without_plaintext(
        self,
        request: main_models.GenerateDataKeyWithoutPlaintextRequest,
    ) -> main_models.GenerateDataKeyWithoutPlaintextResponse:
        runtime = RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    async def generate_data_key_without_plaintext_async(
        self,
        request: main_models.GenerateDataKeyWithoutPlaintextRequest,
    ) -> main_models.GenerateDataKeyWithoutPlaintextResponse:
        runtime = RuntimeOptions()
        return await self.generate_data_key_without_plaintext_with_options_async(request, runtime)

    def generate_mac_with_options(
        self,
        request: main_models.GenerateMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateMac',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_mac_with_options_async(
        self,
        request: main_models.GenerateMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateMac',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_mac(
        self,
        request: main_models.GenerateMacRequest,
    ) -> main_models.GenerateMacResponse:
        runtime = RuntimeOptions()
        return self.generate_mac_with_options(request, runtime)

    async def generate_mac_async(
        self,
        request: main_models.GenerateMacRequest,
    ) -> main_models.GenerateMacResponse:
        runtime = RuntimeOptions()
        return await self.generate_mac_with_options_async(request, runtime)

    def get_client_key_with_options(
        self,
        request: main_models.GetClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientKeyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_key_with_options_async(
        self,
        request: main_models.GetClientKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientKeyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_key(
        self,
        request: main_models.GetClientKeyRequest,
    ) -> main_models.GetClientKeyResponse:
        runtime = RuntimeOptions()
        return self.get_client_key_with_options(request, runtime)

    async def get_client_key_async(
        self,
        request: main_models.GetClientKeyRequest,
    ) -> main_models.GetClientKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_client_key_with_options_async(request, runtime)

    def get_default_kms_instance_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultKmsInstanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetDefaultKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_kms_instance_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultKmsInstanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetDefaultKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_kms_instance(self) -> main_models.GetDefaultKmsInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_default_kms_instance_with_options(runtime)

    async def get_default_kms_instance_async(self) -> main_models.GetDefaultKmsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_default_kms_instance_with_options_async(runtime)

    def get_key_policy_with_options(
        self,
        request: main_models.GetKeyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKeyPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_key_policy_with_options_async(
        self,
        request: main_models.GetKeyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKeyPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_key_policy(
        self,
        request: main_models.GetKeyPolicyRequest,
    ) -> main_models.GetKeyPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_key_policy_with_options(request, runtime)

    async def get_key_policy_async(
        self,
        request: main_models.GetKeyPolicyRequest,
    ) -> main_models.GetKeyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_key_policy_with_options_async(request, runtime)

    def get_kms_instance_with_options(
        self,
        request: main_models.GetKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kms_instance_with_options_async(
        self,
        request: main_models.GetKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kms_instance(
        self,
        request: main_models.GetKmsInstanceRequest,
    ) -> main_models.GetKmsInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_kms_instance_with_options(request, runtime)

    async def get_kms_instance_async(
        self,
        request: main_models.GetKmsInstanceRequest,
    ) -> main_models.GetKmsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_kms_instance_with_options_async(request, runtime)

    def get_kms_instance_quota_infos_with_options(
        self,
        request: main_models.GetKmsInstanceQuotaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKmsInstanceQuotaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKmsInstanceQuotaInfos',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKmsInstanceQuotaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kms_instance_quota_infos_with_options_async(
        self,
        request: main_models.GetKmsInstanceQuotaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKmsInstanceQuotaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKmsInstanceQuotaInfos',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKmsInstanceQuotaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kms_instance_quota_infos(
        self,
        request: main_models.GetKmsInstanceQuotaInfosRequest,
    ) -> main_models.GetKmsInstanceQuotaInfosResponse:
        runtime = RuntimeOptions()
        return self.get_kms_instance_quota_infos_with_options(request, runtime)

    async def get_kms_instance_quota_infos_async(
        self,
        request: main_models.GetKmsInstanceQuotaInfosRequest,
    ) -> main_models.GetKmsInstanceQuotaInfosResponse:
        runtime = RuntimeOptions()
        return await self.get_kms_instance_quota_infos_with_options_async(request, runtime)

    def get_parameters_for_import_with_options(
        self,
        request: main_models.GetParametersForImportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersForImportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParametersForImport',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersForImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_for_import_with_options_async(
        self,
        request: main_models.GetParametersForImportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersForImportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not DaraCore.is_null(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParametersForImport',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersForImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters_for_import(
        self,
        request: main_models.GetParametersForImportRequest,
    ) -> main_models.GetParametersForImportResponse:
        runtime = RuntimeOptions()
        return self.get_parameters_for_import_with_options(request, runtime)

    async def get_parameters_for_import_async(
        self,
        request: main_models.GetParametersForImportRequest,
    ) -> main_models.GetParametersForImportResponse:
        runtime = RuntimeOptions()
        return await self.get_parameters_for_import_with_options_async(request, runtime)

    def get_public_key_with_options(
        self,
        request: main_models.GetPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPublicKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_key_with_options_async(
        self,
        request: main_models.GetPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPublicKey',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_key(
        self,
        request: main_models.GetPublicKeyRequest,
    ) -> main_models.GetPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    async def get_public_key_async(
        self,
        request: main_models.GetPublicKeyRequest,
    ) -> main_models.GetPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_public_key_with_options_async(request, runtime)

    def get_random_password_with_options(
        self,
        request: main_models.GetRandomPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRandomPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_characters):
            query['ExcludeCharacters'] = request.exclude_characters
        if not DaraCore.is_null(request.exclude_lowercase):
            query['ExcludeLowercase'] = request.exclude_lowercase
        if not DaraCore.is_null(request.exclude_numbers):
            query['ExcludeNumbers'] = request.exclude_numbers
        if not DaraCore.is_null(request.exclude_punctuation):
            query['ExcludePunctuation'] = request.exclude_punctuation
        if not DaraCore.is_null(request.exclude_uppercase):
            query['ExcludeUppercase'] = request.exclude_uppercase
        if not DaraCore.is_null(request.password_length):
            query['PasswordLength'] = request.password_length
        if not DaraCore.is_null(request.require_each_included_type):
            query['RequireEachIncludedType'] = request.require_each_included_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRandomPassword',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRandomPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_random_password_with_options_async(
        self,
        request: main_models.GetRandomPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRandomPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_characters):
            query['ExcludeCharacters'] = request.exclude_characters
        if not DaraCore.is_null(request.exclude_lowercase):
            query['ExcludeLowercase'] = request.exclude_lowercase
        if not DaraCore.is_null(request.exclude_numbers):
            query['ExcludeNumbers'] = request.exclude_numbers
        if not DaraCore.is_null(request.exclude_punctuation):
            query['ExcludePunctuation'] = request.exclude_punctuation
        if not DaraCore.is_null(request.exclude_uppercase):
            query['ExcludeUppercase'] = request.exclude_uppercase
        if not DaraCore.is_null(request.password_length):
            query['PasswordLength'] = request.password_length
        if not DaraCore.is_null(request.require_each_included_type):
            query['RequireEachIncludedType'] = request.require_each_included_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRandomPassword',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRandomPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_random_password(
        self,
        request: main_models.GetRandomPasswordRequest,
    ) -> main_models.GetRandomPasswordResponse:
        runtime = RuntimeOptions()
        return self.get_random_password_with_options(request, runtime)

    async def get_random_password_async(
        self,
        request: main_models.GetRandomPasswordRequest,
    ) -> main_models.GetRandomPasswordResponse:
        runtime = RuntimeOptions()
        return await self.get_random_password_with_options_async(request, runtime)

    def get_secret_policy_with_options(
        self,
        request: main_models.GetSecretPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_policy_with_options_async(
        self,
        request: main_models.GetSecretPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_policy(
        self,
        request: main_models.GetSecretPolicyRequest,
    ) -> main_models.GetSecretPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_secret_policy_with_options(request, runtime)

    async def get_secret_policy_async(
        self,
        request: main_models.GetSecretPolicyRequest,
    ) -> main_models.GetSecretPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_policy_with_options_async(request, runtime)

    def get_secret_value_with_options(
        self,
        request: main_models.GetSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.fetch_extended_config):
            query['FetchExtendedConfig'] = request.fetch_extended_config
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_value_with_options_async(
        self,
        request: main_models.GetSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.fetch_extended_config):
            query['FetchExtendedConfig'] = request.fetch_extended_config
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_value(
        self,
        request: main_models.GetSecretValueRequest,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    async def get_secret_value_async(
        self,
        request: main_models.GetSecretValueRequest,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_value_with_options_async(request, runtime)

    def import_key_material_with_options(
        self,
        request: main_models.ImportKeyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted_key_material):
            query['EncryptedKeyMaterial'] = request.encrypted_key_material
        if not DaraCore.is_null(request.import_token):
            query['ImportToken'] = request.import_token
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_material_expire_unix):
            query['KeyMaterialExpireUnix'] = request.key_material_expire_unix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyMaterial',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_material_with_options_async(
        self,
        request: main_models.ImportKeyMaterialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted_key_material):
            query['EncryptedKeyMaterial'] = request.encrypted_key_material
        if not DaraCore.is_null(request.import_token):
            query['ImportToken'] = request.import_token
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.key_material_expire_unix):
            query['KeyMaterialExpireUnix'] = request.key_material_expire_unix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyMaterial',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_material(
        self,
        request: main_models.ImportKeyMaterialRequest,
    ) -> main_models.ImportKeyMaterialResponse:
        runtime = RuntimeOptions()
        return self.import_key_material_with_options(request, runtime)

    async def import_key_material_async(
        self,
        request: main_models.ImportKeyMaterialRequest,
    ) -> main_models.ImportKeyMaterialResponse:
        runtime = RuntimeOptions()
        return await self.import_key_material_with_options_async(request, runtime)

    def list_aliases_with_options(
        self,
        request: main_models.ListAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliases',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        request: main_models.ListAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliases',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        request: main_models.ListAliasesRequest,
    ) -> main_models.ListAliasesResponse:
        runtime = RuntimeOptions()
        return self.list_aliases_with_options(request, runtime)

    async def list_aliases_async(
        self,
        request: main_models.ListAliasesRequest,
    ) -> main_models.ListAliasesResponse:
        runtime = RuntimeOptions()
        return await self.list_aliases_with_options_async(request, runtime)

    def list_aliases_by_key_id_with_options(
        self,
        request: main_models.ListAliasesByKeyIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesByKeyIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliasesByKeyId',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesByKeyIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_by_key_id_with_options_async(
        self,
        request: main_models.ListAliasesByKeyIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesByKeyIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliasesByKeyId',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesByKeyIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases_by_key_id(
        self,
        request: main_models.ListAliasesByKeyIdRequest,
    ) -> main_models.ListAliasesByKeyIdResponse:
        runtime = RuntimeOptions()
        return self.list_aliases_by_key_id_with_options(request, runtime)

    async def list_aliases_by_key_id_async(
        self,
        request: main_models.ListAliasesByKeyIdRequest,
    ) -> main_models.ListAliasesByKeyIdResponse:
        runtime = RuntimeOptions()
        return await self.list_aliases_by_key_id_with_options_async(request, runtime)

    def list_application_access_points_with_options(
        self,
        request: main_models.ListApplicationAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccessPoints',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_access_points_with_options_async(
        self,
        request: main_models.ListApplicationAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccessPoints',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_access_points(
        self,
        request: main_models.ListApplicationAccessPointsRequest,
    ) -> main_models.ListApplicationAccessPointsResponse:
        runtime = RuntimeOptions()
        return self.list_application_access_points_with_options(request, runtime)

    async def list_application_access_points_async(
        self,
        request: main_models.ListApplicationAccessPointsRequest,
    ) -> main_models.ListApplicationAccessPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_access_points_with_options_async(request, runtime)

    def list_client_keys_with_options(
        self,
        request: main_models.ListClientKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientKeysResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientKeys',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_keys_with_options_async(
        self,
        request: main_models.ListClientKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientKeysResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientKeys',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_keys(
        self,
        request: main_models.ListClientKeysRequest,
    ) -> main_models.ListClientKeysResponse:
        runtime = RuntimeOptions()
        return self.list_client_keys_with_options(request, runtime)

    async def list_client_keys_async(
        self,
        request: main_models.ListClientKeysRequest,
    ) -> main_models.ListClientKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_client_keys_with_options_async(request, runtime)

    def list_key_versions_with_options(
        self,
        request: main_models.ListKeyVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeyVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeyVersions',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_key_versions_with_options_async(
        self,
        request: main_models.ListKeyVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeyVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeyVersions',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_key_versions(
        self,
        request: main_models.ListKeyVersionsRequest,
    ) -> main_models.ListKeyVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_key_versions_with_options(request, runtime)

    async def list_key_versions_async(
        self,
        request: main_models.ListKeyVersionsRequest,
    ) -> main_models.ListKeyVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_key_versions_with_options_async(request, runtime)

    def list_keys_with_options(
        self,
        request: main_models.ListKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeys',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keys_with_options_async(
        self,
        request: main_models.ListKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeys',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keys(
        self,
        request: main_models.ListKeysRequest,
    ) -> main_models.ListKeysResponse:
        runtime = RuntimeOptions()
        return self.list_keys_with_options(request, runtime)

    async def list_keys_async(
        self,
        request: main_models.ListKeysRequest,
    ) -> main_models.ListKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_keys_with_options_async(request, runtime)

    def list_kms_instances_with_options(
        self,
        request: main_models.ListKmsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKmsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKmsInstances',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKmsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kms_instances_with_options_async(
        self,
        request: main_models.ListKmsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKmsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKmsInstances',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKmsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kms_instances(
        self,
        request: main_models.ListKmsInstancesRequest,
    ) -> main_models.ListKmsInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_kms_instances_with_options(request, runtime)

    async def list_kms_instances_async(
        self,
        request: main_models.ListKmsInstancesRequest,
    ) -> main_models.ListKmsInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_kms_instances_with_options_async(request, runtime)

    def list_network_rules_with_options(
        self,
        request: main_models.ListNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkRules',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_rules_with_options_async(
        self,
        request: main_models.ListNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkRules',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_rules(
        self,
        request: main_models.ListNetworkRulesRequest,
    ) -> main_models.ListNetworkRulesResponse:
        runtime = RuntimeOptions()
        return self.list_network_rules_with_options(request, runtime)

    async def list_network_rules_async(
        self,
        request: main_models.ListNetworkRulesRequest,
    ) -> main_models.ListNetworkRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_network_rules_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_resource_tags_with_options(
        self,
        request: main_models.ListResourceTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTags',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_tags_with_options_async(
        self,
        request: main_models.ListResourceTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTags',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_tags(
        self,
        request: main_models.ListResourceTagsRequest,
    ) -> main_models.ListResourceTagsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    async def list_resource_tags_async(
        self,
        request: main_models.ListResourceTagsRequest,
    ) -> main_models.ListResourceTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_tags_with_options_async(request, runtime)

    def list_secret_version_ids_with_options(
        self,
        request: main_models.ListSecretVersionIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretVersionIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_deprecated):
            query['IncludeDeprecated'] = request.include_deprecated
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretVersionIds',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretVersionIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_version_ids_with_options_async(
        self,
        request: main_models.ListSecretVersionIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretVersionIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_deprecated):
            query['IncludeDeprecated'] = request.include_deprecated
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretVersionIds',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretVersionIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_version_ids(
        self,
        request: main_models.ListSecretVersionIdsRequest,
    ) -> main_models.ListSecretVersionIdsResponse:
        runtime = RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    async def list_secret_version_ids_async(
        self,
        request: main_models.ListSecretVersionIdsRequest,
    ) -> main_models.ListSecretVersionIdsResponse:
        runtime = RuntimeOptions()
        return await self.list_secret_version_ids_with_options_async(request, runtime)

    def list_secrets_with_options(
        self,
        request: main_models.ListSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: main_models.ListSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    async def list_secrets_async(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        return await self.list_secrets_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def open_kms_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenKmsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenKmsService',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenKmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_kms_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenKmsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenKmsService',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenKmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_kms_service(self) -> main_models.OpenKmsServiceResponse:
        runtime = RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    async def open_kms_service_async(self) -> main_models.OpenKmsServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_kms_service_with_options_async(runtime)

    def put_secret_value_with_options(
        self,
        request: main_models.PutSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_data):
            query['SecretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.version_stages):
            query['VersionStages'] = request.version_stages
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutSecretValue',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_secret_value_with_options_async(
        self,
        request: main_models.PutSecretValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutSecretValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_data):
            query['SecretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.version_stages):
            query['VersionStages'] = request.version_stages
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutSecretValue',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_secret_value(
        self,
        request: main_models.PutSecretValueRequest,
    ) -> main_models.PutSecretValueResponse:
        runtime = RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    async def put_secret_value_async(
        self,
        request: main_models.PutSecretValueRequest,
    ) -> main_models.PutSecretValueResponse:
        runtime = RuntimeOptions()
        return await self.put_secret_value_with_options_async(request, runtime)

    def re_encrypt_with_options(
        self,
        tmp_req: main_models.ReEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReEncryptResponse:
        tmp_req.validate()
        request = main_models.ReEncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        if not DaraCore.is_null(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.destination_encryption_context_shrink):
            query['DestinationEncryptionContext'] = request.destination_encryption_context_shrink
        if not DaraCore.is_null(request.destination_key_id):
            query['DestinationKeyId'] = request.destination_key_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.source_encryption_algorithm):
            query['SourceEncryptionAlgorithm'] = request.source_encryption_algorithm
        if not DaraCore.is_null(request.source_encryption_context_shrink):
            query['SourceEncryptionContext'] = request.source_encryption_context_shrink
        if not DaraCore.is_null(request.source_key_id):
            query['SourceKeyId'] = request.source_key_id
        if not DaraCore.is_null(request.source_key_version_id):
            query['SourceKeyVersionId'] = request.source_key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReEncrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_encrypt_with_options_async(
        self,
        tmp_req: main_models.ReEncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReEncryptResponse:
        tmp_req.validate()
        request = main_models.ReEncryptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        if not DaraCore.is_null(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        query = {}
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.destination_encryption_context_shrink):
            query['DestinationEncryptionContext'] = request.destination_encryption_context_shrink
        if not DaraCore.is_null(request.destination_key_id):
            query['DestinationKeyId'] = request.destination_key_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.source_encryption_algorithm):
            query['SourceEncryptionAlgorithm'] = request.source_encryption_algorithm
        if not DaraCore.is_null(request.source_encryption_context_shrink):
            query['SourceEncryptionContext'] = request.source_encryption_context_shrink
        if not DaraCore.is_null(request.source_key_id):
            query['SourceKeyId'] = request.source_key_id
        if not DaraCore.is_null(request.source_key_version_id):
            query['SourceKeyVersionId'] = request.source_key_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReEncrypt',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_encrypt(
        self,
        request: main_models.ReEncryptRequest,
    ) -> main_models.ReEncryptResponse:
        runtime = RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    async def re_encrypt_async(
        self,
        request: main_models.ReEncryptRequest,
    ) -> main_models.ReEncryptResponse:
        runtime = RuntimeOptions()
        return await self.re_encrypt_with_options_async(request, runtime)

    def release_kms_instance_with_options(
        self,
        request: main_models.ReleaseKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_without_backup):
            query['ForceDeleteWithoutBackup'] = request.force_delete_without_backup
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_kms_instance_with_options_async(
        self,
        request: main_models.ReleaseKmsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseKmsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_without_backup):
            query['ForceDeleteWithoutBackup'] = request.force_delete_without_backup
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseKmsInstance',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_kms_instance(
        self,
        request: main_models.ReleaseKmsInstanceRequest,
    ) -> main_models.ReleaseKmsInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_kms_instance_with_options(request, runtime)

    async def release_kms_instance_async(
        self,
        request: main_models.ReleaseKmsInstanceRequest,
    ) -> main_models.ReleaseKmsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_kms_instance_with_options_async(request, runtime)

    def restore_secret_with_options(
        self,
        request: main_models.RestoreSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_secret_with_options_async(
        self,
        request: main_models.RestoreSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_secret(
        self,
        request: main_models.RestoreSecretRequest,
    ) -> main_models.RestoreSecretResponse:
        runtime = RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    async def restore_secret_async(
        self,
        request: main_models.RestoreSecretRequest,
    ) -> main_models.RestoreSecretResponse:
        runtime = RuntimeOptions()
        return await self.restore_secret_with_options_async(request, runtime)

    def rotate_secret_with_options(
        self,
        request: main_models.RotateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RotateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RotateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RotateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def rotate_secret_with_options_async(
        self,
        request: main_models.RotateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RotateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RotateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RotateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rotate_secret(
        self,
        request: main_models.RotateSecretRequest,
    ) -> main_models.RotateSecretResponse:
        runtime = RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    async def rotate_secret_async(
        self,
        request: main_models.RotateSecretRequest,
    ) -> main_models.RotateSecretResponse:
        runtime = RuntimeOptions()
        return await self.rotate_secret_with_options_async(request, runtime)

    def schedule_key_deletion_with_options(
        self,
        request: main_models.ScheduleKeyDeletionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScheduleKeyDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.pending_window_in_days):
            query['PendingWindowInDays'] = request.pending_window_in_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScheduleKeyDeletion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScheduleKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def schedule_key_deletion_with_options_async(
        self,
        request: main_models.ScheduleKeyDeletionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScheduleKeyDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.pending_window_in_days):
            query['PendingWindowInDays'] = request.pending_window_in_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScheduleKeyDeletion',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScheduleKeyDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def schedule_key_deletion(
        self,
        request: main_models.ScheduleKeyDeletionRequest,
    ) -> main_models.ScheduleKeyDeletionResponse:
        runtime = RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    async def schedule_key_deletion_async(
        self,
        request: main_models.ScheduleKeyDeletionRequest,
    ) -> main_models.ScheduleKeyDeletionResponse:
        runtime = RuntimeOptions()
        return await self.schedule_key_deletion_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: main_models.SetDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not DaraCore.is_null(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.protected_resource_arn):
            query['ProtectedResourceArn'] = request.protected_resource_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeletionProtection',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: main_models.SetDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not DaraCore.is_null(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not DaraCore.is_null(request.protected_resource_arn):
            query['ProtectedResourceArn'] = request.protected_resource_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeletionProtection',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_deletion_protection(
        self,
        request: main_models.SetDeletionProtectionRequest,
    ) -> main_models.SetDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: main_models.SetDeletionProtectionRequest,
    ) -> main_models.SetDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def set_key_policy_with_options(
        self,
        request: main_models.SetKeyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetKeyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetKeyPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetKeyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_key_policy_with_options_async(
        self,
        request: main_models.SetKeyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetKeyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetKeyPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetKeyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_key_policy(
        self,
        request: main_models.SetKeyPolicyRequest,
    ) -> main_models.SetKeyPolicyResponse:
        runtime = RuntimeOptions()
        return self.set_key_policy_with_options(request, runtime)

    async def set_key_policy_async(
        self,
        request: main_models.SetKeyPolicyRequest,
    ) -> main_models.SetKeyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.set_key_policy_with_options_async(request, runtime)

    def set_secret_policy_with_options(
        self,
        request: main_models.SetSecretPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecretPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecretPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSecretPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_secret_policy_with_options_async(
        self,
        request: main_models.SetSecretPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecretPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecretPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSecretPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_secret_policy(
        self,
        request: main_models.SetSecretPolicyRequest,
    ) -> main_models.SetSecretPolicyResponse:
        runtime = RuntimeOptions()
        return self.set_secret_policy_with_options(request, runtime)

    async def set_secret_policy_async(
        self,
        request: main_models.SetSecretPolicyRequest,
    ) -> main_models.SetSecretPolicyResponse:
        runtime = RuntimeOptions()
        return await self.set_secret_policy_with_options_async(request, runtime)

    def tag_resource_with_options(
        self,
        request: main_models.TagResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResource',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resource_with_options_async(
        self,
        request: main_models.TagResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResource',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resource(
        self,
        request: main_models.TagResourceRequest,
    ) -> main_models.TagResourceResponse:
        runtime = RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    async def tag_resource_async(
        self,
        request: main_models.TagResourceRequest,
    ) -> main_models.TagResourceResponse:
        runtime = RuntimeOptions()
        return await self.tag_resource_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resource_with_options(
        self,
        request: main_models.UntagResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResource',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resource_with_options_async(
        self,
        request: main_models.UntagResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResource',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resource(
        self,
        request: main_models.UntagResourceRequest,
    ) -> main_models.UntagResourceResponse:
        runtime = RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

    async def untag_resource_async(
        self,
        request: main_models.UntagResourceRequest,
    ) -> main_models.UntagResourceResponse:
        runtime = RuntimeOptions()
        return await self.untag_resource_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_alias_with_options(
        self,
        request: main_models.UpdateAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        request: main_models.UpdateAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlias',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        request: main_models.UpdateAliasRequest,
    ) -> main_models.UpdateAliasResponse:
        runtime = RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    async def update_alias_async(
        self,
        request: main_models.UpdateAliasRequest,
    ) -> main_models.UpdateAliasResponse:
        runtime = RuntimeOptions()
        return await self.update_alias_with_options_async(request, runtime)

    def update_application_access_point_with_options(
        self,
        request: main_models.UpdateApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_access_point_with_options_async(
        self,
        request: main_models.UpdateApplicationAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAccessPoint',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_access_point(
        self,
        request: main_models.UpdateApplicationAccessPointRequest,
    ) -> main_models.UpdateApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return self.update_application_access_point_with_options(request, runtime)

    async def update_application_access_point_async(
        self,
        request: main_models.UpdateApplicationAccessPointRequest,
    ) -> main_models.UpdateApplicationAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.update_application_access_point_with_options_async(request, runtime)

    def update_key_description_with_options(
        self,
        request: main_models.UpdateKeyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKeyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKeyDescription',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKeyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_key_description_with_options_async(
        self,
        request: main_models.UpdateKeyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKeyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKeyDescription',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKeyDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_key_description(
        self,
        request: main_models.UpdateKeyDescriptionRequest,
    ) -> main_models.UpdateKeyDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    async def update_key_description_async(
        self,
        request: main_models.UpdateKeyDescriptionRequest,
    ) -> main_models.UpdateKeyDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_key_description_with_options_async(request, runtime)

    def update_kms_instance_bind_vpc_with_options(
        self,
        request: main_models.UpdateKmsInstanceBindVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKmsInstanceBindVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_vpcs):
            query['BindVpcs'] = request.bind_vpcs
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKmsInstanceBindVpc',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKmsInstanceBindVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kms_instance_bind_vpc_with_options_async(
        self,
        request: main_models.UpdateKmsInstanceBindVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKmsInstanceBindVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_vpcs):
            query['BindVpcs'] = request.bind_vpcs
        if not DaraCore.is_null(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKmsInstanceBindVpc',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKmsInstanceBindVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kms_instance_bind_vpc(
        self,
        request: main_models.UpdateKmsInstanceBindVpcRequest,
    ) -> main_models.UpdateKmsInstanceBindVpcResponse:
        runtime = RuntimeOptions()
        return self.update_kms_instance_bind_vpc_with_options(request, runtime)

    async def update_kms_instance_bind_vpc_async(
        self,
        request: main_models.UpdateKmsInstanceBindVpcRequest,
    ) -> main_models.UpdateKmsInstanceBindVpcResponse:
        runtime = RuntimeOptions()
        return await self.update_kms_instance_bind_vpc_with_options_async(request, runtime)

    def update_network_rule_with_options(
        self,
        request: main_models.UpdateNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_rule_with_options_async(
        self,
        request: main_models.UpdateNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkRule',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_rule(
        self,
        request: main_models.UpdateNetworkRuleRequest,
    ) -> main_models.UpdateNetworkRuleResponse:
        runtime = RuntimeOptions()
        return self.update_network_rule_with_options(request, runtime)

    async def update_network_rule_async(
        self,
        request: main_models.UpdateNetworkRuleRequest,
    ) -> main_models.UpdateNetworkRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_network_rule_with_options_async(request, runtime)

    def update_policy_with_options(
        self,
        request: main_models.UpdatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        request: main_models.UpdatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        return self.update_policy_with_options(request, runtime)

    async def update_policy_async(
        self,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_policy_with_options_async(request, runtime)

    def update_rotation_policy_with_options(
        self,
        request: main_models.UpdateRotationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRotationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRotationPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rotation_policy_with_options_async(
        self,
        request: main_models.UpdateRotationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRotationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRotationPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRotationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rotation_policy(
        self,
        request: main_models.UpdateRotationPolicyRequest,
    ) -> main_models.UpdateRotationPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    async def update_rotation_policy_async(
        self,
        request: main_models.UpdateRotationPolicyRequest,
    ) -> main_models.UpdateRotationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_rotation_policy_with_options_async(request, runtime)

    def update_secret_with_options(
        self,
        request: main_models.UpdateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.extended_config):
            query['ExtendedConfig'] = request.extended_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        request: main_models.UpdateSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.extended_config):
            query['ExtendedConfig'] = request.extended_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        return self.update_secret_with_options(request, runtime)

    async def update_secret_async(
        self,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        return await self.update_secret_with_options_async(request, runtime)

    def update_secret_rotation_policy_with_options(
        self,
        request: main_models.UpdateSecretRotationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretRotationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretRotationPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_rotation_policy_with_options_async(
        self,
        request: main_models.UpdateSecretRotationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretRotationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not DaraCore.is_null(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretRotationPolicy',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretRotationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_rotation_policy(
        self,
        request: main_models.UpdateSecretRotationPolicyRequest,
    ) -> main_models.UpdateSecretRotationPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    async def update_secret_rotation_policy_async(
        self,
        request: main_models.UpdateSecretRotationPolicyRequest,
    ) -> main_models.UpdateSecretRotationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_secret_rotation_policy_with_options_async(request, runtime)

    def update_secret_version_stage_with_options(
        self,
        request: main_models.UpdateSecretVersionStageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretVersionStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.move_to_version):
            query['MoveToVersion'] = request.move_to_version
        if not DaraCore.is_null(request.remove_from_version):
            query['RemoveFromVersion'] = request.remove_from_version
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretVersionStage',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretVersionStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_version_stage_with_options_async(
        self,
        request: main_models.UpdateSecretVersionStageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretVersionStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.move_to_version):
            query['MoveToVersion'] = request.move_to_version
        if not DaraCore.is_null(request.remove_from_version):
            query['RemoveFromVersion'] = request.remove_from_version
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretVersionStage',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretVersionStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_version_stage(
        self,
        request: main_models.UpdateSecretVersionStageRequest,
    ) -> main_models.UpdateSecretVersionStageResponse:
        runtime = RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    async def update_secret_version_stage_async(
        self,
        request: main_models.UpdateSecretVersionStageRequest,
    ) -> main_models.UpdateSecretVersionStageResponse:
        runtime = RuntimeOptions()
        return await self.update_secret_version_stage_with_options_async(request, runtime)

    def verify_mac_with_options(
        self,
        request: main_models.VerifyMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyMac',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_mac_with_options_async(
        self,
        request: main_models.VerifyMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyMac',
            version = '2016-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_mac(
        self,
        request: main_models.VerifyMacRequest,
    ) -> main_models.VerifyMacResponse:
        runtime = RuntimeOptions()
        return self.verify_mac_with_options(request, runtime)

    async def verify_mac_async(
        self,
        request: main_models.VerifyMacRequest,
    ) -> main_models.VerifyMacResponse:
        runtime = RuntimeOptions()
        return await self.verify_mac_with_options_async(request, runtime)
