# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_kms20160120 import models as kms_20160120_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def asymmetric_decrypt_with_options(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricDecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_decrypt_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricDecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_decrypt(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    async def asymmetric_decrypt_async(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_decrypt_with_options_async(request, runtime)

    def asymmetric_encrypt_with_options(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_encrypt_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_encrypt(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    async def asymmetric_encrypt_async(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_encrypt_with_options_async(request, runtime)

    def asymmetric_sign_with_options(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricSign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_sign_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricSign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_sign(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    async def asymmetric_sign_async(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_sign_with_options_async(request, runtime)

    def asymmetric_verify_with_options(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def asymmetric_verify_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asymmetric_verify(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    async def asymmetric_verify_async(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_verify_with_options_async(request, runtime)

    def cancel_key_deletion_with_options(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CancelKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_key_deletion_with_options_async(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CancelKeyDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_key_deletion(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    async def cancel_key_deletion_async(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_key_deletion_with_options_async(request, runtime)

    def certificate_private_key_decrypt_with_options(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeyDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeyDecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def certificate_private_key_decrypt_with_options_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeyDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeyDecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def certificate_private_key_decrypt(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_decrypt_with_options(request, runtime)

    async def certificate_private_key_decrypt_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.certificate_private_key_decrypt_with_options_async(request, runtime)

    def certificate_private_key_sign_with_options(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeySign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeySignResponse(),
            self.call_api(params, req, runtime)
        )

    async def certificate_private_key_sign_with_options_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeySign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeySignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def certificate_private_key_sign(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_sign_with_options(request, runtime)

    async def certificate_private_key_sign_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.certificate_private_key_sign_with_options_async(request, runtime)

    def certificate_public_key_encrypt_with_options(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def certificate_public_key_encrypt_with_options_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def certificate_public_key_encrypt(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_encrypt_with_options(request, runtime)

    async def certificate_public_key_encrypt_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.certificate_public_key_encrypt_with_options_async(request, runtime)

    def certificate_public_key_verify_with_options(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signature_value):
            query['SignatureValue'] = request.signature_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def certificate_public_key_verify_with_options_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signature_value):
            query['SignatureValue'] = request.signature_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def certificate_public_key_verify(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_verify_with_options(request, runtime)

    async def certificate_public_key_verify_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.certificate_public_key_verify_with_options_async(request, runtime)

    def create_alias_with_options(
        self,
        request: kms_20160120_models.CreateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        request: kms_20160120_models.CreateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        request: kms_20160120_models.CreateAliasRequest,
    ) -> kms_20160120_models.CreateAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alias_with_options(request, runtime)

    async def create_alias_async(
        self,
        request: kms_20160120_models.CreateAliasRequest,
    ) -> kms_20160120_models.CreateAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alias_with_options_async(request, runtime)

    def create_certificate_with_options(
        self,
        tmp_req: kms_20160120_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateCertificateResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateCertificateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subject_alternative_names):
            request.subject_alternative_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subject_alternative_names, 'SubjectAlternativeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.exportable_private_key):
            query['ExportablePrivateKey'] = request.exportable_private_key
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.subject_alternative_names_shrink):
            query['SubjectAlternativeNames'] = request.subject_alternative_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_with_options_async(
        self,
        tmp_req: kms_20160120_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateCertificateResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateCertificateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subject_alternative_names):
            request.subject_alternative_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subject_alternative_names, 'SubjectAlternativeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.exportable_private_key):
            query['ExportablePrivateKey'] = request.exportable_private_key
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.subject_alternative_names_shrink):
            query['SubjectAlternativeNames'] = request.subject_alternative_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate(
        self,
        request: kms_20160120_models.CreateCertificateRequest,
    ) -> kms_20160120_models.CreateCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    async def create_certificate_async(
        self,
        request: kms_20160120_models.CreateCertificateRequest,
    ) -> kms_20160120_models.CreateCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_options_async(request, runtime)

    def create_key_with_options(
        self,
        request: kms_20160120_models.CreateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_with_options_async(
        self,
        request: kms_20160120_models.CreateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key(
        self,
        request: kms_20160120_models.CreateKeyRequest,
    ) -> kms_20160120_models.CreateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    async def create_key_async(
        self,
        request: kms_20160120_models.CreateKeyRequest,
    ) -> kms_20160120_models.CreateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_key_with_options_async(request, runtime)

    def create_key_version_with_options(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_version_with_options_async(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_version(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_key_version_with_options(request, runtime)

    async def create_key_version_async(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_key_version_with_options_async(request, runtime)

    def create_secret_with_options(
        self,
        tmp_req: kms_20160120_models.CreateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateSecretResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        tmp_req: kms_20160120_models.CreateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateSecretResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: kms_20160120_models.CreateSecretRequest,
    ) -> kms_20160120_models.CreateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    async def create_secret_async(
        self,
        request: kms_20160120_models.CreateSecretRequest,
    ) -> kms_20160120_models.CreateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        tmp_req: kms_20160120_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DecryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.DecryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Decrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_with_options_async(
        self,
        tmp_req: kms_20160120_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DecryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.DecryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Decrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrypt(
        self,
        request: kms_20160120_models.DecryptRequest,
    ) -> kms_20160120_models.DecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: kms_20160120_models.DecryptRequest,
    ) -> kms_20160120_models.DecryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_alias_with_options(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
    ) -> kms_20160120_models.DeleteAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alias_with_options(request, runtime)

    async def delete_alias_async(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
    ) -> kms_20160120_models.DeleteAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alias_with_options_async(request, runtime)

    def delete_certificate_with_options(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_certificate_with_options_async(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_certificate(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    async def delete_certificate_async(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_certificate_with_options_async(request, runtime)

    def delete_key_material_with_options(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_material_with_options_async(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteKeyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_material(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    async def delete_key_material_async(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_material_with_options_async(request, runtime)

    def delete_secret_with_options(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_without_recovery):
            query['ForceDeleteWithoutRecovery'] = request.force_delete_without_recovery
        if not UtilClient.is_unset(request.recovery_window_in_days):
            query['RecoveryWindowInDays'] = request.recovery_window_in_days
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_without_recovery):
            query['ForceDeleteWithoutRecovery'] = request.force_delete_without_recovery
        if not UtilClient.is_unset(request.recovery_window_in_days):
            query['RecoveryWindowInDays'] = request.recovery_window_in_days
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
    ) -> kms_20160120_models.DeleteSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    async def delete_secret_async(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
    ) -> kms_20160120_models.DeleteSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_with_options_async(request, runtime)

    def describe_account_kms_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAccountKmsStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeAccountKmsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_kms_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAccountKmsStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeAccountKmsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_kms_status(self) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_kms_status_with_options(runtime)

    async def describe_account_kms_status_async(self) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_kms_status_with_options_async(runtime)

    def describe_certificate_with_options(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_with_options_async(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_with_options(request, runtime)

    async def describe_certificate_async(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_with_options_async(request, runtime)

    def describe_key_with_options(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_with_options_async(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
    ) -> kms_20160120_models.DescribeKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    async def describe_key_async(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
    ) -> kms_20160120_models.DescribeKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_with_options_async(request, runtime)

    def describe_key_version_with_options(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_version_with_options_async(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key_version(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_key_version_with_options(request, runtime)

    async def describe_key_version_async(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_version_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> kms_20160120_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> kms_20160120_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_secret_with_options(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
    ) -> kms_20160120_models.DescribeSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    async def describe_secret_async(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
    ) -> kms_20160120_models.DescribeSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_secret_with_options_async(request, runtime)

    def disable_key_with_options(
        self,
        request: kms_20160120_models.DisableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DisableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_key_with_options_async(
        self,
        request: kms_20160120_models.DisableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DisableKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_key(
        self,
        request: kms_20160120_models.DisableKeyRequest,
    ) -> kms_20160120_models.DisableKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_key_with_options(request, runtime)

    async def disable_key_async(
        self,
        request: kms_20160120_models.DisableKeyRequest,
    ) -> kms_20160120_models.DisableKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_key_with_options_async(request, runtime)

    def enable_key_with_options(
        self,
        request: kms_20160120_models.EnableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EnableKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EnableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_key_with_options_async(
        self,
        request: kms_20160120_models.EnableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EnableKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EnableKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_key(
        self,
        request: kms_20160120_models.EnableKeyRequest,
    ) -> kms_20160120_models.EnableKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_key_with_options(request, runtime)

    async def enable_key_async(
        self,
        request: kms_20160120_models.EnableKeyRequest,
    ) -> kms_20160120_models.EnableKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_key_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        tmp_req: kms_20160120_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EncryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.EncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Encrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_with_options_async(
        self,
        tmp_req: kms_20160120_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EncryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.EncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Encrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt(
        self,
        request: kms_20160120_models.EncryptRequest,
    ) -> kms_20160120_models.EncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: kms_20160120_models.EncryptRequest,
    ) -> kms_20160120_models.EncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def export_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.ExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_data_key_with_options_async(
        self,
        tmp_req: kms_20160120_models.ExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ExportDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_data_key(
        self,
        request: kms_20160120_models.ExportDataKeyRequest,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_data_key_with_options(request, runtime)

    async def export_data_key_async(
        self,
        request: kms_20160120_models.ExportDataKeyRequest,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_data_key_with_options_async(request, runtime)

    def generate_and_export_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateAndExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateAndExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAndExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateAndExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_and_export_data_key_with_options_async(
        self,
        tmp_req: kms_20160120_models.GenerateAndExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateAndExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAndExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateAndExportDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_and_export_data_key(
        self,
        request: kms_20160120_models.GenerateAndExportDataKeyRequest,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_and_export_data_key_with_options(request, runtime)

    async def generate_and_export_data_key_async(
        self,
        request: kms_20160120_models.GenerateAndExportDataKeyRequest,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_and_export_data_key_with_options_async(request, runtime)

    def generate_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_data_key_with_options_async(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_data_key(
        self,
        request: kms_20160120_models.GenerateDataKeyRequest,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    async def generate_data_key_async(
        self,
        request: kms_20160120_models.GenerateDataKeyRequest,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_data_key_with_options_async(request, runtime)

    def generate_data_key_without_plaintext_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKeyWithoutPlaintext',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_data_key_without_plaintext_with_options_async(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKeyWithoutPlaintext',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_data_key_without_plaintext(
        self,
        request: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    async def generate_data_key_without_plaintext_async(
        self,
        request: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_data_key_without_plaintext_with_options_async(request, runtime)

    def get_certificate_with_options(
        self,
        request: kms_20160120_models.GetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_certificate_with_options_async(
        self,
        request: kms_20160120_models.GetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_certificate(
        self,
        request: kms_20160120_models.GetCertificateRequest,
    ) -> kms_20160120_models.GetCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    async def get_certificate_async(
        self,
        request: kms_20160120_models.GetCertificateRequest,
    ) -> kms_20160120_models.GetCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_certificate_with_options_async(request, runtime)

    def get_parameters_for_import_with_options(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParametersForImport',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetParametersForImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_for_import_with_options_async(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParametersForImport',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetParametersForImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters_for_import(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_for_import_with_options(request, runtime)

    async def get_parameters_for_import_async(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_for_import_with_options_async(request, runtime)

    def get_public_key_with_options(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_key_with_options_async(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_key(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    async def get_public_key_async(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_public_key_with_options_async(request, runtime)

    def get_random_password_with_options(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_characters):
            query['ExcludeCharacters'] = request.exclude_characters
        if not UtilClient.is_unset(request.exclude_lowercase):
            query['ExcludeLowercase'] = request.exclude_lowercase
        if not UtilClient.is_unset(request.exclude_numbers):
            query['ExcludeNumbers'] = request.exclude_numbers
        if not UtilClient.is_unset(request.exclude_punctuation):
            query['ExcludePunctuation'] = request.exclude_punctuation
        if not UtilClient.is_unset(request.exclude_uppercase):
            query['ExcludeUppercase'] = request.exclude_uppercase
        if not UtilClient.is_unset(request.password_length):
            query['PasswordLength'] = request.password_length
        if not UtilClient.is_unset(request.require_each_included_type):
            query['RequireEachIncludedType'] = request.require_each_included_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRandomPassword',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetRandomPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_random_password_with_options_async(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_characters):
            query['ExcludeCharacters'] = request.exclude_characters
        if not UtilClient.is_unset(request.exclude_lowercase):
            query['ExcludeLowercase'] = request.exclude_lowercase
        if not UtilClient.is_unset(request.exclude_numbers):
            query['ExcludeNumbers'] = request.exclude_numbers
        if not UtilClient.is_unset(request.exclude_punctuation):
            query['ExcludePunctuation'] = request.exclude_punctuation
        if not UtilClient.is_unset(request.exclude_uppercase):
            query['ExcludeUppercase'] = request.exclude_uppercase
        if not UtilClient.is_unset(request.password_length):
            query['PasswordLength'] = request.password_length
        if not UtilClient.is_unset(request.require_each_included_type):
            query['RequireEachIncludedType'] = request.require_each_included_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRandomPassword',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetRandomPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_random_password(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_random_password_with_options(request, runtime)

    async def get_random_password_async(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_random_password_with_options_async(request, runtime)

    def get_secret_value_with_options(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_extended_config):
            query['FetchExtendedConfig'] = request.fetch_extended_config
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_value_with_options_async(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_extended_config):
            query['FetchExtendedConfig'] = request.fetch_extended_config
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_value(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
    ) -> kms_20160120_models.GetSecretValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    async def get_secret_value_async(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
    ) -> kms_20160120_models.GetSecretValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_value_with_options_async(request, runtime)

    def import_key_material_with_options(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypted_key_material):
            query['EncryptedKeyMaterial'] = request.encrypted_key_material
        if not UtilClient.is_unset(request.import_token):
            query['ImportToken'] = request.import_token
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_material_expire_unix):
            query['KeyMaterialExpireUnix'] = request.key_material_expire_unix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ImportKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_material_with_options_async(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypted_key_material):
            query['EncryptedKeyMaterial'] = request.encrypted_key_material
        if not UtilClient.is_unset(request.import_token):
            query['ImportToken'] = request.import_token
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_material_expire_unix):
            query['KeyMaterialExpireUnix'] = request.key_material_expire_unix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ImportKeyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_material(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_key_material_with_options(request, runtime)

    async def import_key_material_async(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_key_material_with_options_async(request, runtime)

    def list_aliases_with_options(
        self,
        request: kms_20160120_models.ListAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        request: kms_20160120_models.ListAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        request: kms_20160120_models.ListAliasesRequest,
    ) -> kms_20160120_models.ListAliasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_with_options(request, runtime)

    async def list_aliases_async(
        self,
        request: kms_20160120_models.ListAliasesRequest,
    ) -> kms_20160120_models.ListAliasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aliases_with_options_async(request, runtime)

    def list_aliases_by_key_id_with_options(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliasesByKeyId',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesByKeyIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_by_key_id_with_options_async(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliasesByKeyId',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesByKeyIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases_by_key_id(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_by_key_id_with_options(request, runtime)

    async def list_aliases_by_key_id_async(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aliases_by_key_id_with_options_async(request, runtime)

    def list_key_versions_with_options(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyVersions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_key_versions_with_options_async(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyVersions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_key_versions(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_key_versions_with_options(request, runtime)

    async def list_key_versions_async(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_key_versions_with_options_async(request, runtime)

    def list_keys_with_options(
        self,
        request: kms_20160120_models.ListKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeys',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keys_with_options_async(
        self,
        request: kms_20160120_models.ListKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeys',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keys(
        self,
        request: kms_20160120_models.ListKeysRequest,
    ) -> kms_20160120_models.ListKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_keys_with_options(request, runtime)

    async def list_keys_async(
        self,
        request: kms_20160120_models.ListKeysRequest,
    ) -> kms_20160120_models.ListKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_keys_with_options_async(request, runtime)

    def list_resource_tags_with_options(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTags',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_tags_with_options_async(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTags',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_tags(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    async def list_resource_tags_async(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_tags_with_options_async(request, runtime)

    def list_secret_version_ids_with_options(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_deprecated):
            query['IncludeDeprecated'] = request.include_deprecated
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretVersionIds',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretVersionIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_version_ids_with_options_async(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_deprecated):
            query['IncludeDeprecated'] = request.include_deprecated
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretVersionIds',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretVersionIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_version_ids(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    async def list_secret_version_ids_async(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_version_ids_with_options_async(request, runtime)

    def list_secrets_with_options(
        self,
        request: kms_20160120_models.ListSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: kms_20160120_models.ListSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: kms_20160120_models.ListSecretsRequest,
    ) -> kms_20160120_models.ListSecretsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    async def list_secrets_async(
        self,
        request: kms_20160120_models.ListSecretsRequest,
    ) -> kms_20160120_models.ListSecretsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_secrets_with_options_async(request, runtime)

    def open_kms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenKmsService',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.OpenKmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_kms_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenKmsService',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.OpenKmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_kms_service(self) -> kms_20160120_models.OpenKmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    async def open_kms_service_async(self) -> kms_20160120_models.OpenKmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_kms_service_with_options_async(runtime)

    def put_secret_value_with_options(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.PutSecretValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stages):
            query['VersionStages'] = request.version_stages
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.PutSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_secret_value_with_options_async(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.PutSecretValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stages):
            query['VersionStages'] = request.version_stages
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.PutSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_secret_value(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
    ) -> kms_20160120_models.PutSecretValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    async def put_secret_value_async(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
    ) -> kms_20160120_models.PutSecretValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_secret_value_with_options_async(request, runtime)

    def re_encrypt_with_options(
        self,
        tmp_req: kms_20160120_models.ReEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReEncryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ReEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.destination_encryption_context_shrink):
            query['DestinationEncryptionContext'] = request.destination_encryption_context_shrink
        if not UtilClient.is_unset(request.destination_key_id):
            query['DestinationKeyId'] = request.destination_key_id
        if not UtilClient.is_unset(request.source_encryption_algorithm):
            query['SourceEncryptionAlgorithm'] = request.source_encryption_algorithm
        if not UtilClient.is_unset(request.source_encryption_context_shrink):
            query['SourceEncryptionContext'] = request.source_encryption_context_shrink
        if not UtilClient.is_unset(request.source_key_id):
            query['SourceKeyId'] = request.source_key_id
        if not UtilClient.is_unset(request.source_key_version_id):
            query['SourceKeyVersionId'] = request.source_key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ReEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_encrypt_with_options_async(
        self,
        tmp_req: kms_20160120_models.ReEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReEncryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ReEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.destination_encryption_context_shrink):
            query['DestinationEncryptionContext'] = request.destination_encryption_context_shrink
        if not UtilClient.is_unset(request.destination_key_id):
            query['DestinationKeyId'] = request.destination_key_id
        if not UtilClient.is_unset(request.source_encryption_algorithm):
            query['SourceEncryptionAlgorithm'] = request.source_encryption_algorithm
        if not UtilClient.is_unset(request.source_encryption_context_shrink):
            query['SourceEncryptionContext'] = request.source_encryption_context_shrink
        if not UtilClient.is_unset(request.source_key_id):
            query['SourceKeyId'] = request.source_key_id
        if not UtilClient.is_unset(request.source_key_version_id):
            query['SourceKeyVersionId'] = request.source_key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ReEncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_encrypt(
        self,
        request: kms_20160120_models.ReEncryptRequest,
    ) -> kms_20160120_models.ReEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    async def re_encrypt_async(
        self,
        request: kms_20160120_models.ReEncryptRequest,
    ) -> kms_20160120_models.ReEncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_encrypt_with_options_async(request, runtime)

    def restore_secret_with_options(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RestoreSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RestoreSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_secret_with_options_async(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RestoreSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RestoreSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_secret(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
    ) -> kms_20160120_models.RestoreSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    async def restore_secret_async(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
    ) -> kms_20160120_models.RestoreSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_secret_with_options_async(request, runtime)

    def rotate_secret_with_options(
        self,
        request: kms_20160120_models.RotateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RotateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RotateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RotateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def rotate_secret_with_options_async(
        self,
        request: kms_20160120_models.RotateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RotateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RotateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RotateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rotate_secret(
        self,
        request: kms_20160120_models.RotateSecretRequest,
    ) -> kms_20160120_models.RotateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    async def rotate_secret_async(
        self,
        request: kms_20160120_models.RotateSecretRequest,
    ) -> kms_20160120_models.RotateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rotate_secret_with_options_async(request, runtime)

    def schedule_key_deletion_with_options(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.pending_window_in_days):
            query['PendingWindowInDays'] = request.pending_window_in_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScheduleKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ScheduleKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def schedule_key_deletion_with_options_async(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.pending_window_in_days):
            query['PendingWindowInDays'] = request.pending_window_in_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScheduleKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ScheduleKeyDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def schedule_key_deletion(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        runtime = util_models.RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    async def schedule_key_deletion_async(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.schedule_key_deletion_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not UtilClient.is_unset(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not UtilClient.is_unset(request.protected_resource_arn):
            query['ProtectedResourceArn'] = request.protected_resource_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not UtilClient.is_unset(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not UtilClient.is_unset(request.protected_resource_arn):
            query['ProtectedResourceArn'] = request.protected_resource_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.SetDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_deletion_protection(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def tag_resource_with_options(
        self,
        request: kms_20160120_models.TagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resource_with_options_async(
        self,
        request: kms_20160120_models.TagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.TagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resource(
        self,
        request: kms_20160120_models.TagResourceRequest,
    ) -> kms_20160120_models.TagResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    async def tag_resource_async(
        self,
        request: kms_20160120_models.TagResourceRequest,
    ) -> kms_20160120_models.TagResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resource_with_options_async(request, runtime)

    def untag_resource_with_options(
        self,
        request: kms_20160120_models.UntagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resource_with_options_async(
        self,
        request: kms_20160120_models.UntagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UntagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resource(
        self,
        request: kms_20160120_models.UntagResourceRequest,
    ) -> kms_20160120_models.UntagResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

    async def untag_resource_async(
        self,
        request: kms_20160120_models.UntagResourceRequest,
    ) -> kms_20160120_models.UntagResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resource_with_options_async(request, runtime)

    def update_alias_with_options(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
    ) -> kms_20160120_models.UpdateAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    async def update_alias_async(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
    ) -> kms_20160120_models.UpdateAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alias_with_options_async(request, runtime)

    def update_certificate_status_with_options(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCertificateStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateCertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_certificate_status_with_options_async(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCertificateStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateCertificateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_certificate_status(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_certificate_status_with_options(request, runtime)

    async def update_certificate_status_async(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_certificate_status_with_options_async(request, runtime)

    def update_key_description_with_options(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeyDescription',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateKeyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_key_description_with_options_async(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeyDescription',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateKeyDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_key_description(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    async def update_key_description_async(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_key_description_with_options_async(request, runtime)

    def update_rotation_policy_with_options(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rotation_policy_with_options_async(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateRotationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rotation_policy(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    async def update_rotation_policy_async(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rotation_policy_with_options_async(request, runtime)

    def update_secret_with_options(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.extended_config):
            query['ExtendedConfig'] = request.extended_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.extended_config):
            query['ExtendedConfig'] = request.extended_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
    ) -> kms_20160120_models.UpdateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_secret_with_options(request, runtime)

    async def update_secret_async(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
    ) -> kms_20160120_models.UpdateSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_with_options_async(request, runtime)

    def update_secret_rotation_policy_with_options(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_rotation_policy_with_options_async(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretRotationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_rotation_policy(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    async def update_secret_rotation_policy_async(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_rotation_policy_with_options_async(request, runtime)

    def update_secret_version_stage_with_options(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.move_to_version):
            query['MoveToVersion'] = request.move_to_version
        if not UtilClient.is_unset(request.remove_from_version):
            query['RemoveFromVersion'] = request.remove_from_version
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretVersionStage',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretVersionStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_version_stage_with_options_async(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.move_to_version):
            query['MoveToVersion'] = request.move_to_version
        if not UtilClient.is_unset(request.remove_from_version):
            query['RemoveFromVersion'] = request.remove_from_version
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretVersionStage',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretVersionStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_version_stage(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    async def update_secret_version_stage_async(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_version_stage_with_options_async(request, runtime)

    def upload_certificate_with_options(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UploadCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.certificate_chain):
            query['CertificateChain'] = request.certificate_chain
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UploadCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_certificate_with_options_async(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UploadCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.certificate_chain):
            query['CertificateChain'] = request.certificate_chain
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UploadCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_certificate(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
    ) -> kms_20160120_models.UploadCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_certificate_with_options(request, runtime)

    async def upload_certificate_async(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
    ) -> kms_20160120_models.UploadCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_certificate_with_options_async(request, runtime)
